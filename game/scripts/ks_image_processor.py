import customtkinter as ctk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
import os 
import re 
from tkinter import TclError 
from typing import Dict, Any, Tuple

# --- CONFIGURATION AND CONSTANTS ---

# Default output/processing resolution
TARGET_WIDTH = 1920
TARGET_HEIGHT = 1080

DEFAULT_CONFIG: Dict[str, Any] = {
    "LAYER4_ENABLED": False, 
    
    # Layer 1
    "OILIFY1_R": 4, "OILIFY1_EXPONENT": 5, "OILIFY1_OPACITY": 80,
    # Layer 2
    "OILIFY2_R": 6, "OILIFY2_EXPONENT": 5, "OILIFY2_OPACITY": 20,
    # Layer 3
    "MEDIAN1_K": 7, "LAPLACE_K": 3, "EDGE_SUB_OPACITY": 20, 
    # Layer 4
    "MEDIAN2_K": 33, "LCH_OPACITY": 25, "LCH_SHIFT": 10, 
    
    # Global Adjustments
    "BRIGHTNESS_ADJ": 0, "CONTRAST_ADJ": 0,   
    
    "TARGET_WIDTH": TARGET_WIDTH,
    "TARGET_HEIGHT": TARGET_HEIGHT, 
    "OUTPUT_COMPRESS_ENABLED": True,
}

# Mapping slider keys to their configuration key, range, and format
SLIDER_PARAMS = {
    "Oilify 1 Radius": {"key": "OILIFY1_R", "from": 1, "to": 7, "steps": 6, "format": "d"},
    "Oilify 1 Opacity": {"key": "OILIFY1_OPACITY", "from": 0, "to": 100, "steps": 100, "format": "d"},
    "Oilify 2 Radius": {"key": "OILIFY2_R", "from": 5, "to": 15, "steps": 10, "format": "d"},
    "Oilify 2 Opacity": {"key": "OILIFY2_OPACITY", "from": 0, "to": 100, "steps": 100, "format": "d"},
    "Edge Subtract Opacity": {"key": "EDGE_SUB_OPACITY", "from": 0, "to": 100, "steps": 100, "format": "d"},
    "Final LCh Opacity": {"key": "LCH_OPACITY", "from": 0, "to": 100, "steps": 100, "format": "d"},
    "LCh Shift (Blue/Chroma)": {"key": "LCH_SHIFT", "from": -50, "to": 50, "steps": 100, "format": "d"},
    "Global Brightness (+/-)": {"key": "BRIGHTNESS_ADJ", "from": -100, "to": 100, "steps": 200, "format": "d"},
    "Global Contrast (+/-)": {"key": "CONTRAST_ADJ", "from": -50, "to": 50, "steps": 100, "format": "d"},
}

# Grouping sliders for dynamic display control
CORE_SLIDER_KEYS = ["OILIFY1_R", "OILIFY1_OPACITY", "OILIFY2_R", "OILIFY2_OPACITY", "EDGE_SUB_OPACITY"]
GLOBAL_ADJ_KEYS = ["BRIGHTNESS_ADJ", "CONTRAST_ADJ"]
LAYER4_SLIDER_KEYS = ["LCH_OPACITY", "LCH_SHIFT"]

# --- BATCH PROCESSING CONSTANTS (UPDATED) ---
# NOTE: The suffix is now just the extension. The check logic is updated to match.
KS_SUFFIX = ".webp"
SUPPORTED_INPUT_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp')

# --- 1. Custom OpenCV Processing Functions (functions omitted for brevity, assumed functional) ---

def ks_ffmpeg_like_downscale(img: np.ndarray, target_w: int, target_h: int) -> np.ndarray:
    return cv2.resize(img, (target_w, target_h), interpolation=cv2.INTER_AREA)

def ks_oilify_approx(img: np.ndarray, radius: int, exponent: int) -> np.ndarray:
    d = radius * 2 + 1 
    d = d if d % 2 == 1 else d + 1
    sigma = int(exponent * (255 / 15.0))
    sigmaColor = max(10, sigma) 
    sigmaSpace = max(10, sigma)
    return cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace) 

