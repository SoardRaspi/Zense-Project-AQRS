import os.path

import nltk
from nltk import FreqDist
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter

import ssl
import csv
import string

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')

text_list = []

path = os.path.join(os.getcwd(), 'States/Maharashtra')

# with open(os.path.join(path, 'data_cleaner.csv'), mode='r') as file:
with open(os.path.join(path, 'content.csv'), mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for _, h, __ in csvFile:
        translator = str.maketrans("", "", string.punctuation)
        clean_sentence = h.translate(translator)

        text_list.append(clean_sentence)

tokenized_texts = [nltk.word_tokenize(text.lower()) for text in text_list]
all_tokens = [token for text_tokens in tokenized_texts for token in text_tokens]

stop_words = set(stopwords.words("english"))
filtered_tokens = [token for token in all_tokens if token not in stop_words]

unigrams = Counter(filtered_tokens)
bigrams = Counter(ngrams(filtered_tokens, 2))
trigrams = Counter(ngrams(filtered_tokens, 3))

# Print the most common unigrams, bigrams, and trigrams
print("Most Common Unigrams:")
print(unigrams.most_common(10))

print("\nMost Common Bigrams:")
print(bigrams.most_common(10))

print("\nMost Common Trigrams:")
print(trigrams.most_common(10))
