import requests, time
from embeddings import embed, cosine_similarity

NEWS_API = "https://newsapi.org/v2/top-headlines"

docs_store = []
vector_store = []

def build_pipeline(api_key):
    print("Fetching initial news...")

    params = {
        "country": "us",
        "apiKey": api_key,
        "pageSize": 20
    }

    res = requests.get(NEWS_API, params=params).json()
    articles = res.get("articles", [])

    print(f"Fetched {len(articles)} articles. Streaming like LIVE data...")

    for a in articles:
        text = f"{a.get('title','')} {a.get('description','')}"
        vector = embed(text)[0]

        docs_store.append({
            "id": a["url"],
            "text": text,
            "timestamp": a.get("publishedAt","")
        })

        vector_store.append(vector)

        print("STREAMED:", a.get("title",""))
        time.sleep(5)

def search_similar(query, top_k=3):
    if not docs_store:
        return []

    q_vec = embed(query)[0]
    sims = []

    for i, vec in enumerate(vector_store):
        sim = cosine_similarity(q_vec, vec)
        sims.append((sim, docs_store[i]))

    sims.sort(reverse=True, key=lambda x: x[0])
    return [x[1] for x in sims[:top_k]]
