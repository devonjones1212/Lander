import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BlogToolset Pro",
    page_icon="📝",
    layout="centered" # Use centered layout for a landing page
)

# Hide Streamlit's default menu and footer
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
""", unsafe_allow_html=True)


# Lander content
st.title("📝 BlogToolset Pro")
st.header("Professional content creation tools powered by AI.")
st.write(
    "Generate engaging blog descriptions, SEO-friendly outlines, and more. "
    "Save time and create content that resonates with your audience."
)

st.divider()

# Gumroad link button
st.link_button(
    "Get Access on Gumroad",
    "https://YOUR_GUMROAD_LINK_HERE", # <-- IMPORTANT: Replace with your link
    type="primary",
    use_container_width=True
)