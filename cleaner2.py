import string
import csv
from collections import defaultdict

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import spacy
from spacy import displacy

def detect_accident(sentence, target_noun=None):
    # Load the language model
    nlp = spacy.load('en_core_web_sm')

    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Initialize a list to store adjectives for the target noun
    adjectives = defaultdict(list)
    nouns = defaultdict(list)
    verbs = defaultdict(list)

    tok_l = doc.to_json()['tokens']
    # print("tok_l:", tok_l)

    for t in tok_l:
        head = tok_l[t['head']]

        # if (t['dep'] != 'punct') and (t['dep'] != 'ROOT'):
        #     print(f"'{sentence[t['start']:t['end']]} ({t['pos']})' is {t['dep']} of '{sentence[head['start']:head['end']]} ({t['pos']})'")

        if t['pos'] == 'VERB':
            verbs[sentence[t['start']:t['end']]] = []

            # graph[sentence[head['start']:head['end']]].append([sentence[t['start']:t['end']], t['dep']]) # u: [v, weight]

    # print("graph:", graph)
    # print("verbs:", verbs)

    # for ent in doc.ents:
        # print("ent:", ent, "label:", ent.label_)

    # # Iterate through each token in the sentence
    # for token in doc:
    #     if token.pos_ == 'ADJ':
    #         adjectives[token].append(token.head.text)
    #
    #     if token.pos_ == 'NOUN':
    #         nouns[token].append(token.head.text)
    #
    #     if token.pos_ == 'VERB':
    #         verbs[token].append(token.head.text)
    #
    #     # print(token.head.text, ":", token, ",", token.pos_)
    #     # print("tokens from spacy:", token, token.pos_, token.head.text)
    #
    #     # # Check if the token is an adjective and its head (parent) is the target noun
    #     # if token.pos_ == 'ADJ' and token.head.text.lower() == target_noun.lower():
    #     #     # Add the adjective to the list
    #     #     adjectives.append(token.text)

    # displacy.serve(doc, style="dep", auto_select_port=True)

    return True

article = "Cops rushed 470 Road accident victims to hospitals in PCR vans in 18 months"
article = "74% vehicles using blinding headlights on highways"
article = "At least seven people died in tragic mishaps across the state on Wednesday.Six people died in two separate Road accidents while one, a labourer, died after falling from a construction site."
article = "Indoreans get vital lessons on basic life support to Road accident victims"
# article = "He has a good track record: Bus owner defends driver"
# article = "Speeding bus crushes couple to death"
# article = "Couple was crushed to death by speeding bus"
# article = "One dead, two injured as car hits motorcycle due to fog in Uttar Pradesh's Balrampur"
# article = "One dead, two injured as motorcycle was hit by car due to fog in Uttar Pradesh's Balrampur"
# article = "According to Danapur DRM LM Jha, an irate mob led by RJD MP Ram Kripal Yadav rushed to Sachivalaya halt around 2pm and squatted on railway tracks to protest the death of a youth in Road accident."
# article = "One dead two injured as car hit motorcycle due to fog in Uttar Pradeshs Balrampur"
# article = "One dead, two injured as a motorcycle had been hit by a car and a truck due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "One dead, two injured as a motorcycle was hit by a car due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "One dead, two injured as a motorcycle was strongly hit by a car due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "One dead, two injured as a motorcycle had been strongly and badly but mildly hit by a big blue car due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "One dead, two injured as a motorcycle had been strongly and badly but mildly hit by a big blue car and a very big and red truck due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "One dead, two injured as a motorcycle had been strongly and badly but mildly hit by a big blue car and a very big and red truck due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "One dead, two injured as a small, green and dirty motorcycle had been strongly and badly but mildly hit by a big blue car and a very big and red truck due to fog in Uttar Pradesh's Balrampur" # One dead, two injured as a car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "A motorcycle had been hit by a car due to fog in Uttar Pradesh's Balrampur" # A car hit a motorcycle due to fog in Uttar Pradesh's Balrampur
# article = "The plans were made by our Principal"
# article = "These trees have been planted by me"
# article = "The boy is known to me."
# article = "The table is covered with the dust"
# article = "The car had been damaged by the collision."
# article = "That book was read by Seema"
# article = "The girl enchanted the poet"
# article = "Biker fakes rd accident, extorts Rs 22,000 and gold ring"
# article = "Biker extorts Rs 22,000 and gold ring in fake rd accident"
# article = "Hospital to offer training in first aid"
article = "Road accident deaths dip in April-May than in 2022"
article = "Cops rushed 470 Road accident victims to hospitals in PCR vans in 18 months"
article = "Akola doctors reconstruct 17-yr-old’s broken jaw with multiple fractures"
article = "Part of 100-yr-old building collapses"

