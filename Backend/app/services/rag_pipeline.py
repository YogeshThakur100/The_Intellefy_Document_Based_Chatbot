from services.embedding_service import embedding_model
from services.vector_store import search_vectorstore
from services.llm_service import llm

from utils.prompts import SYSTEM_PROMPT


def generate_answer(question: str):

    # Generate query embedding
    query_embedding = embedding_model.embed_query(question)

    # Retrieve relevant chunks
    results = search_vectorstore(query_embedding)

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    # Final prompt
    final_prompt = f"""
    {SYSTEM_PROMPT}

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(final_prompt)

    return {
        "answer": response.content,
        "context_chunks": documents
    }