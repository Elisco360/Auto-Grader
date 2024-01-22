import os
import shutil
from zipfile import ZipFile


def extract_and_organize(zip_file_path, output_folder):
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)


def organize_submission(submission_folder):
    for root, dirs, files in os.walk(submission_folder):
        for file in files:
            if file.endswith('.py') or file.endswith('.java'):
                source_path = os.path.join(root, file)
                destination_folder = os.path.join(submission_folder, os.path.basename(root))
                destination_path = os.path.join(destination_folder, file)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.copy(source_path, destination_path)


def main():
    submissions_zip = 'subs.zip'
    output_folder = 'subs'

    # Extract the submissions.zip
    extract_and_organize(submissions_zip, output_folder)

    # Organize the extracted contents
    for submission_folder in os.listdir(output_folder):
        submission_path = os.path.join(output_folder, submission_folder)
        if os.path.isdir(submission_path):
            organize_submission(submission_path)


if __name__ == "__main__":
    main()
