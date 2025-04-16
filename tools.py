from main import mcp
import helpers


@mcp.tool()
def list_dir_and_files():
    """
    Lists all files and directories in a specified path with detailed categorization.

    **Description:**
    - Scans the given directory and its subdirectories.
    - Categorizes files and directories with tags like [Playlist], [Audio], [Lyrics], [FILE], and [DIR].
    - Helps in understanding the directory structure and locating specific files.

    **Parameters:**
    - None (uses the root directory specified in the system configuration).

    **Returns:**
    - dict: A dictionary with categorized lists of paths for files and directories.
      Example:
      {
          "Audio": [...],
          "Playlist": [...],
          "Lyrics": [...],
          "File": [...],
          "DIR": [...]
      }
    """
    helpers.list_dir_and_files()


@mcp.tool()
def search_files(pat: str):
    """
    Searches for files matching a specific pattern recursively within a directory.

    **Description:**
    - Mainly used for finding `.m3u`, `.m3u8` files and audio files.
    - Recursively searches for files in the root directory and its subdirectories.
    - Matches files based on the provided pattern (case-insensitive, partial matches allowed).
    - Categorizes matching files with prefixes [Playlist] and [Audio].

    **Parameters:**
    - pat (str): The search pattern (e.g., file name or extension).

    **Returns:**
    - dict: A dictionary with categorized lists of matching file paths.
      Example:
      {
          "Audio": [...],
          "Playlist": [...],
          "Lyrics": [...],
          "File": [...]
      }
    """
    helpers.search_files(pat)


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
    helpers.generate_playlist(path, playlist_name)


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
    helpers.edit_playlist(path)


@mcp.tool()
def get_metadata(path: str):
    """
    Retrieves detailed metadata about an audio file.

    **Description:**
    - Extracts metadata such as size, duration, author, genre, last modified time, permissions, and file type.
    - Useful for analyzing file characteristics without accessing the file's content.

    **Parameters:**
    - path (str): The path to the audio file.

    **Returns:**
    - dict: A dictionary containing metadata about the file.
      Example:
      {
          "size": ...,
          "duration": ...,
          "author": ...,
          "genre": ...,
          "last_modified": ...,
          "permissions": ...,
          "type": ...
      }
    """
    helpers.get_metadata(path)
