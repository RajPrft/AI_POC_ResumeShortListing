import streamlit as st

# st.title("Step 4: Cloud Technologies")
st.title("Cloud Technologies")

# Initialize list in session_state if not already present
if "cloud" not in st.session_state:
    st.session_state["cloud"] = ['AWS', 'Azure', 'GCP', 'DigitalOcean']


# --- Multi-select current list ---
st.markdown("### Select relevant Clouds:")
selected = st.multiselect("Choose from list:", st.session_state.get("cloud", []), key="cloud_multi")
st.session_state["selected_cloud"] = selected

if selected:
    st.info(f"Selected Cloud technologies: {', '.join(selected)}")
else:
    st.info("No Cloud selected yet.")

# --- Reset Button ---
if st.button("Reset Cloud list", key="cloud_reset_btn"):
    st.session_state["cloud"] = ['AWS', 'Azure', 'GCP', 'DigitalOcean']
    st.session_state["selected_cloud"] = []
    st.success("List and selections reset!")

# --- Add new item ---
new_item = st.text_input("Add a new Cloud technology:", key="cloud_new_item")
if st.button("Add Cloud", key="cloud_add_btn"):
    if new_item and new_item not in st.session_state["cloud"]:
        st.session_state["cloud"].append(new_item)
        st.success(f"Added {new_item}")
    elif new_item in st.session_state["cloud"]:
        st.warning(f"{new_item} already exists!")

# --- Remove existing item ---
remove_item = st.selectbox("Remove existing Cloud:", [""] + st.session_state.get("cloud", []), key="cloud_remove_select")
if st.button("Remove Cloud", key="cloud_remove_btn"):
    if remove_item and remove_item in st.session_state["cloud"]:
        st.session_state["cloud"].remove(remove_item)
        st.warning(f"Removed {remove_item}")
    elif not remove_item:
        st.info("Please select an item to remove.")

