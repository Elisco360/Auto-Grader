import zipfile
import os
import shutil

# Specify the main zip file
main_zip_file = 'subs.zip'
main_folder = 'submissions'

# Create a temporary folder for extracting the main zip file
temp_main_folder = os.path.join(main_folder, 'temp_main_folder')

# Extract the main zip file
with zipfile.ZipFile(main_zip_file, 'r') as main_zip_ref:
    main_zip_ref.extractall(temp_main_folder)

# Iterate through all files in the temporary main folder
for user_folder in os.listdir(temp_main_folder):
    user_folder_path = os.path.join(temp_main_folder, user_folder)

    # Check if the file is a directory
    if os.path.isdir(user_folder_path):
        # Get the user's name from the folder structure
        user_name = user_folder.split('_')[0]

        # Specify the destination folder based on the user's name
        destination_folder = os.path.join(main_folder, user_name)

        # Move the contents of the user's folder to the destination folder
        for root, dirs, files in os.walk(user_folder_path):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(source_path, destination_path)

# Remove the temporary main folder
shutil.rmtree(temp_main_folder)

print(f'Successfully extracted and organized files from {main_zip_file}')
