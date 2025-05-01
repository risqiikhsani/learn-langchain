import getpass
import os    
from langchain_community.agent_toolkits import SlackToolkit

from dotenv import load_dotenv
load_dotenv()

if not os.getenv("SLACK_USER_TOKEN"):
    os.environ["SLACK_USER_TOKEN"] = getpass.getpass("Enter your Slack user token: ")

toolkit = SlackToolkit()

tools = toolkit.get_tools()

# print(tools)

############# use with agent

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

llm = ChatOpenAI(model="gpt-4o-mini")

agent_executor = create_react_agent(llm, tools)

# These values could come from an API request or another system
channel_name = "general"
message_text = "Hello from backend via AI!"

# Dynamic prompt
example_query = f'Send the message "{message_text}" to the Slack channel named "{channel_name}".'

events = agent_executor.stream(
    {"messages": [("user", example_query)]},
    stream_mode="values",
)
for event in events:
    message = event["messages"][-1]
    if message.type != "tool":  # mask sensitive information
        event["messages"][-1].pretty_print()