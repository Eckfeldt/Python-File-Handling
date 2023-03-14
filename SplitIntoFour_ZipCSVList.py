import os
import zipfile
import math

def split_zip_file(zip_file_path, num_splits=4):
    # Open the input zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Get the list of all file names in the input zip file
        file_list = zip_file.namelist()
        
        # Calculate the number of files to include in each split
        num_files_per_split = math.ceil(len(file_list) / num_splits)
        
        # Create the output zip files and split the input files across them
        for i in range(num_splits):
            # Define the name of the output zip file
            output_zip_file_name = os.path.splitext(zip_file_path)[0] + '_split{}.zip'.format(i+1)
            
            # Create a new empty output zip file
            with zipfile.ZipFile(output_zip_file_name, 'w', compression=zipfile.ZIP_DEFLATED) as output_zip_file:
                # Determine the range of files to include in this split
                start_index = i * num_files_per_split
                end_index = min(start_index + num_files_per_split, len(file_list))
                
                # Add the selected files to the output zip file
                for j in range(start_index, end_index):
                    file_name = file_list[j]
                    file_data = zip_file.read(file_name)
                    output_zip_file.writestr(file_name, file_data)

if __name__ == '__main__':
    # Specify the path to the input zip file
    zip_file_path = 'D:\output.zip'
    
    # Split the input zip file into 4 parts
    split_zip_file(zip_file_path, num_splits=4)
