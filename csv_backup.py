"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 1
Week 15
Chat Gpt Assistance 
"""
import os
import shutil
import zipfile


# Step 1: Find CSV files
def find_csv_files():
    folder = "data"
    files = os.listdir(folder)

    csv_files = []
    for file in files:
        if file.endswith(".csv"):
            csv_files.append(file)

    print(f"Found {len(csv_files)} CSV files.")
    return csv_files


# Step 2: Move CSV files
def move_csv_files(csv_files):
    source_folder = "data"
    destination_folder = os.path.join(source_folder, "CSV_Files")

    # Create folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    count = 0

    for file in csv_files:
        src = os.path.join(source_folder, file)
        dst = os.path.join(destination_folder, file)

        shutil.move(src, dst)
        count += 1

    print(f"Moved {count} CSV files.")

    return destination_folder


# Step 3: Create ZIP file
def create_zip(folder):
    zip_name = "data_backup.zip"

    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            zipf.write(file_path, file)

    print("ZIP file created.")


def main():
    print("SCRIPT STARTED")
    csv_files = find_csv_files()

    if len(csv_files) == 0:
        print("No CSV files found.")
        return

    folder = move_csv_files(csv_files)

    create_zip(folder)


if __name__ == "__main__":
    main()