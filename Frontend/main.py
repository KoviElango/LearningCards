# Main application for PDF processing
import streamlit as st
from topic_extractor import topic_extractor
from pdf_display import pdf_viewer
from flash_cards import question_list

def main():
    # Set up the Streamlit page configuration
    st.set_page_config(layout="wide")
    st.title("PDF Processing Tool")

    # Create a three-column layout
    col1, col2, col3 = st.columns(3)

    # Add a file uploader to the sidebar for PDF files
    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

    # Populate the first column with the topic extractor
    with col1:
        topic_extractor(uploaded_file)

    # Populate the second column with the PDF viewer
    with col2:
        pdf_viewer(uploaded_file)

    # Populate the third column with the question list
    with col3:
        question_list()

# Ensure the main function is only run when this script is executed directly
if __name__ == "__main__":
    main()