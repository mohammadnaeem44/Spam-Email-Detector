import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("dataset/emails.csv", encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip()

print("Columns found:", df.columns)

# AUTO-DETECT correct columns
if "v1" in df.columns and "v2" in df.columns:
    df = df[["v1", "v2"]]
    df.columns = ["label", "text"]

elif "Category" in df.columns and "Message" in df.columns:
    df = df[["Category", "Message"]]
    df.columns = ["label", "text"]

elif "label" in df.columns and "text" in df.columns:
    df = df[["label", "text"]]

else:
    # fallback: assume first column = label, second = text
    df = df.iloc[:, :2]
    df.columns = ["label", "text"]

# Convert labels
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1,
    "0": 0,
    "1": 1
})

df = df.dropna()

# Split data
X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model/spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Model trained successfully!")