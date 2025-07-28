import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    sections = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        sections.append({
            "document": file_path.split("/")[-1],
            "page_number": page_num + 1,
            "text": text.strip()
        })
    return sections