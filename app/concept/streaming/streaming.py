from app.chatmodels.openai import llm

print(llm.invoke("Hello, world!").content)
for chunk in llm.stream("Hello, world!"):
    print(chunk.content)