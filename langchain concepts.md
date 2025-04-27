<!-- -Chat models
-Messages
-Chat history
-Tools
-Tool calling
-Structured Output
-Memory
-Multimodality
-Runnable Interface
-Streaming
-Langchain Expression Language LCEL
-Document Loaders
-Retrieval
-Text Splitters
-Embedding Models
-Vector Stores
-Retriever
-Retriever Augmented Generation RAG
-Agents
-Prompt Tempalates
-Output Parsers
-Few-shot prompting
-Example Selectors
-Async Programming
-Callbacks
-Tracing
-Evaluation
-Testing -->


Components
These are the core building blocks you can use when building applications.
    Chat models         (newer forms of language models that take messages in and output a message.)
    Messages            (are the input and output of chat models. They have some content and a role, which describes the source of the message.)
    Prompt templates    (are responsible for formatting user input into a format that can be passed to a language model.)
    Example selectors   (are responsible for selecting the correct few shot examples to pass to the prompt.)
    LLMs                (older forms of language models that take a string in and output a string.)
    Output parsers      (are responsible for taking the output of an LLM and parsing into more structured format.)
    Document loaders    (are responsible for loading documents from a variety of sources.)
    Text splitters      (take a document and split into chunks that can be used for retrieval.)
    Embedding models    (take a piece of text and create a numerical representation of it.)
    Vector stores       (databases that can efficiently store and retrieve embeddings. )
    Retrievers          (responsible for taking a query and returning relevant documents.)
    Indexing            (process of keeping your vectorstore in-sync with the underlying data source.)
    Tools               (contain a description of the tool (to pass to the language model) as well as the implementation of the function to call.)
    Multimodal
    Agents
    Callbacks           (allow you to hook into the various stages of your LLM application's execution.)
    Custom              (can easily be extended to support your own versions.)
    Serialization