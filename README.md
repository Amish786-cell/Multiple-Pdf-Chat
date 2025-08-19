Chat with Multiple PDFs using AI:

Overview:

This project allows you to chat with multiple PDF documents using AI. Instead of manually reading through lengthy reports, research papers, or contracts, you can upload PDFs and query them in natural language. The system extracts content, builds embeddings, stores them in a vector database, and retrieves relevant context to answer your questions.

Features:

Upload and process multiple PDFs at once
Intelligent semantic search across documents
Summarization and Q&A with context
Interactive chat interface (Streamlit/Gradio)
Powered by LLMs + Vector Databases

Tech Stack Used:

Python 

PDF Parsing → PyPDF2

Embeddings → OpenAI Embeddings, SentenceTransformers

Vector DB → FAISS or Chroma

LLM Orchestration → LangChain

Frontend → Streamlit 

Use Cases:
Research Papers → Summarize findings across sources
Legal Contracts → Extract clauses, compare terms
Business Reports → Quick insights from long docs