def ks_subtract_blend(base_img: np.ndarray, blend_img: np.ndarray, opacity: float) -> np.ndarray:
    alpha = opacity / 100.0
    base_f = base_img.astype(np.float32)
    blend_f = blend_img.astype(np.float32)
    subtracted = np.clip(base_f - blend_f, 0, 255)
    result_float = base_f * (1.0 - alpha) + subtracted * alpha
    return np.clip(result_float, 0, 255).astype(np.uint8)

def ks_color_blend(base_img: np.ndarray, blend_img: np.ndarray, opacity: float) -> np.ndarray:
    base_v = cv2.cvtColor(base_img, cv2.COLOR_BGR2HSV)[:,:,2]
    blend_hs = cv2.cvtColor(blend_img, cv2.COLOR_BGR2HSV)[:,:,0:2]
    new_hsv = cv2.merge([blend_hs[:,:,0], blend_hs[:,:,1], base_v])
    new_bgr = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)
    return cv2.addWeighted(base_img, 1.0 - (opacity / 100.0), new_bgr, (opacity / 100.0), 0)

def ks_lch_color_adjust(img: np.ndarray, config: Dict[str, Any]) -> np.ndarray:
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_img)
    shift = config["LCH_SHIFT"]
    b = cv2.add(b, shift) 
    a = cv2.add(a, int(abs(shift) * 0.5)) 
    shifted_lab = cv2.merge([l, a, b])
    shifted_bgr = cv2.cvtColor(shifted_lab, cv2.COLOR_LAB2BGR)
    return shifted_bgr

def ks_adjust_brightness_contrast(img: np.ndarray, config: Dict[str, Any]) -> np.ndarray:
    beta = config["BRIGHTNESS_ADJ"] 
    contrast_adj = config["CONTRAST_ADJ"]
    alpha = 1.0 + (contrast_adj / 100.0) 
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)


def ks_process_image(base_image_path: str, config: Dict[str, Any]) -> Tuple[np.ndarray, np.ndarray, str | None]:
    img = cv2.imread(base_image_path)
    if img is None: 
        return np.zeros((1, 1, 3), dtype=np.uint8), np.zeros((1, 1, 3), dtype=np.uint8), "Error: Could not load image."
        
    original_img_for_display = img.copy() 
    
    # --- 1. Initial Resize/Downscale to TARGET_WIDTH/HEIGHT (1920x1080) ---
    target_w, target_h = config["TARGET_WIDTH"], config["TARGET_HEIGHT"]
    
    if img.shape[1] != target_w or img.shape[0] != target_h:
        img = cv2.resize(img, (target_w, target_h), interpolation=cv2.INTER_LANCZOS4)
    
    img_base = img.copy() 
    
    # --- 2. IMAGE PROCESSING LAYERS (Oilify, Edge, Polish) ---

    img_layer1 = ks_oilify_approx(img_base, config["OILIFY1_R"], config["OILIFY1_EXPONENT"])
    img_current = cv2.addWeighted(img_base, 1.0 - (config["OILIFY1_OPACITY"]/100.0), img_layer1, (config["OILIFY1_OPACITY"]/100.0), 0)
    img_base = img_current.copy() 
    
    img_layer2 = ks_oilify_approx(img_base, config["OILIFY2_R"], config["OILIFY2_EXPONENT"])
    img_current = cv2.addWeighted(img_base, 1.0 - (config["OILIFY2_OPACITY"]/100.0), img_layer2, (config["OILIFY2_OPACITY"]/100.0), 0)
    img_base = img_current.copy() 
    
    k_med1 = config["MEDIAN1_K"]; k_med1 = k_med1 if k_med1 % 2 == 1 else k_med1 + 1 
    img_layer3 = cv2.medianBlur(img_base, k_med1)
    k_lapl = config["LAPLACE_K"]; k_lapl = k_lapl if k_lapl % 2 == 1 else k_lapl + 1 
    laplacian_edges = cv2.Laplacian(cv2.cvtColor(img_layer3, cv2.COLOR_BGR2GRAY), cv2.CV_16S, ksize=k_lapl)
    img_layer3_blend = cv2.cvtColor(cv2.convertScaleAbs(laplacian_edges), cv2.COLOR_GRAY2BGR) 
    img_current = ks_subtract_blend(img_base, img_layer3_blend, config["EDGE_SUB_OPACITY"])
    img_base = img_current.copy() 
    
    if config["LAYER4_ENABLED"]:
        k_med2 = config["MEDIAN2_K"]; k_med2 = k_med2 if k_med2 % 2 == 1 else k_med2 + 1 
        img_layer4 = cv2.medianBlur(img_base, k_med2)
        img_layer4_color = ks_lch_color_adjust(img_layer4, config)
        img_current = ks_color_blend(img_base, img_layer4_color, config["LCH_OPACITY"])
        img_base = img_current.copy() 
    
    processed_img = img_base
    processed_img = ks_adjust_brightness_contrast(processed_img, config)
    
    # --- 3. FINAL COMPRESSION/SCALING FOR DISPLAY/SAVING ---
    if config["OUTPUT_COMPRESS_ENABLED"]:
        processed_img = ks_ffmpeg_like_downscale(
            processed_img, 
            config['TARGET_WIDTH'], 
            config['TARGET_HEIGHT']
        )
    
    return original_img_for_display, processed_img, None


