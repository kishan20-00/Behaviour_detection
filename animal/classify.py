import os
import csv

def extract_text_from_filename(filename):
    # Extract text from the filename until the "_" symbol
    return filename.split('_')[0]

def create_csv_with_file_text_mapping(source_dirs, csv_file):
    # Create CSV file and write header
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Text'])
        
        # Iterate through source directories and extract text from file names
        for source_dir in source_dirs:
            # Collect all files from the source directory
            files = [f for f in os.listdir(source_dir) if f.endswith('.mp4') and os.path.isfile(os.path.join(source_dir, f))]
            
            # Extract text from file names and write to CSV
            for file_name in files:
                # Extract text from filename
                text = extract_text_from_filename(file_name)
                
                # Write to CSV
                writer.writerow([file_name, text])

# Replace these paths with your source directories and CSV file path
source_dirs = ['F:/KA Projects/Thushani/animal/Images/test']
csv_file = 'test.csv'  # CSV file path

create_csv_with_file_text_mapping(source_dirs, csv_file)
