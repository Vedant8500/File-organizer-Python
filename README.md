# File Organizer Python

A simple file organization script using Python to automatically sort files into categorized folders like Images, Documents, Videos, and Others.

## 📂 How It Works

- Scans the specified folder
- Detects file types by extension
- Moves files into folders:
  - Images (`.jpg`, `.jpeg`, `.png`, `.gif`)
  - Documents (`.pdf`, `.docx`, `.txt`)
  - Videos (`.mp4`, `.mkv`, `.avi`)
  - Others (uncategorized files)

## 🚀 How to Run

1. Install Python (if not already)
2. Clone/download this repo
3. Edit the last line in `File manager.py` to your target path:
   ```python
   organize_folder("G:/YourFolder")
