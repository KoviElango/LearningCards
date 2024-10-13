import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def summarize_text(extracted_text):
    # Prepare the API request to generate a summary with an analogy
    prompt = f"Summarize the following text with an analogy:\n\n{extracted_text[:4000]}."
    
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Print the full response for debugging
        print(response.choices[0].message.content)  # Print the raw response from the LLM
        
        return response.choices[0].message.content.strip()  # Return the summary
    
    except Exception as e:
        return f"Error summarizing text: {str(e)}"
