import os
import streamlit as st

# Suppress TensorFlow warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

st.set_page_config(page_title="RAG Research Paper Reader", layout="centered")

st.title("📚 AI Research Paper Reader")

@st.cache_resource
def load_rag_modules():
    """Load RAG modules once and cache them"""
    with st.spinner("⏳ Loading AI models... (this may take 1-2 minutes on first run)"):
        from rag import load_pdf, chunk_text, create_index, retrieve, ask_llm
        return load_pdf, chunk_text, create_index, retrieve, ask_llm

load_pdf, chunk_text, create_index, retrieve, ask_llm = load_rag_modules()


with st.sidebar:
    st.header("Settings")
    k = st.number_input("Number of retrieved chunks (k)", min_value=1, max_value=10, value=5)
    show_sources = st.checkbox("Show retrieved chunks", value=True)
    if st.button("Clear session"):
        for kname in list(st.session_state.keys()):
            del st.session_state[kname]
        st.rerun()


uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file and "index" not in st.session_state:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded — processing...")
    with st.spinner("Processing document — extracting text and building index..."):
        text = load_pdf("temp.pdf")
        chunks = chunk_text(text)
        index, chunks = create_index(chunks)

        st.session_state.index = index
        st.session_state.chunks = chunks

    st.success("Processing complete. You can ask questions below.")


if "index" in st.session_state:
    query = st.text_input("Ask a question about the uploaded paper")

    if st.button("Ask") and query:
        with st.spinner("Retrieving relevant passages and asking the LLM..."):
            docs = retrieve(query, st.session_state.index, st.session_state.chunks, k=k)
            answer = ask_llm(query, docs)

        st.subheader("Answer")
        st.write(answer)

        if show_sources:
            st.subheader("Retrieved passages")
            for i, d in enumerate(docs, start=1):
                st.expander(f"Passage {i}").write(d)

else:
    st.info("Upload a PDF on the left to get started.")
