"""
this Python script read all csv files from provided path
downloads all links provided in the second column of the CSV file
saves them in a specified folder with same name as the CSV file
Please specify path folder containing CSV files and path of Output folder
"""
import csv
import os
import requests
import time


# provide folder path where csv files stored
CSV_FOLDER_PATH = "/home/accubits/Desktop/PyScript"

# provide the path where the output folders needs to be created
OUTPUT_FOLDER_PATH = "/home/accubits/Desktop/Output"

csv_files = [file for file in os.listdir(CSV_FOLDER_PATH) if file.endswith('.csv')]

for csv_file in csv_files:
    print(f"Performing operations for {CSV_FOLDER_PATH}{csv_file}")

    file_name = csv_file.split(".")[0]

    folder_name = os.path.splitext(file_name)[0]

    path = os.path.join(OUTPUT_FOLDER_PATH, folder_name)

    if not os.path.exists(path):
        os.makedirs(path)

    # download files from the link in the second column of the CSV
    with open(f"{CSV_FOLDER_PATH}/{csv_file}", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            img_url = row[1]
            # perform a double check to make sure string is url
            if "/" and "." in img_url:
                # download file and save to desired folder
                print(f"Downloading {img_url}")
                response = requests.get(img_url)
                img_file_name = img_url.split('/')[-1]
                open(f"{path}/{img_file_name}", 'wb').write(response.content)
                print(f"The file was saved and retrieved from the location {path}/{img_file_name}")
                time.sleep(3)

print("Process completed successfully")
