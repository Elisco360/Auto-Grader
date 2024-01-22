import os
from zipfile import ZipFile

def unzip_and_organize(zip_folder, output_folder):
    for zip_file in os.listdir(zip_folder):
        zip_file_path = os.path.join(zip_folder, zip_file)
        student_name = os.path.splitext(zip_file)[0]

        destination_folder = os.path.join(output_folder, student_name)
        with ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)

def main():
    zip_folder = 'subs/subs'
    output_folder = 'submissions'

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Unzip and organize the contents
    unzip_and_organize(zip_folder, output_folder)


if __name__ == "__main__":
    main()
