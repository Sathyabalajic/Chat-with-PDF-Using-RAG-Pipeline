from pdf_processor import extract_text_from_pdf, chunk_text
from embedding_handler import generate_embeddings, store_embeddings_in_faiss
from query_handler import query_to_embeddings, retrieve_relevant_chunks
from llm_responder import generate_response_with_llm

def main_pipeline(pdf_path, user_query):
    # Step 1: Extract and Chunk PDF
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    
    # Step 2: Generate Embeddings and Store
    embeddings, model = generate_embeddings(chunks)
    index = store_embeddings_in_faiss(embeddings)
    
    # Step 3: Handle Query
    query_embedding = query_to_embeddings(user_query, model)
    relevant_chunks = retrieve_relevant_chunks(query_embedding, index, chunks)
    
    # Step 4: Generate Response
    response = generate_response_with_llm(relevant_chunks, user_query)
    return response

if __name__ == "__main__":
    pdf_path = "data/sample.pdf"
    user_query = "What is the unemployment rate for Bachelor's degree holders?"
    
    response = main_pipeline(pdf_path, user_query)
    print("Response:\n", response)
