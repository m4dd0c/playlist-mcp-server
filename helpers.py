import sys
import os
import re


def is_secure(path: str) -> bool:
    """
    Returns True if the path is valid and secure.

    Conditions:
        Check if the root_path (sys.argv[1]) is valid or not
        Check if the params:path is valid or not
        Check if the params:path resides within the root_path or not

    Args:
        path (str): The path to check.

    Returns:
        bool: True if all conditions are met, False otherwise.
    """

    try:
        root = os.path.abspath(sys.argv[1])
        target = os.path.abspath(path)

        is_valid_root = os.path.exists(root)
        is_valid_target = os.path.exists(target)
        has_common_prefix = os.path.commonpath([root]) == os.path.commonpath(
            [root, target]
        )

        return is_valid_root and is_valid_target and has_common_prefix

    except Exception:
        return False


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
        "dir": "DIR",
    }
    try:
        dictionary = {"Audio": [], "Playlist": [], "Lyrics": [], "File": [], "DIR": []}

        def explore(path: str):
            dirs = os.listdir(path)

            for dir in dirs:
                dir_path = os.path.abspath(os.path.join(path, dir))

                if os.path.isdir(dir_path):
                    dictionary[extnames["dir"]].append(dir_path)
                    explore(dir_path)

                else:
                    extension = dir.split(".").pop()
                    if extension not in extnames:
                        extension = "other"

                    dictionary[extnames[extension]].append(dir_path)

        explore(sys.argv[1])
        print(dictionary)
        return dictionary

    except Exception:
        pass


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


# Make line-based edits to a `.m3u` file.
# Add, remove, or re-order songs in the playlist.
def edit_playlist(path: str):
    try:
        print("Edit-File: Yet to build", path)
    except Exception:
        pass


# Generate a `.m3u` file, Add all the `media` that has been categorised.
def generate_playlist(path: str, playlist_name: str | None = ""):
    try:
        print("Generate-Playlist: Yet to build", path, playlist_name)
    except Exception:
        pass


# @Returns metadata of the media file, including: Author, Album, Title, Genre, Year, Duration, and Bitrate.
# Other infomation like: size, name, last modified time, permissions, and type.
def get_metadata(path: str):
    try:
        print("Get-Metadata: Yet to build", path)
    except Exception:
        pass
