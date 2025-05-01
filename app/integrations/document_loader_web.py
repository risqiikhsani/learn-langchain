from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.example.com/")
loader.requests_kwargs = {'verify':False}
docs = loader.load()
print(docs[0])


from langchain_community.document_loaders.firecrawl import FireCrawlLoader

loader = FireCrawlLoader(
    api_key="YOUR_API_KEY", url="https://firecrawl.dev", mode="scrape"
)
docs = loader.load()
print(docs[0])
