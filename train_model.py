import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the CSV
df = pd.read_csv("remedies.csv")

# ✅ Use 'symptoms' as input, 'ailment' as output
X = df["symptoms"]
y = df["ailment"]

# ✅ Vectorize the symptoms
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# ✅ Train the model
model = MultinomialNB()
model.fit(X_vectorized, y)

# ✅ Save model and vectorizer
joblib.dump(model, "remedy_predictor.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained and saved as remedy_predictor.pkl")
