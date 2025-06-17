AI Agent with OpenRouter - README
This project demonstrates how to set up a simple AI agent using OpenRouter's API and the deepseek/deepseek-r1 model.

🛠️ Prerequisites
Python 3.8+

An API key from OpenRouter

A .env file to store your API key

📦 Dependencies
Install the required packages:

bash
pip install python-dotenv openai
Note: The agents library appears to be a custom module. Ensure it is installed or available in your project.

🚀 Step-by-Step Explanation
1. Import Required Libraries
python
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os
dotenv: Loads environment variables from .env.

agents: Custom module for agent management (assumed to provide Agent, Runner, etc.).

os: Accesses environment variables.

2. Load Environment Variables
python
load_dotenv()
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
Loads the .env file.

Retrieves the OPEN_ROUTER_API_KEY (must be set in .env).

3. Disable Tracing (Optional)
python
set_tracing_disabled(disabled=True)
Disables tracing if the agents library supports it (useful for debugging).

4. Configure Async OpenAI Client for OpenRouter
python
client = AsyncOpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
Initializes an AsyncOpenAI client pointing to OpenRouter's API.

5. Create an AI Agent
python
agent = Agent(
    name="My Agent",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-r1:free",
        openai_client=client
    ),
)
Defines an agent with:

Name: "My Agent"

Instructions: Basic assistant behavior.

Model: Uses OpenRouter’s free deepseek-r1 model.

6. Run the Agent & Get Response
python
runner = Runner.run_sync(
    starting_agent=agent,
    input="Hi, Who are you?"
)
print(runner.final_output)
Runs the agent synchronously with the input "Hi, Who are you?".

Prints the agent’s response.

🔧 How to Use
Set Up .env File

env
OPEN_ROUTER_API_KEY="your_openrouter_api_key_here"
Run the Script

bash
python your_script_name.py
Expected Output
The agent will respond with an introduction (e.g., "I am a helpful AI assistant.").

📌 Notes
Replace "deepseek/deepseek-r1:free" with another OpenRouter model if needed.

For asynchronous execution, use Runner.run_async() if supported.

Ensure the agents module is properly installed or available in your project.

🚀

