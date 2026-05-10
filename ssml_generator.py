#!/usr/bin/env python
# coding: utf-8

# In[3]:


class SSMLGenerator:

    def __init__(self):

        pass

    # ======================================================
    # MAIN FUNCTION
    # ======================================================

    def generate(self, state):

        text = state["text"]

        voice = state["voice"]

        # SAFE ACCESS
        prosody = state.get("prosody", {})

        stress_words = set(
            prosody.get("stress_regions", [])
        )

        pauses = prosody.get("pauses", [])

        # VOICE SETTINGS
        pitch = voice.get("pitch", 1.0)

        speed = voice.get("speed", 1.0)

        # ======================================================
        # APPLY EMPHASIS
        # ======================================================

        ssml_text = self._apply_emphasis(
            text,
            stress_words
        )

        # ======================================================
        # APPLY PAUSES
        # ======================================================

        ssml_text = self._apply_pauses(
            ssml_text,
            pauses
        )

        # ======================================================
        # CONVERT VALUES
        # ======================================================

        pitch_percent = int(
            (pitch - 1.0) * 50
        )

        rate_percent = int(
            (speed - 1.0) * 40
        )

        # ======================================================
        # BUILD FINAL SSML
        # ======================================================

        ssml = f"""
<speak version="1.0" xml:lang="en-US">

    <voice name="en-IN-NeerjaNeural">

        <prosody
            pitch="{pitch_percent}%"
            rate="{rate_percent}%">

            {ssml_text}

        </prosody>

    </voice>

</speak>
"""

        return ssml.strip()

    # ======================================================
    # EMPHASIS HANDLER
    # ======================================================

    def _apply_emphasis(
        self,
        text,
        stress_words
    ):

        strong_keywords = {
            "important",
            "critical",
            "urgent",
            "amazing",
            "incredible"
        }

        moderate_keywords = {
            "experience",
            "project",
            "learning",
            "development",
            "opportunity"
        }

        words = text.split()

        processed = []

        for word in words:

            clean = word.strip(".,!?").lower()

            if clean in strong_keywords:

                processed.append(
                    f"<emphasis level='strong'>{word}</emphasis>"
                )

            elif clean in moderate_keywords:

                processed.append(
                    f"<emphasis level='moderate'>{word}</emphasis>"
                )

            elif clean in stress_words:

                processed.append(
                    f"<emphasis level='moderate'>{word}</emphasis>"
                )

            else:

                processed.append(word)

        return " ".join(processed)

    # ======================================================
    # PAUSE HANDLER
    # ======================================================

    def _apply_pauses(
        self,
        text,
        pauses
    ):

        text = text.replace(
            ".",
            ". <break time='350ms'/>"
        )

        text = text.replace(
            ",",
            ", <break time='150ms'/>"
        )

        return text


# In[3]:





# In[ ]:




