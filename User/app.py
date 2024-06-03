import boto3
from langchain_community.embeddings import BedrockEmbeddings ## Bedrock
from langchain.text_splitter import RecursiveCharacterTextSplitter ## Text Splitter
from langchain_community.document_loaders import PyPDFLoader ## Pdf Loader
from langchain_community.vectorstores import FAISS ## import FAISS
import streamlit as st
import os
import uuid

## s3_client
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")

## Bedrock client
bedrock_client = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock_client)

# Define Helper Functions
def get_unique_id():
    return str(uuid.uuid4())

folder_path = "/tmp/"

## load index
def load_index():
    s3_client.download_file(Bucket=BUCKET_NAME, Key="my_faiss.faiss", Filename=f"{folder_path}my_faiss.faiss")
    s3_client.download_file(Bucket=BUCKET_NAME, Key="my_faiss.pkl", Filename=f"{folder_path}my_faiss.pkl")

# Main Function for Streamlit Application
## main method
def main():
    st.header("This is Client Site for Chat with PDF demo using Bedrock, RAG etc")
   



if __name__ == "__main__":
    main()