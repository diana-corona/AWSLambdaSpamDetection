import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from joblib import dump
# Text Preprocessing
import re
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text



# Train, Test Split
data = pd.read_csv('data/SPAM.csv')

X = data['Message'].apply(preprocessor)
y = data['Category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2703)

# Training a Neural Network Pipeline
max_features = 700
tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, 
                        max_features=max_features, 
                        ngram_range=(1,1))

mplclassifier = MLPClassifier(hidden_layer_sizes=(max_features, max_features),activation='relu',solver='adam',learning_rate='constant')

neural_net_pipeline = Pipeline([('vectorizer', tfidf), 
                                ('nn', mplclassifier)])

neural_net_pipeline.fit(X_train, y_train)

# Testing the Pipeline
y_pred = neural_net_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print('Accuracy: {} %'.format(100 * accuracy_score(y_test, y_pred)))

# Save
dump(neural_net_pipeline, 'spam_classifier.joblib')