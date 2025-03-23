from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"], 
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            
            # Initialize the connection
            await session.initialize()

            # List available tools
            response = await session.list_tools()

            # getting tool name
            tool_name = response.tools[0].name # 'say_hello'

            # defining tool argument
            tool_args = {'name': 'Daniel'}

            #calling tool
            response = await session.call_tool(tool_name, tool_args)

            # printing response
            print(response.content)





if __name__ == "__main__":
    import asyncio

    asyncio.run(run())