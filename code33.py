import openai
import pandas as pd
import os
from tqdm import tqdm
import streamlit as st
 
# Initialize OpenAI API key
openai.api_key = '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'
 

# Function to retrieve relevant information based on user input
def retrieve_information(user_input):
    # Implement retrieval logic here
    # Example: Retrieve relevant information from a database or external source
    return "Relevant information retrieved based on user input."

# Function to generate a sample request for proposal using GPT-3
def generate_rfp(prompt, retrieved_info):
    # Combine user prompt with retrieved information
    combined_input = prompt + " " + retrieved_info

    try:
        # Generate RFP using GPT-3
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Use the text-davinci-003 model
            prompt=combined_input,
            max_tokens=500
        )
        generated_rfp = response.choices[0].text.strip()
        return generated_rfp
    except openai.error.InvalidRequestError as e:
        st.error(f"Error generating RFP: {e}")

# Streamlit interface
def main():
    st.title("Retrieval-Augmented Generative Model for RFP Generation")

    # User input prompt
    user_input = st.text_input("Enter your RFP prompt or requirements:")

    # Retrieve relevant information based on user input
    retrieved_info = retrieve_information(user_input)

    if retrieved_info:
        # Generate RFP using the retrieval-augmented generative model
        generated_rfp = generate_rfp(user_input, retrieved_info)

        # Display generated RFP
        st.subheader("Generated RFP:")
        st.write(generated_rfp)

if __name__ == "__main__":
    main()
