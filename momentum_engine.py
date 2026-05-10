#!/usr/bin/env python
# coding: utf-8

# In[3]:


class EmotionalMomentum:

    def blend(
        self,
        previous,
        current,
        alpha=0.7
    ):

        blended = {}

        for key in [

            "pitch",
            "speed",
            "energy",
            "pause"
        ]:

            blended[key] = (

                previous[key] * alpha +

                current[key] * (1 - alpha)
            )

        blended["voice_style"] = (
            current["voice_style"]
        )

        blended["music"] = (
            current["music"]
        )

        return blended


# In[ ]:




