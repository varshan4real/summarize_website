import os 
import asyncio

'''I have directly used the GROQ API key here for demonstration purposes.
   In production, you should use environment variables or a secure vault to manage sensitive information.
   Make sure to replace the key with your own valid GROQ API key.
   You can set the environment variable
   GROQ_API_KEY in your system or use a .env file to load it securely.
   For example, you can create a .env file with the following content:
   GROQ_API_KEY=*****************************
   Then, you can load it using the dotenv package:   
   from dotenv import load_dotenv
   load_dotenv()'''

os.environ["GROQ_API_KEY"] = "******************************"


from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio


mcp_fetch_server  = MCPServerStdio(command= "python", args= ["-m", "mcp_server_fetch"])


agent = Agent ( model ="groq:llama-3.3-70b-versatile",
              mcp_server = [mcp_fetch_server])
async def main():
    async with agent.run_mcp_servers():
        response = await agent.run("Summarize the website in 5 lines: https://en.wikipedia.org/wiki/Main_Page ")
        output = response.output
        print(output)
if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)
