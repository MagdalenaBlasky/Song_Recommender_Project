#!/usr/bin/env python
# coding: utf-8

# In[14]:


import config
import spotipy
import pickle
import json 
import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id,
                                                           client_secret= config.client_secret))

import Spotify_Recommender

songs_df = pd.read_csv('Data/songs_dataframe_concatenated.csv')


# In[15]:


scaler = load(filename = "Model/scaler.pickle")
kmeans = load(filename = "Model/kmeans.pickle")


# In[16]:


from Spotify_Recommender import song_recommender


# In[17]:


song_recommender()


# In[ ]:




