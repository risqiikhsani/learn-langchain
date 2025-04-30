from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()


### embed documents
list_of_strings = [
    "Hi there!",
    "Oh, hello!",
    "What's your name?",
    "My friends call me World",
    "Hello World!",
]

result = embedding_model.embed_documents(list_of_strings)
print(len(result), len(result[0]))

### embed query
query = "Hello how are you"
result2 = embedding_model.embed_query(query)
print(len(result2))