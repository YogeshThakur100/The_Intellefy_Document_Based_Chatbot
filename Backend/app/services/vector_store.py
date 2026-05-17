import chromadb
from config import CHROMA_DB_PATH

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH
)

collection = client.get_or_create_collection(
    name="documents"
)


def add_to_vectorstore(
    chunks,
    embeddings,
    document_id,
    filename
):

    ids = []

    for index in range(len(chunks)):
        ids.append(f"{document_id}_{index}")

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {
                "document_id": document_id,
                "filename": filename
            }
            for _ in chunks
        ]
    )


def has_indexed_documents():
    return collection.count() > 0


def search_vectorstore(query_embedding, top_k=4):
    n_results = min(top_k, max(collection.count(), 1))

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "distances"],
    )

    return results


def delete_document_embeddings(
    document_id,
    chunk_count
):

    ids = [
        f"{document_id}_{index}"
        for index in range(chunk_count)
    ]

    collection.delete(
        ids=ids
    )