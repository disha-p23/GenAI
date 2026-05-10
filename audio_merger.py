#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pydub import AudioSegment


class AudioMerger:

    def merge(self, audio_paths, output_path="final_narration.mp3"):

        combined = AudioSegment.empty()

        for path in audio_paths:

            audio = AudioSegment.from_file(path)

            combined += audio

        combined.export(output_path, format="mp3")

        return output_path

