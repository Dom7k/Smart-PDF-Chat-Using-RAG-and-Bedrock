import boto3
from langchain_community.embeddings import BedrockEmbeddings ## Bedrock
from langchain.text_splitter import RecursiveCharacterTextSplitter ## Text Splitter
from langchain_community.document_loaders import PyPDFLoader ## Pdf Loader
from langchain_community.vectorstores import FAISS ## import FAISS
import streamlit as st
import os
import uuid