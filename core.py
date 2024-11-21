import streamlit as st
import pandas as pd
import os

# File to store the wish list
DATA_FILE = "wish_list.csv"
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
        color: white !important; /* Keep text white */
        text-shadow: 2px 2px 4px black; /* Ensure proper shadow for readability */
    }}
    .stMarkdown, h1, h2, h3, h4, h5, h6, label {{
        color: white !important; /* Keep all other text white */
        text-shadow: 2px 2px 4px black; /* Add clear text shadow */
    }}
    /* Styling for the table */
    table {{
        background-color: rgba(0, 128, 0, 0.9); /* Brighter green with slight transparency */
        border-radius: 10px;
        padding: 10px;
        color: white;
        width: 100%;
    }}
    th, td {{
        padding: 10px;
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px black; /* Apply shadow to table text */
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

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

# "Add a New Wish" section with styled text
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

# Display the current wish list with delete functionality
st.subheader("Current Wish List")
if not wish_list.empty:
    for i, row in wish_list.iterrows():
        col1, col2, col3, col4 = st.columns([3, 3, 3, 1])
        with col1:
            st.text(row["Name"])
        with col2:
            st.text(row["Gift"])
        with col3:
            if pd.notna(row["Link"]) and row["Link"]:
                st.markdown(f"[Link]({row['Link']})", unsafe_allow_html=True)
            else:
                st.text("No Link")
        with col4:
            if st.button("❌", key=f"delete_{i}"):
                wish_list = wish_list.drop(i).reset_index(drop=True)
                save_wish_list()
                st.experimental_rerun()
else:
    st.write("No items in the wish list yet. Add one above!")
