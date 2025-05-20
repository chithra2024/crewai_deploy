import streamlit as st
from main import FinanceCrew
import os

st.title('💼 Investment Recommendation Assistant')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Input Financial Topic')
    topic = st.text_input("Financial Topic or Market:")
    detailed_questions = st.text_area("Investment Questions or Concerns:")

if st.button('Get Recommendation'):
    if not topic or not detailed_questions:
        st.error("Please fill in all fields.")
    else:
        inputs = f"Topic: {topic}\nDetails: {detailed_questions}"
        finance_crew = FinanceCrew(inputs)
        result = finance_crew.run()
        st.subheader("📊 Investment Report:")
        st.write(result)
