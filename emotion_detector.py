#!/usr/bin/env python
# coding: utf-8

# In[2]:


from transformers import pipeline
from collections import Counter
import re


# =========================================================
# EMOTION DETECTOR
# =========================================================

class EmotionDetector:

    def __init__(self):

        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )

    # =====================================================
    # CONTEXT WINDOWS
    # =====================================================

    def create_context_windows(self, sentences):

        contexts = []

        for i in range(len(sentences)):

            prev_sent = sentences[i - 1] if i > 0 else ""

            curr_sent = sentences[i]

            next_sent = (
                sentences[i + 1]
                if i < len(sentences) - 1
                else ""
            )

            context = f"{prev_sent} {curr_sent} {next_sent}"

            contexts.append(context.strip())

        return contexts

    # =====================================================
    # INTENSITY
    # =====================================================

    def get_intensity(self, confidence):

        if confidence > 0.85:
            return "high"

        elif confidence > 0.70:
            return "medium"

        return "low"

    # =====================================================
    # CHUNKING
    # =====================================================

    def chunk_long_sentence(
        self,
        sentence,
        max_words=25
    ):

        words = sentence.split()

        if len(words) <= max_words:
            return [sentence]

        chunks = re.split(r'[,;:.!?]', sentence)

        return [

            chunk.strip()

            for chunk in chunks

            if chunk.strip()
        ]

    # =====================================================
    # PREPROCESS
    # =====================================================

    def preprocess_sentences(self, sentences):

        processed = []

        mapping = []

        for sentence in sentences:

            chunks = self.chunk_long_sentence(
                sentence
            )

            for chunk in chunks:

                processed.append(chunk)

                mapping.append(sentence)

        return processed, mapping

    # =====================================================
    # DETECT
    # =====================================================

    def detect_emotions(
        self,
        sentences,
        threshold=0.55
    ):

        contexts = self.create_context_windows(
            sentences
        )

        results = self.classifier(contexts)

        final_results = []

        for result in results:

            sorted_results = sorted(
                result,
                key=lambda x: x["score"],
                reverse=True
            )

            primary = sorted_results[0]

            secondary = sorted_results[1]

            emotion = primary["label"]

            confidence = primary["score"]

            if confidence < threshold:

                emotion = "neutral"

            final_results.append({

                "emotion": emotion,

                "confidence": confidence,

                "intensity":
                    self.get_intensity(
                        confidence
                    ),

                "secondary_emotion":
                    secondary["label"],

                "secondary_confidence":
                    secondary["score"]
            })

        return final_results

    # =====================================================
    # AGGREGATE CHUNKS
    # =====================================================

    def aggregate_chunk_emotions(
        self,
        results,
        mapping
    ):

        grouped = {}

        for result, original in zip(
            results,
            mapping
        ):

            grouped.setdefault(
                original,
                []
            ).append(result)

        final = []

        for sentence, chunk_results in grouped.items():

            emotions = [
                r["emotion"]
                for r in chunk_results
            ]

            dominant = Counter(
                emotions
            ).most_common(1)[0][0]

            avg_confidence = sum(

                r["confidence"]

                for r in chunk_results

            ) / len(chunk_results)

            secondary = Counter(

                r["secondary_emotion"]

                for r in chunk_results

            ).most_common(1)[0][0]

            avg_secondary = sum(

                r["secondary_confidence"]

                for r in chunk_results

            ) / len(chunk_results)

            final.append({

                "emotion": dominant,

                "confidence": avg_confidence,

                "intensity":
                    self.get_intensity(
                        avg_confidence
                    ),

                "secondary_emotion":
                    secondary,

                "secondary_confidence":
                    avg_secondary
            })

        return final



# In[ ]:





# In[ ]:




