import os

# 1. Target Folder Path (Disk D: par Test_Folder)
target_dir = r"D:\Test_Folder"

# 2. Dummy files list (Alag extensions ke sath)
files_to_create = [
    "sample1.txt",
    "notes.txt",
    "report.pdf",
    "invoice.pdf",
    "photo1.jpg",
    "background.png",
    "archive.zip",
    "setup.exe",
    "random_data.xyz",  # Unknown extension for "Others" category
]

# 3. Agar D:\Test_Folder exist nahi karta toh bana do
os.makedirs(target_dir, exist_ok=True)

# 4. Files create karo aur dummy text daalo
for file_name in files_to_create:
  file_path = os.path.join(target_dir, file_name)

  # Standard 'w' mode file create aur text write karne ke liye
  with open(file_path, "w") as f:
    f.write(f"This is sample content for {file_name}\nCreated for testing.")

print(f"✅ Success! {len(files_to_create)} dummy files created in '{target_dir}'.")