# --- 2. BATCH PROCESSING FUNCTIONS (UPDATED for no suffix) ---

def convert_to_webp_with_metadata(image_path: str, output_dir: str, config: Dict[str, Any]) -> str | None:
    """
    Processes a single image, converts it to WebP, and saves it with the 
    original base name + .webp extension.
    """
    
    # 1. Process the image
    _, processed_img, error = ks_process_image(image_path, config)
    
    if error or processed_img is None:
        print(f"Skipping {os.path.basename(image_path)} due to processing error: {error}")
        return None

    # 2. Generate automatic filename (Original base name + .webp)
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_filename = base_name + KS_SUFFIX # e.g., 'image.webp'
    output_path = os.path.join(output_dir, output_filename)
    
    # 3. Save as WebP with high quality
    webp_quality = 95 # A high-quality setting for WebP
    success = cv2.imwrite(output_path, processed_img, [cv2.IMWRITE_WEBP_QUALITY, webp_quality])
    
    if success:
        return output_path
    else:
        print(f"Error saving processed image to {output_path}")
        return None

def process_directory(input_dir: str, output_dir: str, config: Dict[str, Any]):
    """
    Processes all supported image files in a directory, converting them to WebP 
    with filtering applied. Checks for and skips already processed files by 
    looking for a matching .webp file.
    """
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory not found: {input_dir}")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    total_files = 0
    processed_count = 0
    skipped_count = 0

    print(f"\n--- Starting Batch Processing ---\nInput: {input_dir}\nOutput: {output_dir}\n")

    for filename in os.listdir(input_dir):
        # 1. Filter for supported input image files
        if not filename.lower().endswith(SUPPORTED_INPUT_EXTENSIONS):
            continue
            
        total_files += 1
        input_path = os.path.join(input_dir, filename)
        
        # 2. Check for already processed file (matching base name + .webp)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        expected_output_filename = base_name + KS_SUFFIX
        expected_output_path = os.path.join(output_dir, expected_output_filename)

        if os.path.exists(expected_output_path):
            # Prompt user that the file seems already processed
            print(f"[{total_files}] WARNING: '{filename}' seems already processed (found '{expected_output_filename}'). Skipping to avoid reprocessing/overwriting. To reprocess, delete the existing output file.")
            skipped_count += 1
            continue

        # 3. Process and convert
        print(f"[{total_files}] Processing '{filename}'…")
        output_path = convert_to_webp_with_metadata(input_path, output_dir, config)
        
        if output_path:
            processed_count += 1
            print(f"  -> SUCCESS: Saved as {os.path.basename(output_path)}")
        else:
            print(f"  -> FAILED processing {filename}.")

    print(f"\n--- Batch Processing Complete ---\nTotal images found: {total_files}\nProcessed: {processed_count}\nSkipped (already processed): {skipped_count}\n")


