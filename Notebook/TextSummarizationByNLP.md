---
layout: lecture
title: "Text Summarization using NLP."
date: 2020-02-19
ready: true
video:
  aspect:
  id:
---


# What is text summarization?

Text summarization is the process of distilling the most important information from a source text.

# Why automatic text summarization?

- Summaries reduce reading time.
- When researching documents, summaries make the selection process easier.
- Automatic summarization improves the effectiveness of indexing.
- Automatic summarization algorithms are less biased than human summarizers.
- Personalized summaries are useful in question-answering system as they provide personalized information.
- Using automatic or semi-automatic summarization systems enables commercial abstract services to - increase the number of textdocuments they are able to process.

# How to do text summarization?

- Text cleaning.
- Sentence tokenization.
- Word tokenization.
- Word-frequency table.
- Summarization.

## Text

```python
text = """
Beautiful Soup, so rich and green,
Waiting in a hot tureen!
Who for such dainties would not stoop?
Soup of the evening, beautiful Soup!
Soup of the evening, beautiful Soup!
Beau--ootiful Soo--oop!
Beau--ootiful Soo--oop!
Soo--oop of the e--e--evening,
Beautiful, beautiful Soup!
Beautiful Soup! Who cares for fish,
Game or any other dish?
Who would not give all else for two
Pennyworth only of Beautiful Soup?
Pennyworth only of beautiful Soup?
Beau--ootiful Soo--oop!
Beau--ootiful Soo--oop!
Soo--oop of the e--e--evening,
Beautiful, beauti--FUL SOUP!
"""
```

## Let's Get Started with SpaCy

```python
# !pip install -U spacy
# !python -m spacy download en_core_web_sm
```
```python
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
tokens = [token.text for token in doc]
#print(tokens)

punctuation = punctuation + '\n'
#print(punctuation)

word_frequencies = {}
for word in doc:
  if word.text.lower() not in stopwords:
    if word.text.lower() not in punctuation:
      if word.text not in word_frequencies.keys():
        word_frequencies[word.text] = 1
      else:
        word_frequencies[word.text] += 1
#print(word_frequencies)
```
```python
max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
  word_frequencies[word] = word_frequencies[word] / max_frequency # Normalization
#print(word_frequencies)
```
```python
sentence_tokens = [sent for sent in doc.sents]
#print(sentence_tokens)
```
     
