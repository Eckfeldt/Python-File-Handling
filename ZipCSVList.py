import csv
import os
import zipfile

def zip_files_from_csv(file_path, zip_file_path):
    """
    Reads a CSV file containing file paths and zips each file into a single ZIP file.
    :param file_path: The file path of the input CSV file.
    :param zip_file_path: The file path of the output ZIP file.
    """
    # Open the input CSV file for reading.
    with open(file_path, 'r') as csv_file:
        # Create a new ZIP file for writing.
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Create a CSV reader object to iterate over the rows in the input CSV file.
            csv_reader = csv.reader(csv_file)
            # Skip the first row of the CSV file (i.e., the header row).
            next(csv_reader)
            # Iterate over each row in the input CSV file.
            for row in csv_reader:
                # Get the file path from the first (and only) column in the current row.
                file_to_zip = row[0]
                # Add the file to the ZIP file using just the file name (without directory path).
                zip_file.write(file_to_zip, arcname=os.path.basename(file_to_zip))

    # Print out the contents of the ZIP file for debugging purposes.
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        print(f'Contents of {zip_file_path}:')
        for info in zip_file.infolist():
            print(info.filename)

# Example usage:
zip_files_from_csv(r'D:\Reunion Exploration Dropbox\MATTHEW ECKFELDT\IMAGO Setup\Files to Zip V2.csv', 'output.zip')
