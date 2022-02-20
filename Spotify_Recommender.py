#!/usr/bin/env python
# coding: utf-8

# In[23]:


import config
import spotipy
import pickle
import json 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sklearn.preprocessing import StandardScaler
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id,
                                                           client_secret= config.client_secret))


# In[24]:


songs_df = pd.read_csv('Data/songs_dataframe_concatenated.csv')


# In[25]:


def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as f: 
            return pickle.load(f) 
        
    except FileNotFoundError: 
        print("File not found!")


# In[26]:


scaler = load(filename = "Model/scaler.pickle")
kmeans = load(filename = "Model/kmeans.pickle")


# In[27]:


def embeded_player(track_id):
    
    from IPython.display import IFrame

    player = IFrame(src="https://open.spotify.com/embed/track/"+track_id,
               width="320",
               height="80",
               frameborder="0",
               allowtransparency="true",
               allow="encrypted-media",
              )
    return player


# In[28]:


def find_features_input_ver_1(user_input):  
        
    x = sp.search(q=user_input, limit =10, market="US")['tracks']['items'][1]['external_urls']["spotify"][31:]

    y = sp.audio_features(x)

    input_song_name = sp.track(x,market='US')['name']
    input_song_artist = sp.track(x, market='US')['album']['artists'][0]['name']
    
    print('Your song is: ' + input_song_name + ' by ' + input_song_artist)
    
    song_features = pd.DataFrame(y)
    song_id = song_features['id']
    song_features = song_features.drop(['id','type', 'uri', 'track_href', 'analysis_url','time_signature', 'duration_ms'], axis =  1)
    
    features_scaled = scaler.transform(song_features)
    song_features_scaled = pd.DataFrame(features_scaled, columns = song_features.columns)
    
    return (song_features_scaled)


# In[29]:


def find_features_input(user_input):
    
    import re


    song_ids_list = []
    
    for i in range (0, 3):
        song_ids_list.append(sp.search(q=user_input, limit =3, market="GB")['tracks']['items'][i]['external_urls']["spotify"][31:])
    
    song_name_list = []
    
    for i in song_ids_list: 
        song_name_list.append(sp.track(i, market='GB')['name'])
    
    artist_name_list = []
    
    for i in song_ids_list:
        artist_name_list.append(sp.track(i, market='GB')['album']['artists'][0]['name'])
    

    user_menu_df = pd.DataFrame({'title': song_name_list, 'artists': artist_name_list, 'id': song_ids_list})
    user_menu_df.index += 1

    print (user_menu_df[['title','artists']])

    r = None
    while r not in ('1', '2', '3'):  
    
        r = input ('Which song did you mean? Please select 1, 2 or 3. ')
        r = re.sub("\D", "", r)
    
        if r in ('1', '2' ,'3'):
            r = int(r)
            response_title = user_menu_df.loc[r , 'title' ]
            response_artist = user_menu_df.loc[r , 'artists' ]
            response_id = user_menu_df.loc[r , 'id' ]
            print('\n' + 'Your song choice is: ' + response_title + ' by ' + response_artist)
            user_final_choice_name = response_title
            break 
        else:
            print('\n' + "Your entry is invalid. Please choose 1, 2 or 3")  
    
    
    y = sp.audio_features(response_id)

    song_features = pd.DataFrame(y)
    song_id = song_features['id']
    song_features = song_features.drop(['id','type', 'uri', 'track_href', 'analysis_url','time_signature', 'duration_ms'], axis =  1)
        
    
    
    features_scaled = scaler.transform(song_features)
    song_features_scaled = pd.DataFrame(features_scaled, columns = song_features.columns)
    
    
    return (song_features_scaled)


# In[30]:


def spotify_song_recommender_ver_1(user_input):
    
    songs_df = pd.read_csv('Data/songs_dataframe_concatenated.csv')
    
    user_song = find_features_input(user_input)
    prediction = kmeans.predict(user_song)
    predict_cluster = prediction[0]
    
    recommendation_spotify = songs_df[songs_df['cluster']==predict_cluster].sample(n=1)
    title = recommendation_spotify.iloc[0,0]
    artist = recommendation_spotify.iloc[0,1]

    track_id = response_id
    
    player = empeded_player(track_id)
    
    return print('Your recommendation from Spotify is: ' + title + ' by '+ artist +'\n'+ track_id)


# In[31]:


