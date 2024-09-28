import streamlit as st

st.write(
    """
    # My First Word
    """
)
st.image("assets/pic_1.jpg",
         caption='Kuta Beach',
         use_column_width="auto")

st.markdown(
    "Hi guys, my name is Mahardi, I'm just ordinary guy who has special interest on Geospatial Tech something."
    " I have been workin in Geospatial Indsutry for almost 10 years with various role and responsibillity such as analyst, business development, and project management. Currently working on produt operations stufff."
    " I'm trying to shift myself in remote worker world, especially in Geospatial Data analyst role. Let's take look at my journey one by one through this my personal blog ya."
    " See you when I see you!!"
)
SOCIAL_MEDIA = {
    "LINKEDIN": "https://www.linkedin.com/in/mahardi-setyoso-pratomo-5ab97432/",
    "GITHUB": "https://github.com/mahardisetyoso",
    "TWITTER": "https://twitter.com/MasMahardi",
    "DISCORD": "https://discordapp.com/users/785121800525709324",
}

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
