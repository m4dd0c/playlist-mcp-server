# todo: use os.walk for efficiency
import sys
import os
import re
from mcp.server.fastmcp import FastMCP
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

from typing import TypedDict, List, Union


class PlaylistMetadata(TypedDict):
    filename: str
    file_path: str
    title: str
    artist: str
    album: str
    genre: str
    year: Union[str, int]
    duration: Union[str, float]


# MCP Server Initialization
mcp = FastMCP("playlister")


#### List all files and directories in a specified path with detailed categorization. ####
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


#### Search for files matching a specific pattern recursively within a directory. ####
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
    }

    records = []

    def search(path: str):
        try:
            for entry in os.scandir(path):
                if entry.is_dir():
                    search(entry.path)
                elif re.search(pat, entry.name, flags=re.IGNORECASE):
                    extension = entry.name.split(".")[-1].lower()
                    category = extnames.get(extension, "File")
                    records.append(f"[{category}]: {entry.path}")
        except Exception:
            pass

    search(sys.argv[1])
    return "\n".join(records)


#### Remove entries in a playlist ####
def remove_song_from_playlist_helper(
    path: str,
    songs_to_remove: List[str],
):
    try:
        with open(path, "r") as f:
            lines = f.readlines()

        updated_lines = []
        for i, line in enumerate(lines):
            # Check if the current line is a song path to be removed
            if any(song == line.strip() for song in songs_to_remove):
                # Skip the metadata line (previous line) and the song path line
                if i > 0:  # Ensure we don't go out of bounds
                    updated_lines.pop()  # Remove the metadata line
                continue

            updated_lines.append(line)

        if updated_lines:
            with open(path, "w") as f:
                f.writelines(updated_lines)

        return True

    except Exception as e:
        print(e)
        return False


#### Generate or Append to a `.m3u` file, Add the `playlist_metadata_list` ####
def generate_playlist_helper(
    playlist_metadata_list: List[PlaylistMetadata],
    playlist_name: str,
):
    try:
        store = sys.argv[1]

        sub_dirs = os.listdir(store)
        if "Playlist" not in sub_dirs:
            os.mkdir(os.path.join(store, "Playlist"))

        # Forming the path for the playlist
        playlist_path = os.path.join(store, "Playlist", playlist_name)

        # If the playlist already exists, appending to it, Otherwise creating a new one
        if os.path.exists(playlist_path):
            file_mode = "a+"
        else:
            file_mode = "w+"

        with open(playlist_path, file_mode) as f:
            # Moving cursor to the beginning of the file (a+ mode)
            f.seek(0)

            # Checking if the file already has the #EXTM3U header, Otherwise writing it
            extm3u_written = False

            for line in f.readlines():
                if line.strip().startswith("#EXTM3U"):
                    extm3u_written = True
                    break

            if not extm3u_written:
                f.write("#EXTM3U\n")

            # Writing the metadata of each audio file to the playlist
            for audio in playlist_metadata_list:
                f.write(f"\n#EXTINF:{audio['duration']}, {audio['title']}\n")
                f.write(f"{audio['file_path']}\n")

            f.close()

        return True

    except Exception:
        return False


#### Generate Metadata for the audio files ####
# Optional Chaining logic in python for List
def safe_tag(audio: MP3, key: str) -> str:
    val = audio.get(key)
    return val[0] if val else "Unknown"


# Generate Metadata using mutagen
def gen_metadata(root: str, file: str) -> PlaylistMetadata:
    file_path = os.path.join(root, file)
    audio = MP3(file_path, ID3=EasyID3)
    metadata: PlaylistMetadata = {
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


# Get Metadata helper function
def get_metadata_helper(path: str) -> List[PlaylistMetadata] | None:
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
def generate_playlist(
    playlist_metadata_list: List[PlaylistMetadata], playlist_name: str
) -> bool:
    """
    Generates a playlist file (`.m3u`) based on provided metadata or Append songs to the existing Playlist.

    **Description:**
    - Builds a playlist using `playlist_metadata_list` or appends playlist_metadata_list to an
      existing playlist file.
    - If a playlist name is provided, uses `<playlist_name>` as the file name.
    - The <playlist_name> must have the `.m3u` extension, If not append it yourself.
    - If no name is provided, generates an appropriate name automatically.

    **Parameters:**
    - playlist_metadata_list (List[PlaylistMetadata]): A list of metadata
      dictionaries for audio files.
    - playlist_name (str): The name of the playlist file to create or append to.

    **Returns:**
    - bool: True if the playlist was successfully generated or appended,
      False otherwise.
    """
    return generate_playlist_helper(playlist_metadata_list, playlist_name)


@mcp.tool()
def remove_song_from_playlist(path: str, songs_to_remove: List[str]):
    """
    - Allow removing entries in a playlist.

    **Parameters:**
    - path (str): The path to the playlist file to be edited.
    - songs_to_remove (str): List of path of songs to be removed.

    **Returns:**
    - bool: Returns True if operation was successful, False otherwise.
    """
    remove_song_from_playlist_helper(path, songs_to_remove)


@mcp.tool()
def get_metadata(path: str) -> List[PlaylistMetadata] | None:
    """
    Retrieves detailed metadata about an audio file.

    **Description:**
    - Extracts metadata such as size, duration, author, genre, last modified time, permissions, and file type.
    - Useful for analyzing file characteristics without accessing the file's content.

    **Parameters:**
    - path (str): The path to the audio file.

    **Returns:**
    - List[PlaylistMetadata] | None: A List of dictionaries containing metadata about all audio files within the path.
      None in case of error.
    """
    return get_metadata_helper(path)


@mcp.tool()
def is_allowed_path(path: str) -> bool:
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


@mcp.tool()
def list_allowed_directory() -> str:
    """
    Returns the allowed directory path for the application.
    """
    return sys.argv[1]


if __name__ == "__main__":
    # transport="stdio" is default, yet specifing since It looks cool
    mcp.run(transport="stdio")  # stdio | sse