# --- 3. CustomTkinter GUI Application (Unchanged from previous revision except for save path default) ---
class KSApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # --- ATTRIBUTES ---
        self.title("KS-ify Image Processor (GIMP 3 Style)")
        self.geometry("1800x900") 
        ctk.set_appearance_mode("System") 
        # CHANGE: Increased Preview Size
        self.DISPLAY_WIDTH = 720
        self.DISPLAY_HEIGHT = 405
        self.input_image_path: str | None = None
        self.output_cv_img: np.ndarray | None = None
        self.config = DEFAULT_CONFIG.copy()
        self.slider_widgets: Dict[str, Dict[str, Any]] = {}
        
        # --- UI SETUP ---
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._setup_sidebar()
        self._setup_command_bar()
        self._setup_image_display()
        
    def _update_slider(self, value: float, key: str, label: ctk.CTkLabel, fmt: str):
        if fmt == 'd': 
            self.config[key] = int(value)
        else:
            self.config[key] = round(value, 2)
        label.configure(text=f"{label.cget('text').split(':')[0]}:\n{self.config[key]:{fmt}}")

    def _toggle_output_compress(self):
        self.config['OUTPUT_COMPRESS_ENABLED'] = not self.config['OUTPUT_COMPRESS_ENABLED']

    def _toggle_layer4(self):
        is_enabled = not self.config['LAYER4_ENABLED']
        self.config['LAYER4_ENABLED'] = is_enabled
        
        start_row = self.global_adj_title_label.grid_info()['row']
        row_delta = 4 if is_enabled else -4

        if is_enabled:
            self.layer4_frame.grid(row=start_row, column=0, sticky="ew")
            
            for key in LAYER4_SLIDER_KEYS:
                title = next(t for t, p in SLIDER_PARAMS.items() if p['key'] == key)
                fmt = SLIDER_PARAMS[title]['format']
                self.slider_widgets[key]['label'].configure(state="normal", text=f"{title}:\n{self.config[key]:{fmt}}")
                self.slider_widgets[key]['slider'].configure(state="normal")
        else:
            self.layer4_frame.grid_forget()
            
            for key in LAYER4_SLIDER_KEYS:
                self.slider_widgets[key]['label'].configure(state="disabled", text=f"{self.slider_widgets[key]['label'].cget('text').split(':')[0]}:\n<Layer 4 Disabled>")
                self.slider_widgets[key]['slider'].configure(state="disabled")
        
        self._regrid_elements_below(start_row, row_delta)

    def _regrid_elements_below(self, start_row: int, row_delta: int):
        """Regrids the elements following the Layer 4 Frame based on the new anchor row."""
        
        new_anchor_row = start_row + row_delta
        next_free_row = new_anchor_row
        
        # A. Global Adjustments Title
        self.global_adj_title_label.grid_forget(); self.global_adj_title_label.grid(row=next_free_row, column=0, padx=10, pady=(20, 10), sticky="ew"); next_free_row += 1
        
        # B. Global Adjustments Sliders (4 rows)
        for key in GLOBAL_ADJ_KEYS:
             self.slider_widgets[key]['label'].grid_forget(); self.slider_widgets[key]['label'].grid(row=next_free_row, column=0, padx=10, pady=(5, 0), sticky="ew"); next_free_row += 1
             self.slider_widgets[key]['slider'].grid_forget(); self.slider_widgets[key]['slider'].grid(row=next_free_row, column=0, padx=10, pady=(0, 10), sticky="ew"); next_free_row += 1
             
        # C. Output Compression (2 rows)
        self.output_compress_title_label.grid_forget(); self.output_compress_title_label.grid(row=next_free_row, column=0, padx=10, pady=(20, 10), sticky="ew"); next_free_row += 1
        self.output_compress_checkbox.grid_forget(); self.output_compress_checkbox.grid(row=next_free_row, column=0, padx=10, pady=(0, 10), sticky="ew"); next_free_row += 1
        
        # D. Save Button (1 row)
        self.save_button.grid_forget(); self.save_button.grid(row=next_free_row, column=0, padx=10, pady=20); next_free_row += 1
        
        # E. Process Button (1 row)
        self.reprocess_button.grid_forget(); self.reprocess_button.grid(row=next_free_row, column=0, padx=10, pady=20); next_free_row += 1
        
        # F. Process Dir Button (1 row)
        self.process_dir_button.grid_forget(); self.process_dir_button.grid(row=next_free_row, column=0, padx=10, pady=(5, 20)); next_free_row += 1
        
        # G. Set the weight to the last row
        self.control_frame.grid_rowconfigure(next_free_row, weight=1)

    # --- BATCH PROCESSING HANDLER ---
    def _select_and_process_dir(self):
        """Prompts user for input and output directories and starts batch processing."""
        input_dir = filedialog.askdirectory(title="Select Input Directory (Images to Process)")
        if not input_dir:
            return

        output_dir = filedialog.askdirectory(title="Select Output Directory (Processed WebP Files)")
        if not output_dir:
            return

        # Removing the strict check for input_dir == output_dir is risky when overwriting 
        # is enabled by no suffix, but since the output extension is always different (.webp), 
        # it *should* be fine unless we start processing .webp inputs. I'll keep the check.
        # RETHINK: The check is only needed to prevent overwriting/conflicts. Since input 
        # types are limited (jpg, png, bmp) and output is always webp, this is less critical 
        # but good practice to separate for batch jobs. I will rely on the user to separate.
        # I'll remove the messagebox error for simplicity but recommend console warning.
        if input_dir == output_dir:
             print("WARNING: Input and Output directories are the same. Proceed with caution. Files will be saved with a new .webp extension.")

        self.reprocess_button.configure(state="disabled")
        self.save_button.configure(state="disabled")
        self.process_dir_button.configure(state="disabled", text="Processing…")
        
        print("\nNOTE: GUI may freeze during batch processing. Check console for progress.")
        try:
            process_directory(input_dir, output_dir, self.config)
            messagebox.showinfo("Batch Complete", f"Directory processing finished! Check output folder: {output_dir}")
        except Exception as e:
            messagebox.showerror("Batch Error", f"An error occurred during batch processing: {e}")
        finally:
            self.reprocess_button.configure(state="normal" if self.input_image_path else "disabled")
            self.process_dir_button.configure(state="normal", text="Process Directory to WebP")


    # --- IMAGE MANAGEMENT ---

    def load_image(self):
        """Opens file dialog, loads and displays image, and prepares UI for processing."""
        self.input_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if self.input_image_path:
            self._display_image_on_canvas(self.input_image_path, self.input_canvas)
            
            # Reset output state
            self.output_canvas.configure(image=None, text="PRESS PROCESS IMAGE", text_color="gray50")
            self.output_cv_img = None 
            
            # Enable Process Button
            self.save_button.configure(state="disabled") 
            self.reprocess_button.configure(state="normal") 

    def process_and_display(self):
        """Runs the image processing pipeline and updates the display."""
        if not self.input_image_path: 
             print("Error: No image loaded to process.")
             return
        
        # UI Feedback during processing
        self.reprocess_button.configure(state="disabled") 
        self.output_canvas.configure(text="Processing…", text_color="yellow")

        try:
            input_img_original, processed_img, error = ks_process_image(self.input_image_path, self.config)
        except Exception as e:
            error = f"Processing failed: {e}"
            processed_img = None

        self.reprocess_button.configure(state="normal") 

        if error or processed_img is None: 
            error_msg = error if error else "Processing returned no image."
            print(f"Error during processing: {error_msg}")
            self.output_canvas.configure(text=f"ERROR: {error_msg}", text_color="red")
            self.save_button.configure(state="disabled")
            return
            
        # Success path
        self.input_cv_img = input_img_original
        self.output_cv_img = processed_img
        self._display_cv_image_on_canvas(self.output_cv_img, self.output_canvas) 
        self.save_button.configure(state="normal")
        self.output_canvas.configure(text="", text_color="white")

    def _display_image_on_canvas(self, path: str, label_widget: ctk.CTkLabel):
        """Loads a PIL image from path, scales it for display, and updates the canvas."""
        img = Image.open(path)
        img_display = img.resize((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT), Image.Resampling.LANCZOS)
        
        self.tk_img = ctk.CTkImage(light_image=img_display, dark_image=img_display, size=(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)) 
        label_widget.configure(image=self.tk_img, text="")
        label_widget.image = self.tk_img
        
    def _display_cv_image_on_canvas(self, cv_img: np.ndarray, label_widget: ctk.CTkLabel):
        """Converts an OpenCV image, scales it for display, and updates the canvas."""
        img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_display = img_pil.resize((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT), Image.Resampling.LANCZOS)
        
        tk_img = ctk.CTkImage(light_image=img_display, dark_image=img_display, size=(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.tk_img_out = tk_img
        label_widget.configure(image=self.tk_img_out, text="")
        label_widget.image = self.tk_img_out

    def save_image(self):
        """Opens save dialog and writes the processed OpenCV image to file."""
        if self.output_cv_img is None: return

        # Offer the default .webp extension first
        save_path = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WebP files", "*.webp"), ("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        
        if save_path:
            # Check for WebP extensions to ensure we use the WebP quality parameter
            if save_path.lower().endswith('.webp'):
                webp_quality = 95
                cv2.imwrite(save_path, self.output_cv_img, [cv2.IMWRITE_WEBP_QUALITY, webp_quality])
            else:
                 cv2.imwrite(save_path, self.output_cv_img)
                 
            print(f"Image saved to {save_path}. Resolution: {self.output_cv_img.shape[1]}x{self.output_cv_img.shape[0]}")


    # --- UI SETUP METHODS (Unchanged) ---

    def _setup_sidebar(self):
        self.control_frame = ctk.CTkScrollableFrame(self, width=250, corner_radius=0)
        self.control_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.control_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(self.control_frame, text="PARAMETERS", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=0, padx=10, pady=10)

        self.row_idx = 1
        
        def add_slider(title, key, master_frame=self.control_frame):
            params = SLIDER_PARAMS[title]
            label = ctk.CTkLabel(master_frame, text=f"{title}:\n{self.config[key]:{params['format']}}")
            label.grid(row=self.row_idx, column=0, padx=10, pady=(5, 0), sticky="ew")
            self.row_idx += 1
            slider = ctk.CTkSlider(master_frame, from_=params["from"], to=params["to"], number_of_steps=params["steps"], 
                                   command=lambda v, k=key, l=label, f=params['format']: self._update_slider(v, k, l, f))
            slider.set(self.config[key])
            slider.grid(row=self.row_idx, column=0, padx=10, pady=(0, 10), sticky="ew")
            self.slider_widgets[key] = {"label": label, "slider": slider}
            self.row_idx += 1
            return label, slider

        # 1. CORE SLIDERS
        for key in CORE_SLIDER_KEYS:
            title = next(t for t, p in SLIDER_PARAMS.items() if p['key'] == key)
            add_slider(title, key)
            
        # 2. Layer 4 Polish (Optional)
        ctk.CTkLabel(self.control_frame, text="Layer 4 Polish", font=ctk.CTkFont(size=14, weight="bold")).grid(row=self.row_idx, column=0, padx=10, pady=(20, 10)); self.row_idx += 1
        self.layer4_checkbox = ctk.CTkCheckBox(self.control_frame, text="Enable Layer 4 (LCh Polish)", command=self._toggle_layer4)
        if self.config['LAYER4_ENABLED']: self.layer4_checkbox.select()
        self.layer4_checkbox.grid(row=self.row_idx, column=0, padx=10, pady=(0, 10)); self.row_idx += 1
        
        self.layer4_frame = ctk.CTkFrame(self.control_frame, fg_color="transparent")
        self.layer4_frame.grid_columnconfigure(0, weight=1)
        
        temp_row_idx = 0 
        for key in LAYER4_SLIDER_KEYS:
            title = next(t for t, p in SLIDER_PARAMS.items() if p['key'] == key)
            params = SLIDER_PARAMS[title]
            
            label = ctk.CTkLabel(self.layer4_frame, text=f"{title}:\n{self.config[key]:{params['format']}}")
            label.grid(row=temp_row_idx, column=0, padx=10, pady=(5, 0), sticky="ew")
            temp_row_idx += 1
            
            slider = ctk.CTkSlider(self.layer4_frame, from_=params["from"], to=params["to"], number_of_steps=params["steps"], 
                                   command=lambda v, k=key, l=label, f=params['format']: self._update_slider(v, k, l, f))
            slider.set(self.config[key])
            slider.grid(row=temp_row_idx, column=0, padx=10, pady=(0, 10), sticky="ew")
            temp_row_idx += 1
            self.slider_widgets[key] = {"label": label, "slider": slider}

        # Initial gridding of the layer 4 frame 
        if self.config['LAYER4_ENABLED']:
            self.layer4_frame.grid(row=self.row_idx, column=0, sticky="ew")
            self.row_idx += 1 
        else:
            for key in LAYER4_SLIDER_KEYS:
                 self.slider_widgets[key]['label'].configure(state="disabled", text=f"{self.slider_widgets[key]['label'].cget('text').split(':')[0]}:\n<Layer 4 Disabled>")
                 self.slider_widgets[key]['slider'].configure(state="disabled")

        # 3. GLOBAL ADJUSTMENT SLIDERS
        self.global_adj_title_label = ctk.CTkLabel(self.control_frame, text="Global Adjustments", font=ctk.CTkFont(size=14, weight="bold"))
        self.global_adj_title_label.grid(row=self.row_idx, column=0, padx=10, pady=(20, 10)); self.row_idx += 1
        for key in GLOBAL_ADJ_KEYS:
            title = next(t for t, p in SLIDER_PARAMS.items() if p['key'] == key)
            add_slider(title, key)

        # 4. Output Compression Checkbox 
        self.output_compress_title_label = ctk.CTkLabel(self.control_frame, text="Output Save Compression", font=ctk.CTkFont(size=14, weight="bold"))
        self.output_compress_title_label.grid(row=self.row_idx, column=0, padx=10, pady=(20, 10)); self.row_idx += 1
        self.output_compress_checkbox = ctk.CTkCheckBox(self.control_frame, text=f"Enable Downscale to {DEFAULT_CONFIG['TARGET_WIDTH']}x{DEFAULT_CONFIG['TARGET_HEIGHT']}", command=self._toggle_output_compress)
        if self.config['OUTPUT_COMPRESS_ENABLED']: self.output_compress_checkbox.select()
        self.output_compress_checkbox.grid(row=self.row_idx, column=0, padx=10, pady=(0, 10)); self.row_idx += 1
        
        # 5. SAVE BUTTON 
        self.save_button = ctk.CTkButton(self.control_frame, text="Save Output Image", command=self.save_image, state="disabled")
        self.save_button.grid(row=self.row_idx, column=0, padx=10, pady=20); self.row_idx += 1
        
        # 6. PROCESS BUTTON
        self.reprocess_button = ctk.CTkButton(self.control_frame, text="Process Image", command=self.process_and_display, state="disabled")
        self.reprocess_button.grid(row=self.row_idx, column=0, padx=10, pady=20); self.row_idx += 1

        # 7. NEW: PROCESS DIRECTORY BUTTON
        self.process_dir_button = ctk.CTkButton(self.control_frame, text="Process Directory to WebP", command=self._select_and_process_dir)
        self.process_dir_button.grid(row=self.row_idx, column=0, padx=10, pady=(5, 20)); self.row_idx += 1
        
        # Set the weight to the last row
        self.control_frame.grid_rowconfigure(self.row_idx, weight=1)

    def _setup_command_bar(self):
        # Empty command bar at the top (only for layout)
        self.command_bar = ctk.CTkFrame(self, height=10)
        self.command_bar.grid(row=0, column=1, columnspan=2, padx=10, pady=(10, 5), sticky="ew")
        
    def _setup_image_display(self):
        self.input_label_text = ctk.CTkLabel(self, text=f"Input Image")
        self.input_label_text.grid(row=1, column=1, pady=(0, 5), sticky="s")
        self.input_canvas = ctk.CTkLabel(self, text="CLICK HERE TO LOAD IMAGE", fg_color=("gray75", "gray25"), width=self.DISPLAY_WIDTH, height=self.DISPLAY_HEIGHT, text_color="gray50")
        self.input_canvas.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="nsew")

        self.output_label_text = ctk.CTkLabel(self, text="KS-ify Output Image")
        self.output_label_text.grid(row=1, column=2, pady=(0, 5), sticky="s")
        self.output_canvas = ctk.CTkLabel(self, text="OUTPUT WILL APPEAR HERE", fg_color=("gray75", "gray25"), width=self.DISPLAY_WIDTH, height=self.DISPLAY_HEIGHT)
        self.output_canvas.grid(row=2, column=2, padx=10, pady=(0, 10), sticky="nsew")
        
        self.input_canvas.bind("<Enter>", lambda e: self.input_canvas.configure(fg_color="gray30"))
        self.input_canvas.bind("<Leave>", lambda e: self.input_canvas.configure(fg_color=("gray75", "gray25")))
        self.input_canvas.bind("<ButtonRelease-1>", lambda e: self.load_image()) 

if __name__ == "__main__":
    app = KSApp()
    app.mainloop()