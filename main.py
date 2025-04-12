from mcp.server.fastmcp import FastMCP

# MCP Server Initialization
mcp = FastMCP("playlist-mcp-server")

if __name__ == "__main__":
    # transport="stdio" is default, yet specifing since It looks cool
    mcp.run(transport="stdio")  # stdio | sse
