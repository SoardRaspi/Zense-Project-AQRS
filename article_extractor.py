from collections import defaultdict
import re

import nltk
import spacy
from spacy import displacy

# graph = {}

article = """Nashik: As many as six people were killed in separate road accidents in rural parts of the district in the
last 48 hours. Out of the deceased was also a 56 year old police officer Rajendra Sansane from Amalner in Jalgaon
district. Sansane was knocked down by an unidentified car near Wadali bhoi on Mumbai Agra highway on Thursday. The
driver escaped without informing anyone.Another 55 year old woman was knocked down on the Mumbai Agra highway near
Igatpuri on Wednesday night. She was crossing the highway near Rathi petrol pump when she met with the accident, said
APSI SK Shinde of Igatpuri police station.A 21 year old man identified as Rahul Dagle from Ambe Bahule died after his
car turned turtle due on the Mumbai Agra highway in Vilholi on Wednesday night. Meanwhile, two motorcyclists Ganesh
Shirsath (21) of Dindori and Sampat Thakre (30) were killed at Vilholi and Chandwad respectively. In the last incident,
Sagar Patil (27) of Talwade, Dhule died after his car rammed into a divider at Lonwade village."""

article = """NAGPUR: An eight-year-old boy was seriously injured when a two-wheeler hit him on Kalamna Market Road on 
Thursday afternoon. Victim Durgesh Kothi, a resident of Vijay Nagar, was on way to his Minimata Nagar School when the 
two-wheeler hit him from behind. The irate driver fled leaving behind injured Durgesh who was rushed to Indira Gandhi 
Government Medical College and Hospital (IGGMCH). Kalamna police have registered a case against the unknown driver."""

article = """KOLHAPUR: Five members of a family were injured when the car they were travelling in lost control and hit 
another vehicle near Karad on the Pune-Bengaluru National Highway on Sunday.According to the police, the family was 
travelling towards Pune and has been shifted to a private hospital in Karad. Those injured have been identified as 
Jayendra Sawant (32), his wife Madhuri (27), parents Ravindra (52) and Sanjana (50), and son Virendra (2). “Jayendra’s 
father and wife are seriously injured,” said an officer.The Sawant family started their journey from Kolhapur on Sunday 
afternoon. After crossing Tarali river bridge near Umbraj, the driver of the car lost control over the vehicle. “The 
vehicle hit the divider and then went to the opposite lane where it rammed into another car. Luckily, the driver of the 
other vehicle sustained minor injuries. Passers-by and labourers working on the repair of the Highway rushed to the spot 
and took the injured to the hospital,” the officer said.“Two persons are seriously injured but are out of danger. Others 
received minor injuries and are safe. We are finding the exact cause of the accident and will take action as per the law 
after finding the cause,” said the investigating officer.With inputs from Ram Jagtap """

article = """Nashik: Two people, including a woman, died in separate road accidents on Wednesday. The city police said
Sushila Malgure (63) was hit by an autorickshaw when she was crossing the road near the Thakkar Bazaar area around 8pm
on Wednesday. “The victim succumbed to the serious injuries she sustained. Her son has registered a complaint against
the autorickshaw driver, who is yet to be nabbed,” the police said. On the same night, 18-year-old Bhavesh Gidani died
due to the serious injuries he had sustained while riding a bike on February 5. “He hit a road divider near ABB circle.
He had been undergoing treatment at a city hospital,” the police said."""

# article = """Hyderabad: One person travelling in a car at Gandimaisamma in Dundigal died in a road accident on Saturday
# night. The car was travelling from Outer Ring Road (ORR) to Gandimaisamma. The car hit the railing and flew, before
# falling in a open land"""

# article = """A 60-year-old Hamid Momin, was killed in a road accident on Majiwada Bridge on Saturday afternoon, while
# she was returning to her home in Bhiwandi after taking treatment at the KEM hospital in Mumbai. The taxi driver lost
# control while negotiating a turn on the Majiwada bridge on the kapurbavdi flyover and the taxi turned turtle after
# hitting one of the barricades leaving Momin severly injured. She was immidetialy rushed to the hospital but was declared
# dead on arrival. Her children Nabila and Shanwaz, who were travelling with her suffered minor injuries. The driver, too,
# was injured and was taken to a hospital. The deceased, had gone to KEM hospital for the weekly dressing of her left limb
# which was amputated."""

# article = 'Survey: 7 in 10 kids in ICUs have traumatic brain injuries,"At least 7 out of'
# article = '19 year old dies 2 days after accident'
# article = 'Two dead, five injured in tractor-car collision on Delhi-Dehradun highway'
# article = 'Government allots Rs 130 crore to strengthen care centres for the purpose of accident & emergency '
# article = 'Rs 130 crore have been alloted by the Government to strengthen care centres for the purpose of accident & emergency '
# article = 'State plans accident insurance cover'
# article = '2 killed as truck rams tree'
# article = 'Woman on morning walk, pillion rider killed in Road accidents'
# article = 'State plans accident insurance cover'



injuries_related = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure',
                    'kill', 'wound', 'injury', 'victims']
accident_related = ['accident', 'crash', 'hit', 'smash', 'crush', 'collision', 'accidents', 'mishap', 'explosion',
                    'crashes', 'crashed', 'collapsed', 'wreck']


def remove_extra_spaces(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    return cleaned_text.strip()

article = remove_extra_spaces(article)

def traverse(graph, head_graph, head, sentence):
    children = []

    def dfs(curr, arr):
        if curr not in children:
            children.append(curr)

        for c in arr:
            dfs(c, head_graph[c])

    dfs(head, head_graph[head])
    children.sort()

    final_string = ""

    for index in children:
        final_string += sentence[graph[index]['start']:graph[index]['end']] + " "

    final_string = final_string[:-1]
    # print("final_string:", final_string)

    return final_string, children[0], children[-1], children

def detect_accident(sentence, target_noun=None):
    nlp = spacy.load('en_core_web_md')
    doc = nlp(sentence)

    tok_l = doc.to_json()['tokens']
    # print("tok_l:", tok_l)

    head_graph = {i: [] for i in range(len(tok_l))}
    prep_graph = {}
    accident_list = []

    for token_info in tok_l:
        word_curr = sentence[token_info['start']:token_info['end']]

        if (token_info['dep'] != 'punct') and (token_info['dep'] != 'ROOT'):
            head_graph[token_info['head']].append(token_info['id'])

        for accident_related_word in accident_related:
            if (nlp(word_curr).similarity(nlp(accident_related_word)) > 0.7) \
                    and ([token_info['id'], word_curr] not in accident_list):
                accident_list.append([token_info['id'], word_curr])

    for token_info in tok_l:
        if (token_info['dep'] == 'prep') or (token_info['dep'] == 'agent'):
            prep_graph[(token_info['id'], sentence[token_info['start']:token_info['end']])] = \
                ([[token_info['head'], tok_l[token_info['head']]['pos'],
                   sentence[tok_l[token_info['head']]['start']:tok_l[token_info['head']]['end']]],
                  list(traverse(tok_l, head_graph, token_info['id'], sentence))])

    print("prep_graph:", prep_graph)
    print("accident_list:", accident_list)

    displacy.serve(doc, style="dep", auto_select_port=True)

    return True

detect_accident(article)