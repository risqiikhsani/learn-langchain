# The key methods are:

#     add_documents: Add a list of texts to the vector store.
#     delete: Delete a list of documents from the vector store.
#     similarity_search: Search for similar documents to a given query.


from langchain_core.vectorstores import InMemoryVectorStore
from app.embedding_models.app import embedding_model as my_embedding_model

vector_store = InMemoryVectorStore(embedding=my_embedding_model)

# example

from langchain_core.documents import Document

document_1 = Document(
    page_content="I had chocalate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
)

documents = [document_1, document_2]
# vector_store.add_documents(documents=documents)

# You should usually provide IDs for the documents you add to the vector store, so that instead of adding the same document multiple times, you can update the existing document.
vector_store.add_documents(documents=documents, ids=["doc1", "doc2"])

# To delete documents, use the delete method which takes a list of document IDs to delete.
# vector_store.delete(["doc1"])

# LangChain vectorstore interface has a similarity_search method for all integrations. This will take the search query, create an embedding, find similar documents, and return them as a list of Documents.
results = vector_store.similarity_search("What is the weather tomorrow?")
print(results)

# Many vectorstores support the k, which controls the number of Documents to return, and filter, which allows for filtering documents by metadata.
# Metadata filtering helps narrow down the search by applying specific conditions such as retrieving documents from a particular source or date range.
# results = vector_store.similarity_search("What is the weather tomorrow?", k=1, filter={"source": "tweet"})