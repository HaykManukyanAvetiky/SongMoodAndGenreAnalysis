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
import numpy as np

labels = ['Country', 'Electronic', 'Folk', 'HipHop', 'Indie', 'Jazz', 'Other', 'Pop', 'RB', 'Rock']
vectorizer = load('vectorizer.joblib')
scaler = load('scaler.joblib')
model = models.load_model('model.hdf5', custom_objects=None, compile=True)

def predict_gener(lyrics):
    """
    predicts song genre by lyrics
    """
    
    lyrics = vectorizer.transform(lyrics)
    lyrics = scaler.transform(lyrics)
    lyrics = lyrics.toarray()[:, :, np.newaxis]
    lyrics = model.predict(lyrics)
    lyrics = labels[lyrics.argmax(axis=-1).item()]
    return lyrics


if __name__ == '__main__':
    lyrics =[ """Have a little faith in me
                There's no words for what I feel
                You'll need a little time to see
                Let me prove my love is real
                Have a little faith in me
                And I'll give it back to you
                If I could only make you see
                Then every dream would still come true
                No matter who's to fight
                We gotta hold on tight
                I know, there's an answer to my prayer
                Gotta feeling like I've never had before
                And my love for you can open any door
                Have a little faith
                I could help you find your way
                Cause I know you're not that strong
                It isn't just a game we play
                Oh, you'll believe before too long
                I'll show ya how to love
                And to rise above
                I'll be every answer to your prayer
                If you feel it like you've never felt before
                Then all at once you can open any door
                Have a little faith
                Have a little faith in me
                And I'll give it back to you
                You'll need a little time to see
                We can make the dream come true
                No matter who's to fight
                We gotta hold on tight
                I know, there's an answer to my prayer
                Gotta feeling like I've never had before
                You know my love for you can open any door
                A little faith"""]
    print(predict_gener(lyrics))