import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

from preprocessor import preprocessor

# Train, Test Split
data = pd.read_csv('training/data/SPAM.csv')

X = data['Message'].apply(preprocessor)
y = data['Category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2703)

# TfidfVectorizer
max_features = 700
tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, 
                        max_features=max_features, 
                        ngram_range=(1,1))

# RandomForestClassifier
#n_estimators = number of trees in the forest
classifier = RandomForestClassifier(n_estimators=20, criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1)

DecisionTree_pipeline = Pipeline([('vectorizer', tfidf), 
                                ('nn', classifier)])

DecisionTree_pipeline.fit(X_train, y_train)

# Testing the Pipeline
y_pred = DecisionTree_pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print('DecisionTree Accuracy : {} %'.format(100 * accuracy_score(y_test, y_pred)))

# Save
dump(DecisionTree_pipeline, 'models/spam_classifier_RandomForest.joblib')