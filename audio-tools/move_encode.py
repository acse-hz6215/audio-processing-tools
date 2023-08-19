'''
This script moves all the none .mp3 files from a directory to another directory.
将文件夹中的非mp3文件移动到另一个文件夹中
'''

import os
import shutil

input_dir = 'test'
output_dir = 'none_mp3'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for filename in os.listdir(input_dir):
    source_path = os.path.join(input_dir, filename)


    if os.path.isfile(source_path):
        # 获取文件的后缀
        file_extension = os.path.splitext(filename)[1]

        if file_extension != '.mp3':
            target_path = os.path.join(output_dir, filename)
            shutil.move(source_path, target_path)
            print(f"Moved '{filename}' to target folder.")
