import os
import shutil

def delete_files_except_first_two(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Recursively process subfolders
    for root, _, files in os.walk(folder_path):
        # Sort files to ensure consistent order
        files.sort()

        # Delete all files except the first two in each subfolder
        for file_name in files[150:]:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    delete_files_except_first_two(folder_path)
