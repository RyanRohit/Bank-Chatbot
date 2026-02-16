from openai import OpenAI

def generate_answer(context, query):
    prompt = f"""
    You are a banking assistant.

    Context:
    {context}

    Question:
    {query}

    Answer briefly based only on the context.
    If not found, say: This query requires human assistance.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content