from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator
from sklearn.feature_selection import SelectPercentile
 
class Classifier(BaseEstimator):
    def __init__(self):
        self.clf = Pipeline([
            ('imputer', Imputer(strategy='most_frequent')),
            ('select', SelectPercentile(percentile=90)),
            ('rf', AdaBoostClassifier(
                base_estimator=RandomForestClassifier(
                  max_depth=5, n_estimators=30),
                n_estimators=10)
            )
        ])
 
    def fit(self, X, y):
        self.clf.fit(X, y)
 
    def predict(self, X):
        return self.clf.predict(X)
 
    def predict_proba(self, X):
        return self.clf.predict_proba(X)