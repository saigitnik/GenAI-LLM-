import streamlit as st
from openai import OpenAI

with open('key.txt', 'r') as f:
    api_key = f.read()

st.title("GenAI Code Reviewer")
st.subheader("Let me help you find and fix bugs in your code!")

client = OpenAI(api_key=api_key)

code_to_review = st.text_area("Paste your code here:")

if st.button("Generate"):
    prompt = f"You are an expert in code review. Please find any bugs or errors in the following code and provide the corrected code:\n\n{code_to_review}\n\n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "You are a code bug fixer, you return the bugs in code in an ordered list and also the correct code in jupyter notebook look."}
        ]
    )

    st.write(response.choices[0].message.content)

