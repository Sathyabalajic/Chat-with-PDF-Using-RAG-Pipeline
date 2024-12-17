def query_to_embeddings(query, model):
    query_embedding = model.encode([query])
    return query_embedding

def retrieve_relevant_chunks(query_embedding, index, chunks, top_k=5):
    distances, indices = index.search(query_embedding, top_k)
    relevant_chunks = [chunks[i] for i in indices[0]]
    return relevant_chunks
