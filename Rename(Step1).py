import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Counter for renaming
    counter = 1

    # Loop through each file
    for filename in files:
        # Check if it's a file (not a folder)
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Get the file extension
            ext = os.path.splitext(filename)[1]

            # New filename with 'R' prefix and counter
            new_filename = f"r{counter}{ext}"

            # Build the new path
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(os.path.join(folder_path, filename), new_path)

            # Increment counter
            counter += 1

# Specify the folder containing the images
folder_path = "E:\OneDrive\Music\pqrst\SMALLR" 

# Rename images in the folder
rename_images(folder_path)
