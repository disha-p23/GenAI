#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from reader import DocumentReader
from narration_engine import NarrationEngine
from narration_governor import NarrationGovernor
from ssml_generator import SSMLGenerator
from tts_engine import TTSEngine
from audio_merger import AudioMerger

import json


# =========================================================
# SAVE RESULTS
# =========================================================

def save_results(output_data, output_file="emotion_output.json"):

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(output_data, file, indent=4)

    print(f"\nResults saved to: {output_file}")


# =========================================================
# MAIN PIPELINE
# =========================================================

def main():

    # -----------------------------
    # INITIALIZE COMPONENTS
    # -----------------------------
    reader = DocumentReader()

    engine = NarrationEngine()

    governor = NarrationGovernor()

    ssml_generator = SSMLGenerator()

    tts_engine = TTSEngine()

    merger = AudioMerger()

    # -----------------------------
    # INPUT FILE
    # -----------------------------
    file_path = input(
        "Enter PDF/DOCX/TXT file path: "
    )

    # -----------------------------
    # READ DOCUMENT
    # -----------------------------
    sentences = reader.process_document(
        file_path
    )

    print("\nDocument Processed Successfully!")

    print("Total Sentences:", len(sentences))

    # -----------------------------
    # RUN NARRATION ENGINE
    # -----------------------------
    final_states = engine.process(
        sentences
    )

    print("\nProcessing Narration...\n")

    output_data = []

    # STORE ALL GENERATED AUDIO FILES
    audio_paths = []

    # =====================================================
    # PROCESS EACH SENTENCE
    # =====================================================

    for idx, state in enumerate(final_states):

        # =================================================
        # STEP 1: GOVERN VOICE
        # =================================================

        governed_voice = governor.regulate({

            "content_type":
                state["content_type"],

            "pitch":
                state["voice"]["pitch"],

            "speed":
                state["voice"]["speed"],

            "energy":
                state["voice"]["energy"],

            "pause":
                state["voice"]["pause"],

            "voice_style":
                state["voice"]["style"]
        })

        # =================================================
        # UPDATE STATE
        # =================================================

        state["voice"]["pitch"] = \
            governed_voice["pitch"]

        state["voice"]["speed"] = \
            governed_voice["speed"]

        state["voice"]["energy"] = \
            governed_voice["energy"]

        state["voice"]["pause"] = \
            governed_voice["pause"]

        state["voice"]["style"] = \
            governed_voice["voice_style"]

        state["voice"]["expressiveness"] = \
            governed_voice["expressiveness"]

        # =================================================
        # STEP 2: GENERATE SSML
        # =================================================

        ssml = ssml_generator.generate(
            state
        )

        state["ssml"] = ssml

        # =================================================
        # STEP 3: GENERATE AUDIO
        # =================================================

        audio_path = tts_engine.synthesize(
            state,
            idx
        )

        state["audio_path"] = audio_path

        # STORE FOR FINAL MERGE
        audio_paths.append(audio_path)

        # =================================================
        # STORE OUTPUT
        # =================================================

        output_data.append(state)

        # =================================================
        # DEBUG OUTPUT
        # =================================================

        print(f"\nSentence: {state['text']}")

        print(
            f"Content Type: "
            f"{state['content_type']}"
        )

        print(
            f"Emotion: "
            f"{state['emotion']} "
            f"({state['intensity']})"
        )

        print(f"\nVoice Profile:")

        print(
            f"  Style: "
            f"{state['voice']['style']}"
        )

        print(
            f"  Pitch: "
            f"{round(state['voice']['pitch'], 3)}"
        )

        print(
            f"  Speed: "
            f"{round(state['voice']['speed'], 3)}"
        )

        print(
            f"  Energy: "
            f"{round(state['voice']['energy'], 3)}"
        )

        print(
            f"  Expressiveness: "
            f"{state['voice']['expressiveness']}"
        )

        print(f"\nMusic: {state['music']}")

        print(f"\nSSML:")

        print(state["ssml"])

        print(
            f"\nAudio File: "
            f"{state['audio_path']}"
        )

        print("-" * 60)

    # =====================================================
    # FINAL AUDIOBOOK MERGE
    # =====================================================

    print("\nMerging audio files...\n")

    final_audio = merger.merge(
        audio_paths,
        output_path="final_narration.mp3"
    )

    print("\nFINAL AUDIOBOOK GENERATED!")

    print(f"Output File: {final_audio}")

    # =====================================================
    # SAVE RESULTS
    # =====================================================

    save_results(output_data)




    # =========================================================
# STREAMLIT PIPELINE FUNCTION
# =========================================================

def run_pipeline(file_path):

    # -----------------------------
    # INITIALIZE COMPONENTS
    # -----------------------------
    reader = DocumentReader()

    engine = NarrationEngine()

    governor = NarrationGovernor()

    ssml_generator = SSMLGenerator()

    tts_engine = TTSEngine()

    merger = AudioMerger()

    # -----------------------------
    # READ DOCUMENT
    # -----------------------------
    sentences = reader.process_document(
        file_path
    )

    # -----------------------------
    # RUN NARRATION ENGINE
    # -----------------------------
    final_states = engine.process(
        sentences
    )

    output_data = []

    audio_paths = []

    # =====================================================
    # PROCESS EACH SENTENCE
    # =====================================================

    for idx, state in enumerate(final_states):

        governed_voice = governor.regulate({

            "content_type":
                state["content_type"],

            "pitch":
                state["voice"]["pitch"],

            "speed":
                state["voice"]["speed"],

            "energy":
                state["voice"]["energy"],

            "pause":
                state["voice"]["pause"],

            "voice_style":
                state["voice"]["style"]
        })

        # UPDATE VOICE
        state["voice"]["pitch"] = \
            governed_voice["pitch"]

        state["voice"]["speed"] = \
            governed_voice["speed"]

        state["voice"]["energy"] = \
            governed_voice["energy"]

        state["voice"]["pause"] = \
            governed_voice["pause"]

        state["voice"]["style"] = \
            governed_voice["voice_style"]

        state["voice"]["expressiveness"] = \
            governed_voice["expressiveness"]

        # GENERATE SSML
        ssml = ssml_generator.generate(
            state
        )

        state["ssml"] = ssml

        # GENERATE AUDIO
        audio_path = tts_engine.synthesize(
            state,
            idx
        )

        state["audio_path"] = audio_path

        audio_paths.append(audio_path)

        output_data.append(state)

    # =====================================================
    # MERGE AUDIO
    # =====================================================

    final_audio = merger.merge(
        audio_paths,
        output_path="final_narration.mp3"
    )

    # SAVE JSON
    save_results(output_data)

    # RETURN RESULTS
    return {

        "sentences": sentences,

        "states": output_data,

        "final_audio": final_audio
    }
# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    main()


# In[ ]:





# In[ ]:




