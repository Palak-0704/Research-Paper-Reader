import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import streamlit as st
from rag import load_pdf, chunk_text, create_index, retrieve, ask_llm

st.set_page_config(page_title="RAG Research Paper Reader")

st.title("📚 AI Research Paper Reader")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# ---------------- PROCESS ONLY ONCE ----------------
if uploaded_file and "index" not in st.session_state:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded")

    with st.spinner("Processing document... please wait"):

        text = load_pdf("temp.pdf")
        chunks = chunk_text(text)
        index, chunks = create_index(chunks)

        st.session_state.index = index
        st.session_state.chunks = chunks

    st.success("Ready 🚀 Ask questions below")

# ---------------- CHAT ----------------

if "index" in st.session_state:

    query = st.text_input("Ask your question")

    if query:

        docs = retrieve(
            query,
            st.session_state.index,
            st.session_state.chunks
        )

        answer = ask_llm(query, docs)

        st.subheader("Answer")
        st.write(answer)