import os
import nltk
import streamlit as st

# Tell NLTK where to find the included data
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# (Optional) Verify availability
try:
    from nltk.corpus import wordnet
    _ = wordnet.synsets('dog')  # quick test
except LookupError:
    st.warning("WordNet not found. Please ensure nltk_data is present in repo.")

# ---- Your normal Streamlit app code below ----
st.title("NLTK WordNet Streamlit App")

word = st.text_input("Enter a word:")
if word:
    from nltk.corpus import wordnet
    syns = wordnet.synsets(word)
    if syns:
        st.write(f"Definitions for '{word}':")
        for s in syns[:5]:
            st.write("-", s.definition())
    else:
        st.write("No definitions found.")
