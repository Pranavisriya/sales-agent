import uuid
import streamlit as st
from agent import answer  

st.set_page_config(page_title="Sales Agent", page_icon="🛍️", layout="centered")
st.title("🛍️ Sales Agent (LangGraph prototype)")
st.caption("Frontend only — calls agent.answer(user_text, thread_id)")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = f"thread-{uuid.uuid4().hex[:8]}"
if "chat" not in st.session_state:
    st.session_state.chat = []

with st.sidebar:
    st.subheader("Session")
    st.write(f"**Thread ID:** `{st.session_state.thread_id}`")
    if st.button("🔄 New thread", use_container_width=True):
        st.session_state.thread_id = f"thread-{uuid.uuid4().hex[:8]}"
        st.session_state.chat = []
        st.rerun()

for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

user_text = st.chat_input("Ask for recommendations or checkout by product_id…")
if user_text:
    st.chat_message("user").write(user_text)
    st.session_state.chat.append({"role": "user", "content": user_text})
    resp = answer(st.session_state.thread_id, user_text)  
    st.chat_message("assistant").write(resp)
    st.session_state.chat.append({"role": "assistant", "content": resp})
