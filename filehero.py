import os
import shutil
import csv
import logging
from datetime import datetime

# Create a folder for logs if it does not exist
os.makedirs("logs", exist_ok=True)
log_filename = f"logs/filehero_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Mapping to destination folders
EXTENSION_FOLDERS = {
    '.pdf': 'Documents/PDFs',
    '.docx': 'Documents/Word',
    '.txt': 'Documents/Text',
    '.jpg': 'Images',
    '.png': 'Images',
    '.xlsx': 'Spreadsheets'
}

def organize_files(source_dir, dry_run=True):
    action_logs = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"report_{'dry_run_' if dry_run else ''}{timestamp}.csv"
    
    if not os.path.exists(source_dir):
        logging.error(f"The source file '{source_dir}' was not found.")
        return

    logging.info(f"=== Starting process (Dry Run: {dry_run}) ===")
    
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isdir(file_path):
            continue
            
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        subfolder = EXTENSION_FOLDERS.get(ext, 'Others')
        destination_folder = os.path.join(source_dir, subfolder)
        destination_path = os.path.join(destination_folder, filename)
        
        # Safe handling of double names
        if os.path.exists(destination_path):
            base, extension = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination_path):
                new_filename = f"{base}_{counter}{extension}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1
            logging.warning(f"Found a double. The file '{filename}' was renamed to '{os.path.basename(destination_path)}'.")

        status_str = 'Planned' if dry_run else 'Moved'
        
        action_logs.append({
            'filename': filename,
            'extension': ext,
            'destination': destination_path,
            'status': status_str
        })
        
        if not dry_run:
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file_path, destination_path)
            logging.info(f"Moved: {filename} -> {destination_path}")
        else:
            logging.info(f"[Dry Run] will move: {filename} -> {destination_path}")
            
    # CSV report
    with open(report_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['filename', 'extension', 'destination', 'status']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for log in action_logs:
            writer.writerow(log)
            
    logging.info(f"The CSV report was saved successfully: {report_filename}")
    logging.info(f"The logging file (log) was saved to: {log_filename}")

if __name__ == "__main__":
    target_directory = "test_files"
    
    # Dry Run 
    organize_files(target_directory, dry_run=False)
    
    