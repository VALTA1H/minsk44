# Minsk 1944: No Name
[![Minsk 1944: No Name](https://img.shields.io/badge/Project-Minsk%201944%3A%20No%20Name-BB2020)](https://github.com/sehaxe/minsk44)
[![Engine](https://img.shields.io/badge/Engine-Ren%27Py-F05030)](https://www.renpy.org/)
[![Language](https://img.shields.io/badge/Language-Ren%27Py%20Script%2C%20Python-306998)](https://www.renpy.org/doc/html/language.html)
[![Genre](https://img.shields.io/badge/Genre-Historical%20Drama%2C%20VN-512BD4)](#🚀-about)
[![OS](https://img.shields.io/badge/OS-Windows%2C%20macOS%2C%20Linux-0078D4)](https://www.renpy.org/doc/html/build.html)
[![Features](https://img.shields.io/badge/Features-Core%20Mechanics-4EC5C2)](#⚙️-core-features)
[![Dependencies](https://img.shields.io/badge/Dependencies-Kinetic%20Text%20%26%20Achievements-FF8C00)](#✨-credits-&-acknowledgments)
[![Version](https://img.shields.io/badge/Version-1.0.0--beta-brightgreen)](#✨-whats-new)
[![GitHub last commit](https://img.shields.io/github/last-commit/sehaxe/minsk44)](#)

⭐ Star us on GitHub — your support motivates us a lot! 🙏😊

## 🚀 About

**Minsk 1944: No Name** is a historical drama Visual Novel set during the pivotal **Operation Bagration** in 1944. The story follows an unnamed protagonist, a sergeant in the Soviet army, through five intense days of combat, moral dilemmas, and the brutal reality of the Second World War on the Eastern Front.

The narrative spans from the challenging **Berezina River crossing**, the bloody **liberation of Bobruisk**, to the final, decisive battle for the capital, **Minsk**. The game explores deep themes of duty, personal sacrifice, the bond between comrades, and the enduring memory of wartime horrors.

### Main Characters

The story's core is built around the protagonist's interactions with his squad and the people they meet.

| Variable Name | Character Name | Role |
| :--- | :--- | :--- |
| `ivan` | Иван (Ivan) | The veteran squad leader. |
| `kolya` | Коля (Kolya) | A young, nervous new recruit. |
| `politruk` | Политрук (Political Officer) | Represents military ideology and command. |
| `masha` | Маша (Masha) | A partisan with deep local knowledge and painful history. |
| `hanz` | Немец (German) | Antagonist, used to highlight moral choices. |

## ✨ What's New

### Version 1.1 (Beta)

🚀 **Current Content Scope**
- **Full Story:** Covers the entire timeline from the start of Operation Bagration (Berezina crossing on June 28th) through the liberation of Bobruisk and the final push into Minsk (July 3rd, 1944).
- **Two Major Endings:** Final choice branches into a "Duty" ending (`chose_duty`) and a "Comrades" ending (`chose_comrades`), each with a unique 80-year flash-forward epilogue.
- **Improved Tooling:** Inclusion of the new `ks_ify_image_processor.py` for easier asset management and style consistency.

## ⚙️ Core Features

This project utilizes advanced Ren'Py features to enhance the player experience.

| Feature | Ren'Py Implementation | Script Variables |
| :--- | :--- | :--- |
| **Kinetic Text** | Used for dynamic, high-impact dialogue delivery (e.g., punch, shake effects). | Included via external module. |
| **Achievements** | Tracks key decisions and major milestones in the game. | Included via external `achievements.rpy` module. |
| **Moral/Story Flags** | Tracks major choices that affect character survival and the ending. | `avoided_ambush`, `kolya_saved`, `spared_civilians`, `masha_rep`. |
| **Dynamic Audio** | Defined audio channels for music, SFX, and ambient loops. | `artillery`, `machine_gun`, `theme_tense`, `distant_celebration`. |

> [!NOTE]
> The game uses the `nvl` mode for extended narration and `adv` mode for direct character dialogue, providing a varied reading experience.

## 🖼️ Screenshots

A visual look into **Minsk 1944: No Name**, showcasing the custom, stylized background art and the intense atmosphere of the Eastern Front.

<img width="1920" height="1108" alt="Screenshot_20251113_172819" src="https://github.com/user-attachments/assets/36d63034-ba03-4456-8035-cd993dcc507a" />
<img width="1920" height="1108" alt="Screenshot_20251113_172841" src="https://github.com/user-attachments/assets/7255e9d2-b3df-4910-9051-58f2a47f24ff" />
<img width="1920" height="1108" alt="Screenshot_20251113_172912" src="https://github.com/user-attachments/assets/49ab41cf-1ff7-4ca6-9e87-024817f589ce" />


## 📝 How to Run

To run the Visual Novel, you only need the Ren'Py engine installed.

```shell
# 1. Ensure you have the Ren'Py SDK installed.
#    (Available for Windows, macOS, and Linux)

# 2. Clone the repository
git clone https://github.com/sehaxe/minsk44.git

# 3. Open the Ren'Py Launcher.

# 4. Select 'Minsk 1944: No Name' in the project list.
#    (If not listed, click 'Add Project' and select the cloned directory.)

# 5. Click 'Launch Project'.
```

## 🛠️ Custom Tools & Scripts

The `scripts/` directory contains powerful custom Python tools used to simplify development and asset creation.

### 1. Dialogue Extractor (`dialogue_extractor.py`)

| Purpose | Description |
| :--- | :--- |
| **Function** | Extracts clean dialogue lines from `.rpy` files. |
| **Exclusions** | Automatically filters out narrator variables (`n_narr`, `narr`, `d_text`) to prevent noise. |
| **Usage** | `python dialogue_extractor.py` (processes all `.rpy` files in main directory) |
| **Output** | `dialogues_output.txt` (a single file with `[Character Name]: Dialogue Line`) |

### 2. KS-ify Image Processor (`ks_ify_image_processor.py`)

A GUI tool that applies custom OpenCV filters to images to create a highly stylized, painted visual novel background aesthetic.

<img width="1800" height="928" alt="Screenshot_20251113_173725" src="https://github.com/user-attachments/assets/345a38a6-3376-469f-9ddf-79f4d777484f" />

| Feature | Description |
| :--- | :--- |
| **Style** | GIMP-like Oilify, Median Blur, and Edge Subtraction to create a consistent VN art style. |
| **Batch Mode** | Select input and output directories to process hundreds of assets at once. |
| **Compression** | Automatic downscaling to **1920x1080** and saving as highly optimized **WebP** for efficient deployment. |
| **Usage** | Requires `customtkinter`, `opencv-python`, `numpy`, `pillow`. Run via `python ks_ify_image_processor.py`. |

### 3. Image Definition Generator (`image_definition_generator.py`)

| Purpose | Description |
| :--- | :--- |
| **Function** | Scans specified asset directories for all `.webp` files. |
| **Output** | Generates a clean `images.rpy` file with code like: `image filename = "path/to/asset.webp"`. |
| **Configuration** | Edit the `IMAGE_DIRS` list in the script to map source folders to Ren'Py prefixes. |
| **Usage** | `python image_definition_generator.py` |

## ✨ Credits & Acknowledgments

We extend our deepest gratitude to the tools and individuals who made this project possible.

> [!NOTE]
> **Special thanks to Ren'Py Tom (Tom Rothamel)** for developing the Ren'Py Visual Novel Engine.

| Contribution | Source/Creator |
| :--- | :--- |
| **Engine** | **Ren'Py Tom (Tom Rothamel)** |
| **Kinetic Text Tags** | Creators of the **Kinetic Text Tags** module |
| **Achievement Module** | Developers of the **Renpy Achievement** module |

### Development Team

*   **Scenario:** Arseniy Dernovskiy & Kajakulak Altay
*   **Art/Great Artist:** Footer Heart
*   **Design:** Arseniy Dernovskiy & Kajakulak Altay
*   **Programming:** Arseniy Dernovskiy
*   **Special Thanks:** Khalipov S.S., Zakharova A.S., Alexander Khaev, Alexandra Dernovskaya, Natalia Dernovskaya.

## 📃 License

| Component | License |
| :--- | :--- |
| **Game Assets** | Creative Commons (Refer to in-game credits for specific asset licenses.) |
| **Project Code** | This project is licensed under **GPL3** (General Public License v3). |
| **Third-Party Modules** | Kinetic Text Tags and Renpy Achievement modules belong to their respective creators and are used under their specified licenses. |
