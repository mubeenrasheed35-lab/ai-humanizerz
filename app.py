import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Humanizer & Plagiarism Remover", page_icon="✍️", layout="centered")

st.title("🤖 AI Humanizer & Plagiarism Remover")
st.write("Apna text niche paste karein aur spelling mistakes, plagiarism, aur robotic tone khatam karke 100% human-like text hasil karein.")

api_key = st.text_input("Apni Google Gemini API Key Enter Karein:", type="password")
user_text = st.text_area("Yahan apna text paste karein:", height=200, placeholder="Yahan text likhein ya paste karein...")

if st.button("Transform & Humanize Text"):
    if not api_key:
        st.error("Pehle apni Gemini API Key enter karein!")
    elif not user_text:
        st.error("Kripya kuch text toh enter karein!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-pro")
            
            prompt = f"""
            Act as an advanced AI Humanizer, Professional Copywriter, and Plagiarism Remover. 
            Process the text provided below and transform it completely following these rules:
            1. Plagiarism Removal: Rewrite sentences entirely using fresh structure, synonyms, and unique flow.
            2. Grammar & Spelling: Fix all spelling errors, grammatical mistakes, and punctuation issues.
            3. Human Tone: Make every single word sound natural, conversational, and written by a human. Eliminate any robotic AI patterns or predictable sentence structures.
            4. Core Meaning: Keep the original meaning and context intact.

            Text to process:
            {user_text}
            """
            
            with st.spinner("Processing text... Please wait..."):
                response = model.generate_content(prompt)
                
            st.success("Text Successfully Transformed!")
            st.subheader("Output (Human & Cleaned Text):")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Koi error aa gaya hai: {e}")
