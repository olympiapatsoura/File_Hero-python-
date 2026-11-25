# FileHero 

**FileHero** is a lightweight and user-friendly Python tool designed to clean up and automatically organize your folders by sorting files based on their extensions. Additionally, it includes a helper generator for creating test files so you can test its functionality immediately and safely.

## Features

* **Automatic Sorting:** Categorizes documents, images, and spreadsheets into their respective subfolders (`Documents/PDFs`, `Images`, `Spreadsheets`, etc.).
* **Data Safety & Duplicate Handling:** If a file with the same name already exists in the destination, it automatically appends a numeric index (e.g., `filename_1.ext`) to prevent any overwrites.
* **Comprehensive Logging:** Detailed logging of every action in a `logs/` folder with timestamps.
* **CSV Reports:** Automatically generates a report file (`.csv`) detailing all performed actions.
* **Test Environment Generator:** Includes a script for mass-creating test files.

## File Structure

* `filehero.py`: The main script that handles file organization and movement, as well as log and report generation.
* `file_generator.py`: A helper script that creates a `test_files` folder populated with random test files of various types (`.pdf`, `.jpg`, `.png`, `.txt`, `.docx`, `.xlsx`) for testing purposes.

## Usage Instructions

### 1. Create Test Files (Optional)
If you want to test the tool without using your personal files, run:
python file_generator.py

### 2. Run Organization
Run the main script to organize the contents of the target folder:
python filehero.py
Note: In the current code, the target directory is set to "test_files". You can change it by modifying the target_directory variable inside filehero.py.

## Technologies
The project is built entirely in Python (3.x) using only built-in standard libraries (no external pip packages required):

os & shutil (File and folder management)

logging (Event logging)

csv (Report generation)

datetime (Timestamp and date management)
