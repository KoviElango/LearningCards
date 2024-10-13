import streamlit as st
import openai
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API
api_key = os.getenv("GROQ_API_KEY")
openai.api_key = api_key
openai.api_base = "https://api.groq.com/openai/v1"
client = Groq(api_key=api_key)

def extract_topics(text):
    """
    Extract key topics from the given text using an LLM.
    """
    # Check if topics are already in session state
    if 'extracted_topics' not in st.session_state:
        prompt = f"Extract all important topic names from the text:\n\n{text[:4000]}"
        
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}]
            )
            topics = response.choices[0].message.content.strip().split('\n')
            topics = [topic.strip() for topic in topics[1:] if topic]  # Skip the first line
            
            # Store the extracted topics in session state
            st.session_state.extracted_topics = topics
        
        except Exception as e:
            st.error(f"Error extracting topics: {str(e)}")
            st.session_state.extracted_topics = []
    
    return st.session_state.extracted_topics

def display_topics(topics):
    """
    Display the extracted topics using Streamlit.
    """
    st.write("Extracted Topics:")
    
    # Initialize topic states if not already present
    if 'topic_states' not in st.session_state:
        st.session_state.topic_states = {topic: False for topic in topics}
    
    # Display each topic as a checkbox
    for topic in topics:
        st.markdown(f"{topic}")