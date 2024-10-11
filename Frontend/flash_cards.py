import streamlit as st

def question_list():
    """
    Display a list of predefined questions about the document.
    """
    st.subheader("Questions")
    questions = [
        "What is the main topic of this document?",
        "Who is the target audience for this content?",
        "What are the key findings or conclusions?",
        "Are there any important dates or deadlines mentioned?",
        "What are the main arguments presented in the document?"
    ]
    
    # Display numbered questions
    for i, question in enumerate(questions, 1):
        st.write(f"{i}. {question}")