import streamlit as st




API_KEY = "AIzaSyDZT7LoVq0oPheUeV86ObsdwS8Cq7pcN-U"

from google import genai

client = genai.Client(api_key=API_KEY)



st.title("ai school")
ai_text = st.text_area("enter question")

if st.button("run"):
    try:
        response =  client.models.generate_content(model="gemini-2.0-flash",contents=ai_text)
        st.success(response.text,icon="✅")
    except(Exception) as e:
        st.error(f"propmt failed due to {e}")
    