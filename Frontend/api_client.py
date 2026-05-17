import os

import requests
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def upload_document(file):

    files = {
        "file": file
    }

    response = requests.post(
        f"{BASE_URL}/upload-document",
        files=files
    )

    return response.json()


def query_document(question):

    response = requests.post(
        f"{BASE_URL}/query",
        json={
            "question": question
        }
    )

    return response.json()


def get_documents():

    response = requests.get(
        f"{BASE_URL}/documents"
    )

    return response.json()


def delete_document(document_id):

    response = requests.delete(
        f"{BASE_URL}/documents/{document_id}"
    )

    return response.json()