import streamlit as st
import json

# st.title("📊 Step 7: Summary & Export")
st.title("Summary & Export")

keys = ["backend", "frontend", "database", "cloud", "hybrid", "category"]
summary = {key: st.session_state.get(f"selected_{key}", []) for key in keys}

# st.markdown("### 🧠 Your Selected Technologies")
st.markdown("### Your Selected Technologies")
for key, items in summary.items():
    st.write(f"**{key.capitalize()}**: {', '.join(items) if items else 'None selected'}")

if "uploaded_file" in st.session_state:
    st.write("### 📄 Uploaded Resume Info")
    st.write(f"**File Name:** {st.session_state['uploaded_file'].name}")
else:
    st.info("Resume not uploaded yet.")

# st.markdown("### 💾 Export Summary")
st.markdown("### Export Summary")
if st.button("Export as JSON"):
    with open("resume_selection_summary.json", "w") as f:
        json.dump(summary, f, indent=4)
    st.success("✅ Exported as resume_selection_summary.json")

if st.button("Export as Text File"):
    with open("resume_selection_summary.txt", "w") as f:
        for key, items in summary.items():
            f.write(f"{key.capitalize()}: {', '.join(items) if items else 'None'}\n")
    st.success("✅ Exported as resume_selection_summary.txt")