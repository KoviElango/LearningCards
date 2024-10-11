# Import necessary libraries
import streamlit as st
from PyPDF2 import PdfReader
from collections import Counter
import spacy

from rake_nltk import Rake
import nltk

def download_nltk_resources():
    """
    Download required NLTK resources if not already present.
    """
    resources = ['punkt', 'stopwords', 'punkt_tab']
    for resource in resources:
        try:
            nltk.data.find(f'tokenizers/{resource}')
        except LookupError:
            print(f"Downloading {resource}...")
            nltk.download(resource, quiet=True)

def download_spacy_model():
    """
    Download the required spaCy model if not already present.
    """
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading spaCy model...")
        spacy.cli.download("en_core_web_sm")

def list_topics(text, top_n=5):
    """
    Extract the top study topics from the given text using RAKE and filter with spaCy.
    
    Args:
    text (str): The input text to extract topics from.
    top_n (int): Number of top topics to return.
    
    Returns:
    list: A list of tuples containing the top entities and their labels.
    """
    # Ensure required resources are downloaded
    download_nltk_resources()
    download_spacy_model()

    # Initialize RAKE
    rake = Rake()

    # Extract keywords using RAKE
    rake.extract_keywords_from_text(text)
    rake_phrases = rake.get_ranked_phrases()

    # Load spaCy model for filtering
    nlp = spacy.load("en_core_web_sm")

    # Filter and label phrases using spaCy
    filtered_topics = []
    for phrase in rake_phrases:
        doc = nlp(phrase)
        if len(doc.ents) > 0:
            # If spaCy recognizes an entity, use its label
            filtered_topics.extend([(ent.text, ent.label_) for ent in doc.ents])
        else:
            # If not recognized as an entity, label it as a CONCEPT
            filtered_topics.append((phrase, "CONCEPT"))

    # Count occurrences and get top N
    topic_counts = Counter(filtered_topics)
    top_topics = topic_counts.most_common(top_n)

    return top_topics

def topic_extractor(uploaded_file):
    """
    Extract and display topics from an uploaded PDF file.
    
    Args:
    uploaded_file: The uploaded PDF file object.
    """
    st.subheader("Topic Extractor")
    
    if uploaded_file is not None:
        pdf = PdfReader(uploaded_file)
        text = "".join(page.extract_text() for page in pdf.pages)
        
        topics = list_topics(text)
        st.write("Extracted Topics:")
        for entity, label in topics:
            st.write(f"- {entity} - {label}")
    else:
        st.write("Please upload a PDF file.")





