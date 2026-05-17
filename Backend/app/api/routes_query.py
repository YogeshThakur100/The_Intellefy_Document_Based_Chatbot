from fastapi import APIRouter
from pydantic import BaseModel

from services.rag_pipeline import generate_answer

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def query_document(request: QueryRequest):

    response = generate_answer(request.question)

    return response