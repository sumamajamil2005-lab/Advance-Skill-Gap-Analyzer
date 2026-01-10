import os
import pdfplumber
from docx import Document



# pdf and docx support: 
def extract_and_save_resume(file_path):
    """
    Extracts text from PDF/DOCX and saves it to 'data/resume.txt'.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return False

    name, extension = os.path.splitext(file_path)
    extension = extension.lower()

    extracted_text = ""

    try:
        if extension == '.pdf':
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        extracted_text += text + "\n"
            
        elif extension == '.docx':
            doc = Document(file_path)
            for para in doc.paragraphs:
                extracted_text += para.text + "\n"
        
        else:
            print(f"Warning: Extension {extension} is not supported.")
            return False
        
        if extracted_text.strip():
            output_dir = "data"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            output_file = os.path.join(output_dir, "resume.txt")
            
            with open(output_file, "w", encoding="utf-8-sig") as f:
                f.write(extracted_text.strip())
            
            print(f"\nText saved to {output_file}")
            return True
        else:
            print("\nNo text could be extracted.")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False