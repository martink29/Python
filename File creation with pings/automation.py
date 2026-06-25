import os
import sys
import subprocess

def system_automation_example():
    print("=== Начало на системния скрипт ===")

    print (f"1. OS: {sys.platform}")

    current_dir = os.getcwd()
    print(f"2. Current dir: {current_dir}")

    folder_name = "backup_test_folder"
    folder_path = os.path.join(current_dir, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"    -> A new folder was created: {folder_name}")
    else:
        print(f"   -> Папката '{folder_name}' вече съществува.")

    # Създаване на тестов файл в новата папка
    file_path = os.path.join(folder_path, "system_info.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Системна платформа: {sys.platform}\n")
        file.write(f"Директория: {current_dir}\n")
    print(f"   -> Файлът '{file_path}' беше записан успешно.")

    # 3. Използване на 'subprocess' за стартиране на външна команда
    print("\n3. Изпълнение на външна системна команда (ping към google.com):")

    ping_command = ["ping", "-n", "2", "google.com"] if sys.platform == "win32" else ["ping", "-c", "2", "google.com"]

    try:
        # Изпълняваме командата и прихващаме резултата
        result = subprocess.run(ping_command, capture_output=True, text=True)
        print("--- Резултат от командата ---")
        print(result.stdout)
    except Exception as e:
        print(f"Възникна грешка при изпълнението на командата: {e}")
        
if __name__ == "__main__":
    system_automation_example()
