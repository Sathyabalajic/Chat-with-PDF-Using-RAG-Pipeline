from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def generate_embeddings(chunks, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    return embeddings, model

def store_embeddings_in_faiss(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index
