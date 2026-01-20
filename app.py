from pipeline import build_pipeline, search_similar
from gemini_client import init_gemini

NEWS_API_KEY = "YOUR_NEWS_API_KEY" 
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

model_g = init_gemini(GEMINI_API_KEY)

def ask(q):
    docs = search_similar(q)

    if not docs:
        print("No streamed news yet")
        return

    context = "\n\n".join([d["text"] for d in docs])

    prompt = f"""
You are a REAL-TIME NEWS AI.
Answer ONLY using the context below.
Do NOT hallucinate.
If unsure say you don't know.

Context:
{context}

Question: {q}

Answer clearly and concise:
"""

    response = model_g.generate_content(prompt)
    print("\nANSWER:\n", response.text)
    print("\n---- SOURCES ----")
    for d in docs:
        print(d["timestamp"], "|", d["text"][:120], "...")

if __name__ == "__main__":
    build_pipeline(NEWS_API_KEY)
    ask("What is news on Trump right now?")
