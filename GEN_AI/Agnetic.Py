cdimport os
import pandas as pd
from docx import Document
from openpyxl import load_workbook
import PyPDF2

# Specify path
path = "/path/to/your/files"

# Retrieve files
files = os.listdir(path)

# Process files
for file in files:
    file_path = os.path.join(path, file)
    
    # Handle .txt files
    if file.endswith(".txt"):
        with open(file_path, "r") as f:
            text = f.read()
            print(text)

    # Handle .docx files
    elif file.endswith(".docx"):
        document = Document(file_path)
        text = "\n".join([paragraph.text for paragraph in document.paragraphs])
        print(text)

    # Handle .xlsx files
    elif file.endswith(".xlsx"):
        wb = load_workbook(file_path)
        sheet = wb.active
        data = []
        for row in sheet.rows:
            data.append([cell.value for cell in row])
        df = pd.DataFrame(data)
        print(df)

    # Handle .pdf files
    elif file.endswith(".pdf"):
        pdf_file_obj = open(file_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        pdf_file_obj.close()
        print(text)