def remove_punctuation(sentence):
    translator = str.maketrans('', '', string.punctuation)  # Create a translation table for punctuation removal
    clean_sentence = sentence.translate(translator)  # Apply the translation to remove punctuation
    return clean_sentence

# article = remove_punctuation(article)

# detect_accident(article)

def sentiment(text):
    # Process text with spaCy
    nlp = spacy.load('en_core_web_md')
    doc = nlp(text)
    sid = SentimentIntensityAnalyzer()

    # Get the sentiment scores using VADER
    sentiment_scores = sid.polarity_scores(text)

    # Determine sentiment label based on compound score
    sentiment_label = "positive" if sentiment_scores['compound'] > 0.2 else "negative" if sentiment_scores[
                                                                                            'compound'] < -0.2 else "neutral"

    # return sentiment_label, sentiment_scores
    if sentiment_label == "negative":
        return True

    else:
        return False

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

def change_voice(sentence):
    nlp = spacy.load('en_core_web_sm')

    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Initialize a list to store adjectives for the target noun
    adjectives = defaultdict(list)
    nouns = defaultdict(list)
    verbs_temp = defaultdict(dict)
    verbs = defaultdict(dict)

    # print("doc.to_json() :-:", doc.to_json())

    tok_l = doc.to_json()['tokens']
    # print("tok_l:", tok_l)

    graph = defaultdict(list)
    head_graph = {i: [] for i in range(len(tok_l))}
    # child_graph = {i: [] for i in range(len(tok_l))}

    # for token in doc:
    #     print("token is", token, " : ", token.ent_type_)

    time_prep = []
    place_prep = []
    directional_prep = []
    cause_or_reason_prep = []

    index_t = 0
    for t in tok_l:
        head = tok_l[t['head']]

        if (t['dep'] != 'punct') and (t['dep'] != 'ROOT'):
            head_graph[t['head']].append(t['id'])
            # child_graph[t['id']].append(t['head'])

            graph[sentence[head['start']:head['end']]].append([t['dep'], sentence[t['start']:t['end']], index_t])
        #     print(
        #         f"'{sentence[t['start']:t['end']]} ({t['pos']})' is {t['dep']} of '{sentence[head['start']:head['end']]} ({t['pos']})'")

        if t['pos'] == 'VERB':
            verbs_temp[t['id']] = {}

        index_t += 1

    # print('verbs:', verbs)
    # print('graph:', graph)
    # print('head_graph:', head_graph)
    # print('child_graph:', child_graph)

    flag_passive = False
    verb_passive = False

    agent_s, agent_e = None, None
    advmod_s, advmod_e = None, None
    target_s, target_e = None, None

    for verb_index in verbs_temp:
        verb = sentence[tok_l[int(verb_index)]['start']:tok_l[int(verb_index)]['end']]

        connected = graph[verb]

        verb = verb_index
        verbs[verb]['aux'] = None
        verbs[verb]['advmod'] = []
        verbs[verb]['prep'] = []
        verbs[verb]['dobj'] = []

        aux_index = None

        for type, token, index_token in connected:
            if (type == 'auxpass') or (type == 'aux'):
                flag_passive = True
                verb_passive = verb

                if verbs[verb]['aux'] == None:
                    verbs[verb]['aux'] = token

                else:
                    verbs[verb]['aux'] += " " + token

                if aux_index == None:
                    aux_index = index_token

                elif index_token < aux_index:
                    aux_index = index_token

            if type == 'agent':
                verbs[verb]['agent'], agent_s, agent_e, _ = traverse(tok_l, head_graph, head=index_token, sentence=sentence)

            if type == 'advmod':
                # verbs[verb]['advmod'].append(token)
                verbs[verb]['advmod'], advmod_s, advmod_e, _ = traverse(tok_l, head_graph, head=index_token, sentence=sentence)

            if type == 'prep':
                verbs[verb]['prep'].append(
                    {(sentence[tok_l[index_token]['start']:tok_l[index_token]['end']], index_token):
                         traverse(tok_l, head_graph, head=index_token, sentence=sentence)})

            if type == 'dobj':
                verbs[verb]['dobj'].append(
                    {(sentence[tok_l[index_token]['start']:tok_l[index_token]['end']], index_token):
                         traverse(tok_l, head_graph, head=index_token, sentence=sentence)})

        # ðððððððððððððððððððððððððððððððððððððððð
        # verbs[verb]['target'] = None
        #
        # if verbs[verb]['aux'] != None:
        #     # return "The sentence is in passive voice"
        #
        #     target_index = 0
        #     target_counter = 0
        #
        #     while target_counter < aux_index:
        #         if tok_l[target_counter]['pos'] == 'NOUN':
        #             target_index = target_counter
        #
        #         target_counter += 1
        #
        #     verbs[verb]['target'], target_s, target_e = traverse(tok_l, head_graph, head=target_index, sentence=sentence)
        # ðððððððððððððððððððððððððððððððððððððððð

    # return "The sentence is in active voice"
    # print("verbs new", verbs)

    # displacy.serve(doc, style="dep", auto_select_port=True)

    # if flag_passive:
    #     final_sentence = ""
    #     for i in range(target_s):
    #         final_sentence += sentence[tok_l[i]['start']:tok_l[i]['end']] + " "
    #
    #     agent_spot = verbs[verb_passive]['agent']
    #     final_sentence += (agent_spot if 'by' not in agent_spot else agent_spot[3:]) + " "
    #
    #     final_sentence += verb_passive + " " + verbs[verb_passive]['target'] + " "
    #
    #     for i in range(agent_e + 1, len(tok_l)):
    #         final_sentence += sentence[tok_l[i]['start']:tok_l[i]['end']] + " "
    #
    #     final_sentence = final_sentence[:-1]
    #
    #     return final_sentence
    #
    # else:
    #     return sentence

    return verbs

