from pypdf import PdfReader

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

from resume_parser import extract_text

text = extract_text("resume.pdf")

print(text[:1000])