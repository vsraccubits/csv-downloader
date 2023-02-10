"""
this Python script read all csv files from provided path
downloads all links provided in the second column of the CSV file
saves them in a specified folder with same name as the CSV file
Please specify path folder containing CSV files and path of Output folder
"""
import csv
import os

from concurrent import futures
from urllib import request


# provide folder path where csv files stored
CSV_FOLDER_PATH = "/home/accubits/Desktop/PyScript"

# provide the path where the output folders needs to be created
OUTPUT_FOLDER_PATH = "/home/accubits/Desktop/Output"


def download_file(url: str, path: str) -> str:
    """Download file from url and save to path.

    Keyword arguments:
    url -- download link
    path -- file save location 
    """
    img_file_name = url.split('/')[-1]
    file_path = f"{path}/{img_file_name}"
    request.urlretrieve(url, file_path)
    return file_path

csv_files = [file for file in os.listdir(CSV_FOLDER_PATH) if file.endswith('.csv')]

for csv_file in csv_files:
    print(f"Performing operations for {CSV_FOLDER_PATH}{csv_file} 🚀")

    file_name = csv_file.split(".")[0]

    folder_name = os.path.splitext(file_name)[0]

    path = os.path.join(OUTPUT_FOLDER_PATH, folder_name)

    if not os.path.exists(path):
        os.makedirs(path)

    # store all urls from csv file
    urls_list = []

    with open(f"{CSV_FOLDER_PATH}/{csv_file}", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            img_url = row[1]
            # perform a double check to make sure string is url
            if "/" and "." in img_url:
                urls_list.append(img_url)
    
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        # start load operations
        future_to_file = {executor.submit(download_file, url, path): url for url in urls_list}

        for future in futures.as_completed(future_to_file):
            url = future_to_file[future]
            try:
                file_path = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('file saved to %r' % (url))

print("Process completed successfully ✅")
