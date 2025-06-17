from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import os

#-----------------------------------
load_dotenv()
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

set_tracing_disabled(disabled = True)

#-----------------------------------

client = AsyncOpenAI(
    api_key = OPEN_ROUTER_API_KEY,
    base_url = "https://openrouter.ai/api/v1"
)

agent = Agent(
    name = "My Agent",
    instructions = "You are a helpful assistant.",
    model = OpenAIChatCompletionsModel(
        model = "deepseek/deepseek-r1:free",
        openai_client = client
    ),
)

# -----------------------------------
runner = Runner.run_sync(starting_agent= agent, input = "Hi,Who are you?")
print(runner.final_output)
