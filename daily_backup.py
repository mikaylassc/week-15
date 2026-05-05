"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 2
Week 15
Chat Gpt Assistance 
"""
import os
import zipfile
from datetime import datetime


def create_backup_folder():
    if not os.path.exists("backups"):
        os.makedirs("backups")


def create_zip_backup():
    folder = "important_files"
    files = os.listdir(folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    zip_name = f"backups/backup_{timestamp}.zip"

    with zipfile.ZipFile(zip_name, "w") as zipf:
        for file in files:
            file_path = os.path.join(folder, file)
            zipf.write(file_path, arcname=file)

    return zip_name, len(files)


def log_backup(zip_name, file_count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("backup_log.txt", "a") as log:
        log.write(f"{timestamp} - Created {zip_name} ({file_count} files)\n")


def main():
    create_backup_folder()

    zip_name, file_count = create_zip_backup()

    log_backup(zip_name, file_count)

    print(f"Backup created: {zip_name}")
    print(f"Files backed up: {file_count}")


if __name__ == "__main__":
    main()