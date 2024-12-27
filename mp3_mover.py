import os
import shutil

def move_mp3_files(target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    current_directory = os.getcwd()
    
    for file_name in os.listdir(current_directory):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(current_directory, file_name)
            shutil.move(file_path, target_folder)
            print(f"Moved: {file_name}")

target_folder = "mp3_files"

move_mp3_files(target_folder)
