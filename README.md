# Song_Recommender_Project

## Team members: Magdalena Blaski-Makara, Muhammad Anani
## Project type: Web-scraping / API / K-Means clustering 

#### *Aim:* Create a user interface that returns song recommendations from databases created by scraping the Billboard Hot 100, and by using the Spotify API

#### *Reasoning:*
Work on a topic that we like :) and use API and webscrapping techniques to develope a fool-proof and useful tool; the song recommender.

#### This project consists of four main parts. Each of these parts is in its own notebook:
1. Scrapping artist and song names from the "Billboard Hot 100": This then is used in a song recomm
2. Using Spotify API in order to build a database of songs and their musical features from playlists
3. K-Means Clustering of song features 
4. Building a Song Recommender that takes user input and then if:
      1) the song is in the top 100; returns to the user a recommendendation from the top 100
      2) the song is NOT in the top 100; returns to the user a song recommendation from the same cluster in the database created using spotify. The user            can also play the song using the API imported player.
  
#### *Data:*

| Data-Set Features | Billboard Hot 100  | Spotify Playlists |
| ----------------- | ------------------ | ----------------- |
| Columns           | 2                  | 18                |
| Rows (songs)      | 100                | 10270             |
| Source            | Billboard Hot 100  | Spotify API (GB)  |


#### *Frameowork*
*Using python:*
1. Scrapping from Billboard Hot 100: this section defines a function that scrapes song and corresponding artist names and concatenates them into a .csv
2. Building a database of songs with Spotify API: sampling a wide variety of playlists and then adding them all into a .csv file that contains features of songs
3. Clustering songs from spotify playlists: clustering using K-Means. Choosing the most appropriate number of clusters based on elbow and silhouette methods
4. Building the song recommender: Finally, build the functions that allow the user to interact with the databases created in order to provide appropriate and ~fun~ recommendations

All notebooks all labeled with the corresponding numbers from 1-4 as the bullet points above



