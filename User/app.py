import boto3
from langchain_community.embeddings import BedrockEmbeddings ## Bedrock
from langchain.text_splitter import RecursiveCharacterTextSplitter ## Text Splitter
from langchain_community.document_loaders import PyPDFLoader ## Pdf Loader
from langchain_community.vectorstores import FAISS ## import FAISS
from langchain.llms.bedrock import Bedrock ## Bedrock
from langchain.chains import RetrievalQA ## chain
from langchain.prompts import PromptTemplate ## prompt
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

# Get Bedrock LLM
def get_llm():
    llm = Bedrock(model_id="anthropic.claude-v2:1", client=bedrock_client,
                  model_kwargs={'max_tokens_to_sample': 512})
    return llm

# get_response()
def get_response(llm,vectorstore, question ):
    ## create prompt / template
    prompt_template = """

    Human: Please use the given context to provide concise answer to the question
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    <context>
    {context}
    </context>

    Question: {question}

    Assistant:"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 5}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
    answer=qa({"query":question})
    return answer['result']

# Main Function for Streamlit Application
## main method
def main():
    st.header("Chat with Your PDF - Powered by RAG")

    load_index()

    # # List files in the folder_path
    # dir_list = os.listdir(folder_path)
    # st.write(f"Files and Directories in {folder_path}")
    # st.write(dir_list)

    ## create index
    faiss_index = FAISS.load_local(
        index_name="my_faiss",
        folder_path=folder_path,
        embeddings=bedrock_embeddings,
        allow_dangerous_deserialization=True
    )

    st.write("INDEX IS READY")
    question = st.text_input("what is your question?")
    if st.button("Ask Question"):
        with st.spinner("Querying..."):

            llm = get_llm()

            # get_response
            st.write(get_response(llm, faiss_index, question))
            st.success("Done")
   



if __name__ == "__main__":
    main()