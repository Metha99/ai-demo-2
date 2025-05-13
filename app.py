import streamlit as st
import requests

st.set_page_config(page_title="OpenRouter Chat", layout="centered")
st.title("🤖 Chat with OpenRouter (Free LLMs)")

API_KEY = st.secrets["OPENROUTER_KEY"]

def ask_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://your-app-name.streamlit.app",  # Replace with your actual Streamlit Cloud URL
        "Content-Type": "application/json",
    }

    json_data = {
        "model": "mistralai/mixtral-8x7b",  # free and powerful
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

query = st.text_input("Ask anything about infrastructure, Azure, or GitLab:")
if query:
    with st.spinner("Thinking..."):
        response = ask_openrouter(query)
        st.success("Response:")
        st.markdown(response)
