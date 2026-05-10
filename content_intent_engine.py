#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ContentIntentEngine:

    def __init__(self):

        self.educational_keywords = {

            "definition",
            "theorem",
            "formula",
            "chapter",
            "example",
            "solution"
        }

        self.professional_keywords = {

            "meeting",
            "project",
            "deadline",
            "report",
            "client"
        }

        self.story_keywords = {

            "suddenly",
            "whispered",
            "blood",
            "dark",
            "screamed"
        }

    # =====================================================
    # DETECT CONTENT TYPE
    # =====================================================

    def detect_content_type(
        self,
        text
    ):

        text_lower = text.lower()

        educational_score = sum(

            word in text_lower

            for word in self.educational_keywords
        )

        professional_score = sum(

            word in text_lower

            for word in self.professional_keywords
        )

        story_score = sum(

            word in text_lower

            for word in self.story_keywords
        )

        scores = {

            "educational":
                educational_score,

            "professional":
                professional_score,

            "storytelling":
                story_score
        }

        return max(
            scores,
            key=scores.get
        )


# In[ ]:




