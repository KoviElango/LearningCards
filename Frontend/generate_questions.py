import os
from groq import Groq
from dotenv import load_dotenv
import openai
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Initialize OpenAI client with the API key and base URL for Groq
openai.api_key = api_key
openai.api_base = "https://api.groq.com/openai/v1"


def generate_questions_from_text(extracted_text, num_questions=5):
    # Prepare the API request to generate questions based on the text
    prompt = f"Generate {num_questions} important questions in the format 'Q: [Question]' and 'A: [Answer]' based on the following text:\n\n{extracted_text[:4000]}."
    
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Print the full response for debugging
        print(response.choices[0].message.content)  # Print the raw response from the LLM
        
        # Split the response into question-answer pairs
        questions_and_answers = response.choices[0].message.content.split("\n")
        
        questions = []
        current_question = None
        
        for line in questions_and_answers:
            if line.startswith("Q:"):
                current_question = {"question": line[2:].strip(), "answer": ""}
                questions.append(current_question)
            elif line.startswith("A:") and current_question is not None:
                current_question["answer"] = line[2:].strip()
        
        return questions[:num_questions]
    
    except Exception as e:
        st.error(f"Error generating questions: {str(e)}")
        return []


