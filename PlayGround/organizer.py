import os
import shutil

EXTENSIONS = {
    ".jpg" : "Images",
    ".jpeg": "Images",
    ".png" : "Images",
    ".pdf" : "Documents",
    ".docx": "Documents",
    ".txt" : "Documents",
    ".zip" : "Compressed",
    ".exe" : "Executables",
}

folder_path = input("Enter folder path to Organize: ")

if os.path.exists(folder_path):
    files = os.listdir(folder_path)

    for file in files:
        file_src = os.path.join(folder_path, file)

        if os.path.isdir(file_src): # Skipping the same files
            continue

        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in EXTENSIONS:
            subfolder_name = EXTENSIONS[ext]
        else:
            subfolder_name = "Others"

        target_dir = os.path.join(folder_path, subfolder_name)

        os.makedirs(target_dir, exist_ok=True)
        file_dest = os.path.join(target_dir, file)

        shutil.move(file_src, file_dest)
        print(f"Moved: {file} -> {subfolder_name}/")
    print("\n✨ All files organized successfully!")

else:
    print("Folder not Found.")
