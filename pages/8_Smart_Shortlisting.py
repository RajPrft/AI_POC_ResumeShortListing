import streamlit as st
import re, json, os
import nltk
import shutil

# === 1️⃣ Define the absolute path to your included NLTK data ===
LOCAL_NLTK_PATH = os.path.join(os.getcwd(), "nltk_data")

# === 2️⃣ Force NLTK to ONLY use this path ===
nltk.data.path.clear()
nltk.data.path.append(LOCAL_NLTK_PATH)

corpora_path = os.path.join(LOCAL_NLTK_PATH, "corpora")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyPDF2 import PdfReader
from docx import Document



st.title("Smart Resume Shortlisting (Keyword Match)")

if "uploaded_file" not in st.session_state:
    st.warning("Please upload your resume first.")
else:
    uploaded_file = st.session_state["uploaded_file"]
    file_type = uploaded_file.name.split(".")[-1]

    resume_text = ""
    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            resume_text += page.extract_text() or ""
    elif file_type == "docx":
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            resume_text += para.text + "\n"

    text = re.sub(r"[^a-zA-Z0-9+]+", " ", resume_text.lower())
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_words = [w for w in words if w not in stop_words]

    keys = ["backend", "frontend", "database", "cloud", "hybrid", "category"]
    selected_keywords = [k.lower() for key in keys for k in st.session_state.get(f"selected_{key}", [])]

    matched = [kw for kw in selected_keywords if kw in filtered_words]
    missing = [kw for kw in selected_keywords if kw not in filtered_words]
    total = len(selected_keywords)
    score = round((len(matched) / total) * 100, 2) if total > 0 else 0

    st.markdown("## Match Result")
    st.metric("Overall Match Percentage", f"{score}%")

    st.markdown("### ✅ Matched Keywords")
    st.success(", ".join(matched) if matched else "No matches found.")

    st.markdown("### ❌ Missing Keywords")
    st.error(", ".join(missing) if missing else "All selected keywords matched!")

    if st.button("Export Match Report"):
        report = {"match_score": score, "matched": matched, "missing": missing}
        with open("resume_match_report.json", "w") as f:
            json.dump(report, f, indent=4)
        st.success("✅ Exported as resume_match_report.json")
