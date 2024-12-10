import os
import requests
import zipfile

# Define the directory where you want to save the ZIP files and extract them
save_dir = r"U:\BigData\CompaniesHouse\2024-11"
extract_dir = os.path.join(save_dir, 'psc')

# Ensure the directories exist
os.makedirs(save_dir, exist_ok=True)
os.makedirs(extract_dir, exist_ok=True)

# Base URL for the files
base_url = "https://download.companieshouse.gov.uk/psc-snapshot-2024-11-16_{}of28.zip"

# Loop through all 27 files
for i in range(1, 28):
    url = base_url.format(i)
    file_name = f"psc-snapshot-2024-11-16_{i}of28.zip"
    
    print(f"Downloading {file_name}...")
    
    # Request the file from the server
    response = requests.get(url)
    
    # Define the full file path
    zip_file_path = os.path.join(save_dir, file_name)
    
    # Save the ZIP file
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Saved {file_name} successfully at {zip_file_path}.")
    
    # Unzip the file into the 'psc' directory
    print(f"Unzipping {file_name} into {extract_dir}...")
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"Unzipped {file_name} successfully into {extract_dir}.")

print("All files downloaded and unzipped.")
