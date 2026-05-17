import streamlit as st

from api_client import query_document


def render_chat_section():

    st.subheader("Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    user_question = st.chat_input(
        "Ask a question..."
    )

    if user_question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        with st.chat_message("user"):
            st.write(user_question)

        with st.spinner("Generating answer..."):

            response = query_document(user_question)

            answer = response["answer"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.write(answer)