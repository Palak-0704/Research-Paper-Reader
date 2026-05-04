import streamlit as st

st.title("Test App")
st.write("If you see this, Streamlit is working!")

try:
    from rag import load_pdf, chunk_text, create_index, retrieve, ask_llm
    st.success("All RAG imports successful!")
except Exception as e:
    st.error(f"Error importing RAG modules: {e}")

st.info("Test complete")
