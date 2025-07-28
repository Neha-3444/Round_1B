## Approach Explanation

Our system solves the Persona-Driven Document Intelligence problem using lightweight sentence embeddings and relevance ranking. Given a persona and job-to-be-done, we generate a dense query vector using the MiniLM-based SentenceTransformer, which is under 1GB and optimized for CPU.

We extract text from PDF documents using PyMuPDF and divide the content by pages. Each page is treated as a section and embedded. Using cosine similarity, we compute relevance scores between the persona-job query and all document sections. The top 5 most relevant sections are selected and stack-ranked.

For sub-section analysis, we split the top sections into paragraphs and pick the most meaningful ones based on length and position. This provides deeper insights while maintaining performance constraints.

The model runs under 60 seconds on 3–5 documents on CPU. It does not require internet access as all models are downloaded beforehand. Output is provided in a structured JSON format as specified in the challenge.