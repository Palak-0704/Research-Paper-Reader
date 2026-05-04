# 📚 AI Research Paper Reader (RAG System)

An AI-powered application that allows users to upload research papers and ask questions using Retrieval-Augmented Generation (RAG). Get instant answers backed by semantic search and LLM intelligence.

---

## 🚀 Features
✅ **PDF Upload** — Upload any research paper instantly  
✅ **Semantic Search** — FAISS-powered retrieval of relevant passages  
✅ **LLM Answers** — Groq API for fast, accurate responses  
✅ **Interactive UI** — Clean Streamlit interface  
✅ **Source Display** — See retrieved passages alongside answers  
✅ **Adjustable Settings** — Control retrieval parameters (k value)  

---

## 🧠 Tech Stack
| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| Vector DB | FAISS |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| LLM | Groq API (llama-3.1-8b-instant) |
| PDF Parser | PyPDF |
| Language | Python 3.8+ |

---

## 📋 Prerequisites
- Python 3.8 or higher
- Groq API key (free at https://console.groq.com)
- ~500MB disk space

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Palak-0704/Research-Paper-Reader.git
cd "Research Paper Reader"
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_api_key_here
```
Get your free API key from: https://console.groq.com

---

## 🚀 Running the App

```bash
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

---

## 📸 UI Preview
Upload PDF → Ask question → Get AI answer

---

## 💡 Future Improvements
- [ ] Multi-document support (compare across papers)
- [ ] Chat history & session persistence
- [ ] Deploy on Streamlit Cloud
- [ ] Citation highlighting & references
- [ ] Support for other file formats (DOCX, TXT)
- [ ] Streaming LLM responses
- [ ] Advanced filtering & metadata search

---

## ⚠️ Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'streamlit'`  
**Fix:** Run `pip install -r requirements.txt` in the virtual environment

**Issue:** `API key not found` or Groq errors  
**Fix:** Verify `.env` file exists with valid `GROQ_API_KEY`

**Issue:** Slow performance on large PDFs  
**Fix:** Adjust `chunk_size` in `rag.py` or increase `overlap` for better context

---

## 📄 License
Open source — feel free to fork and contribute!

---

## 👩‍💻 Author
Built as an AI + NLP project for internship portfolio.