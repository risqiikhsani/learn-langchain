# Indexing: a pipeline for ingesting data from a source and indexing it. This usually happens offline.
# Load: First we need to load our data. This is done with Document Loaders.
# Split: Text splitters break large Documents into smaller chunks. This is useful both for indexing data and passing it into a model, as large chunks are harder to search over and won't fit in a model's finite context window.
# Store: We need somewhere to store and index our splits, so that they can be searched over later. This is often done using a VectorStore and Embeddings model.

# Retrieval and generation: the actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.
# Retrieve: Given a user input, relevant splits are retrieved from storage using a Retriever.
# Generate: A ChatModel / LLM produces an answer using a prompt that includes both the question with the retrieved data


from app.concept.chatmodels.openai import llm

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

from langchain_core.vectorstores import InMemoryVectorStore

vector_store = InMemoryVectorStore(embeddings)


import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain_core.prompts import PromptTemplate

################### Indexing ##################

# load
loader = WebBaseLoader(
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)

docs = loader.load()

# split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

# store
vector_store.add_documents(all_splits)

############# Retrieve and Generate ##################

# create retriever
retriever = vector_store.as_retriever()

# Define prompt for question-answering
# prompt = hub.pull("rlm/rag-prompt")
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="Use the following context to answer the question. If you don't know the answer, say you don't know.\n\nContext: {context}\n\nQuestion: {question}\nAnswer:"
)

# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str
    
def retrieve(state: State):
    retrieved_docs_from_vectorstore = retriever.invoke(state["question"])
    return {"context": retrieved_docs_from_vectorstore}

def generate(state: State):
    prompt_with_context = prompt.format(
        question=state["question"],
        context="\n".join([d.page_content for d in state["context"]]),
    )
    return {"answer": llm.invoke(prompt_with_context)}

# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

response = graph.invoke({"question": "What is Task Decomposition?"})
print(response["answer"].content)