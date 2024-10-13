import streamlit as st
from PyPDF2 import PdfReader
from generate_questions import generate_questions_from_text  # Ensure to import the function

def pdf_viewer(uploaded_file):
    """
    Display PDF content and extract text with pagination.
    """
    st.subheader("PDF Viewer")
    
    if uploaded_file is not None:
        pdf = PdfReader(uploaded_file)
        total_pages = len(pdf.pages)
        page_number = st.session_state.get('page_number', 0)  # Get current page number from session state

        # Pagination controls
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("Previous") and page_number > 0:
                st.session_state.page_number -= 1  # Go to the previous page
        with col2:
            if st.button("Next") and page_number < total_pages - 1:
                st.session_state.page_number += 1  # Go to the next page

        # Display the current page
        st.write(f"Page {page_number + 1}")
        text = pdf.pages[page_number].extract_text()
        st.write(text)

        # Automatically generate questions when the page is switched
        if 'extracted_text' not in st.session_state or st.session_state.page_number != page_number:
            st.session_state.extracted_text = "".join(page.extract_text() for page in pdf.pages)  # Store all text
            st.session_state.questions = generate_questions_from_text(st.session_state.extracted_text, num_questions=5)

        return st.session_state.extracted_text
    else:
        st.write("Please upload a PDF file.")
        return None