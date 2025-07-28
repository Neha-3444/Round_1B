# 🔍 Challenge 1B – Persona-Driven Document Intelligence

> Adobe India Hackathon 2025 – Round 1B Submission  
> Author: **Aditya Bayya**

---

##  Problem Statement

Given a persona and a job-to-be-done (JTBD), extract the most relevant sections from a set of PDF documents. The system must semantically understand the request and provide ranked document excerpts without internet access, under 1GB RAM, and within 60 seconds.

---

## 🏗️ Approach Overview

Our pipeline follows these steps:

1. **Extract Text** from PDF documents page-wise using PyMuPDF (`fitz`).
2. **Embed Text Sections** using `all-MiniLM-L6-v2` from Sentence Transformers.
3. **Compute Similarity** between the embedded query and each document section using cosine similarity.
4. **Rank Sections** and pick the top 5 most relevant sections.
5. **Subsection Extraction** from top sections based on paragraph length and position.

---

##  Project Structure

├── Dockerfile
├── main.py
├── requirements.txt
├── challenge1b_output.json
├── approach_explanation.md
└── documents/

---
## Build Docker Image

docker build -t adobe-1b-solution .
---

## Run Container

docker run -v $(pwd)/documents:/app/documents adobe-1b-solution

---
## Sample challenge1b_output

{
  "metadata": {
    "input_documents": ["Learn Acrobat - Share_1.pdf", ...],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a trip of 4 days for a group of 10 college friends.",
    "processing_timestamp": "2025-07-27T14:47:14.300665"
  },
  "extracted_sections": [
    {
      "document": "The Ultimate PDF Sharing Checklist.pdf",
      "section_title": "The Ultimate PDF Sharing Checklist",
      "importance_rank": 1,
      "page_number": 1
    },
    ...
  ],
  "subsection_analysis": [
    {
      "document": "Learn Acrobat - Share_1.pdf",
      "refined_text": "This is sample content for Learn Acrobat - Share_1...",
      "page_number": 1
    }
  ]
}
---

