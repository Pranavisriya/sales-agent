# # frontend/streamlit_app.py
# import os
# import uuid
# import requests
# import streamlit as st

# API_BASE = os.getenv("API_BASE", "http://127.0.0.1:8000")

# st.set_page_config(page_title="Sales Agent", page_icon="🛍️", layout="centered")
# st.title("🛍️ Sales Agent (FastAPI + LangGraph)")
# st.caption("Frontend calls your existing LangGraph agent via a FastAPI endpoint.")

# # Session state
# if "thread_id" not in st.session_state:
#     st.session_state.thread_id = f"thread-{uuid.uuid4().hex[:8]}"
# if "chat" not in st.session_state:
#     st.session_state.chat = []

# with st.sidebar:
#     st.subheader("Session")
#     st.write(f"**Thread ID:** `{st.session_state.thread_id}`")
#     new_api = st.text_input("API Base", value=API_BASE, help="e.g., http://127.0.0.1:8000")
#     if new_api != API_BASE:
#         os.environ["API_BASE"] = new_api
#     if st.button("🔄 New thread", use_container_width=True):
#         st.session_state.thread_id = f"thread-{uuid.uuid4().hex[:8]}"
#         st.session_state.chat = []
#         st.rerun()

# # Render history
# for msg in st.session_state.chat:
#     st.chat_message(msg["role"]).write(msg["content"])

# # Chat input -> call backend /answer (no changes to your agent code)
# user_text = st.chat_input("Ask for recommendations or checkout by product_id…")
# if user_text:
#     st.chat_message("user").write(user_text)
#     st.session_state.chat.append({"role": "user", "content": user_text})

#     try:
#         api_base = os.getenv("API_BASE", API_BASE)
#         r = requests.post(
#             f"{api_base}/answer",
#             json={"thread_id": st.session_state.thread_id, "user_text": user_text},
#             timeout=60,
#         )
#         r.raise_for_status()
#         reply = r.json().get("reply", "")
#     except Exception as e:
#         reply = f"Sorry, backend error: {e}"

#     st.chat_message("assistant").write(reply)
#     st.session_state.chat.append({"role": "assistant", "content": reply})

# frontend/streamlit_app.py
import os
import uuid
import requests
import streamlit as st

# Point to your FastAPI server; override with: API_BASE="http://127.0.0.1:8000" streamlit run frontend/streamlit_app.py
API_BASE = os.getenv("API_BASE", "http://127.0.0.1:8000")

st.set_page_config(page_title="Sales Agent", page_icon="🛍️", layout="centered")
st.title("🛍️ Sales Agent (FastAPI + LangGraph)")

# ---- Session state ----
if "thread_id" not in st.session_state:
    st.session_state.thread_id = f"thread-{uuid.uuid4().hex[:8]}"
if "chat" not in st.session_state:
    st.session_state.chat = []

with st.sidebar:
    st.subheader("Session")
    st.write(f"**Thread ID:** `{st.session_state.thread_id}`")
    api_base_in = st.text_input("API Base", value=API_BASE, help="e.g., http://127.0.0.1:8000")
    if api_base_in != API_BASE:
        API_BASE = api_base_in  # use typed value for this session
    if st.button("🔄 New thread", use_container_width=True):
        st.session_state.thread_id = f"thread-{uuid.uuid4().hex[:8]}"
        st.session_state.chat = []
        st.rerun()

# ---- Render history ----
for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

# ---- Chat input -> call backend /answer ----
user_text = st.chat_input("Ask for recommendations or checkout by product_id…")
if user_text:
    st.chat_message("user").write(user_text)
    st.session_state.chat.append({"role": "user", "content": user_text})

    try:
        r = requests.post(
            f"{API_BASE}/answer",
            json={"thread_id": st.session_state.thread_id, "user_text": user_text},
            timeout=60,
        )
        r.raise_for_status()
        reply = r.json().get("reply", "")
    except Exception as e:
        reply = f"Sorry, backend error: {e}"

    st.chat_message("assistant").write(reply)
    st.session_state.chat.append({"role": "assistant", "content": reply})
