#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import Counter



class EmotionSmoother:

    def smooth_emotions(
        self,
        emotion_results
    ):

        smoothed = []

        emotions = [
            r['emotion']
            for r in emotion_results
        ]

        for i in range(len(emotions)):

            weights = Counter()

            # PREVIOUS
            if i > 0:

                weights[
                    emotions[i - 1]
                ] += 1

            # CURRENT
            weights[
                emotions[i]
            ] += 3

            # NEXT
            if i < len(emotions) - 1:

                weights[
                    emotions[i + 1]
                ] += 1

            dominant = weights.most_common(
                1
            )[0][0]

            smoothed.append(dominant)

        return smoothed


# In[ ]:





# In[ ]:




