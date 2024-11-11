import os
import shutil
import re

# Path to the folder containing the images
source_folder = 'path to the fake dataset either /train/FAKE or /test/FAKE'
base_dest_folder = 'path to your directory under which 10 different directories will be created.'

# Number of directories = number of classes 
num_dirs = 10

# Create the directories if they don't already exist
for i in range(1, num_dirs + 1):
    os.makedirs(os.path.join(base_dest_folder, f"{i}"), exist_ok=True)

#Get a list of all image files in the source folder
images = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Loop through images and move each one to the corresponding directory
for image in images:
    match = re.search(r"\((\d+)\)", image)
    number_in_bracket = 1
    if match:
     number_in_bracket = match.group(1)
    dir_index = str(number_in_bracket) 
    print(image)
    print(dir_index)

    dest_dir = os.path.join(base_dest_folder, f"{dir_index}")
 
    # Define source and destination paths
    source_path = os.path.join(source_folder, image)
    dest_path = os.path.join(dest_dir, image)
    
    # Move the image to the destination directory
    shutil.move(source_path, dest_path)

print("Images have been sorted into directories.")
