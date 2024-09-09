
from flask import Flask
# app.py
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
# from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_community.vectorstores import FAISS
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory

# Load environment variables from .env file
load_dotenv()

# Set up Google API key for accessing AI models
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Set up the language model for generating responses
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

messages = [
    (
        "system",
        "you are a helpful assistant that translates English to Hindi and Tamil, Translate the user sentence.",
    ),
    ("human","I love Programming")
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)


# app = Flask(__name__)

# # Add your routes and logic here

# if __name__ == "__main__":
#     app.run(debug=True)
    