# print("voice changed:", change_voice("The city police said Sushila Malgure (63) was hit by an autorickshaw when she was crossing the road near the Thakkar Bazaar area around 8pm on Wednesday."))

# verbs_new = change_voice(article)
# print(verbs_new)

injuries_related = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure',
                    'kill', 'wound', 'injury', 'victims']
accident_related = ['accident', 'crash', 'hit', 'smash', 'crush', 'collision', 'accidents', 'mishap', 'explosion',
                    'crashes', 'crashed', 'collapsed', 'wreck', 'knocked']
negating = ['dishonest', 'dull', 'miserable', 'wispy', 'depressed', 'counteract', 'blind', 'black', 'dribble',
            'deceptive', 'overleap', 'undermine', 'deceitful', 'unload', 'dumb', 'gloomy', 'broken', 'underhanded',
            'fraudulent', 'thin', 'lower', 'incorrect', 'dampen', 'damp', 'lowly', 'false', 'mute', 'blue', 'trim',
            'compact', 'condense', 'phony', 'bleak', 'counterfeit', 'vague', 'low', 'inaccurate', 'lour', 'neglect',
            'small', 'exhaust', 'improper', 'slow', 'decrement', 'foreshorten', 'unethical', 'grim', 'deaden',
            'erroneous', 'unsubstantiated', 'humble', 'bogus', 'modest', 'untrue', 'dense', 'funk', 'dispirited',
            'baseless', 'abbreviate', 'narrow', 'dip', 'drop', 'diminution', 'diminish', 'subjugate', 'abridge',
            'shrink', 'shorten', 'subside', 'fall', 'belittle', 'decrease', 'downplay', 'derogate', 'denigrate',
            'minimise', 'wither', 'shrivel', 'curb']

