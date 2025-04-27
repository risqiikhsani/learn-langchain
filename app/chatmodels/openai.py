# 1.interface
# key methods of chat models :
#     invoke
#     stream
#     batch
#     bind_tools
#     with_structured_output

# 2.tool calling
#   Chat models can call tools to perform tasks such as fetching data from a database, making API requests, or running custom code. 
# 3.structured outputs
#   can be requested to respond in a particular format (e.g., JSON or matching a particular schema). 
#   This feature is extremely useful for information extraction tasks.
# 4.multimodality
#   are not limited to processing text. They can also be used to process other types of data, such as images, audio, and video.
# 5.context window
#   context window refers to the maximum size of the input sequence the model can process at one time
# 6.advanced topics
#   -rate limiting
#   -caching


import getpass
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9, max_tokens=2000)

# print(llm.invoke("Hello, world!").content)


##### try structured output

# schema = {
#     "title": "SimpleAnswer",
#     "description": "Answer and follow-up structure",
#     "type": "object",
#     "properties": {
#         "answer": {
#             "type": "string",
#             "description": "The answer to the user's question"
#         },
#         "followup_question": {
#             "type": "string",
#             "description": "A followup question the user could ask"
#         }
#     },
#     "required": ["answer", "followup_question"]
# }

# llm_with_schema = llm.with_structured_output(schema)
# print(llm_with_schema.invoke("Hello what are the best countries to visit to?"))

##### try structured output with pydanytic schema

# from pydantic import BaseModel, Field
# class ResponseFormatter(BaseModel):
#     """Always use this tool to structure your response to the user."""
#     answer: str = Field(description="The answer to the user's question")
#     followup_question: str = Field(description="A followup question the user could ask")
    
# llm_with_other_schema = llm.with_structured_output(ResponseFormatter)
# print(llm_with_other_schema.invoke("Hello what are the mostly read popular good books?"))
