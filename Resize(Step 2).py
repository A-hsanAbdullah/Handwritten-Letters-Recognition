import os
import cv2

def convert_folder_to_grayscale_and_resize(input_folder, output_folder, target_size=(128, 128)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check if the file is an image
            # Read the image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resize the grayscale image
            resized_image = cv2.resize(grayscale_image, target_size)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_image)

            print(f"Converted: {filename}")

# Example usage:
input_folder = "E:\OneDrive\Pictures\CP_2\cpraw"  # Specify the path to the input folder containing images
output_folder = "E:\OneDrive\Pictures\CP_2\J1"  # Specify the path to the output folder
convert_folder_to_grayscale_and_resize(input_folder, output_folder)
