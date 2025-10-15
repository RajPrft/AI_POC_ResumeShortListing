import streamlit as st

# st.title("Step 6: Categories")
st.title("Categories")

# Initialize list in session_state if not already present
if "category" not in st.session_state:
    st.session_state["category"] = ['Full Stack', 'Frontend', 'Backend', 'DevOps']


# --- Multi-select current list ---
st.markdown("### Select relevant Categorys:")
selected = st.multiselect("Choose from list:", st.session_state.get("category", []), key="category_multi")
st.session_state["selected_category"] = selected

if selected:
    st.info(f"Selected Category technologies: {', '.join(selected)}")
else:
    st.info("No Category selected yet.")

# --- Reset Button ---
if st.button("Reset Category list", key="category_reset_btn"):
    st.session_state["category"] = ['Full Stack', 'Frontend', 'Backend', 'DevOps']
    st.session_state["selected_category"] = []
    st.success("List and selections reset!")

# --- Add new item ---
new_item = st.text_input("Add a new Category technology:", key="category_new_item")
if st.button("Add Category", key="category_add_btn"):
    if new_item and new_item not in st.session_state["category"]:
        st.session_state["category"].append(new_item)
        st.success(f"Added {new_item}")
    elif new_item in st.session_state["category"]:
        st.warning(f"{new_item} already exists!")

# --- Remove existing item ---
remove_item = st.selectbox("Remove existing Category:", [""] + st.session_state.get("category", []), key="category_remove_select")
if st.button("Remove Category", key="category_remove_btn"):
    if remove_item and remove_item in st.session_state["category"]:
        st.session_state["category"].remove(remove_item)
        st.warning(f"Removed {remove_item}")
    elif not remove_item:
        st.info("Please select an item to remove.")

