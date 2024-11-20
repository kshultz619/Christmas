import streamlit as st
import pandas as pd
import random

# Title of the app
st.title("🎄 Shultz Family Christmas List 🎁")

# Initialize the wish list in session state
if "wish_list" not in st.session_state:
    st.session_state["wish_list"] = []

# Set a background image
st.markdown(
    """
    <style>
    body {
        background-image: url('/static/christmas_background.JPG');
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add snowfall effect
st.components.v1.html(
    """
    <style>
    body {
        overflow: hidden;
    }
    .snowflake {
        position: absolute;
        color: white;
        font-size: 20px;
        animation: fall linear infinite;
    }
    @keyframes fall {
        from {
            transform: translateY(-100%);
        }
        to {
            transform: translateY(100%);
        }
    }
    </style>
    <script>
    const createSnowflake = () => {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.textContent = '❄';
        snowflake.style.left = `${Math.random() * window.innerWidth}px`;
        snowflake.style.animationDuration = `${Math.random() * 3 + 2}s`;
        snowflake.style.opacity = `${Math.random()}`;
        document.body.appendChild(snowflake);
        setTimeout(() => snowflake.remove(), 5000);
    };

    setInterval(createSnowflake, 300);
    </script>
    """,
    height=0,
)

# Add holiday music from the local file
st.markdown(
    """
    <audio autoplay loop>
        <source src="/static/Christmas-Countdown-Long-Version-chosic.com_.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """,
    unsafe_allow_html=True,
)

# Sidebar with Christmas links
st.sidebar.markdown("🎅 **Check Out These Gift Ideas:**")
st.sidebar.markdown("- 🎁 [Amazon](https://www.amazon.com)")
st.sidebar.markdown("- 🎄 [Etsy](https://www.etsy.com)")
st.sidebar.markdown("- ❄ [Best Buy](https://www.bestbuy.com)")
st.sidebar.markdown("- 🌟 [Target](https://www.target.com)")

# Add a random holiday greeting
greetings = [
    "Merry Christmas! 🎅",
    "Happy Holidays! 🎄",
    "Season's Greetings! ❄",
    "Warm Wishes for the Holidays! 🌟",
]
st.sidebar.markdown(f"### {random.choice(greetings)}")

# Add a new item to the list
st.subheader("Add a New Wish")
with st.form("add_item_form", clear_on_submit=True):
    name = st.selectbox("Name", ["Kevin", "Jackie", "Robin", "Joe", "Dana", "Dan"], key="selected_name")
    gift = st.text_input("Gift", key="gift_input")
    link = st.text_input("Link (URL to gift)", key="link_input")
    submitted = st.form_submit_button("Add to List")

    if submitted:
        if name and gift:
            st.session_state["wish_list"].append({"Name": name, "Gift": gift, "Link": link})
            st.success(f"Added: {name}'s gift '{gift}' to the list!")
        else:
            st.error("Both Name and Gift are required to add to the list.")

# Display the current wish list
st.subheader("Current Wish List")
if st.session_state["wish_list"]:
    df = pd.DataFrame(st.session_state["wish_list"])
    df["Link"] = df.apply(
        lambda row: f'<a href="{row["Link"]}" target="_blank">{row["Gift"]} link</a>' if row["Link"] else "No Link Provided",
        axis=1,
    )
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
else:
    st.write("No items in the wish list yet. Add one above!")

# Option to clear the list
if st.button("Clear Wish List"):
    st.session_state["wish_list"] = []
    st.success("Wish list cleared!")
