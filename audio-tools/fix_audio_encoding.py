'''
This script is used to fix the encoding of audio tags.
修复音频中的乱码问题，将字符串从ISO-8859-1编码转换到GB2312编码
'''

import os
import eyed3

def fix_encoding(string):
    try:
        return string.encode('ISO-8859-1').decode('GB2312')
    except Exception as e:
        print(f"Failed to fix encoding for string '{string}': {e}")
        return string

def fix_audio_tag(file_path):
    audiofile = eyed3.load(file_path)
    if audiofile.tag is not None:
        audiofile.tag.artist = fix_encoding(audiofile.tag.artist) if audiofile.tag.artist is not None else None
        audiofile.tag.album = fix_encoding(audiofile.tag.album) if audiofile.tag.album is not None else None
        audiofile.tag.title = fix_encoding(audiofile.tag.title) if audiofile.tag.title is not None else None
        audiofile.tag.album_artist = fix_encoding(audiofile.tag.album_artist) if audiofile.tag.album_artist is not None else None
        try:
            audiofile.tag.save(encoding='utf-8')
        except Exception as e:
            print(f"Failed to save tag for file '{file_path}': {e}")

def fix_folder_tags(input_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.mp3'):
                fix_audio_tag(os.path.join(root, file))

if __name__ == '__main__':
    input_dir = 'temp'  # 修改为你的文件夹路径
    fix_folder_tags(input_dir)
