from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import os
from api.routes_upload import router as upload_router
from api.routes_query import router as query_router
from api.routes_documents import router as document_router



def initialize_storage():

    os.makedirs(
        "storage/chroma_db",
        exist_ok=True
    )

    os.makedirs(
        "storage/uploaded_docs",
        exist_ok=True
    )

    documents_file = "storage/documents.json"

    if not os.path.exists(documents_file):

        with open(documents_file, "w") as file:
            file.write("[]")

initialize_storage()

app = FastAPI(
    title="Document Chatbot API",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(query_router)
app.include_router(document_router)



@app.get("/")
def home():
    return {
        "message": "Document Chatbot API Running"
    }


# Global Validation Error Handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    errors = exc.errors()

    error_message = "Invalid request"

    if errors:
        first_error = errors[0]

        field_name = first_error.get("loc", [])[-1]

        if field_name == "file":
            error_message = "File is required"

        elif field_name == "question":
            error_message = "Question is required"

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": error_message
        }
    )