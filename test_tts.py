#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from prosody_engine import (
    ProsodyEngine,
    EmotionVoiceMapper
)

from ssml_generator import SSMLGenerator
from tts_engine import TTSEngine


voice_mapper = EmotionVoiceMapper()

prosody_engine = ProsodyEngine()

ssml_generator = SSMLGenerator()

tts_engine = TTSEngine()


samples = [

    {
        "text": "I am so happy to see you today!",
        "emotion": "joy"
    },

    {
        "text": "Everything feels empty and cold.",
        "emotion": "sadness"
    },

    {
        "text": "Get out of my way right now!",
        "emotion": "anger"
    },

    {
        "text": "Did you hear that strange noise?",
        "emotion": "fear"
    },

    {
        "text": "The meeting starts at 4 PM.",
        "emotion": "neutral"
    }
]


for i, sample in enumerate(samples):

    # Emotion-based voice
    voice = voice_mapper.get_voice_settings(
        sample["emotion"]
    )

    # Sentence-level prosody
    prosody = prosody_engine.analyze(
        sample["text"]
    )

    narration_state = {

        "text": sample["text"],

        "speed": voice["rate"],

        "pitch": voice["pitch"],

        "volume": voice["volume"],

        "intonation":
            prosody["intonation"],

        "cadence":
            prosody["cadence"]
    }

    path = tts_engine.synthesize(
        narration_state,
        i
    )

    print(f"Generated: {path}")


# In[ ]:




