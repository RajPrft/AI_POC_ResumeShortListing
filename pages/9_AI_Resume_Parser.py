import streamlit as st
import spacy, re, json
from PyPDF2 import PdfReader
from docx import Document

# st.title("🧠 Step 9: AI Resume Parser & Auto Match")
st.title("AI Resume Parser & Auto Match (NLP)")

nlp = spacy.load("en_core_web_sm")

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
            resume_text += para.text + "\\n"

    resume_text = re.sub(r"[^A-Za-z0-9+]+", " ", resume_text)
    doc = nlp(resume_text)
    tokens = [t.text.lower() for t in doc if not t.is_stop and not t.is_punct]

    tech_terms = [
        "python", "java", "javascript", "node", "react", "angular", "vue", "django", "flask",
        "aws", "azure", "gcp", "docker", "kubernetes", "mysql", "mongodb", "postgresql",
        "flutter", "react native", "ionic", "xamarin", "devops", "terraform", "linux"
    ]

    skill_keywords = {term for term in tech_terms if term in " ".join(tokens)}

    # st.markdown("### 🤖 Extracted Skills from Resume")
    st.markdown("### Extracted Skills from Resume")
    st.info(", ".join(sorted(skill_keywords)) or "None found")

    selected = [s.lower() for key in ["backend", "frontend", "database", "cloud", "hybrid", "category"]
                for s in st.session_state.get(f"selected_{key}", [])]

    matched = [s for s in selected if s in skill_keywords]
    missing = [s for s in selected if s not in skill_keywords]
    score = round((len(matched) / len(selected)) * 100, 2) if selected else 0

    # st.markdown("## 🎯 AI Match Result")
    st.markdown("## AI Match Result")
    st.metric("AI Match Percentage", f"{score}%")

    st.markdown("### ✅ Matched Skills")
    st.success(", ".join(matched) if matched else "No matches found.")

    st.markdown("### ❌ Missing Skills")
    st.error(", ".join(missing) if missing else "All matched!")

    # if st.button("💾 Export AI Report"):
    if st.button("Export AI Report"):
        report = {"ai_detected": list(skill_keywords), "matched": matched, "missing": missing, "match_score": score}
        with open("ai_resume_report.json", "w") as f:
            json.dump(report, f, indent=4)
        st.success("✅ Exported as ai_resume_report.json")