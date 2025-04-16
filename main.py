# todo: use os.walk for efficiency
import sys
import os
import re
from typing import Dict, List
from mcp.server.fastmcp import FastMCP
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# MCP Server Initialization
mcp = FastMCP("playlister")


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
def list_dir_and_files_helper() -> str:
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
        records = []

        def explore(path: str):
            dirs = os.listdir(path)

            for dir in dirs:
                dir_path = os.path.abspath(os.path.join(path, dir))

                if os.path.isdir(dir_path):
                    records.append(f"[DIR]: {dir_path}")
                    explore(dir_path)

                else:
                    extension = dir.split(".").pop()
                    if extension not in extnames:
                        extension = "other"

                    records.append(f"[{extnames[extension]}]: {dir_path}")

        explore(sys.argv[1])
        return "\n".join(records)

    except Exception:
        return ""


def search_files_helper(pat: str) -> str:
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

                        records.append(f"[{extnames[extension]}]: {dir_path}")

        search(sys.argv[1])
        return "\n".join(records)

    except Exception:
        return ""


# Make line-based edits to a `.m3u` file.
# Add, remove, or re-order songs in the playlist.
def edit_playlist_helper(path: str):
    try:
        print("Edit-File: Yet to build", path)
    except Exception:
        pass


# Generate a `.m3u` file, Add all the `media` that has been categorised.
def generate_playlist_helper(path: str, playlist_name: str | None = ""):
    try:
        print("Generate-Playlist: Yet to build", path, playlist_name)
    except Exception:
        pass


def safe_tag(audio, key):
    val = audio.get(key)
    return val[0] if val else "Unknown"


def gen_metadata(root, file):
    file_path = os.path.join(root, file)
    audio = MP3(file_path, ID3=EasyID3)
    metadata = {
        "filename": os.path.basename(file),
        "file_path": file_path,
        "title": safe_tag(audio, "title"),
        "artist": safe_tag(audio, "artist"),
        "album": safe_tag(audio, "album"),
        "genre": safe_tag(audio, "genre"),
        "year": safe_tag(audio, "date"),
        "duration": round(audio.info.length, 2),
    }
    return metadata


def get_metadata_helper(path: str) -> List[Dict[str, str | int]] | None:
    extnames = (".mp3", ".m4a", ".wav", ".wma", ".flac", ".aac", ".ogg", ".opus")
    try:
        records = []

        # Check if the path is a file or directory
        if path.lower().endswith(extnames):
            # First path is serving as root
            # Second path is serving as file, Basically os.path.basename(path), Basically filename
            metadata = gen_metadata(path, path)
            records.append(metadata)

        else:
            for root, _, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(extnames):
                        metadata = gen_metadata(root, file)
                        records.append(metadata)

        return records

    except Exception:
        return None


@mcp.tool()
def list_dir_and_files() -> str:
    """
    Lists all files and directories in a specified path with detailed categorization.

    **Description:**
    - Scans the given directory and its subdirectories.
    - Categorizes files and directories with tags like [Playlist], [Audio], [Lyrics], [FILE], and [DIR].
    - Helps in understanding the directory structure and locating specific files.

    **Parameters:**
    - None (uses the root directory specified in the system configuration).

    **Returns:**
    - str: A String with categorized lists of matching file paths.
      Example:
          [Audio]: <audio_name>
          [Playlist]: <playlist_name>
          [Lyrics]:  <lyrics_name>
          [File]: <file_name>
    """
    return list_dir_and_files_helper()


@mcp.tool()
def search_files(pattern: str) -> str:
    """
    Searches for files matching a specific pattern recursively within a directory.

    **Description:**
    - Mainly used for finding `.m3u`, `.m3u8` files and audio files.
    - Recursively searches for files in the root directory and its subdirectories.
    - Matches files based on the provided pattern (case-insensitive, partial matches allowed).
    - Categorizes matching files with prefixes [Playlist] and [Audio].

    **Parameters:**
    - pattern (str): The search pattern (e.g., file name or extension).
    - e.g., "mp3", "lrc", "m3u", etc.

    **Returns:**
    - str: A String with categorized lists of matching file paths.
      Example:
          [Audio]: <audio_name>
          [Playlist]: <playlist_name>
          [Lyrics]:  <lyrics_name>
          [File]: <file_name>
    """
    return search_files_helper(pattern)


@mcp.tool()
def generate_playlist(path: str, playlist_name: str | None = ""):
    """
    Generates a playlist file (`.m3u`) based on media files in a directory.

    **Description:**
    - Scans the specified directory for media files and creates a playlist.
    - If a playlist name is provided, uses `[playlist-name].m3u` as the file name.
    - If no name is provided, generates an appropriate name automatically.

    **Parameters:**
    - path (str): The directory path containing media files.

    **Returns:**
    - str: The path to the generated playlist file.
    """
    generate_playlist_helper(path, playlist_name)


@mcp.tool()
def edit_playlist(path: str):
    """
    Edits a playlist file (`.m3u`) by making line-based modifications.

    **Description:**
    - Allows editing of playlist files by replacing specific line sequences.
    - Useful for reordering, adding, or removing entries in a playlist.

    **Parameters:**
    - path (str): The path to the playlist file to be edited.

    **Returns:**
    - dict: A summary of changes made to the playlist.
      Example:
      {
          "added": [...],
          "removed": [...],
          "modified": [...]
      }
    """
    edit_playlist_helper(path)


@mcp.tool()
def get_metadata(path: str) -> List[Dict[str, str | int]] | None:
    """
    Retrieves detailed metadata about an audio file.

    **Description:**
    - Extracts metadata such as size, duration, author, genre, last modified time, permissions, and file type.
    - Useful for analyzing file characteristics without accessing the file's content.

    **Parameters:**
    - path (str): The path to the audio file.

    **Returns:**
    - List[Dict[str, str | int]] | None: A List of dictionaries containing metadata about all audio files within the path.
    None in case of error.

      Optimistic Example:
      [
        {
            "filename": <filename>,
            "file_path": <file_path>,
            "title": <title>,
            "artist": <artist>,
            "album": <album>,
            "genre": <genre>,
            "year": <year>,
            "duration": <duration>
        },
        ...
      ]
    """
    return get_metadata_helper(path)


@mcp.tool()
def list_allowed_directory() -> str:
    """
    Returns the allowed directory path for the application.
    """
    return sys.argv[1]


if __name__ == "__main__":
    # transport="stdio" is default, yet specifing since It looks cool
    mcp.run(transport="stdio")  # stdio | sse
