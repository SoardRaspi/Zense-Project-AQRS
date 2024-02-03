import csv
import spacy
import os
import re

from spacy import displacy

curr_path = os.path.join(os.getcwd(), 'Maharashtra')

place_prep = ['in', 'on', 'at', 'by', 'under', 'over', 'beside', 'between', 'among', 'above', 'below', 'behind',
              'in-front-of', 'near']

def remove_extra_spaces(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    return cleaned_text.strip()

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

    for token_info in tok_l:
        word_curr = sentence[token_info['start']:token_info['end']]

        if (token_info['dep'] == 'prep') or (token_info['dep'] == 'agent'):
            prep_graph[(token_info['id'], word_curr)] = \
                [[token_info['head'], tok_l[token_info['head']]['pos'],
                   sentence[tok_l[token_info['head']]['start']:tok_l[token_info['head']]['end']]],
                  list(traverse(tok_l, head_graph, token_info['id'], sentence))]

    # print("prep_graph:", prep_graph)
    # print("accident_list:", accident_list)

    # displacy.serve(doc, style="dep", auto_select_port=True)

    return prep_graph

file_target = "content3.csv"
sno_new = 1

with open(os.path.join(curr_path, file_target), 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['sno', 'content', 'link', 'date'])
#
# injuries_related = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure',
#                     'kill', 'wound', 'injury', 'victims']
# accident_related = ['accident', 'crash', 'hit', 'smash', 'crush', 'collision', 'accidents', 'mishap', 'explosion',
#                     'crashes', 'crashed', 'collapsed', 'wreck', 'knocked']

# with open(os.path.join(curr_path, 'data_cleaner.csv'), mode='r') as file:
# with open(os.path.join(curr_path, 'data.csv'), mode='r') as file:
with open(os.path.join(curr_path, 'content2.csv'), mode='r') as file:
    nlp = spacy.load('en_core_web_md')

    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
        sno, h, link, date = csvFile[i]
        h = h[1:len(h) - 1]
        h = h.split(',')

        try:

            for i in range(len(h)):
                h[i] = h[i].strip(" ")
                # h[i] = h[i][1:len(h[i]) - 1]

            collec_temp = []

            for sentence in h:
                sentence = sentence[1:len(sentence) - 1]
                sentence_temp = sentence.split(" ")

                flag_present = False

                for word in place_prep:
                    if nlp(word).similarity(nlp(sentence_temp[1])) > 0.7:
                        flag_present = True

                if flag_present is True:
                    collec_temp.append(sentence)

            if len(collec_temp) != 0:
                with open(os.path.join(curr_path, file_target), 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([sno_new, collec_temp, link, date])

                sno_new += 1

        except:
            pass