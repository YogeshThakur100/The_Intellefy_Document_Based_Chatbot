import streamlit as st

from api_client import (
    get_documents,
    delete_document
)


def render_document_manager():

    st.subheader("Uploaded Documents")

    response = get_documents()

    documents = response.get("documents", [])

    if not documents:
        st.info("No documents uploaded")
        return

    for document in documents:

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(document["filename"])

        with col2:

            if st.button(
                "Delete",
                key=document["document_id"]
            ):

                delete_document(
                    document["document_id"]
                )

                st.rerun()