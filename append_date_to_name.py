import os
from datetime import datetime

def get_file_creation_date(filename):
    filetime = os.path.getctime(filename)
    return datetime.fromtimestamp(filetime).strftime('%Y%m%d')

def rename_files_in_directory(dir, ext=['docx', 'odt']):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if any(file.endswith('.' + e) for e in ext):
                filename = os.path.join(root, file)
                creation_date = get_file_creation_date(filename)
                
                # Correctly extract the base name and extension
                base, extension = os.path.splitext(file)

                 # Check if filename already begins with the date
                if base.startswith(creation_date):
                    print(f"Skipping {filename}, as it appears to already have a creation date.")
                    continue  # Skip this file and move on to the next one

                new_name = f"{creation_date}_{base}{extension}"
                
                # Form the full path for the new filename
                new_filename = os.path.join(root, new_name)
                
                os.rename(filename, new_filename)

def get_directory():
    while True:
        dir = input("Please enter the directory (e.g., 'C:\\my directory') in which you want to make changes: ")
        
        if os.path.isdir(dir):
            return dir
        else:
            print("Invalid directory. Please try again.")

if __name__ == "__main__":
    dir = get_directory()
    rename_files_in_directory(dir)

