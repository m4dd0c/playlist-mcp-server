# TODO  ::type : impr::
# Will Complete once created the MVP
#
# @mcp.tool()
# def save_playlist_to_file():
#   pass
#
# NOTE: ::type : done::
#
# search_files: [Audio] or [Playlist]
# generate_playlist: Creates .m3u
# edit_file: Edits .m3u files
# get_metadata

from main import mcp


@mcp.tool()
def search_files():
    """Recursively search for files matching `.m3u`, '.m3u8' or `audio` files."
    Searches through all subdirectories from the starting path. The search
    is case-insensitive and matches partial names. Returns full paths to all
    matching items. Great for finding files when you don't know their exact location.
    Can clearly distinguish between `Playlist` and `Audio` files.
    Uses [Playlist] and [Audio] as prefix for each file in search result.
    Only searches within allowed directories."""
    pass


@mcp.tool()
def generate_playlist():
    """Generates the playlist based on metadata of media files.
    Creates a `.m3u` file.
    If Provided, use playlist name as [playlist-name].m3u file, Otherwise use an appropriate name for the playlist.
    Only works within allowed directories."""
    pass


@mcp.tool()
def edit_playlist():
    """Make line-based edits to a `.m3u` file.
    Each edit replaces exact line sequences with new content.
    Returns the changes in a way that one can understand what has changed in the playlist file.
    Only works within allowed directories."""
    pass


@mcp.tool()
def list_dir_and_files():
    """Get a detailed listing of all files and directories in a specified path.
    Results clearly distinguish between files and directories with [Playlist], [Audio], and [DIR]
    prefixes. This tool is essential for understanding directory structure and
    finding specific files within a directory. Only works within allowed directories."""
    pass


@mcp.tool()
def get_audio_metadata():
    """Retrieve detailed metadata about an audio file. Returns comprehensive
    information including size, duration, author, genre, last modified time, permissions,
    and type. This tool is perfect for understanding file characteristics
    without reading the actual content. Only works within allowed directories."""
    pass
