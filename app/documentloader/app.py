import getpass
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
if not os.environ.get("FIRECRAWL_API_KEY"):
  os.environ["FIRECRAWL_API_KEY"] = getpass.getpass("Enter FIRECRAWL_API_KEY : ")


from langchain_community.document_loaders import PyPDFLoader
import pprint

file_path = "app\documentloader\waf-or-shield.pdf"

loader = PyPDFLoader(file_path)

docs = loader.load()
print(len(docs))
pprint.pp(docs[2].metadata)
pprint.pp(docs[2].page_content)

from langchain_community.document_loaders import WebBaseLoader

# loader = WebBaseLoader("https://dev.to/imranmind/deep-dive-into-javascript-event-loop-20je")

# docs = loader.load()

# pprint.pp(docs[0].metadata)
# pprint.pp(docs[0].page_content)

from langchain_community.document_loaders.firecrawl import FireCrawlLoader

loader = FireCrawlLoader(
    api_key=os.environ.get("FIRECRAWL_API_KEY"), url="https://firecrawl.dev", mode="scrape"
)

# docs = []
# docs_lazy = loader.lazy_load()

# # async variant:
# # docs_lazy = await loader.alazy_load()

# for doc in docs_lazy:
#     docs.append(doc)
# print(docs[0].page_content[:100])
# print(docs[0].metadata)