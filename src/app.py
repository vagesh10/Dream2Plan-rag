import streamlit as st
from rag import get_answer

st.set_page_config(
    page_title="Dream2Plan",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Dream2Plan")
st.caption("AI-powered Startup Knowledge Assistant")

question = st.chat_input("Ask a startup-related question...")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching knowledge base..."):

            answer, sources = get_answer(question)

            st.markdown(answer)

            if sources and "I could not find information" not in answer:
                with st.expander("📚 Sources"):
                    for source in sources:
                        st.write(f"• {source}")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )