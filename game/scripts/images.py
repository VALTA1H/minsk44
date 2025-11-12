import os
import re
import sys

# ====== CONFIGURATION ======
# CHANGE THESE PATHS TO MATCH YOUR PROJECT STRUCTURE!
# Use absolute paths OR paths relative to THIS SCRIPT'S LOCATION

# List of (source_folder, renpy_prefix) tuples
IMAGE_DIRS = [
    # Format: (path_to_scan, path_to_use_in_renpy)
    ("../gui/splashscreen", "gui/splashscreen"),
    ("../images", "images"),
    # ADD MORE DIRECTORIES HERE AS NEEDED
    # Example: ("../../other_assets", "assets/other")
]

# Where to save images.rpy (relative to THIS script)
OUTPUT_DIR = "../"

OUTPUT_FILENAME = "images.rpy"
EXTENSIONS = {'.webp'}  # Only process WebP files
# ===========================

def sanitize_identifier(filename: str) -> str:
    """Convert filename to valid Ren'Py identifier."""
    base = os.path.splitext(filename)[0]
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', base)
    if sanitized and sanitized[0].isdigit():
        sanitized = '_' + sanitized
    sanitized = re.sub(r'_+', '_', sanitized).strip('_')
    return sanitized or 'image'

def resolve_path(base_path: str, relative_path: str) -> str:
    """Safely resolve relative paths with clear error messages."""
    if os.path.isabs(relative_path):
        return relative_path
    
    combined = os.path.normpath(os.path.join(base_path, relative_path))
    return combined

def main():
    # Get ABSOLUTE path to this script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📍 Script location: {script_dir}")
    
    # Resolve output directory
    output_dir_abs = resolve_path(script_dir, OUTPUT_DIR)
    print(f"📤 Output directory: {output_dir_abs}")
    
    # Verify output directory exists or create it
    if not os.path.exists(output_dir_abs):
        try:
            os.makedirs(output_dir_abs, exist_ok=True)
            print(f"✅ Created output directory: {output_dir_abs}")
        except Exception as e:
            print(f"❌ Failed to create output directory: {e}")
            sys.exit(1)
    
    all_images = []
    found_any = False
    
    # Process each source directory
    for source_rel, renpy_prefix in IMAGE_DIRS:
        # Resolve source directory path
        source_abs = resolve_path(script_dir, source_rel)
        print(f"\n📁 Processing source: {source_rel}")
        print(f"   → Absolute path: {source_abs}")
        
        # Verify source directory exists
        if not os.path.isdir(source_abs):
            print(f"   ⚠️ ERROR: Directory does NOT exist!")
            print(f"   💡 TIP: Check if path is correct relative to script location:")
            print(f"          {script_dir}")
            continue
        
        print(f"   ✅ Directory exists! Scanning for .webp files…")
        found_any = True
        
        # Walk through directory
        for root, _, files in os.walk(source_abs):
            for file in files:
                if os.path.splitext(file)[1].lower() in EXTENSIONS:
                    # Get path relative to source directory
                    rel_path = os.path.relpath(os.path.join(root, file), source_abs)
                    clean_path = os.path.join(renpy_prefix, rel_path).replace(os.sep, '/')
                    
                    identifier = sanitize_identifier(file)
                    all_images.append((identifier, clean_path))
                    print(f"   ➕ Found: {file} → {clean_path}")
    
    if not found_any:
        print("\n❌ NO VALID SOURCE DIRECTORIES FOUND!")
        print("💡 Please check your IMAGE_DIRS configuration in the script.")
        print(f"   Script directory: {script_dir}")
        print("   Example valid path: " + os.path.join(script_dir, "../gui/splashscreen"))
        sys.exit(1)
    
    if not all_images:
        print("\n❌ NO WEBP FILES FOUND in any directory!")
        print("💡 Check if your source directories contain .webp files")
        sys.exit(1)
    
    # Sort and write output
    all_images.sort(key=lambda x: x[0])
    output_path = os.path.join(output_dir_abs, OUTPUT_FILENAME)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Auto-generated on {os.path.basename(__file__)}\n")
        f.write(f"# Source directories: {[src for src, _ in IMAGE_DIRS]}\n\n")
        for identifier, path in all_images:
            f.write(f'image {identifier} = "{path}"\n')
    
    print(f"\n✨ SUCCESS! Generated {len(all_images)} image definitions")
    print(f"💾 Saved to: {output_path}")
    print("\n📋 FIRST 5 ENTRIES:")
    for i, (identifier, path) in enumerate(all_images[:5]):
        print(f"   {i+1}. image {identifier} = \"{path}\"")
    if len(all_images) > 5:
        print(f"   … and {len(all_images)-5} more")

if __name__ == "__main__":
    print("="*50)
    print("WEBP TO REN'PY IMAGE DEFINITIONS GENERATOR")
    print("="*50)
    main()
    print("\n✅ Done!")