import os
from groq import Groq
from dotenv import load_dotenv
import openai

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
    prompt = f"Generate {num_questions} important questions based on the following text:\n\n{extracted_text}. Just return 5 questions seperated by /n and nothing else."
    
    # Sending request to Groq API using OpenAI client
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Use the model of your choice
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extracting the questions from the response
    questions = response.choices[0].message.content
    print(questions)
    return questions