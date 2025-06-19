
# 📊 Player Similarity Finder (Football Stats + ML)

A Streamlit web app that helps you find players similar to any footballer based on performance stats — filtered by playing position. Powered by unsupervised Machine Learning (KMeans) and PCA for visualization.

---

## 🚀 Features

- 🔍 Search a player by name (e.g., *Cole Palmer*)
- 🧠 Uses **KMeans Clustering** to group similar players
- 🧩 Suggests other players in the **same cluster & position**
- 📈 Visualizes players on a 2D **PCA scatter plot**
- 🌍 Displays player nationalities with emoji flags 🇧🇷🇫🇷🇩🇪

---

## 🛠 Built With

- **Python**
- **Pandas & Scikit-learn** (ML & data prep)
- **Streamlit** (Web interface)
- **Matplotlib & Seaborn** (Charts)

---

## 📁 File Structure

```
├── app.py                    # Main Streamlit app
├── players_with_clusters.csv # ML-processed player data
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## 📦 How to Run Locally

```bash
git clone https://github.com/your-username/player-similarity-app.git
cd player-similarity-app

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🧠 How It Works (Behind the Scenes)

1. Clean and scale performance stats from top 5 leagues
2. Apply **KMeans Clustering** to group players by similar metrics
3. Use **PCA** to reduce dimensionality for visual plots
4. Let users input a player and find similar ones from same **cluster & position**

---

## 📊 Sample Output

- Input: `Cole Palmer`
- Result: Players who play in the same position (`FW`, `MF`, etc.) with similar G+A, xG, xAG per 90 mins
- Bonus: Sees their location in PCA plot and nation flags 🇬🇧🇦🇷🇫🇷

---

## ✅ TODO / Coming Soon

- [ ] Filter by age or league
- [ ] Export similar player list to CSV
- [ ] Add cosine similarity or DBSCAN alternative
- [ ] Deploy to Hugging Face Spaces

---

## 📬 Contact

Feel free to reach out with feedback or feature ideas!

📧 your-email@example.com  
🐦 [@yourhandle](https://twitter.com/yourhandle)
