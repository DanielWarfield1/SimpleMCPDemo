from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool()
def say_hello(name: str) -> str:
    """Constructs a greeting from a name"""
    return f"hello {name}, from the server!"