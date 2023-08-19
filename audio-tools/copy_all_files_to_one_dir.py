'''
This script copies all the files from mutiple subdirectories to a single directory.
'''

import os
import shutil

input_dir = 'music-backup'
output_dir = 'output'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        # Construct the full path of the file
        input_dir_path = os.path.join(dirpath, filename)
        output_dir_path = os.path.join(output_dir, filename)

        # Check if the file already exists 
        counter = 1
        while os.path.exists(output_dir_path):
            output_dir_path = os.path.join(output_dir, f"{filename.split('.')[0]}_{counter}.{filename.split('.')[-1]}")
            counter += 1

        # Copy the file to the output directory
        shutil.copy2(input_dir_path, output_dir_path)
        print(f"Copied {input_dir_path} to {output_dir_path}")

print("Copying completed.")

