from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings



def loader_function(file_path):
    pdf = PyPDFLoader(file_path=file_path)
    loader = pdf.load()
    return loader



def recursive_function(loader):
    spliter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    docs = spliter.split_documents(loader)
    return docs


def embedding_function():
    hf_embedding = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")
    return hf_embedding
