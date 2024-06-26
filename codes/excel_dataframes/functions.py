import pandas as pd
import os
import requests

def get_NetflixData(url, path, file):
    # Create the 'data' directory if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # Path to save the downloaded file
    file_path = os.path.join(path, file)

    # Download the file
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful    

    # Save the content to the file
    with open(file_path, 'wb') as file:
        file.write(response.content)

    print(f"File downloaded and saved to {file_path}")    

def create_NetflixExcelFile():
    get_NetflixData('https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv', 'raw_data', 'all-weeks-global.tsv')
    get_NetflixData('https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv', 'raw_data', 'all-weeks-countries.tsv')
    get_NetflixData('https://www.netflix.com/tudum/top10/data/most-popular.tsv', 'raw_data', 'most-popular.tsv')

    # Define the input folder and output folder
    input_folder = 'raw_data'
    output_folder = 'data'

    # Define the TSV files and their corresponding sheet names
    files = {
        'all-weeks-global.tsv': 'all-weeks-global',
        'all-weeks-countries.tsv': 'all-weeks-countries',
        'most-popular.tsv': 'most-popular'
    }

    # Define the output Excel file path
    output_file = os.path.join(output_folder, 'Netflix Top 10 Weekly Dataset.xlsx')

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create a Pandas Excel writer using openpyxl as the engine
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for file_name, sheet_name in files.items():
            # Read each TSV file into a DataFrame
            file_path = os.path.join(input_folder, file_name)
            df = pd.read_csv(file_path, sep='\t')
            
            # Write the DataFrame to the specified sheet in the Excel file
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Excel file created at {output_file}")
