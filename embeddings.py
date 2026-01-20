from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading Embedding Model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Loaded!")

def embed(texts):
    if isinstance(texts, str):
        texts = [texts]
    vectors = model.encode(texts)
    return np.array(vectors)

def cosine_similarity(a, b):
    a_norm = a / np.linalg.norm(a)
    b_norm = b / np.linalg.norm(b)
    return float(np.dot(a_norm, b_norm))
