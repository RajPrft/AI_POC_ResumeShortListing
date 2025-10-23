
# 10_Batch_Ranking.py
import streamlit as st
from pathlib import Path
import pandas as pd
import re, json, os
from PyPDF2 import PdfReader
from docx import Document
import nltk
# === 1️⃣ Define the absolute path to your included NLTK data ===
LOCAL_NLTK_PATH = os.path.join(os.getcwd(), "nltk_data")

# === 2️⃣ Force NLTK to ONLY use this path ===
nltk.data.path.clear()
nltk.data.path.append(LOCAL_NLTK_PATH)

corpora_path = os.path.join(LOCAL_NLTK_PATH, "corpora")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# st.title("📂 Step 10: Batch Ranking (Multiple Resumes)")
st.title("Upload Multiple Resumes")

uploaded_files = st.file_uploader("Upload multiple resumes (pdf/docx)", type=["pdf","docx"], accept_multiple_files=True)
# folder_path = st.text_input("Or provide server-side folder path (absolute):", "")

use_ai = st.checkbox("Use AI (spaCy) to augment detection", value=False)
include_preview = st.checkbox("Include resume text preview in results", value=False)

def extract_text(file_obj, fname):
    text = ""
    if fname.lower().endswith(".pdf"):
        reader = PdfReader(file_obj)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif fname.lower().endswith(".docx"):
        doc = Document(file_obj)
        for para in doc.paragraphs:
            text += para.text + "\\n"
    return text

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#\\s]+", " ", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    return [t for t in tokens if t not in stop_words and len(t)>1]

if st.button("Run Batch Ranking"):
    files = []
    if uploaded_files:
        for f in uploaded_files:
            files.append((f, f.name))
#     if folder_path:
#         p = Path(folder_path)
#         if p.exists() and p.is_dir():
#            for ext in ("*.pdf","*.docx"):
#                 for fp in p.glob(ext):
#                     files.append((fp, fp.name))
#         else:
#             st.error("Folder path invalid.")
    if not files:
        st.warning("No resumes provided.")
    else:
        selected = [s.lower() for key in ["backend","frontend","database","cloud","hybrid","category"] for s in st.session_state.get(f"selected_{key}", [])]
        results = []
        for file_obj, fname in files:
            text = extract_text(file_obj, fname)
            tokens = preprocess(text)
            matched = [s for s in selected if s.lower() in tokens]
            missing = [s for s in selected if s.lower() not in tokens]
            score = round((len(matched)/len(selected))*100,2) if selected else 0
            row = {"file_name": fname, "match_score": score, "matched": ";".join(matched), "missing": ";".join(missing)}
            if include_preview:
                row["preview"] = text[:1000]
            results.append(row)
        df = pd.DataFrame(results).sort_values("match_score", ascending=False).reset_index(drop=True)
        st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download rankings as CSV", data=csv, file_name="resume_rankings.csv", mime="text/csv")
