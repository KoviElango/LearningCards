# PDF Processing Tool + Learning Cards

![PDF Processing Tool](https://img.shields.io/badge/Streamlit-PDF--Processing-blue)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
The ** PDF Processing Tool + Learning Cards** is a web application built with Streamlit that allows users to upload PDF documents, view their contents, and extract key topics and questions from the text using Large Language Models (LLMs). It provides a user-friendly interface for document analysis and navigation through multiple pages.

## Features
- 📄 **PDF Viewer**: Displays the contents of uploaded PDF documents.
- 📋 **Topic Extraction**: Automatically extracts key topics from each page of the PDF using LLMs.
- ❓ **Question Generation**: Generates questions based on the text of each page.
- 📑 **Page Navigation**: Allows users to navigate between different pages of the PDF without losing extracted data.
- ⚡ **State Management**: Uses Streamlit's session state to cache and persist extracted topics and questions for each page.

## Tech Stack
- **Python**: Core programming language used for backend logic.
- **Streamlit**: Used for building an interactive web-based user interface.
- **LLM APIs**: Utilizes APIs such as Groq or OpenAI to extract topics and generate questions.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pdf-processing-tool.git
    cd pdf-processing-tool
    ```

2. Set up a virtual environment (recommended):
    ```bash
    python3 -m venv ai
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory with your API keys:
     ```
     GROQ_API_KEY=your_groq_api_key
     ```

## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the tool.

3. **Upload a PDF**: Choose a PDF file from your system using the file uploader.

4. **Navigate through pages**: Use the "Next Page" and "Previous Page" buttons to browse through the document.

5. **View Extracted Data**: 
   - **Topics**: View the automatically extracted topics from each page.
   - **Questions**: Check the generated questions based on the text from each page.
