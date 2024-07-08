# -*- coding: utf-8 -*-
"""Movie recommendation system using ML with python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lQrEcnjxTKb8VHbPKZz7o5WK8PMMA7we

Importing The dependencies
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""Data collection and preprocessing"""

movie_data = pd.read_csv('/content/movies.csv')

#print first 5 rows of df
movie_data.head()

#number of rows and columns
movie_data.shape

# selecting relevant features for recommendation
selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

# replacing the null values with null string
for feature in selected_features:
  movie_data[feature] = movie_data[feature].fillna('')

#combining the all the 5 selected features
combined_feature = movie_data['genres']+' '+movie_data['keywords']+' '+movie_data['tagline']+' '+movie_data['cast']+' '+movie_data['director']

print(combined_feature)

#converting the text data into feature vector
vectorizer = TfidfVectorizer()
feature_vector = vectorizer.fit_transform(combined_feature)

print(feature_vector)

#