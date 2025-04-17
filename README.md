# 🎧 MCP Playlist Generator

This project is a **Model Context Provider (MCP) server** designed to work with Claude or any AI assistant that supports tool usage. It generates `.m3u` playlists on the user's PC based on their current mood or theme. The playlist gets saved to a user-specified directory, ready to be queued up in your favorite media player.

> Built with Python, powered by `uv` and `mutagen`, and inspired by the legendary **Filesystem MCP Server** — major shoutout for the idea and foundational reference!

---

## 🛠 How It Works

1. **User sets up the MCP server** using Python and `uv`.
2. Server listens for requests from Claude or any LLM agent.
3. Based on the request (e.g., "make a chill evening playlist"), it:
   - Scans local music files.
   - Uses `mutagen` to read metadata (genre, title, artist, etc.).
   - Filters songs matching the vibe.
   - Creates an `.m3u` playlist.
   - Saves it at the desired location on the user's machine.

---

## 🔧 Tech Stack

- **Python**
- [`uv`](https://pypi.org/project/uv/) — for the async web server
- [`mutagen`](https://mutagen.readthedocs.io/) — for metadata extraction

---

## 📦 Installation

```bash
pip install uv mutagen
```

Clone this repo and run:

```bash
uvicorn mcp_server:app --reload
```

## 🧠 Example Claude Prompt

> "Hey Claude, can you make me a happy vibe playlist."

Claude will then use the MCP server tool and boom — you get a playlist in your music app.

> [!important]
> Make sure you `re-index` the Music app after creating the playlist.

## 🙏 Special Thanks

Massive thanks to the `Filesystem MCP Server` — this project was built with your idea as the spark.

## 💬 Got Feedback?

Open an issue or hit me up. PRs are welcome, mood-based jams even more so 🎶

---

### Need:

- What's the default directory fallback if user doesn't pick a location?
- Are you supporting MP3 only, or other formats too?
- Should I include API route structure for devs?

Lemme know and I’ll update it.
