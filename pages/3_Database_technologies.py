import streamlit as st

# st.title("Step 3: Database Technologies")
st.title("Database Technologies")

# Initialize list in session_state if not already present
if "database" not in st.session_state:
    st.session_state["database"] = ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite']


# --- Multi-select current list ---
st.markdown("### Select relevant Databases:")
selected = st.multiselect("Choose from list:", st.session_state.get("database", []), key="database_multi")
st.session_state["selected_database"] = selected

if selected:
    st.info(f"Selected Database technologies: {', '.join(selected)}")
else:
    st.info("No Database selected yet.")

# --- Reset Button ---
if st.button("Reset Database list", key="database_reset_btn"):
    st.session_state["database"] = ['MySQL', 'PostgreSQL', 'MongoDB', 'SQLite']
    st.session_state["selected_database"] = []
    st.success("List and selections reset!")

# --- Add new item ---
new_item = st.text_input("Add a new Database technology:", key="database_new_item")
if st.button("Add Database", key="database_add_btn"):
    if new_item and new_item not in st.session_state["database"]:
        st.session_state["database"].append(new_item)
        st.success(f"Added {new_item}")
    elif new_item in st.session_state["database"]:
        st.warning(f"{new_item} already exists!")

# --- Remove existing item ---
remove_item = st.selectbox("Remove existing Database:", [""] + st.session_state.get("database", []), key="database_remove_select")
if st.button("Remove Database", key="database_remove_btn"):
    if remove_item and remove_item in st.session_state["database"]:
        st.session_state["database"].remove(remove_item)
        st.warning(f"Removed {remove_item}")
    elif not remove_item:
        st.info("Please select an item to remove.")

