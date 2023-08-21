'''
This script renames .MP3 files to .mp3 and converts .wma and .aac files to .wav.
'''

import os
from pydub import AudioSegment

# Conversion function
def convert_audio(input_path, output_path, format):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=format)


input_dir = 'none_mp3'
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)


for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    
    # Rename .MP3 to .mp3
    if file_name.endswith(".MP3"):
        new_name = file_name[:-4] + ".mp3"
        new_path = os.path.join(output_dir, new_name)
        os.rename(file_path, new_path)
    
    # Convert .wma to .wav
    elif file_name.endswith(".wma"):
        output_path = os.path.join(output_dir, file_name[:-4] + ".wav")
        convert_audio(file_path, output_path, "wav")
    
    # Convert .aac to .wav
    elif file_name.endswith(".aac"):
        output_path = os.path.join(output_dir, file_name[:-4] + ".wav")
        convert_audio(file_path, output_path, "wav")

