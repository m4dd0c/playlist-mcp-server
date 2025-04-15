# search_files(): [Audio] or [Playlist]
# list_dir_and_files(): [Audio], [Playlist], and [DIR]
# generate_playlist(): Creates .m3u
# edit_file(): Edits .m3u files
# get_metadata(): Returns metadata of file.
import sys
import os


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
def search_files():
    try:
        pass
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
    try:

        def lisDir(path: str, count: int):
            count_str = "{Level " + str(count) + "}: "
            dirs = os.listdir(path)
            for dir in dirs:
                if os.path.isdir(os.path.abspath(os.path.join(path, dir))):
                    print(count_str + "[DIR]:" + dir)
                    count += 1
                    lisDir(os.path.abspath(os.path.join(path, dir)), count)
                else:
                    print(count_str + "[FILE]:" + dir)
                    count += 1

        lisDir(sys.argv[1], 0)

    except Exception:
        pass
