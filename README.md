# AI Document Interaction Chatbot

This project is an AI chatbot that allows users to upload their documents and interact with them within the context of the document. The chatbot utilizes Amazon Bedrock, S3, FAISS, RAG, LangChain, and Streamlit to provide an efficient and user-friendly experience.

### **Technologies Used**
- Amazon Bedrock
- Amazon S3
- FAISS
- RAG
- LangChain
- Streamlit
- Docker

## Architecture

![Architecture Diagram](https://github.com/Dom7k/Smart-PDF-Chat-Using-RAG-and-Bedrock/blob/main/images/Architecture%20diagram.gif)

1. **Document Chunking**: The uploaded document is broken up into manageable chunks of text.
2. **Vector Embedding**: Each chunk is converted to FAISS vectors using Amazon Titan Embeddings.
3. **Vector Storage**: The vectors are stored in a vector store within an S3 bucket.
4. **Question Submission**: The user submits a question to the chatbot.
5. **Vector Matching**: The question is converted to a vector using Amazon Titan Embeddings and matched to the closest vectors in the vector store.
6. **Response Generation**: The combined content from the matching vectors and the original question is passed to a large language model (LLM) to generate the best answer.

## Key Features

- **Custom Document Interaction**: Upload your own document and interact with it through the chatbot.
- **Context-Aware Responses**: The chatbot provides answers based on the context of the uploaded document.
- **Efficient Vector Storage**: Utilizes FAISS vectors stored in S3 for fast and efficient retrieval.

## Setup

### AWS S3 Bucket

1. **Create an S3 Bucket**:
   - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   - Navigate to the S3 service.
   - Click on "Create bucket".
   - Name the bucket `bedrock-chatbot-pdf` and leave everything else default.
   - Click "Create bucket".
   - create a folder inside your bucket `bedrock-chatbot-pdf` and name it `my_faiss`

2. **Generate an IAM Access Key**:
   - Go to the IAM service in the AWS Management Console.
   - Select "Users" and then your IAM user.
   - Go to the "Security credentials" tab.
   - Click "Create access key".
   - Save the access key ID and secret access key securely.

### Install AWS CLI

1. **Download the AWS CLI Installer**:
   - Download the installer from the [AWS CLI installation page](https://aws.amazon.com/cli/).

2. **Run the Installer**

3. **Verify the Installation**:
   ```bash
   aws --version


## Configure the CLI:
 ```bash
aws configure
 ```

### **Enter your AWS credentials**

- AWS Access Key ID: YOUR_ACCESS_KEY_ID
- AWS Secret Access Key: YOUR_SECRET_ACCESS_KEY
- Default region name: us-west-2
- Default output format: 


## Usage
### Backend
1. **Clone the repository**
```bash
git clone https://github.com/Dom7k/Smart-PDF-Chat-Using-RAG-and-Bedrock.git
```

2. **Navigate to the admin directory**
```bash
cd Smart-PDF-Chat-Using-RAG-and-Bedrock/Admin
````

3. **Build the Docker image**
```bash
docker build -t pdf-reader-admin .
````

4. **Run the Docker container on port `8083`**
```bash
docker run -d -e BUCKET_NAME=bedrock-chatbot-pdf -v ~/.aws:/root/.aws -p 8083:8083 -it pdf-reader-admin
````

## Frontend
1. **Navigate to the user directory**
```bash
cd ../user
```

2. **Build the Docker image**
```bash
docker build -t pdf-reader-client .
````

3. **Run the Docker container on port `8084`**
```bash
docker run -d -e BUCKET_NAME=bedrock-chatbot-pdf -v ~/.aws:/root/.aws -p 8084:8084 -it pdf-reader-client
```

## Screenshots

### Admin page / Upload document
![Architecture Diagram](https://github.com/Dom7k/Smart-PDF-Chat-Using-RAG-and-Bedrock/blob/main/images/upload.png)

### User page / Chat with document
![Architecture Diagram](https://github.com/Dom7k/Smart-PDF-Chat-Using-RAG-and-Bedrock/blob/main/images/chat.png)

### When you ask any question out of context, you do not get any answer
![Architecture Diagram](https://github.com/Dom7k/Smart-PDF-Chat-Using-RAG-and-Bedrock/blob/main/images/chat2.png)
