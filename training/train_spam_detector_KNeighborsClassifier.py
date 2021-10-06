import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from joblib import dump

from preprocessor import preprocessor

# Text Preprocessing


# Train, Test Split
data = pd.read_csv('training/data/SPAM.csv')

X = data['Message'].apply(preprocessor)
y = data['Category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2703)

# TfidfVectorizer
max_features = 700
n_neighbors = 2
tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, 
                        max_features=max_features, 
                        ngram_range=(1,1))

# KNeighborsClassifier
kNeighbors = KNeighborsClassifier(n_neighbors=n_neighbors, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=None)

kNeighbors_pipeline = Pipeline([('vectorizer', tfidf), 
                                ('nn', kNeighbors)])

kNeighbors_pipeline.fit(X_train, y_train)

# Testing the Pipeline
y_pred = kNeighbors_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print('kNeighbors Accuracy : {} %'.format(100 * accuracy_score(y_test, y_pred)))

# Save
dump(kNeighbors_pipeline, 'models/spam_classifier_KNeighbors.joblib')