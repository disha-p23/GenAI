#!/usr/bin/env python
# coding: utf-8

# In[3]:


import fitz
from docx import Document
from nltk.tokenize import sent_tokenize
import re


class DocumentReader:

    def read_pdf(self, file_path):

        text = ""

        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text

    def read_docx(self, file_path):

        doc = Document(file_path)

        text = "\n".join([para.text for para in doc.paragraphs])

        return text

    def read_txt(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read()

        return text

    def clean_text(self, text):

        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text)

        # Replace line breaks
        text = text.replace("\n", " ")

        return text.strip()

    def split_sentences(self, text):

        sentences = sent_tokenize(text)

        # Remove empty sentences
        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    def filter_sentences(self, sentences):

        filtered = []

        for sentence in sentences:

            sentence = sentence.strip()

            # Remove very short sentences
            if len(sentence.split()) < 4:
                continue

            # Remove emails
            if "@" in sentence:
                continue

            # Remove phone-number heavy lines
            digit_count = sum(c.isdigit() for c in sentence)

            if digit_count > 5:
                continue

            filtered.append(sentence)

        return filtered

    def process_document(self, file_path):

        file_path = file_path.replace("file:///", "")

        if file_path.endswith(".pdf"):

            text = self.read_pdf(file_path)

        elif file_path.endswith(".docx"):

            text = self.read_docx(file_path)

        elif file_path.endswith(".txt"):

            text = self.read_txt(file_path)

        else:
            raise ValueError("Unsupported file format")

        cleaned_text = self.clean_text(text)

        sentences = self.split_sentences(cleaned_text)

        # Apply filtering
        sentences = self.filter_sentences(sentences)

        return sentences


# In[ ]:




