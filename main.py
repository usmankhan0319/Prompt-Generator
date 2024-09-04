import openai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def gptInit(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you prefer
        messages=[
            {"role": "system", "content": "You are the most helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=0.9,
        n=1,  # Number of responses to generate
        stop=None,
        frequency_penalty=0.9,
        presence_penalty=0.9
    )
    # Extract the generated text from the response
    response_text = response.choices[0].message['content'].strip()

    return response_text

# Streamlit UI
st.title("Prompt Generator")

# Input for the prompt
prompt_input = st.text_area("Enter your prompt here", height=50)

if st.button("Generate Response"):
    if prompt_input.strip():
        response = gptInit(prompt_input)
        st.markdown("### Generated Response:")
        st.markdown(response)
    else:
        st.warning("Please enter a prompt to generate a response.")
