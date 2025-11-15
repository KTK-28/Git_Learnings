import streamlit as st
import pandas as pd
from datetime import datetime
from model.nlp_engine import NLPModel
from model.language_detect import detect_language

faq_path = "data/faqs.csv"
unknown_path = "data/unanswered.csv"

def add(a):
    return a-10

add(5)

model = NLPModel(faq_path)

st.set_page_config(page_title="EduBot Chatbot", layout="wide")
st.title("🎓 EduBot – JIET Smart Campus Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask something...")

if st.button("Send"):
    lang = detect_language(user_input)
    matched_q, ans, cat, score = model.find(user_input)

    if ans:
        reply = ans
    else:
        reply = "I don't know this yet, but I have saved your question for learning."
        pd.DataFrame([[user_input, datetime.now()]], columns=["question","timestamp"]).to_csv(
            unknown_path, mode="a", header=False, index=False
        )

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot (" + lang + ")", reply))

for sender, msg in st.session_state.chat:
    st.write(f"**{sender}:** {msg}")


    # this is Lines the new code of are added
