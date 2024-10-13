import streamlit as st
from topic_extractor import extract_topics, display_topics
from pdf_display import pdf_viewer
from flash_cards import question_list
from summarize_text import summarize_text  # Import the new summarize function

def main():
    """
    Main function to run the PDF Processing Tool.
    """
    st.set_page_config(layout="wide")
    st.sidebar.title("PDF Processing Tool")

    # Upload PDF and display the content in the sidebar
    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")
    
    # Check if the uploaded file has changed
    if uploaded_file is not None:
        extracted_text = pdf_viewer(uploaded_file)
        
        if extracted_text:
            # Reset session state for topics when a new file is uploaded
            if 'extracted_topics' in st.session_state:
                del st.session_state['extracted_topics']
            if 'topic_states' in st.session_state:
                del st.session_state['topic_states']
            if 'page_number' not in st.session_state:
                st.session_state.page_number = 0  # Initialize page number

            # Three-column layout
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("_This is the list of Key Topics from the page_")
                topics = extract_topics(extracted_text)
                display_topics(topics)
            
            with col2:
                st.write("_Hover to reveal answers_")
                
                # Display the questions if they have been generated
                if 'questions' in st.session_state and st.session_state.questions:
                    question_list(st.session_state.questions)
            
            with col3:
                st.write("_Summary with analogy_")
                summary = summarize_text(extracted_text)  # Call the new summarize function
                st.write(summary)  # Display the summary

if __name__ == "__main__":
    main()
