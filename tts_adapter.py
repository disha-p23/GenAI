#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyttsx3')


# In[3]:


class TTSAdapter:

    def convert(
        self,
        narration_state
    ):

        voice = narration_state["voice"]

        prosody = narration_state["prosody"]

        return {

            "text":
                narration_state["text"],

            "speed":
                voice["speed"],

            "pitch":
                voice["pitch"],

            "energy":
                voice["energy"],

            "pause":
                voice["pause"],

            "voice_style":
                voice["style"],

            "intonation":
                prosody["intonation"],

            "cadence":
                prosody["cadence"],

            "stress_regions":
                prosody["stress_regions"]
        }

    # =====================================================
    # BATCH CONVERSION
    # =====================================================

    def batch_convert(
        self,
        narration_states
    ):

        return [

            self.convert(state)

            for state in narration_states
        ]


# In[ ]:




