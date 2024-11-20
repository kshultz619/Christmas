import streamlit as st
import pandas as pd
import os

# File to store the wish list
DATA_FILE = "wish_list.csv"
MUSIC_FILE = "MUSIC_FILE = "https://drive.google.com/uc?export=download&id=1-kPl_t-G9j4Vxa_AlfbsiAn4wZO6tF4B"


# "https://drive.google.com/uc?export=download&id=1-kPl_t-G9j4Vxa_AlfbsiAn4wZO6tF4B"

# Debugging: Display the file path
st.write(f"Music file path: {MUSIC_FILE}")

# Add a clickable link to test file accessibility
st.markdown(f"[Test MP3 File]({MUSIC_FILE})")

# Title of the app
st.title("🎄 Shultz Family Christmas List 🎁")

# Load or initialize the wish list
if os.path.exists(DATA_FILE):
    wish_list = pd.read_csv(DATA_FILE)
else:
    wish_list = pd.DataFrame(columns=["Name", "Gift", "Link"])

# Save the wish list to file
def save_wish_list():
    wish_list.to_csv(DATA_FILE, index=False)


# Debugging: Display the file path
st.write(f"Music file path: {MUSIC_FILE}")

# Add a clickable link to test file accessibility
st.markdown(f"[Test MP3 File]({MUSIC_FILE})")

# Add a music player
st.markdown(
    f"""
    <audio controls loop autoplay>
        <source src="{MUSIC_FILE}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """,
    unsafe_allow_html=True,
)

# Add a new item to the list
st.subheader("Add a New Wish")
with st.form("add_item_form", clear_on_submit=True):
    name = st.selectbox("Name", ["Kevin", "Jackie", "Robin", "Joe", "Dana", "Dan"])
    gift = st.text_input("Gift")
    link = st.text_input("Link (URL to gift)")
    submitted = st.form_submit_button("Add to List")

    if submitted:
        if name and gift:
            # Add new item to the DataFrame
            new_entry = pd.DataFrame({"Name": [name], "Gift": [gift], "Link": [link]})
            wish_list = pd.concat([wish_list, new_entry], ignore_index=True)
            save_wish_list()  # Save changes to file
            st.success(f"Added: {name}'s gift '{gift}' to the list!")
        else:
            st.error("Both Name and Gift are required to add to the list.")

# Display the current wish list
st.subheader("Current Wish List")
if not wish_list.empty:
    # Add delete buttons
    for index, row in wish_list.iterrows():
        col1, col2, col3, col4 = st.columns([3, 3, 3, 1])
        with col1:
            st.write(row["Name"])
        with col2:
            st.write(row["Gift"])
        with col3:
            if pd.notna(row["Link"]) and row["Link"]:
                st.markdown(f"[{row['Gift']} link]({row['Link']})", unsafe_allow_html=True)
            else:
                st.write("No Link Provided")
        with col4:
            if st.button("Delete", key=f"delete_{index}"):
                wish_list = wish_list.drop(index).reset_index(drop=True)
                save_wish_list()  # Save changes to file
                st.experimental_rerun()  # Refresh the page
else:
    st.write("No items in the wish list yet. Add one above!")

# Option to clear the list
if st.button("Clear Wish List"):
    wish_list = pd.DataFrame(columns=["Name", "Gift", "Link"])
    save_wish_list()  # Save changes to file
    st.success("Wish list cleared!")
