# SimpleMCPDemo
 
A simple MCP example, featuring a client and a server communicating with one another. This uses the MCP Python SDK with uv.

the server can be tested by running:
```
uv run mcp dev server.py
```

to run the client, and thus run the server, use:
```
uv run client.py
```

the client will spawn the server, then the client will list the tools available in the server.