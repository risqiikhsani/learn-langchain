# Approaches

#     Length-based
#     Text-structured based
#     Document-structured based
#     Semantic meaning based

from app.documentloader.app import docs
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
doc = text_splitter.split_documents(docs)
print(len(doc))
print(doc[0].page_content)