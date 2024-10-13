import streamlit as st
from topic_extractor import extract_topics, display_topics
from pdf_display import pdf_viewer
from generate_questions import generate_questions_from_text
from flash_cards import question_list

def main():
    """
    Main function to run the PDF Processing Tool.
    """
    st.set_page_config(layout="wide")
    st.title("PDF Processing Tool")

    # Upload PDF and display the content
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
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
                st.write("**Topics Extracted**")
                topics = extract_topics(extracted_text)
                display_topics(topics)
            
            with col2:
                st.write("**Questions**")
                
                # Display the questions if they have been generated
                if 'questions' in st.session_state and st.session_state.questions:
                    question_list(st.session_state.questions)
            
            with col3:
                st.write("**PDF Preview**")
                st.write(extracted_text[:500])  # Limit text shown to a preview

if __name__ == "__main__":
    main()
