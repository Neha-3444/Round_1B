# 🔍 Challenge 1B – Persona-Driven Document Intelligence

> **Adobe India Hackathon 2025 – Round 1B Submission**  
> **Author**: Aditya Bayya & M. Neha Reddy

---

## 🧩 Problem Statement

Design a system that, given a **persona** and a **job-to-be-done (JTBD)**, can extract and rank the most relevant sections from a set of PDF documents. The system should:

- Semantically understand the query.
- Run **without internet access**.
- Complete processing within **60 seconds**.
- Consume **≤ 1GB RAM**.

---

## 🏗️ Approach Overview

Our document intelligence pipeline follows these steps:

1. **Text Extraction**  
   - Extract text **page-wise** from PDF files using `PyMuPDF` (`fitz`).

2. **Text Embedding**  
   - Embed sections using **`all-MiniLM-L6-v2`** model from **Sentence Transformers**.

3. **Semantic Similarity**  
   - Compute **cosine similarity** between query embedding and section embeddings.

4. **Ranking & Selection**  
   - Rank sections based on similarity scores.
   - Select **top 5** most relevant sections.

5. **Subsection Analysis**  
   - Refine output using **paragraph segmentation**, **length filtering**, and **positional context**.

---

## 📁 Project Structure

```
Round_1B/
├── Dockerfile
├── main.py
├── requirements.txt
├── challenge1b_output.json
├── approach_explanation.md
└── documents/
```

---

## 🐳 Build Docker Image

```bash
docker build -t adobe-1b-solution .
```

---

## 🚀 Run Container

```bash
docker run -v $(pwd)/documents:/app/documents adobe-1b-solution
```

> 📝 Ensure your PDFs are placed inside the `documents/` folder before running.

---

## 🧾 Sample `challenge1b_output.json`

```json
{
  "metadata": {
    "input_documents": ["Learn Acrobat - Share_1.pdf", "The Ultimate PDF Sharing Checklist.pdf"],
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
    {
      "document": "Learn Acrobat - Share_1.pdf",
      "section_title": "Quick Sharing Tools",
      "importance_rank": 2,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "document": "Learn Acrobat - Share_1.pdf",
      "refined_text": "This is sample content for Learn Acrobat - Share_1...",
      "page_number": 1
    }
  ]
}
```

---
