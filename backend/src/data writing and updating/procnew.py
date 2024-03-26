import os
import data_upload_update as uu

def process_new_files():
    new_files_folder = "newfiles"
    # Check if the new files folder exists
    if os.path.exists(new_files_folder):
        # Get all files in the folder
        files = os.listdir(new_files_folder)
        for file in files:
            file_path = os.path.join(new_files_folder, file)  # Corrected line
            # Read and process each file
            uu.update_student_data(file_path, file)  # Corrected line

    else:
        print(f"Folder '{new_files_folder}' not found.")


if __name__ == '__main__':
    process_new_files()