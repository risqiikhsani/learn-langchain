# There are a few different types of prompt templates:
#     String PromptTemplates
#     ChatPromptTemplates
#     MessagesPlaceholder

from app.concept.chatmodels.openai import llm


# String prompttemplates
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

print(prompt_template.invoke({"topic": "cats"}))

# ChatPromptTemplates
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me a joke about {topic}")
])

print(prompt_template.invoke({"topic": "cats"}))

# MessagesPlaceholder
# This prompt template is responsible for adding a list of messages in a particular place. In the above ChatPromptTemplate, we saw how we could format two messages, each one a string. But what if we wanted the user to pass in a list of messages that we would slot into a particular spot? This is how you use MessagesPlaceholder.

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("msgs")
])

print(prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]}))