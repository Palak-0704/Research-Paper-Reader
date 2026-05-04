import os
import numpy as np
import faiss
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@lru_cache(maxsize=1)
def get_model():
    """Load and cache the embedding model"""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


# ---------------- PDF ----------------
def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# ---------------- CHUNK ----------------
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += chunk_size - overlap
    return chunks



# ---------------- INDEX ----------------
def create_index(chunks):
    model = get_model()

    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks


# ---------------- RETRIEVE ----------------
def retrieve(query, index, chunks, k=5):
    # Ensure the embedding model is initialized before encoding the query
    m = get_model()
    q_emb = m.encode([query]).astype("float32")
    _, indices = index.search(q_emb, k)
    # Guard against out-of-range indices
    return [chunks[i] for i in indices[0] if 0 <= i < len(chunks)]


# ---------------- CONTEXT ----------------
def build_context(docs):
    return "\n\n".join(docs)


# ---------------- LLM ----------------
def ask_llm(query, docs):
    context = build_context(docs)

    prompt = f"""
You are an AI research assistant.

Context:
{context}

Question:
{query}

Answer clearly and structured.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content