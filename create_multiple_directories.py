import os

# Define the base directory where you want to create the folders
base_directory = "C:\\Users\\justi\\Documents\\CS50P"  # Replace with your desired path

# Create directories in the pattern "Lecture<N>"
for i in range(13):  # Creates folders with numbers 0 to 12
    folder_name = f"Lecture{i}"
    folder_path = os.path.join(base_directory, folder_name)

    # Check if the folder already exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
