import streamlit as st

from components.upload_section import (
    render_upload_section
)

from components.chat_section import (
    render_chat_section
)

from components.document_manager import (
    render_document_manager
)

st.set_page_config(
    page_title="Document Chatbot",
    layout="wide"
)

st.title("Document-based Chatbot")

col1, col2 = st.columns([1, 2])

with col1:

    render_upload_section()

    st.divider()

    render_document_manager()

with col2:

    render_chat_section()