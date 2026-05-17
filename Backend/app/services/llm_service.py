from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY , LLM_MODEL

llm = ChatOpenAI(
    model=LLM_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0
)