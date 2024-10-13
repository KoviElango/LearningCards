import streamlit as st

def question_list(questions):
    """
    Display a list of predefined questions with hidden answers revealed on hover.
    """
    st.subheader("Flash cards on the topic")
    for i, question in enumerate(questions):
        question_text = question['question']
        answer_text = question['answer']

        # CSS for hover effect
        st.markdown(f"""
        <style>
        .answer{i} {{
            color: transparent;
            background-color: transparent;
            transition: color 0.4s ease;
        }}
        .answer-container{i}:hover .answer{i} {{
            color: Red;
        }}
        .answer-container{i} {{
            margin-bottom: 20px;
        }}
        </style>
        """, unsafe_allow_html=True)

        # Display the question and the hidden answer with hover effect
        st.markdown(f"""
        <div class="answer-container{i}">
            <p><strong>Question {i + 1}: {question_text}</strong></p>
            <p>Answer: <span class="answer{i}"><em>{answer_text}</em></span></p>
        </div>
        """, unsafe_allow_html=True)