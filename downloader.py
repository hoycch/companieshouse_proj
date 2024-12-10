import os
import requests

# Define the directory where you want to save the files
save_dir = r"U:\BigData\CompaniesHouse\2024-11"

# Ensure the directory exists
os.makedirs(save_dir, exist_ok=True)

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
    file_path = os.path.join(save_dir, file_name)
    
    # Save the file to the specified directory
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Saved {file_name} successfully at {file_path}.")

print("All files downloaded.")
