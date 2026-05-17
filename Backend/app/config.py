import os

from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHROMA_DB_PATH = "storage/chroma_db"

UPLOAD_DIR = "storage/uploaded_docs"

EMBEDDING_MODEL = "text-embedding-3-small"

LLM_MODEL = "gpt-4o-mini"