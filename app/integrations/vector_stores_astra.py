from dotenv import load_dotenv
load_dotenv()

import os

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

from langchain_astradb import AstraDBVectorStore

ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
desired_namespace = os.environ.get("ASTRA_DB_NAMESPACE")
if desired_namespace:
    ASTRA_DB_NAMESPACE = desired_namespace
else:
    ASTRA_DB_NAMESPACE = None

vector_store = AstraDBVectorStore(
    collection_name="astra_vector_langchain",
    embedding=embeddings,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace=ASTRA_DB_NAMESPACE,
)

# from uuid import uuid4

# from langchain_core.documents import Document

# document_1 = Document(
#     page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
#     metadata={"source": "tweet"},
# )

# document_2 = Document(
#     page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
#     metadata={"source": "news"},
# )

# document_3 = Document(
#     page_content="Building an exciting new project with LangChain - come check it out!",
#     metadata={"source": "tweet"},
# )

# document_4 = Document(
#     page_content="Robbers broke into the city bank and stole $1 million in cash.",
#     metadata={"source": "news"},
# )

# document_5 = Document(
#     page_content="Wow! That was an amazing movie. I can't wait to see it again.",
#     metadata={"source": "tweet"},
# )

# document_6 = Document(
#     page_content="Is the new iPhone worth the price? Read this review to find out.",
#     metadata={"source": "website"},
# )

# document_7 = Document(
#     page_content="The top 10 soccer players in the world right now.",
#     metadata={"source": "website"},
# )

# document_8 = Document(
#     page_content="LangGraph is the best framework for building stateful, agentic applications!",
#     metadata={"source": "tweet"},
# )

# document_9 = Document(
#     page_content="The stock market is down 500 points today due to fears of a recession.",
#     metadata={"source": "news"},
# )

# document_10 = Document(
#     page_content="I have a bad feeling I am going to get deleted :(",
#     metadata={"source": "tweet"},
# )

# documents = [
#     document_1,
#     document_2,
#     document_3,
#     document_4,
#     document_5,
#     document_6,
#     document_7,
#     document_8,
#     document_9,
#     document_10,
# ]
# uuids = [str(uuid4()) for _ in range(len(documents))]

# vector_store.add_documents(documents=documents, ids=uuids)

results = vector_store.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
    filter={"source": "tweet"},
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
    
    
from langchain.chat_models import init_chat_model
llm = init_chat_model("gpt-4o-mini", model_provider="openai")
retriever = vector_store.as_retriever(search_kwargs={"k": 3}, search_type="similarity")

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain import hub

retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

combine_docs_chain = create_stuff_documents_chain(
    llm, retrieval_qa_chat_prompt
)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

print(retrieval_chain.invoke({"input": "best framework for building stateful, agentic applications?"}))