import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from config import UPLOAD_DIR
from services.document_loader import load_pdf, load_txt
from services.text_splitter import split_text
from services.embedding_service import generate_embeddings
from services.vector_store import add_to_vectorstore
from services.document_service import (
    create_document,
    get_all_documents,
    update_documents
)

from config import UPLOAD_DIR

router = APIRouter()


@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported"
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    document = create_document(file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    if file.filename.endswith(".pdf"):
        text = load_pdf(file_path)
    else:
        text = load_txt(file_path)

    # Split into chunks
    chunks = split_text(text)

    document["chunk_count"] = len(chunks)

    documents = get_all_documents()

    for doc in documents:

        if doc["document_id"] == document["document_id"]:
            doc["chunk_count"] = len(chunks)

    update_documents(documents)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Store in Chroma
    add_to_vectorstore(
        chunks=chunks,
        embeddings=embeddings,
        document_id=document["document_id"],
        filename=file.filename
    )

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "chunks_created": len(chunks)
    }