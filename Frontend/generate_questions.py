import os
from groq import Groq

# Fetch the API key from the environment (or hardcode it here)
api_key = os.getenv("API_KEY")

# Initialize Groq client with the API key

import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
api_key = os.getenv("GROQ_API_KEY")

# Initialize OpenAI client with the API key and base URL for Groq
openai.api_key = api_key
openai.api_base = "https://api.groq.com/openai/v1"

def generate_questions_from_text(extracted_text, num_questions=5):
    # Prepare the API request to generate questions based on the text
    prompt = f"Generate {num_questions} important questions based on the following text:\n\n{extracted_text}"
    
    # Sending request to Groq API using OpenAI client
    response = openai.ChatCompletion.create(
        model="llama3-8b-8192",  # Use the model of your choice
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extracting the questions from the response
    questions = response.choices[0].message.content
    return questions

# Example usage with mock extracted text
mock_extracted_text = """
Electric vehicles (EVs) are automobiles that are propelled by electric motors, which are powered by rechargeable battery packs. 
Compared to internal combustion engine vehicles, electric cars are quieter, have no exhaust emissions, and lower emissions overall.
They can also reduce dependency on oil and are considered more energy efficient.
"""

# Generate 5 questions from the text
questions = generate_questions_from_text(mock_extracted_text, num_questions=5)

# Print the generated questions
print(questions)
