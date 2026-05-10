#!/usr/bin/env python
# coding: utf-8

# In[4]:


class NarrativeEmotionMapper:

    def __init__(self):

        self.emotion_map = {

            "joy": "uplifting",

            "sadness": "dramatic",

            "anger": "intense",

            "fear": "suspense",

            "surprise": "mysterious",

            "neutral": "calm",

            "disgust": "dark",

            "love": "warm"
        }

    def map_emotion(self, emotion):

        return self.emotion_map.get(
            emotion,
            "calm"
        )


# In[ ]:





# In[ ]:




