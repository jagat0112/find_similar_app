import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
@st.cache_data
def load_data():
    return pd.read_csv("players_with_clusters1.csv")  # Make sure this file is in the same repo

df = load_data()

# Sidebar input
st.sidebar.title("⚽ Player Similarity Finder")
player_name = st.sidebar.text_input("Enter a player's name", "")

# App title
st.title("🔍 Find Similar Football Players")
st.markdown("Uses KMeans clustering and PCA to suggest players with similar play styles and positions.")

# Process user input
if player_name:
    matches = df[df["Player"].str.contains(player_name, case=False, na=False)]
    
    if matches.empty:
        st.warning("❌ Player not found. Try a different name.")
    else:
        selected = matches.iloc[0]
        cluster = selected["Cluster"]
        position = selected["Pos"]

        st.success(f"✅ Found: **{selected['Player']}** | Position: {position} | Cluster: {cluster}")

        # Filter similar players in the same cluster AND same position
        similar = df[
            (df["Cluster"] == cluster) &
            (df["Pos"] == position) &
            (df["Player"] != selected["Player"])
        ]

        # Show similar players
        st.subheader("👥 Similar Players (Same Position & Cluster)")
        st.dataframe(similar[["Player", "Nation", "Pos", "Age", "G+A_90", "xG_90", "xAG_90"]].reset_index(drop=True))

        # Plot clusters with the selected player
        st.subheader("📊 PCA Cluster Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="PCA1", y="PCA2", hue="Cluster", palette="Set2", ax=ax)
        ax.scatter(selected["PCA1"], selected["PCA2"], color="black", marker="*", s=150, label="Selected Player")
        ax.set_title("PCA Clusters with Selected Player")
        ax.legend()
        st.pyplot(fig)
