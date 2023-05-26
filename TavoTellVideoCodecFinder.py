import os
import subprocess
import argparse

def findFile(folder,codec_list):
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
            if file_codec.stdout.strip() in codec_list:
                print(f"{full_path}")

def main():
    # Arguments are obtained from the terminal
    parser = argparse.ArgumentParser(description="Tavo Tell's Video Codec Finder")

    # I define the arguments
    parser.add_argument('-folder', dest='search_folder', help='Search files in this folder and subfolders')
    parser.add_argument('-codecs', dest='codec_list', action='append', help='List of codec to search. Eg: h264,h265, etc.')

    # Parsing Arguments
    args = parser.parse_args()
    codec_list = [argument.split(',') for argument in args.codec_list][0]
    
    # I call the function with a specific folder
    findFile(args.search_folder, codec_list)

if __name__ == "__main__":
    main()