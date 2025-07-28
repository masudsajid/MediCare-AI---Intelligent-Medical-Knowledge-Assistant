from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from src.prompt import prompt
from src.loader import *
from src.loader import embedding_function
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_pinecone import PineconeVectorStore
import os
from datetime import datetime

load_dotenv()

# Check for required environment variables
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY environment variable is required")
if not os.getenv("PINECONE_API_KEY"):
    raise ValueError("PINECONE_API_KEY environment variable is required")

app = Flask(__name__)

embeddings = embedding_function()

index_name_3 = "medical-rag-project-2"

vector_store = PineconeVectorStore.from_existing_index(
    index_name=index_name_3,
    embedding=embeddings
)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

llm = ChatGroq(model="llama-3.1-8b-instant")

sys_prompt = ChatPromptTemplate.from_messages([
    ("system", prompt),
    ("human", "{input}")
])

create_stuff = create_stuff_documents_chain(prompt=sys_prompt, llm=llm)

chain = create_retrieval_chain(retriever, create_stuff)

# ✅ Serve the frontend
@app.route("/")
@app.route("/chat")
def chat_page():
    return render_template("index.html")

# ✅ Backend endpoint for message
@app.route("/get", methods=["POST"])
def chatbot():
    msg = request.form.get("msg")
    print(f"User: {msg}")
    response = chain.invoke({"input": msg})
    answer = response["answer"]
    print("Response: ", answer)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        "answer": answer,
        "timestamp": timestamp
    })

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
