import streamlit as st
from PyPDF2 import PdfReader

def pdf_viewer(uploaded_file):
    """
    Display the contents of an uploaded PDF file.
    
    Args:
    uploaded_file: The uploaded PDF file object.
    """
    st.subheader("PDF Viewer")
    
    if uploaded_file is not None:
        pdf = PdfReader(uploaded_file)
        for i, page in enumerate(pdf.pages):
            st.write(f"Page {i + 1}")
            st.write(page.extract_text())
            return page.extract_text()
    else:
        st.write("Please upload a PDF file.")