import os
import random

def create_test_files(num_files=100):
    folder_name = "test_files"
    os.makedirs(folder_name, exist_ok=True)
    
    extensions = ['.pdf', '.jpg', '.png', '.txt', '.docx', '.xlsx']
    
    for i in range(1, num_files + 1):
        ext = random.choice(extensions)
        filename = f"file_{i:03d}{ext}"
        filepath = os.path.join(folder_name, filename)
        
        # Creating files for testing
        with open(filepath, 'w') as f:
            f.write(f"This is test file number {i}")
            
    print(f"Successfully created {num_files} files in folder '{folder_name}'.")

if __name__ == "__main__":
    create_test_files()