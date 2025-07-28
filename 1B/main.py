import os
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from utils.pdf_utils import extract_text_from_pdf

DOCUMENTS_DIR = "documents"
TOP_K_SECTIONS = 5
MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

all_sections = []
input_documents = []
for file in os.listdir(DOCUMENTS_DIR):
    if file.endswith(".pdf"):
        full_path = os.path.join(DOCUMENTS_DIR, file)
        input_documents.append(file)
        sections = extract_text_from_pdf(full_path)
        all_sections.extend(sections)

persona = "Travel Planner"
job_to_be_done = "Plan a trip of 4 days for a group of 10 college friends."
query_embedding = model.encode(f"{persona}: {job_to_be_done}")

section_texts = [s["text"] for s in all_sections]
section_embeddings = model.encode(section_texts)
sims = cosine_similarity([query_embedding], section_embeddings)[0]
ranked = sorted(zip(all_sections, sims), key=lambda x: x[1], reverse=True)

extracted_sections = []
for rank, (sec, _) in enumerate(ranked[:TOP_K_SECTIONS]):
    extracted_sections.append({
        "document": sec["document"],
        "section_title": sec["text"].split("\n")[0][:80],
        "importance_rank": rank + 1,
        "page_number": sec["page_number"]
    })

subsection_analysis = []
for sec, _ in ranked[:TOP_K_SECTIONS]:
    paragraphs = [p for p in sec["text"].split("\n\n") if len(p.strip()) > 100]
    for p in paragraphs[:2]:
        subsection_analysis.append({
            "document": sec["document"],
            "refined_text": p.strip(),
            "page_number": sec["page_number"]
        })

output = {
    "metadata": {
        "input_documents": input_documents,
        "persona": persona,
        "job_to_be_done": job_to_be_done,
        "processing_timestamp": datetime.now().isoformat()
    },
    "extracted_sections": extracted_sections,
    "subsection_analysis": subsection_analysis
}

with open("challenge1b_output.json", "w") as f:
    json.dump(output, f, indent=4)

print("✅ Output saved to challenge1b_output.json")