import streamlit as st

# st.title("Step 1: Backend Technologies")
st.title("Backend Technologies")

# Initialize list in session_state if not already present
if "backend" not in st.session_state:
    st.session_state["backend"] = ['Python', 'Node.js', 'Java', 'ASP.NET', 'PHP']


# --- Multi-select current list ---
st.markdown("### Select relevant Backends:")
selected = st.multiselect("Choose from list:", st.session_state.get("backend", []), key="backend_multi")
st.session_state["selected_backend"] = selected

if selected:
    st.info(f"Selected Backend technologies: {', '.join(selected)}")
else:
    st.info("No Backend selected yet.")

# --- Reset Button ---
if st.button("Reset Backend list", key="backend_reset_btn"):
    st.session_state["backend"] = ['Python', 'Node.js', 'Java', 'ASP.NET', 'PHP']
    st.session_state["selected_backend"] = []
    st.success("List and selections reset!")

# --- Add new item ---
new_item = st.text_input("Add a new Backend technology:", key="backend_new_item")
if st.button("Add Backend", key="backend_add_btn"):
    if new_item and new_item not in st.session_state["backend"]:
        st.session_state["backend"].append(new_item)
        st.success(f"Added {new_item}")
    elif new_item in st.session_state["backend"]:
        st.warning(f"{new_item} already exists!")

# --- Remove existing item ---
remove_item = st.selectbox("Remove existing Backend:", [""] + st.session_state.get("backend", []), key="backend_remove_select")
if st.button("Remove Backend", key="backend_remove_btn"):
    if remove_item and remove_item in st.session_state["backend"]:
        st.session_state["backend"].remove(remove_item)
        st.warning(f"Removed {remove_item}")
    elif not remove_item:
        st.info("Please select an item to remove.")

