import streamlit as st

# st.title("Step 5: Hybrid Tools/Technologies")
st.title("Hybrid Tools/Technologies")

# Initialize list in session_state if not already present
if "hybrid" not in st.session_state:
    st.session_state["hybrid"] = ['Flutter', 'React Native', 'Ionic', 'Xamarin']


# --- Multi-select current list ---
st.markdown("### Select relevant Hybrids:")
selected = st.multiselect("Choose from list:", st.session_state.get("hybrid", []), key="hybrid_multi")
st.session_state["selected_hybrid"] = selected

if selected:
    st.info(f"Selected Hybrid technologies: {', '.join(selected)}")
else:
    st.info("No Hybrid selected yet.")

# --- Reset Button ---
if st.button("Reset Hybrid list", key="hybrid_reset_btn"):
    st.session_state["hybrid"] = ['Flutter', 'React Native', 'Ionic', 'Xamarin']
    st.session_state["selected_hybrid"] = []
    st.success("List and selections reset!")

# --- Add new item ---
new_item = st.text_input("Add a new Hybrid technology:", key="hybrid_new_item")
if st.button("Add Hybrid", key="hybrid_add_btn"):
    if new_item and new_item not in st.session_state["hybrid"]:
        st.session_state["hybrid"].append(new_item)
        st.success(f"Added {new_item}")
    elif new_item in st.session_state["hybrid"]:
        st.warning(f"{new_item} already exists!")

# --- Remove existing item ---
remove_item = st.selectbox("Remove existing Hybrid:", [""] + st.session_state.get("hybrid", []), key="hybrid_remove_select")
if st.button("Remove Hybrid", key="hybrid_remove_btn"):
    if remove_item and remove_item in st.session_state["hybrid"]:
        st.session_state["hybrid"].remove(remove_item)
        st.warning(f"Removed {remove_item}")
    elif not remove_item:
        st.info("Please select an item to remove.")

