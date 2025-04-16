# search_files(): [Audio] or [Playlist]
# list_dir_and_files(): [Audio], [Playlist], and [DIR]
# generate_playlist(): Creates .m3u
# edit_file(): Edits .m3u files
# get_metadata(): Returns metadata of file.
import sys
import os
import re


def is_valid():
    try:
        if sys.argv[1]:
            if os.path.exists(sys.argv[1]):
                return True
            else:
                return False
        pass
    except Exception:
        return False


# Search for audio and playlist files in a directory
# Search must be within allowed directories and valid path
def search_files(pat: str):
    extnames = {
        "mp3": "Audio",
        "m4a": "Audio",
        "wav": "Audio",
        "wma": "Audio",
        "flac": "Audio",
        "aac": "Audio",
        "ogg": "Audio",
        "opus": "Audio",
        "m3u": "Playlist",
        "m3u8": "Playlist",
        "pls": "Playlist",
        "asx": "Playlist",
        "wpl": "Playlist",
        "lrc": "Lyrics",
        "other": "File",
    }
    try:
        dictionary = {"Audio": [], "Playlist": [], "Lyrics": [], "File": []}

        def search(path: str):
            dirs = os.listdir(path)

            for dir in dirs:
                dir_path = os.path.abspath(os.path.join(path, dir))
                if os.path.isdir(dir_path):
                    search(dir_path)
                else:
                    match = re.search(pattern=pat, string=dir)
                    if match:
                        extension = dir.split(".").pop()
                        if extension not in extnames:
                            extension = "other"

                        dictionary[extnames[extension]].append(dir_path)

        search(sys.argv[1])
        print(dictionary)
        return dictionary

    except Exception:
        pass


# @security: Checking if the path is valid or not
# By checking, If the path is a valid string
# By checking, If the path is actually a path in PC or not
# By checking, If the path comes under the allowed directory
def validatePath():
    try:
        pass
    except Exception:
        pass


# Make line-based edits to a `.m3u` file.
# Add, remove, or re-order songs in the playlist.
def edit_file():
    try:
        pass
    except Exception:
        pass


# Generate a `.m3u` file, Add all the `media` that has been categorised.
def generate_playlist():
    try:
        pass
    except Exception:
        pass


# @Returns metadata of the media file, including: Author, Album, Title, Genre, Year, Duration, and Bitrate.
# Other infomation like: size, name, last modified time, permissions, and type.
def get_metadata():
    try:
        pass
    except Exception:
        pass


# @Returns a detailed listing of all files and directories in a specified path.
def list_dir_and_files():
    extnames = {
        "mp3": "Audio",
        "m4a": "Audio",
        "wav": "Audio",
        "wma": "Audio",
        "flac": "Audio",
        "aac": "Audio",
        "ogg": "Audio",
        "opus": "Audio",
        "m3u": "Playlist",
        "m3u8": "Playlist",
        "pls": "Playlist",
        "asx": "Playlist",
        "wpl": "Playlist",
        "lrc": "Lyrics",
        "other": "File",
    }
    try:
        records = []

        def explore(path: str):
            dirs = os.listdir(path)
            for dir in dirs:
                if os.path.isdir(os.path.abspath(os.path.join(path, dir))):
                    records.append("[DIR]:" + dir)
                    explore(os.path.abspath(os.path.join(path, dir)))
                else:
                    extension = dir.split(".").pop()
                    if extension not in extnames:
                        extension = "other"

                    records.append("[" + extnames[extension] + "]:" + dir)

        explore(sys.argv[1])
        print(records)
        return records

    except Exception:
        pass
