from docx import Document

# Load the DOCX file
doc = Document("example.docx")

# Extract text from the document
for paragraph in doc.paragraphs:
    print(paragraph.text)


import PyPDF2

# Open the PDF file
with open("example.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    
    # Extract text from each page
    for page in reader.pages:
        print(page.extract_text())

def get_file_type_by_magic_number(file_path):
    with open(file_path, 'rb') as file:
        file_signature = file.read(4)

    # Check for magic numbers
    if file_signature.startswith(b'%PDF'):
        return "PDF File"
    elif file_signature == b'\x50\x4B\x03\x04':  # DOCX starts with PK\x03\x04
        return "DOCX File"
    else:
        with open(file_path, 'rb') as file:
            content = file.read(1024)
            try:
                content.decode('utf-8')
                return "Text File"
            except UnicodeDecodeError:
                return "Unknown File Type"

# Example usage
file_type = get_file_type_by_magic_number("example.docx")
print(file_type)
