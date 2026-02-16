import streamlit as st
from models.vector_store import search
from PIL import Image
import os

import time
from models.local_llm import generate_response
from models.vector_store import search

# Page settings
st.set_page_config(
    page_title="Banking AI Assistant",
    page_icon="🏦",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.header {
    background-color: #0b3d91;
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 12px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
col1, col2 = st.columns([1,6])

with col1:
    logo_path = "assets/bank_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)

with col2:
    st.markdown(
        '<div class="header"><h2>AI Customer Support Assistant</h2></div>',
        unsafe_allow_html=True
    )

st.write("")

# ---------- Sidebar ----------
with st.sidebar:
    st.title("🏦 Banking AI")
    st.markdown("### Services Covered")
    st.write("- Account Information")
    st.write("- Fund Transfers (NEFT/RTGS/IMPS)")
    st.write("- Debit/Credit Cards")
    st.write("- Loan Information")
    st.write("- Branch & Customer Support")
    st.markdown("---")
    st.info("This is an offline AI assistant using Semantic Search (FAISS).")

# ---------- Welcome Section ----------
st.markdown("### Welcome!")
st.write("Ask any banking-related question and the AI will help you instantly.")

# ---------- Chat Memory ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- Chat Input ----------
query = st.chat_input("Ask your banking question...")

if query:
    # Show user message
    with st.chat_message("user"):
        st.write(query)

    # Retrieve context from FAISS
    results = search(query, top_k=3)
    context = "\n".join([r[0] for r in results])

    # Assistant message with typing animation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Get LLM answer
        llm_answer = generate_response(context, query)

        # Typing effect
        for word in llm_answer.split():
            full_response += word + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.03)

        message_placeholder.markdown(full_response)

        # Related suggestions
        st.markdown("**Related information:**")
        for ans, _ in results[1:]:
            st.write("- " + ans)

# ---------- Footer ----------
st.markdown(
    '<div class="footer">Banking AI Assistant | Built with Streamlit, FAISS & Sentence Transformers</div>',
    unsafe_allow_html=True
)