import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches
from nltk.stem.porter import PorterStemmer

# === Google Sheet CSV export link ===
SHEET_ID = "1lWg0xlIPnplK-nnKoThpidP0w5fpLQaSFS1KGBnnAzw"  # your sheet ID
SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

def load_and_preprocess_data():
    # Load sheet dynamically
    df = pd.read_csv(SHEET_CSV_URL)
    df = df.fillna("")  # replace NaN with empty strings

    # Combine text fields into a single column (adjust column names if needed)
    df["combined"] = (
        df.get("Summary", "") + " " +
        df.get("Genres", "") + " " +
        df.get("Themes", "")
    ).str.lower()

    # Apply stemming
    ps = PorterStemmer()
    def stem_text(text):
        return " ".join(ps.stem(word) for word in text.split())
    df["combined_stemmed"] = df["combined"].apply(stem_text)

    # Convert text to vector
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(df["combined_stemmed"])

    # Compute similarity matrix
    similarity = cosine_similarity(vectors)

    return df, similarity

# Load once at startup
df_data, similarity_matrix = load_and_preprocess_data()

def recommend(title_input, top_n=5):
    title = title_input.strip().lower()
    titles_list = [t.lower() for t in df_data["Title"].tolist()]

    # Try to match with closest title
    matches = get_close_matches(title, titles_list, n=1, cutoff=0.6)
    if not matches:
        return []

    matched_title = matches[0]
    matched_index = titles_list.index(matched_title)

    distances = similarity_matrix[matched_index]
    ranked = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)

    # Skip itself (first one is always the same drama)
    top_indices = [idx for idx, _ in ranked[1: top_n + 1]]

    return df_data.iloc[top_indices]["Title"].tolist()

def get_recommendations(user_title):
    return recommend(user_title, top_n=5)
