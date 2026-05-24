import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# Temporary sample data taaki bina bade dataset ke model check ho sake
data = {
    'text': [
        'I am so happy and excited today', 'This is a wonderful and beautiful day',
        'I feel so sad and lonely', 'I want to cry, this is terrible',
        'I am so angry right now', 'Shut up, I hate this behavior'
    ],
    'emotion': ['joy', 'joy', 'sadness', 'sadness', 'anger', 'anger']
}

df = pd.DataFrame(data)

X = df['text']
y = df['emotion']

# Data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline setup
model_pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

print("AI Model seekh raha hai...")
model_pipeline.fit(X_train, y_train)
print("Model ne seekh liya!")

# Save model
with open("emotion_model.pkl", "wb") as file:
    pickle.dump(model_pipeline, file)
print("Model save ho gaya 'emotion_model.pkl' ke naam se!")