import streamlit as st
import PyPDF2
import os

def split_text(content, max_words=400000):
    words = content.split()
    total_words = len(words)
    chunks = []

    for i in range(0, total_words, max_words):
        chunks.append(' '.join(words[i:i + max_words]))

    return chunks

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Streamlit App
st.title("PDF to Chunked Text Converter")
st.markdown("Upload a PDF file, and this app will extract and split the text into smaller files.")

# File upload
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
max_words = st.number_input("Set maximum words per chunk", min_value=1, value=400000, step=1000)

if uploaded_file:
    # Get the original file name without extension
    original_filename = os.path.splitext(uploaded_file.name)[0]

    with st.spinner("Extracting text from PDF..."):
        try:
            text = extract_text_from_pdf(uploaded_file)
            st.success("Text extracted successfully!")
            st.write(f"Total words: {len(text.split())}")

            # Split text into chunks
            chunks = split_text(text, max_words)

            # Provide download links for each chunk with original filename and chunk number
            for i, chunk in enumerate(chunks):
                output_file = f"{original_filename}_chunk_{i + 1}.txt"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(chunk)
                st.download_button(
                    label=f"Download Part {i + 1}",
                    data=chunk,
                    file_name=output_file,
                    mime="text/plain",
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
