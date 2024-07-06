import os
from datetime import datetime
import re

def get_file_creation_date(filename):
    try:
        filetime = os.path.getctime(filename)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    else:
        return datetime.fromtimestamp(filetime).strftime('%Y%m%d')

def rename_files_in_directory(dir, ext=['docx', 'odt']):
    date_pattern = re.compile(r'\d{4,8}')  # This pattern will match any sequence of four to eight digits (i.e., a date in YYYYMMDD format)
    
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

                # Check if filename already begins with a date in YYYYMMDD format
                match = re.match(date_pattern, base)
                if match:  # If base starts with a string containing a date
                    print(f"Skipping {filename}, as it appears to start with a date.")
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

