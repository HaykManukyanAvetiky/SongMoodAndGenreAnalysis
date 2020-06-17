# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:24:55 2020

@author: Hayk
"""

import tensorflow.keras as keras
from tensorflow.keras import Sequential, layers, Input, optimizers, losses, metrics, callbacks, models
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer 
from joblib import dump, load


model = Sequential(layers=None, name=None)

#feature extraction
model.add(layers.Conv1D(1,10))
model.add(layers.BatchNormalization())
model.add(layers.ReLU())
model.add(layers.MaxPooling1D(pool_size=5))
          
model.add(layers.Conv1D(1,8))
model.add(layers.BatchNormalization())
model.add(layers.ReLU())
model.add(layers.MaxPooling1D(pool_size=4))   

model.add(layers.Conv1D(1,4))
model.add(layers.BatchNormalization())
model.add(layers.ReLU())
model.add(layers.MaxPooling1D(pool_size=2))

model.add(layers.Conv1D(1,4))
model.add(layers.BatchNormalization())
model.add(layers.ReLU())
model.add(layers.MaxPooling1D(pool_size=2))

#clasification
model.add(layers.Flatten())
model.add(layers.Dropout(rate=0.3))
model.add(layers.Dense(units=10))
model.add(layers.Softmax())

#model.build(input_shape=(None,49462, 1))

vectorizer = load('vectorizer.joblib')
scaler = load('scaler.joblib')
model = models.load_model('model.hdf5', custom_objects=None, compile=True)

print(model.genres )