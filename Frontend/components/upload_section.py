import streamlit as st

from api_client import upload_document


def render_upload_section():

    st.subheader("Upload Document")

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT",
        type=["pdf", "txt"]
    )

    if uploaded_file:

        if st.button("Upload"):

            with st.spinner("Uploading document..."):

                response = upload_document(uploaded_file)

                st.success(response["message"])