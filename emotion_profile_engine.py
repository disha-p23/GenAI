#!/usr/bin/env python
# coding: utf-8

# In[3]:


class EmotionProfileEngine:

    def __init__(self):

        self.profiles = {

            "uplifting": {

                "pitch": 1.15,
                "speed": 1.08,
                "energy": 0.80,
                "pause": 0.15,
                "voice_style": "bright",
                "music": "hopeful"
            },

            "dramatic": {

                "pitch": 0.92,
                "speed": 0.90,
                "energy": 0.60,
                "pause": 0.45,
                "voice_style": "heavy",
                "music": "cinematic_sad"
            },

            "suspense": {

                "pitch": 0.85,
                "speed": 0.82,
                "energy": 0.70,
                "pause": 0.60,
                "voice_style": "tense",
                "music": "dark_ambient"
            },

            "intense": {

                "pitch": 1.10,
                "speed": 1.18,
                "energy": 0.95,
                "pause": 0.10,
                "voice_style": "aggressive",
                "music": "action"
            },

            "mysterious": {

                "pitch": 0.88,
                "speed": 0.78,
                "energy": 0.55,
                "pause": 0.55,
                "voice_style": "whispered",
                "music": "mystery"
            },

            "dark": {

                "pitch": 0.75,
                "speed": 0.72,
                "energy": 0.50,
                "pause": 0.65,
                "voice_style": "cold",
                "music": "horror"
            },

            "warm": {

                "pitch": 1.05,
                "speed": 0.95,
                "energy": 0.65,
                "pause": 0.30,
                "voice_style": "soft",
                "music": "romantic"
            },

            "calm": {

                "pitch": 1.00,
                "speed": 1.00,
                "energy": 0.40,
                "pause": 0.25,
                "voice_style": "neutral",
                "music": "minimal"
            }
        }

    def get_profile(
        self,
        narrative_emotion
    ):

        return self.profiles.get(

            narrative_emotion,

            self.profiles["calm"]
        )


# In[5]:


class EmotionVoiceMapper:

    def __init__(self):

        self.voice_settings = {

            "joy": {
                "rate": "+15%",
                "pitch": "+10Hz",
                "volume": "+0%"
            },

            "sadness": {
                "rate": "-20%",
                "pitch": "-10Hz",
                "volume": "-10%"
            },

            "anger": {
                "rate": "+10%",
                "pitch": "+5Hz",
                "volume": "+10%"
            },

            "fear": {
                "rate": "-10%",
                "pitch": "+15Hz",
                "volume": "-5%"
            },

            "surprise": {
                "rate": "+20%",
                "pitch": "+20Hz",
                "volume": "+5%"
            },

            "neutral": {
                "rate": "+0%",
                "pitch": "+0Hz",
                "volume": "+0%"
            }
        }

    def get_voice_settings(self, emotion):

        return self.voice_settings.get(
            emotion,
            self.voice_settings["neutral"]
        )


# In[ ]:




