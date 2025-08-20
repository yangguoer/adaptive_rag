### Build Index
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

### from langchain_cohere import CohereEmbeddings
os.environ['OPENAI_API_KEY'] = "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"
os.environ['TAVILY_API_KEY'] = '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'
os.environ['LANGCHAIN_API_KEY'] = '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'
print(os.environ.get("OPENAI_API_KEY"))  # 检查是否已有值
print(os.environ.get("TAVILY_API_KEY"))  # 检查是否已有值
print(os.environ.get("LANGCHAIN_API_KEY"))  # 检查是否已有值
# Set embeddings
embd = OpenAIEmbeddings(openai_api_base="https://api.openai-proxy.com/v1")

# Docs to index
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# Load
docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

# Split
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

# Add to vectorstore
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=embd,
)
retriever = vectorstore.as_retriever()