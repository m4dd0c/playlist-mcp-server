#
#
# list_music_files
# get_metadata
# generate_m3u_playlist
# edit_m3u_playlist
# search_by_genre
# save_playlist_to_file
#
#
from main import mcp


@mcp.tool(
    name="read_files",
    description="""
        Read the complete contents of a file from the file system.
        Handles various text encodings and provides detailed error messages
        if the file cannot be read. Use this tool when you need to examine
        the contents of a single file. Only works within allowed directories.
    """,
)
def read_files():
    pass


@mcp.tool(
    name="find_files",
    description="""
        Create a new file or completely overwrite an existing file with new content.
        Use with caution as it will overwrite existing files without warning.
        Handles text content with proper encoding. Only works within allowed directories.
    """,
)
def find_files():
    pass


@mcp.tool(
    name="edit_file",
    description="""
        Make line-based edits to a text file. Each edit replaces exact line sequences
        with new content. Returns a git-style diff showing the changes made.
        Only works within allowed directories.
    """,
)
def edit_file():
    pass


@mcp.tool(name="write_files", description="Generates Playlist")
def generate_playlist():
    pass


@mcp.tool(
    name="list_directory",
    description="""
         Get a detailed listing of all files and directories in a specified path.
         Results clearly distinguish between files and directories with [FILE] and [DIR]
         prefixes. This tool is essential for understanding directory structure and
         finding specific files within a directory. Only works within allowed directories.
    """,
)
def list_dir():
    pass


@mcp.tool(
    name="search_files",
    description="""
          Recursively search for files and directories matching a pattern."
          Searches through all subdirectories from the starting path. The search
          is case-insensitive and matches partial names. Returns full paths to all
          matching items. Great for finding files when you don't know their exact location.
          Only searches within allowed directories.
    """,
)
def search_files():
    pass


@mcp.tool(
    name="get_file_info",
    description="""
          Retrieve detailed metadata about a file or directory. Returns comprehensive
          information including size, creation time, last modified time, permissions,
          and type. This tool is perfect for understanding file characteristics
          without reading the actual content. Only works within allowed directories.
    """,
)
def get_file_info():
    pass


@mcp.tool(
    name="list_allowed_directories",
    description="""
         Returns the list of directories that this server is allowed to access.
         Use this to understand which directories are available before trying to access files.
    """,
)
def list_allowed_directories():
    pass
