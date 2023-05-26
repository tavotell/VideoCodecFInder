import os
import subprocess

def findFile(folder):
    # I take the files in specified folder and subfolders
    for path, folders, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(path, file)

            # I use ffprobe to get the file codec
            file_codec = subprocess.run(
                ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=codec_name', '-of', 'default=noprint_wrappers=1:nokey=1', full_path],
                capture_output=True,
                text=True)

            # If codec is H264, print file full path in terminal
            if file_codec.stdout.strip() == 'h264':
                print(f"{full_path}")

# I call the function with a specific folder
findFile("/media/tavo/XPG/AKB48")