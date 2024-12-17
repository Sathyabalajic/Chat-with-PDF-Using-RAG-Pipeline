import openai

def generate_response_with_llm(relevant_chunks, query):
    openai.api_key = "your-openai-api-key"
    context = "\n".join(relevant_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return response['choices'][0]['text']
