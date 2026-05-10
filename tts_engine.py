#!/usr/bin/env python
# coding: utf-8

# In[3]:


import edge_tts
import asyncio
import os


class TTSEngine:

    def __init__(self):

        os.makedirs(
            "audio_output",
            exist_ok=True
        )

    # =====================================================
    # ASYNC AUDIO GENERATION
    # =====================================================

    async def async_generate(

        self,

        text,

        voice,

        rate,

        pitch,

        output_path
    ):

        communicate = edge_tts.Communicate(

            text=text,

            voice=voice,

            rate=rate,

            pitch=pitch
        )

        await communicate.save(
            output_path
        )

    # =====================================================
    # MAIN SYNTHESIS
    # =====================================================

    def synthesize(

        self,

        narration_state,

        index
    ):

        # =================================================
        # TEXT
        # =================================================

        text = narration_state["text"]

        # =================================================
        # VOICE SETTINGS
        # =================================================

        voice_data = narration_state["voice"]

        speed = voice_data.get(
            "speed",
            1.0
        )

        pitch = voice_data.get(
            "pitch",
            1.0
        )

        # =================================================
        # CONVERT TO EDGE-TTS FORMAT
        # =================================================

        rate_percent = int(
            (speed - 1.0) * 100
        )

        pitch_percent = int(
            (pitch - 1.0) * 50
        )

        rate = f"{rate_percent:+d}%"

        pitch = f"{pitch_percent:+d}Hz"

        # =================================================
        # VOICE
        # =================================================

        voice = "en-IN-NeerjaNeural"

        # =================================================
        # OUTPUT FILE
        # =================================================

        output_path = (
            f"audio_output/sentence_{index}.mp3"
        )

        # =================================================
        # GENERATE AUDIO
        # =================================================

        asyncio.run(

            self.async_generate(

                text,

                voice,

                rate,

                pitch,

                output_path
            )
        )

        return output_path


# In[ ]:




