import streamlit as st

# st.title("Step 2: Frontend Technologies")
st.title("Frontend Technologies")

# Initialize list in session_state if not already present
if "frontend" not in st.session_state:
    st.session_state["frontend"] = ['React', 'Angular', 'Vue', 'Svelte']


# --- Multi-select current list ---
st.markdown("### Select relevant Frontends:")
selected = st.multiselect("Choose from list:", st.session_state.get("frontend", []), key="frontend_multi")
st.session_state["selected_frontend"] = selected

if selected:
    st.info(f"Selected Frontend technologies: {', '.join(selected)}")
else:
    st.info("No Frontend selected yet.")

# --- Reset Button ---
if st.button("Reset Frontend list", key="frontend_reset_btn"):
    st.session_state["frontend"] = ['React', 'Angular', 'Vue', 'Svelte']
    st.session_state["selected_frontend"] = []
    st.success("List and selections reset!")

# --- Add new item ---
new_item = st.text_input("Add a new Frontend technology:", key="frontend_new_item")
if st.button("Add Frontend", key="frontend_add_btn"):
    if new_item and new_item not in st.session_state["frontend"]:
        st.session_state["frontend"].append(new_item)
        st.success(f"Added {new_item}")
    elif new_item in st.session_state["frontend"]:
        st.warning(f"{new_item} already exists!")

# --- Remove existing item ---
remove_item = st.selectbox("Remove existing Frontend:", [""] + st.session_state.get("frontend", []), key="frontend_remove_select")
if st.button("Remove Frontend", key="frontend_remove_btn"):
    if remove_item and remove_item in st.session_state["frontend"]:
        st.session_state["frontend"].remove(remove_item)
        st.warning(f"Removed {remove_item}")
    elif not remove_item:
        st.info("Please select an item to remove.")

