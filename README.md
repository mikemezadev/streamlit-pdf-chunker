# streamlit-pdf-chunker
# 📚 PDF to Chunked Text Converter 🌟

Easily extract text from PDF files and split it into smaller, manageable chunks for further processing or uploads.

## 🚀 Features
- **PDF to Text Conversion**: Upload any text-based PDF and extract its content seamlessly.
- **Customizable Chunk Size**: Define the maximum number of words per chunk (default: 400,000) for precise control.
- **Downloadable Outputs**: Receive the split text files as ready-to-download `.txt` files.
- **User-Friendly Interface**: Interactive GUI built with Streamlit for hassle-free operation.

## 🛠️ Technologies Used
- **[Streamlit](https://streamlit.io/)**: To build the interactive web app.
- **[PyPDF2](https://pypi.org/project/PyPDF2/)**: For extracting text from PDF files.
- **[Python](https://www.python.org/)**: The programming language powering the app.

## 📖 How It Works
1. Upload a PDF file through the app.
2. Specify the desired word limit per chunk (default is 400,000 words).
3. The app extracts the text from the PDF and splits it into multiple `.txt` files.
4. Download the generated chunks with a single click!

## 🎯 Use Cases
- Preparing large documents for systems with text limits (e.g., NotebookLM, AI tools).
- Extracting and organizing data from PDFs for analysis.
- Simplifying the handling of extensive text files.

## 🔧 Setup and Deployment
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/streamlit-pdf-chunker.git
