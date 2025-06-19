# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your preprocessed dataset (replace with your own file path if needed)
@st.cache_data
def load_data():
    df = pd.read_csv("players_with_clusters.csv")  # Update this to your filename
    return df

df = load_data()

# --- Sidebar ---
st.sidebar.title("Player Similarity Finder")
player_name = st.sidebar.text_input("Enter a player's name", "")

# --- Main UI ---
st.title("⚽ Similar Player Finder Using KMeans Clustering")
st.markdown("Find football players with similar playing stats!")

# --- Show Similar Players ---
if player_name:
    matches = df[df["Player"].str.contains(player_name, case=False, na=False)]
    
    if len(matches) == 0:
        st.warning("No player found. Please try another name.")
    else:
        selected = matches.iloc[0]
        st.success(f"✅ Found: {selected['Player']}")
        cluster = selected["Cluster"]
        
        # Show similar players
        st.subheader("🧩 Players in the Same Cluster:")
        similar = df[(df["Cluster"] == cluster) & (df["Player"] != selected["Player"])]
        st.dataframe(similar[["Player", "Nation", "Pos", "Age", "G+A_90", "xG_90", "xAG_90"]].reset_index(drop=True))

        # --- Optional: PCA Plot ---
        st.subheader("📈 PCA Cluster Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="PCA1", y="PCA2", hue="Cluster", palette="Set2", ax=ax)
        ax.scatter(selected["PCA1"], selected["PCA2"], color="black", marker="*", s=150, label="Selected Player")
        ax.set_title("PCA Clusters with Selected Player")
        ax.legend()
        st.pyplot(fig)
