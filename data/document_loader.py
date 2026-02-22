from pypdf import PdfReader
import os

def load_documents(folder_path="data/documents"):
    texts = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, file))
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)

    return texts

def chunk_text(texts, chunk_size=300):
    chunks = []

    for text in texts:
        words = text.split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i+chunk_size])
            chunks.append(chunk)

    return chunks