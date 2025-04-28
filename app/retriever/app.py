# A component that returns relevant documents from a knowledge base in response to a query.

# Interface
# Common types of retrieval systems
#     Search apis
#     Relational or graph database
#     Lexical search
#     Vector store
# Advanced retrieval patterns
#     Ensemble
#     Source document retention

# Vector stores are a powerful and efficient way to index and retrieve unstructured data. A vectorstore can be used as a retriever by calling the as_retriever() method.
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from app.embedding_models.app import embedding_model as my_embedding_model

# Initialize vector store
vector_store = InMemoryVectorStore(embedding=my_embedding_model)

# Add some documents
document_1 = Document(
    page_content="I had chocalate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
)

vector_store.add_documents(documents=[document_1, document_2], ids=["doc1", "doc2"])

# Get a retriever from the vector store
retriever = vector_store.as_retriever()

# Retrieve documents relevant to the query
docs = retriever.invoke("What is the weather tomorrow?")
print(docs)



# Ensemble
# it is possible to combine multiple retrievers using ensembling

# Initialize the ensemble retriever
# ensemble_retriever = EnsembleRetriever(
#     retrievers=[bm25_retriever, vector_store_retriever], weights=[0.5, 0.5]
# )