def spotify_song_recommender(user_input):
    
    import re

    song_ids_list = []
    
    for i in range (0, 3):
        song_ids_list.append(sp.search(q=user_input, limit =3, market="GB")['tracks']['items'][i]['external_urls']["spotify"][31:])
    
    song_name_list = []
    
    for i in song_ids_list: 
        song_name_list.append(sp.track(i, market='GB')['name'])
    
    artist_name_list = []
    
    for i in song_ids_list:
        artist_name_list.append(sp.track(i, market='GB')['album']['artists'][0]['name'])
    

    user_menu_df = pd.DataFrame({'title': song_name_list, 'artists': artist_name_list, 'id': song_ids_list})
    user_menu_df.index += 1

    print (user_menu_df[['title','artists']])

    r = None
    while r not in ('1', '2', '3'):  
    
        r = input ('Which song did you mean? Please select 1, 2 or 3. ')
        r = re.sub("\D", "", r)
    
        if r in ('1', '2' ,'3'):
            r = int(r)
            response_title = user_menu_df.loc[r , 'title' ]
            response_artist = user_menu_df.loc[r , 'artists' ]
            response_id = user_menu_df.loc[r , 'id' ]
            print('\n' + 'Your song choice is: ' + response_title + ' by ' + response_artist)
            user_final_choice_name = response_title
            break 
        else:
            print('\n' + "Your entry is invalid. Please choose 1, 2 or 3")  
    
    
    y = sp.audio_features(response_id)

    song_features = pd.DataFrame(y)
    song_id = song_features['id']
    song_features = song_features.drop(['id','type', 'uri', 'track_href', 'analysis_url','time_signature', 'duration_ms'], axis =  1)
        
    features_scaled = scaler.transform(song_features)
    song_features_scaled = pd.DataFrame(features_scaled, columns = song_features.columns)
    
    songs_df = pd.read_csv('Data/songs_dataframe_concatenated.csv')
    
    prediction = kmeans.predict(song_features_scaled)
    prediction_cluster = prediction[0]
        
    recommendation_spotify = songs_df[songs_df['cluster']==prediction_cluster].sample(n=1)
    title = recommendation_spotify.iloc[0,0]
    artist = recommendation_spotify.iloc[0,1]
    recommendation_id = recommendation_spotify.iloc[0,2]
    
    
    player = embeded_player(recommendation_id)
    
    print('Your recommendation from Spotify is: ' + title + ' by '+ artist +'\n')
    return (player)


# In[32]:


def song_recommender():
    
    df = pd.read_csv("Data/Scraped_Billboard_Top_100.csv")
    
    from pyjarowinkler import distance
    
    user_input = input("Please enter a song name here: ")
    user_input = user_input.lower()
    
    for i in list(df.song):
        
        dist = distance.get_jaro_distance(i, user_input)
        
        if dist == 1:
            recommendation = df[df.song != user_input].sample(n=1)
            title = recommendation.iloc[0,0]
            artist = recommendation.iloc[0,1]
            return print('Your song is in the Billboard Top 100 Songs!','\n','Here is your recommendation:',title, 'by', artist)
        
        
        elif dist >= 0.90 and dist < 1:
            
            answer = None
            
            while answer not in ("yes", "no"):
                answer = input('Are you sure your input was correct? You entered '+ user_input + ', did you mean '+ i + ' ? (yes/no) ').lower()
            
                if answer == 'yes':
                    recommendation = df[df.song != user_input].sample(n=1)
                    title = recommendation.iloc[0,0]
                    artist = recommendation.iloc[0,1]
                    return print('\n','Your song is in the Billboard Top 100 Songs!','\n','Here is your recommendation:',title, 'by', artist)
            
                elif answer == 'no':
                    
                    answer2 = None
                    
                    while answer2 not in ("yes", "no"):
                    
                        answer2 = input('Your song is not in the Billboard Top 100 Songs. Do you want a recommendation from Spotify? (yes/no)').lower() 
                        
                        if answer2 == 'yes':
                            return spotify_song_recommender(user_input)
                        elif answer2 == 'no':
                            return print('\n',"Your song is not in the Billboard Top 100 Songs and you didn't want any other recommendation, sorry!")
                        else: 
                            print('\n' + '!!!Please enter yes or no!!!') 
                else:
                    print('\n'+'!!!Please enter yes or no!!!')
                
    return spotify_song_recommender(user_input)


# In[36]:


song_recommender()


# In[ ]:




