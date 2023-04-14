import os
import openai
import streamlit as st

# Set OpenAI API key
openai.api_key = "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"

# Set the model
model = "text-davinci-003"

messages = [
        {"role": "system", "content": "You are a helpful but also a very sarcastic assistant. You are also funny and also give random jokes."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "Marv", "content": "Well I guess Google was busy, right? The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"},
        {"role": "Marv", "content": "Gimee a break, I'm not a Google search engine. It was played at Globe Life Field in Arlington, Texas."},
        ]
@st.cache_data
def get_response(prompt):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("Sarcastic Chatbot")

input_text = st.text_input("Ask your question:")

if input_text:
    prompt = f"Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\n, You: {input_text}\nMarv:"
    response = get_response(prompt)
    st.write(f"Marv: {response}")
