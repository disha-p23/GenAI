#!/usr/bin/env python
# coding: utf-8

# In[1]:


from copy import deepcopy


class NarrationGovernor:

    def __init__(self):

        # ======================================================
        # CONTENT TYPE EXPRESSIVENESS CONTROL
        # ======================================================

        self.content_rules = {

            "educational": {
                "expressiveness": 0.25,
                "base_style": "professional_warm"
            },

            "corporate": {
                "expressiveness": 0.20,
                "base_style": "professional"
            },

            "research": {
                "expressiveness": 0.10,
                "base_style": "formal"
            },

            "news": {
                "expressiveness": 0.15,
                "base_style": "neutral"
            },

            "storytelling": {
                "expressiveness": 0.85,
                "base_style": "cinematic"
            },

            "motivational": {
                "expressiveness": 0.75,
                "base_style": "inspiring"
            },

            "casual": {
                "expressiveness": 0.50,
                "base_style": "conversational"
            }
        }

    # ==========================================================
    # GOVERN PARAMETERS
    # ==========================================================

    def regulate(self, narration_data):

        data = deepcopy(narration_data)

        content_type = data.get("content_type", "casual")

        rules = self.content_rules.get(
            content_type,
            self.content_rules["casual"]
        )

        expressiveness = rules["expressiveness"]

        # ======================================================
        # SCALE PITCH
        # ======================================================

        raw_pitch = data["pitch"]

        data["pitch"] = 1 + (
            (raw_pitch - 1) * expressiveness
        )

        # ======================================================
        # SCALE SPEED
        # ======================================================

        raw_speed = data["speed"]

        data["speed"] = 1 + (
            (raw_speed - 1) * expressiveness
        )

        # ======================================================
        # SCALE ENERGY
        # ======================================================

        raw_energy = data["energy"]

        data["energy"] = raw_energy * expressiveness

        # ======================================================
        # SCALE PAUSE
        # ======================================================

        raw_pause = data["pause"]

        pause_scale = 1 + ((1 - expressiveness) * 0.3)

        data["pause"] = raw_pause * pause_scale

        # ======================================================
        # UPDATE STYLE
        # ======================================================

        data["voice_style"] = rules["base_style"]

        # ======================================================
        # SAVE EXPRESSIVENESS
        # ======================================================

        data["expressiveness"] = expressiveness

        return data


# In[ ]:




