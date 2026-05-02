import pickle
import streamlit as st

# ── Config ────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Music Recommender", page_icon="🎵", layout="wide")

FALLBACK_POSTER = "https://i.postimg.cc/0QNxYz4V/social.png"

# ── Load data ──────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    music     = pickle.load(open("df.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return music, similarity

music, similarity = load_data()

# ── Helpers ────────────────────────────────────────────────────────────────────
import requests

def get_album_cover(song_name: str, artist_name: str) -> str:
    try:
        query = f"{song_name} {artist_name}"
        response = requests.get(
            "https://itunes.apple.com/search",
            params={"term": query, "media": "music", "limit": 1}
        )
        data = response.json()
        if data["resultCount"] > 0:
            return data["results"][0]["artworkUrl100"].replace("100x100", "600x600")
    except Exception as e:
        print(f"iTunes error for '{song_name}': {e}")
    return FALLBACK_POSTER

def recommend(song: str):
    matches = music[music["song"] == song]
    if matches.empty:
        st.error(f"'{song}' not found in the dataset.")
        return [], []

    index     = matches.index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)

    names, posters = [], []
    for i, _ in distances[1:6]:
        row = music.iloc[i]
        names.append(row["song"])
        posters.append(get_album_cover(row["song"], row["artist"]))

    return names, posters

# ── UI ─────────────────────────────────────────────────────────────────────────
st.title("🎵 Music Recommender")
st.markdown("Select a song and discover five similar tracks.")

selected_song = st.selectbox("Search or select a song", sorted(music["song"].values))

if st.button("Get Recommendations", use_container_width=True):
    with st.spinner("Finding similar tracks…"):
        names, posters = recommend(selected_song)

    if names:
        st.subheader("You might also like:")
        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.image(poster, use_container_width=True)
                st.caption(name)