def get_WOI(sentence):
    if sentiment(sentence):
        verbs_new = change_voice(sentence)
        print("verbs_new:", verbs_new)

        WOI = defaultdict(list)
        nlp = spacy.load('en_core_web_md')

        doc = nlp(sentence)
        tok_l = doc.to_json()['tokens']

        flag_present = False

        head_graph = {i: [] for i in range(len(tok_l))}

        for token_info in tok_l:
            word_curr = sentence[token_info['start']:token_info['end']]

            if (token_info['dep'] != 'punct') and (token_info['dep'] != 'ROOT'):
                head_graph[token_info['head']].append(token_info['id'])

            flag_found = False
            for wi in injuries_related:
                if flag_found == False:
                    if nlp(word_curr).similarity(nlp(wi)) > 0.7:
                        flag_found = True
                        flag_present = True

                        WOI[0].append([word_curr, token_info['id']])

            for wa in accident_related:
                if flag_found == False:
                    if nlp(word_curr).similarity(nlp(wa)) > 0.7:
                        flag_found = True
                        flag_present = True

                        WOI[1].append([word_curr, token_info['id']])

            for wn in negating:
                if flag_found == False:
                    if nlp(word_curr).similarity(nlp(wn)) > 0.7:
                        flag_found = True
                        flag_present = True

                        WOI[2].append([word_curr, token_info['id']])

        # print("WOI:", WOI)

        if flag_present == False:
            return False

        else:
            if len(WOI) == 0:
                return False
            else:
                list_0 = [i for k, i in WOI[0]]
                list_1 = [i for k, i in WOI[1]]
                list_2 = WOI[2]

                flag_ok = True

                time_preps = ['at', 'by', 'in', 'on', 'to', 'over', 'past', 'within']

                for token_verb in verbs_new:
                    dobj_dict_L = verbs_new[token_verb]['dobj'] if len(verbs_new[token_verb]['dobj']) != 0 else None
                    prep_dict_L = verbs_new[token_verb]['prep'] if len(verbs_new[token_verb]['prep']) != 0 else None
                    advmod_dict_L = verbs_new[token_verb]['advmod'] if len(verbs_new[token_verb]['advmod']) != 0 else None

                    if dobj_dict_L:
                        for dobj_dict in dobj_dict_L:
                            for key in dobj_dict:
                                for key_inner in dobj_dict[key][3]:
                                    if (key_inner in list_1) or (key_inner in list_0):
                                        if prep_dict_L:
                                            for prep_dict in prep_dict_L:
                                                for key_prep in prep_dict:
                                                    # print("key_prep in prep_dict ::", key_prep)
                                                    if key_prep[0] in time_preps:
                                                        temp_tok_l = nlp(prep_dict[key_prep][0]).to_json()['tokens']
                                                        temp_preps = []

                                                        for temp_t in temp_tok_l:
                                                            if temp_t['pos'] == 'ADP':
                                                                temp_preps.append(temp_t['id'])

                                                        temp_pobjs = {}

                                                        for temp_t in temp_tok_l:
                                                            if temp_t['head'] in temp_preps:
                                                                temp_pobjs[temp_t['head']] = temp_t['id']

                                                        for key_prep in temp_pobjs:
                                                            curr_pobj = sentence[temp_tok_l[temp_pobjs[key_prep]]['start']
                                                                                 :temp_tok_l[temp_pobjs[key_prep]]['end']]

                                                            if (nlp(curr_pobj).similarity(nlp('seconds')) > 0.7) or \
                                                                    (nlp(curr_pobj).similarity(nlp('minutes')) > 0.7) or \
                                                                    (nlp(curr_pobj).similarity(nlp('hours')) > 0.7):
                                                                flag_ok = True

                                                            else:
                                                                if nlp(curr_pobj).similarity(nlp('days')) > 0.7:
                                                                    flag_ok = False
                                                                    # temp_data = traverse(temp_tok_l, head_graph, temp_pobjs[key_prep], prep_dict[key_prep][0])[0]
                                                                    #
                                                                    # if curr_pobj in temp_data:
                                                                    #     words = temp_data.split()
                                                                    #     words_without_word = [word for word in words if
                                                                    #                           word != curr_pobj]
                                                                    #     temp_data = ' '.join(words_without_word)

                                                                else:
                                                                    flag_ok = False

                if flag_ok == False:
                    return False

                else:
                    pass

                if 2 not in WOI:
                    return True

                else:
                    # print("WOI later inner:", WOI)

                    if (1 in WOI) and (len(WOI[1]) != 0):
                        list_1 = [i for k, i in WOI[1]]
                        list_2 = WOI[2]

                        # print("list_1:", list_1)
                        # print("list_2:", list_2)

                        for key, token_index in list_2:
                            if token_index in verbs_new:
                                dobj_dict = verbs_new[token_index]['dobj'][0] if len(verbs_new[token_index]['dobj']) != 0 else None
                                prep_dict = verbs_new[token_index]['prep'][0] if len(verbs_new[token_index]['prep']) != 0 else None
                                advmod_dict = verbs_new[token_index]['advmod'][0] if len(verbs_new[token_index]['advmod']) != 0 else None

                                if dobj_dict:
                                    for key_dobj, index_dobj in dobj_dict:
                                        if index_dobj in list_1:
                                            return False

                                if prep_dict:
                                    for key_dobj, index_dobj in prep_dict:
                                        if index_dobj in list_1:
                                            return False

                                if advmod_dict:
                                    for key_dobj, index_dobj in advmod_dict:
                                        if index_dobj in list_1:
                                            return False

                            else:
                                for id in list_1:
                                    if id in traverse(tok_l, head_graph, token_index, sentence)[3]:
                                        return False

                        return True

                    else:
                        return False

    else:
        return False


