import PyPDF2

# Specify the file name
input_file = 'The-Oxford-Bible-Commentary.pdf'
output_file = 'The-Oxford-Bible-Commentary.txt'

# Open the PDF file
with open(input_file, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        for page in reader.pages:
            text = page.extract_text()
            if text:
                txt_file.write(text + '\n')
    print(f"Text has been saved to {output_file}")