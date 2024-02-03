import numpy as np
import ssl
from sklearn.cluster import KMeans
import spacy
from spacy import displacy
from transformers import BertTokenizer, BertModel
import torch
import nltk
import spacy
from nltk.tokenize import sent_tokenize
from collections import defaultdict

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download nltk resources (you only need to run this once)
nltk.download('punkt')

# # Function to get BERT embeddings for sentences
# def get_bert_embeddings(sentences, model_name='bert-base-uncased'):
#     tokenizer = BertTokenizer.from_pretrained(model_name)
#     model = BertModel.from_pretrained(model_name)
#
#     inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
#     with torch.no_grad():
#         outputs = model(**inputs)
#     embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
#     return embeddings
#
# # Function to perform K-means clustering
# def cluster_sentences(sentences, n_clusters=3):
#     embeddings = get_bert_embeddings(sentences)
#     kmeans = KMeans(n_clusters=n_clusters, random_state=42)
#     kmeans.fit(embeddings)
#     return kmeans.labels_
#
# # Function to extract sentences from a document
# def extract_sentences_from_document(document):
#     return sent_tokenize(document)
#
# # Example usage
# if __name__ == "__main__":
#     # document = """
#     # Dear customer,
#     #
#     # Thank you for contacting our support team. We have received your query and will do our best to assist you.
#     #
#     # If you have forgotten your password, you can reset it by clicking on the 'Forgot Password' link on the login page.
#     #
#     # Our team is available 24/7 to help you with any account-related issues or questions you may have. Feel free to reach out to us anytime.
#     #
#     # Best regards,
#     # Support Team
#     # """
#
document = "NASHIK: Two people were killed in two separate road accidents in the city on Thursday and Friday.As per " \
           "the complaint registered with the police, Deepak Patale and his wife Sangita were travelling on their " \
           "bike near the Old Adgaon Naka towards Nashik city on Thursday night. A speeding car came from a gap in " \
           "one of the road dividers and knocked down their bike.Deepak Patale suffered serious injuries in the " \
           "accident and succumbed to the same. While his wife escaped with serious injuries. In another fatal " \
           "accident, a 29-year-old woman of Phule Nagar, Panchavati was killed in a road accident. The woman, " \
           "identified as Mangal Dheringe, and her husband were travelling in a scooter in the Jail Road area on " \
           "Friday night at around 10.30 pm when speeding truck knocked down the two-wheeler.Mangal " \
           "Dheringe suffered serious injuries in the accident and succumbed to the same."

#     num_clusters = 3
#
#     # Extract sentences from the document
#     sentences = extract_sentences_from_document(document)
#
#     # Cluster the sentences based on intent
#     labels = cluster_sentences(sentences, num_clusters)
#
#     # Print the clustered sentences
#     clusters = {}
#     for i, label in enumerate(labels):
#         if label not in clusters:
#             clusters[label] = []
#         clusters[label].append(sentences[i])
#
#     for cluster_id, sentences in clusters.items():
#         print(f"Cluster {cluster_id + 1}:")
#         for sent in sentences:
#             print(f"  - {sent}")

graph = defaultdict(list)

def detect_accident(sentence, target_noun=None):
    # Load the language model
    nlp = spacy.load('en_core_web_sm')

    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Initialize a list to store adjectives for the target noun
    adjectives = defaultdict(list)
    nouns = defaultdict(list)
    verbs = defaultdict(list)

    # displacy.render(doc, style="ent", jupyter=True)
    # displacy.serve(doc, style="ent", auto_select_port=True)
    # displacy.serve(doc, style="dep", auto_select_port=True)

    tok_l = doc.to_json()['tokens']
    # print("tok_l:", tok_l)

    for t in tok_l:
        head = tok_l[t['head']]

        if (t['dep'] != 'punct') and (t['dep'] != 'ROOT'):
            print(f"'{sentence[t['start']:t['end']]}' is {t['dep']} of '{sentence[head['start']:head['end']]}'")

            graph[sentence[head['start']:head['end']]].append([sentence[t['start']:t['end']], t['dep']]) # u: [v, weight]

    print("graph:", graph)

    # Iterate through each token in the sentence
    for token in doc:
        if token.pos_ == 'ADJ':
            adjectives[token].append(token.head.text)

        if token.pos_ == 'NOUN':
            nouns[token].append(token.head.text)

        if token.pos_ == 'VERB':
            verbs[token].append(token.head.text)

        # print(token.head.text, ":", token, ",", token.pos_)
        # print("tokens from spacy:", token, token.pos_, token.head.text)

        # # Check if the token is an adjective and its head (parent) is the target noun
        # if token.pos_ == 'ADJ' and token.head.text.lower() == target_noun.lower():
        #     # Add the adjective to the list
        #     adjectives.append(token.text)

    displacy.serve(doc, style="dep", auto_select_port=True)

    return True

detect_accident(document)
