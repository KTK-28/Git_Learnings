import streamlit as st
import pandas as pd

faq_path = "data/faqs.csv"
unknown_path = "data/unanswered.csv"

st.title("🔧 Admin Panel – Train the Bot")

if st.button("Refresh"):
    st.rerun()

df_unknown = pd.read_csv(unknown_path)
df_faq = pd.read_csv(faq_path)

for idx, row in df_unknown.iterrows():
    st.write(f"❓ {row['question']}")
    ans = st.text_input(f"Answer for Q{idx}")
    if st.button(f"Save {idx}"):
        df_faq.loc[len(df_faq)] = [row['question'], ans, "Uncategorized"]
        df_faq.to_csv(faq_path, index=False)
        df_unknown.drop(idx).to_csv(unknown_path, index=False)
        st.success("Added & learned successfully ✅")
        st.rerun()
