from fastapi import APIRouter ,HTTPException

from services.vector_store import delete_document_embeddings
from services.document_service import (
    get_all_documents,
    delete_document_record
)

router = APIRouter()


@router.get("/documents")
def list_documents():

    documents = get_all_documents()

    return {
        "documents": documents
    }


@router.delete("/documents/{document_id}")
def delete_document(document_id: str):

    documents = get_all_documents()

    document_to_delete = None

    for doc in documents:

        if doc["document_id"] == document_id:
            document_to_delete = doc
            break

    if not document_to_delete:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    delete_document_embeddings(
        document_id=document_id,
        chunk_count=document_to_delete["chunk_count"]
    )

    delete_document_record(document_id)

    return {
        "message": "Document deleted successfully"
    }