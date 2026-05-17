from langchain_openai import OpenAIEmbeddings
from config import EMBEDDING_MODEL

embedding_model = OpenAIEmbeddings(
    model=EMBEDDING_MODEL
)


def generate_embeddings(text_chunks):
    return embedding_model.embed_documents(text_chunks)