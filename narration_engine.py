#!/usr/bin/env python
# coding: utf-8

# In[1]:


from emotion_detector import EmotionDetector
from emotion_smoother import EmotionSmoother


from narrative_mapper import (
    NarrativeEmotionMapper
)

from timeline_stabilizer import (
    EmotionTimelineStabilizer
)

from emotion_profile_engine import (
    EmotionProfileEngine
)

from momentum_engine import (
    EmotionalMomentum
)

from content_intent_engine import (
    ContentIntentEngine
)

from prosody_engine import (
    ProsodyEngine
)


# =========================================================
# MASTER NARRATION ENGINE
# =========================================================

class NarrationEngine:

    def __init__(self):

        self.detector = EmotionDetector()

        self.smoother = EmotionSmoother()

        self.mapper = NarrativeEmotionMapper()

        self.stabilizer = (
            EmotionTimelineStabilizer()
        )

        self.profile_engine = (
            EmotionProfileEngine()
        )

        self.momentum_engine = (
            EmotionalMomentum()
        )

        self.content_engine = (
            ContentIntentEngine()
        )

        self.prosody_engine = (
            ProsodyEngine()
        )

    # =====================================================
    # INTENSITY SCALING
    # =====================================================

    def apply_intensity(
        self,
        profile,
        confidence
    ):

        scaled = profile.copy()

        scaled["speed"] *= (
            0.85 + confidence * 0.3
        )

        scaled["pitch"] *= (
            0.9 + confidence * 0.2
        )

        scaled["energy"] *= confidence

        return scaled

    # =====================================================
    # CONTENT STYLE MODIFIER
    # =====================================================

    def apply_content_style(
        self,
        profile,
        content_type
    ):

        adjusted = profile.copy()

        # EDUCATIONAL
        if content_type == "educational":

            adjusted["pitch"] *= 0.98
            adjusted["speed"] *= 0.92
            adjusted["energy"] *= 0.85
            adjusted["pause"] *= 1.15

        # PROFESSIONAL
        elif content_type == "professional":

            adjusted["pitch"] *= 0.95
            adjusted["energy"] *= 0.80

        # STORYTELLING
        elif content_type == "storytelling":

            adjusted["energy"] *= 1.10
            adjusted["pause"] *= 1.20

        return adjusted

    # =====================================================
    # PAUSE DETECTION
    # =====================================================

    def detect_pause_type(
        self,
        sentence
    ):

        if "..." in sentence:
            return 1.5

        if "?" in sentence:
            return 1.2

        if "!" in sentence:
            return 0.8

        return 1.0

    # =====================================================
    # MAIN PIPELINE
    # =====================================================

    def process(self, sentences):

        # =================================================
        # DETECT GLOBAL CONTENT TYPE
        # =================================================

        full_text = " ".join(sentences)

        content_type = (

            self.content_engine.detect_content_type(
                full_text
            )
        )

        # =================================================
        # PREPROCESS
        # =================================================

        processed, mapping = (

            self.detector.preprocess_sentences(
                sentences
            )
        )

        # =================================================
        # EMOTION DETECTION
        # =================================================

        detected = self.detector.detect_emotions(
            processed
        )

        # =================================================
        # AGGREGATE CHUNK EMOTIONS
        # =================================================

        aggregated = (

            self.detector.aggregate_chunk_emotions(
                detected,
                mapping
            )
        )

        # =================================================
        # SMOOTH EMOTIONS
        # =================================================

        smoothed = self.smoother.smooth_emotions(
            aggregated
        )

        # =================================================
        # MAP TO NARRATIVE STYLES
        # =================================================

        narrative_emotions = [

            self.mapper.map_emotion(
                emotion
            )

            for emotion in smoothed
        ]

        # =================================================
        # STABILIZE TIMELINE
        # =================================================

        stabilized = self.stabilizer.stabilize(
            narrative_emotions
        )

        # =================================================
        # FINAL STATES
        # =================================================

        final_states = []

        previous_voice = None

        # =================================================
        # PROCESS EACH SENTENCE
        # =================================================

        for i, sentence in enumerate(sentences):

            emotion_data = aggregated[i]

            narrative_style = stabilized[i]

            # =============================================
            # GET BASE PROFILE
            # =============================================

            profile = (

                self.profile_engine.get_profile(
                    narrative_style
                )
            )

            # =============================================
            # APPLY INTENSITY
            # =============================================

            profile = self.apply_intensity(

                profile,

                emotion_data["confidence"]
            )

            # =============================================
            # APPLY CONTENT STYLE
            # =============================================

            profile = self.apply_content_style(

                profile,

                content_type
            )

            # =============================================
            # APPLY PAUSE MODIFIER
            # =============================================

            pause_multiplier = (
                self.detect_pause_type(
                    sentence
                )
            )

            profile["pause"] *= (
                pause_multiplier
            )

            # =============================================
            # EMOTIONAL MOMENTUM
            # =============================================

            if previous_voice is not None:

                profile = (
                    self.momentum_engine.blend(
                        previous_voice,
                        profile
                    )
                )

            previous_voice = profile

            # =============================================
            # PROSODY ANALYSIS
            # =============================================

            prosody = (
                self.prosody_engine.analyze(
                    sentence
                )
            )

            # =============================================
            # FINAL OUTPUT
            # =============================================

            final_states.append({

                "text":
                    sentence,

                "content_type":
                    content_type,

                "emotion":
                    emotion_data["emotion"],

                "secondary_emotion":
                    emotion_data[
                        "secondary_emotion"
                    ],

                "confidence":
                    round(
                        emotion_data["confidence"],
                        3
                    ),

                "secondary_confidence":
                    round(
                        emotion_data[
                            "secondary_confidence"
                        ],
                        3
                    ),

                "intensity":
                    emotion_data["intensity"],

                "narrative_style":
                    narrative_style,

                "voice": {

                    "pitch":
                        round(
                            profile["pitch"],
                            3
                        ),

                    "speed":
                        round(
                            profile["speed"],
                            3
                        ),

                    "energy":
                        round(
                            profile["energy"],
                            3
                        ),

                    "pause":
                        round(
                            profile["pause"],
                            3
                        ),

                    "style":
                        profile["voice_style"]
                },

                "music":
                    profile["music"],

                "prosody":
                    prosody
            })

        return final_states


# In[ ]:





# In[ ]:




