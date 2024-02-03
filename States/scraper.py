import os
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import spacy
import re

# driver = webdriver.Chrome('./chromedriver')

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

file_target = "content2.csv"
sno_new = 1

with open(os.path.join(curr_path, file_target), 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['sno', 'content', 'link', 'date'])

injuries_related = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure',
                    'kill', 'wound', 'injury', 'victims']
accident_related = ['accident', 'crash', 'hit', 'smash', 'crush', 'collision', 'accidents', 'mishap', 'explosion',
                    'crashes', 'crashed', 'collapsed', 'wreck', 'knocked']

# with open(os.path.join(curr_path, 'data_cleaner.csv'), mode='r') as file:
# with open(os.path.join(curr_path, 'data.csv'), mode='r') as file:
with open(os.path.join(curr_path, 'content.csv'), mode='r') as file:
    nlp = spacy.load('en_core_web_md')

    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
        # sno, h, sub_h, link = csvFile[i]
        sno, h, link, date = csvFile[i]
        h = h[1:len(h) - 1]
        h = h.split(',')

        for i in range(len(h)):
            h[i] = h[i].strip(" ")
            h[i] = h[i][1:len(h[i]) - 1]

        print(h)

        try:
            # driver.get(link)
            # article = driver.find_elements(By.XPATH, '//div[@class="_s30J clearfix  "]')[0].text
            # date = driver.find_elements(By.XPATH, '//div[@class="xf8Pm byline"]')[0].text[-23:-11]
            #
            # article = remove_extra_spaces(article)
            # prep_dict_t = detect_accident(article)

            prep_list = []

            flag_required = True
            flag_found = False

            for text in h:
                if flag_found is False:
                    # flag_found = False

                    for word in injuries_related:
                        if flag_found is False:
                            if nlp(word).similarity(nlp(str(text.split()[0]))) >= 0.7:
                                flag_found = True

                    for word in accident_related:
                        if flag_found is False:
                            if nlp(word).similarity(nlp(str(text.split()[0]))) >= 0.7:
                                flag_found = True

                prep_list.append(text)

            # for key in prep_dict_t:
            #     if key[1] in place_prep:
            #
            #         # if flag_found is True:
            #         prep_list.append(str(prep_dict_t[key][0][2]) + " " + prep_dict_t[key][1][0])

            if flag_found is True:
                if len(prep_list) != 0:
                    with open(os.path.join(curr_path, file_target), 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow([sno_new, prep_list, link, date])

                    print("data:", sno, prep_list)

                    sno_new += 1

        except Exception as e:
            print("error:", e)

        # time.sleep(2)