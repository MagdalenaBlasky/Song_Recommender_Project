#!/usr/bin/env python
# coding: utf-8

# In[2]:


def scrape_billboard ():
    
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    
    url = "https://www.billboard.com/charts/hot-100/"
    
    response = requests.get(url)
    
    response.content
    
    status = response.status_code
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    artists = []
    songs = []

    for number, item in enumerate(soup.select(".a-no-trucate"), start=0):
        if number % 2 == 0:
            songs.append(item.get_text())
        else:
            artists.append(item.get_text())
            
    artists_names = []
    song_names = []
    
    for i in artists: 
        artists_names.append(i.strip())
    
    for i in songs: 
        song_names.append(i.strip())
    
    billboard_100 = pd.DataFrame({'song':song_names,'artist':artists_names})
    
    billboard_100.song = billboard_100.song.str.lower()
    billboard_100.artist = billboard_100.artist.str.lower()
    
    billboard_100.to_csv('Data/Scraped_Billboard_Top_100.csv', index=False)
    
    return billboard_100

