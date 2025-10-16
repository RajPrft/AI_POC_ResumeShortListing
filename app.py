import os
import nltk
import streamlit as st
import shutil

# === 1️⃣ Define the absolute path to your included NLTK data ===
LOCAL_NLTK_PATH = os.path.join(os.getcwd(), "nltk_data")

# === 2️⃣ Force NLTK to ONLY use this path ===
nltk.data.path.clear()
nltk.data.path.append(LOCAL_NLTK_PATH)

# === 3️⃣ Ensure wordnet.zip does NOT exist anywhere ===
zip_path = os.path.join(LOCAL_NLTK_PATH, "corpora", "wordnet.zip")
if os.path.exists(zip_path):
    try:
        os.remove(zip_path)
        st.warning("Removed stray wordnet.zip from local nltk_data")
    except Exception as e:
        st.error(f"Couldn't remove {zip_path}: {e}")

# === 4️⃣ Optional: Log current NLTK search paths for debugging ===
# st.write("✅ NLTK data paths:")
# for p in nltk.data.path:
#     st.code(p)

# # === 5️⃣ Quick verification to confirm WordNet loads ===
# try:
#     from nltk.corpus import wordnet
#     syns = wordnet.synsets("good")
#     st.success(f"WordNet loaded successfully! Found {len(syns)} synsets for 'good'")
# except LookupError as e:
#     st.error("⚠️ WordNet not found. Ensure nltk_data/corpora/wordnet exists.")
#     st.code(str(e))
# except Exception as e:
#     st.error(f"Unexpected error: {e}")

#st.title("Welcome!")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>AI POC</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Welcome to <b>Resume Shortlisting Utility</b></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Click the button below to start uploading your resume.</p>", unsafe_allow_html=True)

st.write("")
st.write("")
# === 6️⃣ Add a navigation button to go to another page ===
# st.markdown("---")  

col1, col2, col3 = st.columns([1, 1, "auto"])
with col3:
    st.button("Start →")
if st.button("Start →"):
    st.switch_page("pages/0_Select_Resume.py")