# print("result from get_WOI ::-::", get_WOI(article))

# import nltk
# import spacy
# from nltk.corpus import wordnet
#
# import ssl
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# # Download WordNet data (only need to do this once)
# nltk.download('wordnet')
#
# negating = ['fake', 'false', 'deceptive', 'fraudulent', 'misleading', 'dishonest', 'untrue', 'phony', 'counterfeit',
#             'bogus', 'stolen', 'statements', 'unethical', 'underhanded', 'fraud', 'improper', 'inaccurate', 'incorrect',
#             'erroneous', 'deceitful', 'baseless', 'unfounded', 'groundless', 'unsubstantiated', 'reduce', 'decrease',
#             'diminish', 'lower', 'minimize', 'shrink', 'lessen', 'curtail', 'dwindle', 'subside', 'drop', 'abate',
#             'deplete', 'dim', 'taper', 'weaken', 'contract', 'mitigate', 'shrinkage', 'dampen', 'fall', 'de-escalate',
#             'faint', 'dumb', 'point', 'cut_back', 'use_up', 'blur', 'fell', 'downcast', 'driblet', 'frown', 'tighten',
#             'dilute', 'modest', 'let_up', 'cliff', 'dimmed', 'slenderize', 'tone_down', 'lower_berth', 'let_down',
#             'mute', 'dismiss', 'drop_down', 'sign_up', 'funk', 'deoxidize', 'pearl', 'shrivel_up', 'drib', 'eat',
#             'deoxidise', 'throw', 'lowly', 'die_away', 'downhearted', 'consume', 'grim', 'scummy', 'wick', 'palliate',
#             'countermine', 'drop_off', 'downplay', 'blue', 'drop_curtain', 'squeeze', 'send_away', 'low-pitched',
#             'foreshorten', 'black', 'abridge', 'broken', 'sign_on', 'clip', 'take_down', 'unload', 'down',
#             'dwindle_down', 'overleap', 'slur', 'step-down', 'decoct', 'counteract', 'contract_bridge', 'dispirited',
#             'strike_down', 'curb', 'settle', 'set_down', 'trim_back', 'miss', 'wispy', 'low', 'low-down', 'small',
#             'recoil', 'run_through', 'discharge', 'cut_short', 'minify', 'thin', 'drip', 'quash', 'squinch', 'depress',
#             'cut_down', 'quail', 'flatten', 'scurvy', 'deaden', 'belittle', 'sharpen', 'cut', 'drop_cloth', 'bleak',
#             'crushed', 'concentrate', 'devolve', 'humbled', 'damp', 'wax_light', 'throw_away', 'press', 'narrow',
#             'dangle', 'shrivel', 'melt_off', 'trim', 'spend', 'throw_off', 'humiliated', 'depleted', 'denigrate',
#             'wince', 'candle', 'understate', 'low-spirited', 'cringe', 'shorten', 'cast_off', 'sign', 'expend',
#             'dribble', 'dwindle_away', 'extenuate', 'eat_up', 'compress', 'come_down', 'neglect', 'take', 'cast',
#             'sabotage', 'depressed', 'condense', 'wash', 'overlook', 'subvert', 'free_fall', 'drop-off', 'low-toned',
#             'lose_weight', 'blind', 'shoplifting', 'miserable', 'dull', 'bead', 'send_packing', 'muffle', 'diminution',
#             'deteriorate', 'constrict', 'dense', 'abbreviate', 'sink', 'shadowy', 'dip', 'flinch', 'undertake',
#             'obtuse', 'shake_off', 'compact', 'knock_off', 'leave_out', 'keep_down', 'psychiatrist', 'declaration',
#             'glower', 'restrict', 'step_down', 'trim_down', 'decrement', 'vague', 'minimise', 'exhaust', 'slake',
#             'subjugate', 'omit', 'shed', 'subdue', 'pretermit', 'degenerate', 'subdued', 'slow', 'soften', 'thin_out',
#             'humble', 'wither', 'get', 'slim', 'boil_down', 'break', 'gloomy', 'undermine', 'abject', 'shrinking',
#             'lessening', 'lour', 'head-shrinker', 'put_down', 'scale_down', 'slack', 'slack_off', 'get_down',
#             'bring_down', 'wipe_out', 'derogate', 'swing', 'repress', 'moisten', 'turn_down', 'down_in_the_mouth',
#             'reduction', 'stifle', 'slim_down']
#
# def find_similar_words(word):
#     similar_words = set()
#     nlp = spacy.load('en_core_web_sm')
#
#     token1 = nlp(word)
#
#     # Get the synsets (sets of synonymous words) for the word
#     synsets = wordnet.synsets(word)
#
#     # Extract the lemmas (word forms) from the synsets
#     for synset in synsets:
#         for lemma in synset.lemmas():
#             if token1.similarity(nlp(lemma.name().lower())) > 0.6:
#                 similar_words.add(lemma.name().lower())
#
#     # Remove the input word from the set of similar words
#     similar_words.discard(word.lower())
#
#     return list(similar_words)
#
# # Test the function with a sample word
# word = "taper"
# similar_words = find_similar_words(word)
# print(f"Words similar to '{word}':")
# print(similar_words)

import os

curr_path = os.path.join(os.getcwd(), 'States/Maharashtra')

file_target = "data_cleaner2.csv"
sno_new = 1

with open(os.path.join(curr_path, file_target), 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['sno', 'h', 'sub_h', 'link'])

with open(os.path.join(curr_path, 'data_cleaner.csv'), mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
        sno, h, sub_h, link = csvFile[i]
        try:
            if get_WOI(h):
                print(sno, ":", h)

                with open(os.path.join(curr_path, file_target), 'a') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([sno_new, h, sub_h, link])

                sno_new += 1

            elif len(sub_h) != 0:
                if get_WOI(sub_h):
                    print(sno, ":", sub_h)

                    with open(os.path.join(curr_path, file_target), 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow([sno_new, h, sub_h, link])

                    sno_new += 1

        except:
            pass