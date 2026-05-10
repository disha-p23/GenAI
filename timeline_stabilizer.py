#!/usr/bin/env python
# coding: utf-8

# In[3]:


class EmotionTimelineStabilizer:

    def __init__(self):

        self.stable_emotions = {

            "suspense",
            "dramatic",
            "intense",
            "dark"
        }

    def stabilize(
        self,
        emotions,
        persistence=2
    ):

        if not emotions:

            return emotions

        stabilized = [emotions[0]]

        streak_emotion = emotions[0]

        streak_count = 1

        for current in emotions[1:]:

            previous = stabilized[-1]

            # STRONG EMOTIONS PERSIST
            if previous in self.stable_emotions:

                if current != previous:

                    if streak_count < persistence:

                        stabilized.append(
                            previous
                        )

                        streak_count += 1

                        continue

            # NORMAL TRANSITION
            stabilized.append(current)

            if current == streak_emotion:

                streak_count += 1

            else:

                streak_emotion = current

                streak_count = 1

        return stabilized



# In[ ]:




