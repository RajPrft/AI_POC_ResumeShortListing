import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

# st.set_page_config(page_title="Resume Shortlisting", page_icon="🧾")
st.set_page_config(page_title="Resume Shortlisting")

# st.title("🧾 Resume Shortlisting System")
st.title("Resume Shortlisting Utility")
st.markdown("### Upload your Resume (PDF or DOCX)")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if uploaded_file:
    st.session_state["uploaded_file"] = uploaded_file
    file_type = uploaded_file.name.split(".")[-1]
    st.success(f"Uploaded file: **{uploaded_file.name}**")

    content = ""
    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            content += page.extract_text() or ""
    elif file_type == "docx":
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            content += para.text + "\\n"

    if st.checkbox("Show extracted text"):
        st.text_area("Resume Text", content, height=300)