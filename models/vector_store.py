import faiss
import numpy as np

from data.faqs import faqs
from data.document_loader import load_documents, chunk_text
from models.embeddings import get_embedding


#Load FAQs
faq_texts = faqs  # since faqs is already a list of strings

#Load PDF Documents
pdf_texts = load_documents()
pdf_chunks = chunk_text(pdf_texts)

#Combine Knowledge Base
knowledge_base = faq_texts + pdf_chunks

print(f"Total knowledge items: {len(knowledge_base)}")

#Create Embeddings
embeddings = get_embedding(knowledge_base)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

print("FAISS index created successfully.")

#Search Function
def search(query, top_k=3):
    query_embedding = get_embedding([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for i in range(top_k):
        text = knowledge_base[indices[0][i]]
        distance = distances[0][i]
        results.append((text, distance))

    return results