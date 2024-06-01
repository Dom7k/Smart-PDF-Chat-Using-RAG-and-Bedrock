import boto3
import streamlit as st
import os
import uuid

## s3_client
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")


def main():
    st.write("Hello world")


if __name__ == "__main__":
    main()