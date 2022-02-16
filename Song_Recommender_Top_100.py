#!/usr/bin/env python
# coding: utf-8

# In[1]:

import Scraped_Billboard_Top_100

billboard_100 = Scraped_Billboard_Top_100


# In[2]:


def is_song_in_top_100(df):
    
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
            answer = input('Are you sure your input was correct? You entered '+ user_input + ', did you mean '+ i + ' ? (yes/no) ').lower()
            
            if answer == 'yes':
                recommendation = df[df.song != user_input].sample(n=1)
                title = recommendation.iloc[0,0]
                artist = recommendation.iloc[0,1]
                return print('\n','Your song is in the Billboard Top 100 Songs!','\n','Here is your recommendation:',title, 'by', artist)
            
            elif answer == 'no':
                answer2 = input('Do you want to try again? (yes/no)').lower() 
                if answer2 == 'yes':
                    return is_song_in_top_100(df)
                elif answer2 == 'no':
                    return print('\n','Your song is not in the Billboard Top 100 Songs, sorry!')
                else:
                    return print('Your response was neither yes nor no, please start again.') + is_song_in_top_100(df)
            else:
                    return print('Your response was neither yes nor no, please start again.') + is_song_in_top_100(df)
                
    return print('Your song is not in the Billboard Top 100 Songs, sorry!')


# In[3]:


is_song_in_top_100(billboard_100)


# In[ ]:




