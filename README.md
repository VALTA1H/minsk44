# Minsk 1944: No Name

## 📖 About the Project
This is a historical drama Visual Novel built on the **Ren'Py** engine. The story takes place in **1944** during **Operation Bagration**, focusing on the liberation of Belarus. The narrative follows a squad of soldiers as they traverse from the crossing of the Berezina river, through the liberation of Bobruisk, to the final battles in Minsk.

The story explores themes of duty, camaraderie, the horrors of war, and memory.

## ✨ Credits & Acknowledgments

This project exists thanks to the incredible tools and modules provided by the community:

*   **Ren'Py Engine:** Special thanks to **Ren'Py Tom (Tom Rothamel)** for creating the engine that makes this possible.
*   **Kinetic Text Tags:** Huge thanks to the creators of the Kinetic Text Tags module for allowing dynamic text effects.
*   **Achievements RPY:** Sincere gratitude to the developers of the Achievements module for their work, which allows us to track player progress.

### Development Team
*   **Scenario:** Arseniy Dernovskiy & Kajakulak Altay
*   **Art/Great Artist:** Footer Heart
*   **Design:** Arseniy Dernovskiy & Kajakulak Altay
*   **Programming:** Arseniy Dernovskiy
*   **Special Thanks:** Khalipov S.S., Zakharova A.S., Alexander Khaev, Alexandra Dernovskaya, Natalia Dernovskaya.

---

## 🎮 Game Mechanics

### Branches & Morality
The game tracks the player's choices through global flags. Your decisions affect the ending and who survives.

*   **Reputation:** The variable `masha_rep` tracks your relationship with the partisan Masha.
*   **Key Flags:**
    *   `avoided_ambush`: Did the squad avoid the trap in the forest?
    *   `kolya_saved`: Did you save the young soldier Kolya at the bridge?
    *   `chose_duty` vs `chose_comrades`: The final moral choice determining the ending.

### Audio System
The project uses a dedicated audio channel setup defined in the scripts:
*   **Music:** Dynamic tracks (e.g., `theme_tense`, `theme_calm`, `dramatic_theme`).
*   **SFX:** Combat sounds (`machine_gun`, `artillery`, `explosion_loud`) and ambience (`rain`, `crickets_sound`).

---

## 🛠️ Development Tools

This repository includes custom Python scripts to assist with asset management and localization.

### 1. Dialogue Extractor (`dialogue_extractor.py`)
A tool to pull all character dialogue from `.rpy` files into a text file. Useful for proofreading, translation, or voice acting scripts.

*   **Features:** Automatically excludes narrator variables (`n_narr`, `narr`, `d_text`) and system variables to provide clean dialogue lines.
*   **Usage:**
    ```bash
    python dialogue_extractor.py
    # Or to specify files:
    python dialogue_extractor.py -f script.rpy
    ```
*   **Output:** Generates `dialogues_output.txt`.

### 2. KS-ify Image Processor (`ks_ify_image_processor.py`)
A GUI-based tool that processes real photos to give them a "Katawa Shoujo like background" look (similar to GIMP's procces) and converts them to highly compressed `.webp` format.

*   **Requirements:** `customtkinter`, `opencv-python`, `numpy`, `pillow`.
*   **Features:**
    *   Applies Oilify, Median Blur, and Edge detection filters.
    *   Adjusts global brightness and contrast.
    *   **Batch Processing:** Can process entire folders of images at once.
    *   **Compression:** Automatically resizes to 1920x1080 and saves as WebP.
*   **Usage:** Run the script to open the GUI. Select "Process Directory" to convert a folder of assets.

### 3. Image Definition Generator (`image_definition_generator.py`)
Automates the tedious process of writing `image name = "path/file.webp"` lines in Ren'Py.

*   **Configuration:** Edit the `IMAGE_DIRS` list inside the script to point to your asset folders (e.g., `../images`, `../gui`).
*   **Features:**
    *   Scans directories for `.webp` files.
    *   Sanitizes filenames to create valid Ren'Py image tags.
*   **Usage:**
    ```bash
    python image_definition_generator.py
    ```
*   **Output:** Generates `images.rpy` in the base directory.

---

## 📂 Project Structure

*   `script.rpy`: Contains the main story flow, character definitions, and logic.
*   `images.rpy`: (Generated) Contains image definitions.
*   `gui/`: Interface assets.
*   `audio/`: Music and sound effects.
*   `tools/`: Directory containing the Python helper scripts.

---

## 📜 License
*   **Game Assets:** All rights reserved by the development team.
*   **Code:** Custom scripts are provided for use within this project.
*   **Third-Party:** Kinetic Text Tags and Achievements RPY belong to their respective creators.