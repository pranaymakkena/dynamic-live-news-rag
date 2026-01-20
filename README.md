# 📰 Real-Time News AI (RAG + Streaming)

This project implements a **Real-Time News AI system** that simulates live news streaming, stores articles as vector embeddings, and answers user questions using **retrieval-augmented generation (RAG)** with **Gemini**.

It fetches headlines from NewsAPI, streams them gradually like live data, embeds them using `SentenceTransformer`, stores them in a vector store, and answers queries strictly from the streamed context.

---

## 🚀 Features

- Live-style news ingestion (streamed with delay)
- Semantic embeddings using `all-MiniLM-L6-v2`
- Vector similarity search (cosine similarity)
- RAG-based answering using Gemini
- No hallucination: answers only from retrieved context
- Modular, production-style structure

---

## 🔧 Setup

1. Clone the repository:
~~~bash
git clone https://github.com/pranaymakkena/dynamic-live-news-rag/
cd realtime-news-ai
~~~
2. Install dependencies:
~~~bash
pip install -r requirements.txt
~~~
3. Open app.py and add your API keys:
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
4. Run the Project
~~~bash
python app.py
~~~

## What happens:

Top headlines are fetched from NewsAPI

Articles are streamed one by one (every 5 seconds)

Each article is embedded and stored

A query is executed:
~~~bash
ask("What is news on Trump right now?")
~~~
The system:

Finds the most relevant streamed articles

Builds a context

Asks Gemini to answer strictly from that context

Prints the answer with sources

## 🧠 Architecture

NewsAPI  
   │  
   ▼  
Streaming Pipeline (pipeline.py)  
   │  
   ▼  
SentenceTransformer Embeddings (embeddings.py)  
   │  
   ▼  
In-Memory Vector Store  
   │  
   ▼  
Similarity Search  
   │  
   ▼  
Context Builder  
   │  
   ▼  
Gemini (RAG Answer)  
