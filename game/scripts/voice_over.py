import re
import os
import argparse
from glob import glob
from typing import Dict, List, Tuple

# --- Настройки для фильтрации ---

# 1. Список переменных персонажей, которых нужно исключить (на основе предоставленного примера)
NARRATOR_VARS_TO_EXCLUDE = {
    "n_narr",     # Безымянный (NVL)
    "narr",       # Безымянный (ATL)
    "d_text",     # Автор
    "scene_narr", # Без имени
    "variant",
    "style",
    "color",
    "id",
    "font",
    "text",
    "style_prefix",
    "background",
    "thumb",
    "key",
    "label",
    "add",
    "layout",
    "foreground",
    "size_group",
    "hover_color",
    "scrollbars",
    "if",
    "textbutton",
    "kolya",
    "grandson",
    "ivan",
    "politruk",
    "soldier",
    "civil",
    "hanz",
    "old_man",
    "old_woman"
}

OUTPUT_FILENAME = "dialogues_output.txt"

def extract_dialogues_from_text(script_content: str) -> List[Tuple[str, str]]:
    """
    Извлекает диалоги и имена персонажей из содержимого Ren'Py скрипта.
    """
    
    # 1. Регулярное выражение для извлечения переменной персонажа и его отображаемого имени из `define`
    char_define_pattern = re.compile(
        r'^\s*define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*Character\("((?:\\.|[^"])*)",', 
        re.MULTILINE
    )
    
    # 2. Регулярное выражение для извлечения диалога
    dialogue_pattern = re.compile(
        r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+"((?:\\.|[^"])*)"', 
        re.MULTILINE
    )

    char_map: Dict[str, str] = {}
    
    # --- Фаза 1: Создание карты персонажей ---
    for match in char_define_pattern.finditer(script_content):
        var_name = match.group(1).strip()
        display_name = match.group(2).strip()
        char_map[var_name] = display_name
        
    # --- Фаза 2: Извлечение и фильтрация диалогов ---
    extracted_dialogues: List[Tuple[str, str]] = []

    for match in dialogue_pattern.finditer(script_content):
        var_name = match.group(1)
        dialogue = match.group(2)
        
        # 1. Фильтрация по переменной
        if var_name in NARRATOR_VARS_TO_EXCLUDE:
            continue
            
        # 2. Фильтрация по отображаемому имени
        display_name = char_map.get(var_name, var_name)
        if display_name in ("Безымянный", "Автор"):
            continue
            
        extracted_dialogues.append((display_name, dialogue))

    return extracted_dialogues

def get_rpy_files_to_process(directory: str, files: List[str]) -> List[str]:
    """
    Определяет список RPY файлов для обработки на основе переданных аргументов.
    Если указаны конкретные файлы, возвращает их. Иначе сканирует директорию.
    """
    if files:
        # Если указаны конкретные файлы, используем их
        print(f"Будут обработаны только указанные файлы: {files}")
        return [f for f in files if f.endswith('.rpy')]
    else:
        # Иначе сканируем директорию
        search_path = os.path.join(directory, "*.rpy")
        rpy_files = glob(search_path)
        if not rpy_files:
            print(f"В директории '{directory}' не найдено ни одного .rpy файла по пути: {search_path}")
        return rpy_files


def process_rpy_files_and_write_to_file(rpy_files: List[str], source_desc: str, output_file: str = OUTPUT_FILENAME) -> None:
    """
    Обрабатывает список .rpy файлов и записывает результаты в файл.
    """
    all_dialogues: List[Tuple[str, str]] = []
    
    if not rpy_files:
        print("Список файлов для обработки пуст. Работа завершена.")
        return

    print(f"Найдено {len(rpy_files)} .rpy файлов для обработки. Начинаю сбор данных…")

    # Сначала собираем все диалоги
    for file_path in rpy_files:
        try:
            print(f"Обработка файла: {file_path}")
            # Используем try/except для открытия файла, чтобы избежать проблем с кодировкой
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_dialogues = extract_dialogues_from_text(content)
            all_dialogues.extend(file_dialogues)
            
        except FileNotFoundError:
             print(f"Ошибка: Файл не найден {file_path}. Проверьте путь.")
        except Exception as e:
            print(f"Ошибка при обработке файла {file_path}: {e}")
    
    # Затем записываем все в файл
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write("="*50 + "\n")
            outfile.write(f"Извлеченные диалоги из: {source_desc}\n")
            outfile.write("Исключены нарраторы ('Безымянный', 'Автор', переменные в NARRATOR_VARS_TO_EXCLUDE).\n")
            outfile.write("="*50 + "\n\n")

            for character, line in all_dialogues:
                outfile.write(f"[{character}]: {line}\n")
                
        print("\n" + "="*50)
        print(f"Успешно записано {len(all_dialogues)} реплик в файл: {output_file}")
        print("Этот файл находится в текущей директории, где был запущен скрипт.")
        print("="*50)

    except Exception as e:
        print(f"Критическая ошибка при записи в файл {output_file}: {e}")


# --- Основная часть скрипта: Парсинг аргументов ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Извлекает диалоги персонажей (кроме нарраторов) из Ren'Py (.rpy) файлов."
    )
    
    # Аргумент для указания конкретных файлов
    parser.add_argument(
        "-f", "--files",
        type=str, 
        nargs='+', # Ожидаем один или несколько аргументов
        help="Список конкретных .rpy файлов для обработки (пример: -f script.rpy options.rpy)."
    )
    
    # Аргумент для указания директории (используется, только если --files не указан)
    parser.add_argument(
        "directory_path", 
        type=str, 
        nargs='?', 
        default=".", 
        help="Путь к директории, содержащей .rpy файлы (используется, если --files не указан; по умолчанию: текущая директория)."
    )
    
    args = parser.parse_args()
    
    # 1. Определяем список файлов
    rpy_files_to_process = get_rpy_files_to_process(args.directory_path, args.files)
    
    # 2. Определяем описание источника для заголовка файла
    if args.files:
        source_description = "указанных файлов"
    else:
        source_description = f"файлов в директории: {args.directory_path}"

    # 3. Запускаем обработку
    process_rpy_files_and_write_to_file(rpy_files_to_process, source_description)