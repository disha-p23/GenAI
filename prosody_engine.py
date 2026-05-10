#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


class ProsodyEngine:

    def __init__(self):

        self.rising_patterns = [
            "?",
            "really",
            "what",
            "how",
            "why"
        ]

        self.falling_patterns = [
            ".",
            "finally",
            "never",
            "goodbye"
        ]

    # =====================================================
    # DETECT INTONATION
    # =====================================================

    def detect_intonation(
        self,
        sentence
    ):

        sentence_lower = sentence.lower()

        # RISING
        for pattern in self.rising_patterns:

            if pattern in sentence_lower:

                return "rising"

        # FALLING
        for pattern in self.falling_patterns:

            if pattern in sentence_lower:

                return "falling"

        return "neutral"

    # =====================================================
    # DETECT DRAMATIC PAUSES
    # =====================================================

    def detect_pause_locations(
        self,
        sentence
    ):

        pauses = []

        for match in re.finditer(
            r'[,;:.!?]',
            sentence
        ):

            pauses.append({

                "index": match.start(),

                "symbol": match.group()
            })

        return pauses

    # =====================================================
    # STRESS REGIONS
    # =====================================================

    def detect_stress_regions(
        self,
        sentence
    ):

        stress_words = []

        words = sentence.split()

        for i, word in enumerate(words):

            clean = word.lower().strip(
                ".,!?;:"
            )

            # LONG WORDS
            if len(clean) > 7:

                stress_words.append(word)

            # ALL CAPS
            elif word.isupper():

                stress_words.append(word)

            # EXCLAMATION
            elif "!" in word:

                stress_words.append(word)

        return stress_words

    # =====================================================
    # SPEECH CADENCE
    # =====================================================

    def estimate_cadence(
        self,
        sentence
    ):

        word_count = len(sentence.split())

        if word_count < 6:
            return "sharp"

        elif word_count < 15:
            return "balanced"

        return "flowing"

    # =====================================================
    # MAIN ANALYSIS
    # =====================================================

    def analyze(
        self,
        sentence
    ):

        return {

            "intonation":
                self.detect_intonation(
                    sentence
                ),

            "pauses":
                self.detect_pause_locations(
                    sentence
                ),

            "stress_regions":
                self.detect_stress_regions(
                    sentence
                ),

            "cadence":
                self.estimate_cadence(
                    sentence
                )
        }


# In[3]:


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




