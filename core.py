import streamlit as st
import pandas as pd
import os

# File to store the wish list
DATA_FILE = "wish_list.csv"
MUSIC_FILE = "https://drive.google.com/uc?export=download&id=1-kPl_t-G9j4Vxa_AlfbsiAn4wZO6tF4B"
IMAGE_FILE = "https://i.imgur.com/pirD3jd.jpg"

# Inject custom CSS for styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{IMAGE_FILE}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
    }}
    /* Styling for the Add a New Wish section */
    .data-entry {{
        background-color: rgba(0, 100, 0, 0.8); /* Darker green with transparency */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
    }}
    /* Styling for the table */
    table {{
        background-color: rgba(255, 0, 0, 0.8); /* Red with transparency */
        border-radius: 10px;
        padding: 10px;
        color: white;
        width: 100%;
    }}
    th, td {{
        padding: 10px;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.title("🎄 Shultz Family Christmas List 🎁")

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

# Load or initialize the wish list
if os.path.exists(DATA_FILE):
    wish_list = pd.read_csv(DATA_FILE)
else:
    wish_list = pd.DataFrame(columns=["Name", "Gift", "Link"])

# Save the wish list to file
def save_wish_list():
    wish_list.to_csv(DATA_FILE, index=False)

# Wrap the entire "Add a New Wish" section in a green background
st.markdown('<div class="data-entry">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# Display the current wish list
st.subheader("Current Wish List")
if not wish_list.empty:
    # Render the table with the applied styles
    st.markdown(
        wish_list.to_html(escape=False, index=False),
        unsafe_allow_html=True,
    )
else:
    st.write("No items in the wish list yet. Add one above!")

# Option to clear the list
if st.button("Clear Wish List"):
    wish_list = pd.DataFrame(columns=["Name", "Gift", "Link"])
    save_wish_list()  # Save changes to file
    st.success("Wish list cleared!")
