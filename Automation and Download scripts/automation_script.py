import shutil
import os
import datetime

def backup_files(source_dir, backup_dir):
    today = datetime.date.today()
    backup_folder = os.path.join(backup_dir, str(today))
    
    os.makedirs(backup_folder, exist_ok=True)
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            backup_path = os.path.join(backup_folder, file)
            shutil.copy2(source_path, backup_path)
            print(f"Backed up: {source_path} to {backup_path}")

if __name__ == "__main__":
    source_directory = "/path/to/source/files"
    backup_directory = "/path/to/backup/location"
    backup_files(source_directory, backup_directory)

print("The operation was succesful")