import os
import shutil

def organize_folder(folder_path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Others': []
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    target_folder = os.path.join(folder_path, category)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder_path, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

    print("\n✅ Files organized successfully!")

# Modify this path to your real test folder path
folder_to_organize = "G:/Test Folder"

try:
    organize_folder(folder_to_organize)
except FileNotFoundError:
    print(f"\n❌ Folder not found: {folder_to_organize}")
except PermissionError:
    print("\n❌ Permission error. Try running as administrator.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")

input("\nPress Enter to exit...")
