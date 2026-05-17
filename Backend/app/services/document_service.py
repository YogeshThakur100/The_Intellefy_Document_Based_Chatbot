import json
import os
import uuid

DOCUMENTS_FILE = "storage/documents.json"


def load_documents():

    if not os.path.exists(DOCUMENTS_FILE):
        return []

    with open(DOCUMENTS_FILE, "r") as file:
        return json.load(file)


def save_documents(documents):

    with open(DOCUMENTS_FILE, "w") as file:
        json.dump(documents, file, indent=4)


def create_document(filename):

    documents = load_documents()

    document = {
        "document_id": str(uuid.uuid4()),
        "filename": filename,
        "chunk_count": 0
    }

    documents.append(document)

    save_documents(documents)

    return document


def delete_document_record(document_id):

    documents = load_documents()

    updated_documents = [
        doc
        for doc in documents
        if doc["document_id"] != document_id
    ]

    save_documents(updated_documents)


def get_all_documents():

    return load_documents()


def update_documents(documents):

    save_documents(documents)