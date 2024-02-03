import csv
import ssl
from collections import defaultdict
import re
import string

import nltk
from nltk.corpus import wordnet

import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator

import gensim.downloader as api

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('wordnet')




# ###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# # words = ['accident', 'crash', 'dead', 'injured
# # words = ['fake', 'false', 'deceptive', 'fraudulent', 'misleading', 'dishonest', 'untrue
# # words = ['severe', 'serious', 'extreme', 'very', 'much', 'absolutely
# # words = ['Abysmal', 'Atrocious', 'Catastrophic', 'Detestable', 'Diabolical', 'Disastrous', 'Dreadful', 'Horrendous
# #          'Inhumane', 'Monstrous', 'Repulsive', 'Terrible', 'Ghastly', 'Hideous', 'Nauseating', 'Appalling', 'Deplorable
# #          'Ghastly', 'Malevolent', 'Revolting', 'Vile', 'Gruesome', 'Loathsome', 'Odious', 'Repugnant', 'Sinister
# #          'Abominable', 'Grotesque', 'Maleficent', 'Wretched
#
# words = ['Reduce', 'Decrease', 'Diminish', 'Lower', 'Minimize', 'Shrink', 'Lessen', 'Curtail', 'Dwindle',
#          'Subside', 'Drop', 'Abate', 'Deplete', 'Dim', 'Taper', 'Weaken', 'Contract', 'Mitigate','Shrinkage', 'Dampen']
#
# for i in range(len(words)):
#     words[i] = words[i].lower()
#
#
# # def get_similar_words(word, topn=5):
# #     model = api.load('glove-wiki-gigaword-100')
# #
# #     word = word.lower()
# #     if word not in model.key_to_index:
# #         return f"'{word}' not found in vocabulary."
# #
# #     similar_words = model.most_similar(word, topn=topn)
# #
# #     return similar_words
#
# def get_similar_words(word_list):
#     similar_words = set()
#
#     for word in word_list:
#         # Get the synsets (sets of synonymous words) for the word
#         synsets = wordnet.synsets(word)
#
#         # Extract the lemmas (word forms) from the synsets
#         for synset in synsets:
#             for lemma in synset.lemmas():
#                 similar_words.add(lemma.name().lower())
#
#     # Remove the input words from the set of similar words
#     # similar_words = similar_words.difference(set(word_list))
#
#     return list(similar_words)
#
# collection = get_similar_words(words)
#
# print(collection)
#
# # for word in words:
# #     temp = get_similar_words(word)
# #
# #     print(word, ":", temp)
# #     for item in temp:
# #         collection.append(item)
#
# # collection = [('crash', 0.8691697716712952), ('collision', 0.7586742639541626), ('accidents', 0.7397392392158508), ('mishap', 0.7298562526702881), ('explosion', 0.7170404195785522), ('accident', 0.8691698908805847), ('crashes', 0.8019005656242371), ('crashed', 0.797896683216095), ('plane', 0.7928350567817688), ('collision', 0.7619645595550537), ('killed', 0.8328227996826172), ('wounded', 0.7806065082550049), ('missing', 0.7498632669448853), ('people', 0.7165956497192383), ('killing', 0.7130988240242004), ('wounded', 0.8145446181297302), ('injuries', 0.7908446192741394), ('injuring', 0.7419465780258179), ('killed', 0.7374254465103149), ('missing', 0.7341991066932678)]
# # collection = [('dismal', 0.7021490335464478), ('pitiful', 0.6794857382774353), ('appalling', 0.6650002002716064), ('woeful', 0.6390253305435181), ('wretched', 0.6369414329528809), ('horrendous', 0.8207855820655823), ('appalling', 0.8047066926956177), ('heinous', 0.7703807950019836), ('barbaric', 0.7593481540679932), ('abominable', 0.7537192106246948), ('devastating', 0.7599287629127502), ('catastrophe', 0.758402407169342), ('disasters', 0.7283392548561096), ('consequences', 0.7262347340583801), ('disastrous', 0.7248150110244751), ('despicable', 0.7069792151451111), ('contemptible', 0.6959795355796814), ('barbarous', 0.6853452324867249), ('dastardly', 0.6840395331382751), ('odious', 0.6742027997970581), ('devilish', 0.7467020750045776), ('devious', 0.7046182751655579), ('loathsome', 0.6770960688591003), ('hideous', 0.6693168878555298), ('nefarious', 0.6655669212341309),
# #               ('devastating', 0.7614336013793945), ('catastrophic', 0.7248149514198303), ('calamitous', 0.7024896144866943), ('worst', 0.6832916736602783), ('embarrassing', 0.6538358926773071), ('horrendous', 0.8427257537841797), ('awful', 0.8266333937644958), ('horrible', 0.8184823393821716), ('terrible', 0.7821512818336487), ('miserable', 0.7573230266571045), ('dreadful', 0.8427258133888245), ('horrible', 0.8366580605506897), ('atrocious', 0.8207854628562927), ('horrific', 0.8163007497787476), ('appalling', 0.8141598701477051), ('inhuman', 0.9003269076347351), ('cruel', 0.7974693775177002), ('degrading', 0.7821835279464722), ('barbaric', 0.7472432255744934), ('abhorrent', 0.7137900590896606), ('hideous', 0.7046189904212952), ('compendium', 0.6944820880889893), ('grotesque', 0.6208910942077637), ('ghastly', 0.6080833673477173), ('bestial', 0.6033137440681458),
# #               ('repugnant', 0.6511688828468323), ('insidious', 0.6419889330863953), ('distasteful', 0.6393688321113586), ('perverse', 0.6231616735458374), ('contemptible', 0.6211313605308533), ('horrible', 0.919477105140686), ('awful', 0.8742169737815857), ('dreadful', 0.7821513414382935), ('horrendous', 0.7782431244850159), ('horrific', 0.7643980383872986), ('horrifying', 0.8531714081764221), ('hideous', 0.8455531001091003), ('frightful', 0.7681063413619995), ('horrendous', 0.7471814155578613), ('ghoulish', 0.745873212814331), ('ghastly', 0.8455531597137451), ('grotesque', 0.7686301469802856), ('horrifying', 0.7361433506011963), ('monstrous', 0.7046191692352295), ('horrendous', 0.7020121216773987), ('loathsome', 0.7054650187492371), ('disgusting', 0.6925992965698242), ('disagreeable', 0.6867343187332153), ('distasteful', 0.6788433194160461), ('mystifying', 0.6735106706619263),
# #               ('deplorable', 0.856151282787323), ('horrendous', 0.8141599297523499), ('atrocious', 0.8047066926956177), ('disgraceful', 0.7716572284698486), ('horrible', 0.7695969939231873), ('appalling', 0.8561511635780334), ('disgraceful', 0.7925810217857361), ('shameful', 0.7377275824546814), ('atrocious', 0.7371676564216614), ('intolerable', 0.7105647921562195), ('horrifying', 0.8531714081764221), ('hideous', 0.8455531001091003), ('frightful', 0.7681063413619995), ('horrendous', 0.7471814155578613), ('ghoulish', 0.745873212814331), ('demonic', 0.7917079925537109), ('vengeful', 0.6787909269332886), ('otherworldly', 0.6707172393798828), ('evil', 0.6604292392730713), ('bloodthirsty', 0.6492200493812561), ('disgusting', 0.7291666269302368), ('idiotic', 0.661882221698761), ('despicable', 0.630320131778717), ('scandalous', 0.6219301819801331), ('contemptible', 0.617954671382904),
# #               ('despicable', 0.7592575550079346), ('disgusting', 0.7272904515266418), ('odious', 0.7242962121963501), ('heinous', 0.7094600796699524), ('hateful', 0.7090508937835693), ('grisly', 0.9464603066444397), ('horrific', 0.8178263306617737), ('horrifying', 0.8006848692893982), ('gory', 0.766309916973114), ('ghastly', 0.7254741191864014), ('contemptible', 0.7297292351722717), ('insufferable', 0.7069882750511169), ('nauseating', 0.7054649591445923), ('odious', 0.6913245916366577), ('moronic', 0.6910874843597412), ('barbarous', 0.7883291244506836), ('despicable', 0.7665467262268066), ('heinous', 0.7649403214454651), ('barbaric', 0.7595533728599548), ('repugnant', 0.7563058137893677), ('abhorrent', 0.8615434169769287), ('reprehensible', 0.8183709979057312), ('contemptible', 0.7687078714370728), ('odious', 0.7563058137893677), ('distasteful', 0.7531260848045349),
# #               ('nefarious', 0.649056613445282), ('malevolent', 0.6432764530181885), ('menacing', 0.6067799925804138), ('mischievous', 0.6009610295295715), ('shadowy', 0.5934808254241943), ('atrocious', 0.7537192106246948), ('odious', 0.7116844654083252), ('despicable', 0.6852530241012573), ('deplorable', 0.6758942008018494), ('appalling', 0.6649933457374573), ('cartoonish', 0.7707896828651428), ('hideous', 0.7686301469802856), ('comical', 0.759257435798645), ('ghastly', 0.7328396439552307), ('macabre', 0.7181857228279114), ('kayako', 0.6580579876899719), ('morgana', 0.6551783084869385), ('circe', 0.6417213082313538), ('jareth', 0.6307083964347839), ('washu', 0.6280132532119751), ('miserable', 0.7988418936729431), ('pitiful', 0.6937676072120667), ('dreadful', 0.6933331489562988), ('dreary', 0.6846813559532166), ('pathetic', 0.6537805795669556)]
# # collection = [('phony', 0.7495619654655457), ('counterfeit', 0.7484325766563416), ('bogus', 0.7069410681724548), ('false', 0.6840496063232422), ('stolen', 0.6270613074302673), ('misleading', 0.7120209336280823), ('bogus', 0.7118173241615295), ('statements', 0.6948114037513733), ('phony', 0.6856657862663269), ('fake', 0.6840495467185974), ('misleading', 0.7764078378677368), ('dishonest', 0.7487349510192871), ('fraudulent', 0.6952210068702698), ('unethical', 0.6940810680389404), ('underhanded', 0.6922080516815186), ('bogus', 0.7759492993354797), ('fraud', 0.726599395275116), ('phony', 0.7097460627555847), ('deceptive', 0.6952210664749146), ('improper', 0.6914173364639282), ('inaccurate', 0.8515494465827942), ('deceptive', 0.7764078378677368), ('incorrect', 0.7267662882804871), ('erroneous', 0.7197355031967163), ('false', 0.7120208144187927),
# #                ('unethical', 0.7503527998924255), ('deceptive', 0.7487349510192871), ('irresponsible', 0.7384441494941711), ('unprofessional', 0.7247706651687622), ('deceitful', 0.7202274203300476), ('baseless', 0.872560977935791), ('unfounded', 0.8371686935424805), ('groundless', 0.8263939023017883), ('unsubstantiated', 0.8065313696861267), ('inaccurate', 0.7488221526145935)]
#
# for a in collection:
#     if a not in words:
#         words.append(a)
#
# print("words:", words)
#############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

words = ['accident', 'crash', 'dead', 'injured', 'collision', 'accidents', 'mishap', 'explosion', 'crashes', 'crashed',
         'plane', 'killed', 'wounded', 'missing', 'people', 'killing', 'injuries', 'injuring', 'injure', 'kill',
         'wound', 'miss', 'injury']
d_and_i = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure', 'kill',
           'wound', 'miss', 'injury']
others = ['accident', 'crash', 'collision', 'accidents', 'mishap', 'explosion', 'crashes', 'crashed', 'plane', 'people']
negating = ['fake', 'false', 'deceptive', 'fraudulent', 'misleading', 'dishonest', 'untrue', 'phony', 'counterfeit',
            'bogus', 'stolen', 'statements', 'unethical', 'underhanded', 'fraud', 'improper', 'inaccurate', 'incorrect',
            'erroneous', 'deceitful', 'baseless', 'unfounded', 'groundless', 'unsubstantiated', 'reduce', 'decrease',
            'diminish', 'lower', 'minimize', 'shrink', 'lessen', 'curtail', 'dwindle', 'subside', 'drop', 'abate',
            'deplete', 'dim', 'taper', 'weaken', 'contract', 'mitigate', 'shrinkage', 'dampen', 'fall', 'de-escalate',
            'faint', 'dumb', 'point', 'cut_back', 'use_up', 'blur', 'fell', 'downcast', 'driblet', 'frown', 'tighten',
            'dilute', 'modest', 'let_up', 'cliff', 'dimmed', 'slenderize', 'tone_down', 'lower_berth', 'let_down',
            'mute', 'dismiss', 'drop_down', 'sign_up', 'funk', 'deoxidize', 'pearl', 'shrivel_up', 'drib', 'eat',
            'deoxidise', 'throw', 'lowly', 'die_away', 'downhearted', 'consume', 'grim', 'scummy', 'wick', 'palliate',
            'countermine', 'drop_off', 'downplay', 'blue', 'drop_curtain', 'squeeze', 'send_away', 'low-pitched',
            'foreshorten', 'black', 'abridge', 'broken', 'sign_on', 'clip', 'take_down', 'unload', 'down',
            'dwindle_down', 'overleap', 'slur', 'step-down', 'decoct', 'counteract', 'contract_bridge', 'dispirited',
            'strike_down', 'curb', 'settle', 'set_down', 'trim_back', 'miss', 'wispy', 'low', 'low-down', 'small',
            'recoil', 'run_through', 'discharge', 'cut_short', 'minify', 'thin', 'drip', 'quash', 'squinch', 'depress',
            'cut_down', 'quail', 'flatten', 'scurvy', 'deaden', 'belittle', 'sharpen', 'cut', 'drop_cloth', 'bleak',
            'crushed', 'concentrate', 'devolve', 'humbled', 'damp', 'wax_light', 'throw_away', 'press', 'narrow',
            'dangle', 'shrivel', 'melt_off', 'trim', 'spend', 'throw_off', 'humiliated', 'depleted', 'denigrate',
            'wince', 'candle', 'understate', 'low-spirited', 'cringe', 'shorten', 'cast_off', 'sign', 'expend',
            'dribble', 'dwindle_away', 'extenuate', 'eat_up', 'compress', 'come_down', 'neglect', 'take', 'cast',
            'sabotage', 'depressed', 'condense', 'wash', 'overlook', 'subvert', 'free_fall', 'drop-off', 'low-toned',
            'lose_weight', 'blind', 'shoplifting', 'miserable', 'dull', 'bead', 'send_packing', 'muffle', 'diminution',
            'deteriorate', 'constrict', 'dense', 'abbreviate', 'sink', 'shadowy', 'dip', 'flinch', 'undertake',
            'obtuse', 'shake_off', 'compact', 'knock_off', 'leave_out', 'keep_down', 'psychiatrist', 'declaration',
            'glower', 'restrict', 'step_down', 'trim_down', 'decrement', 'vague', 'minimise', 'exhaust', 'slake',
            'subjugate', 'omit', 'shed', 'subdue', 'pretermit', 'degenerate', 'subdued', 'slow', 'soften', 'thin_out',
            'humble', 'wither', 'get', 'slim', 'boil_down', 'break', 'gloomy', 'undermine', 'abject', 'shrinking',
            'lessening', 'lour', 'head-shrinker', 'put_down', 'scale_down', 'slack', 'slack_off', 'get_down',
            'bring_down', 'wipe_out', 'derogate', 'swing', 'repress', 'moisten', 'turn_down', 'down_in_the_mouth',
            'reduction', 'stifle', 'slim_down']
# enhancing = ['abysmal', 'atrocious', 'catastrophic', 'detestable', 'diabolical', 'disastrous', 'dreadful', 'horrendous',
#              'inhumane', 'monstrous', 'repulsive', 'terrible', 'ghastly', 'hideous', 'nauseating', 'appalling',
#              'deplorable', 'ghastly', 'malevolent', 'revolting', 'vile', 'gruesome', 'loathsome', 'odious', 'repugnant',
#              'sinister', 'abominable', 'grotesque', 'maleficent', 'wretched', 'dismal', 'pitiful', 'woeful', 'heinous',
#              'barbaric', 'devastating', 'catastrophe', 'disasters', 'consequences', 'despicable', 'contemptible',
#              'barbarous', 'dastardly', 'devilish', 'devious', 'nefarious', 'calamitous', 'worst', 'embarrassing',
#              'awful', 'horrible', 'miserable', 'horrific', 'inhuman', 'cruel', 'degrading', 'abhorrent', 'compendium',
#              'bestial', 'insidious', 'distasteful', 'perverse', 'horrifying', 'frightful', 'ghoulish', 'disgusting',
#              'disagreeable', 'mystifying', 'disgraceful', 'shameful', 'intolerable', 'demonic', 'vengeful',
#              'otherworldly', 'evil', 'bloodthirsty', 'idiotic', 'scandalous', 'hateful', 'grisly', 'gory',
#              'insufferable', 'moronic', 'reprehensible', 'menacing', 'mischievous', 'shadowy', 'cartoonish', 'comical',
#              'macabre', 'kayako', 'morgana', 'circe', 'jareth', 'washu', 'dreary', 'pathetic']

# def find_adjectives_for_noun(sentence, target_noun):

# words_temp = []
#
# for word in negating:
#     nlp = spacy.load('en_core_web_sm')
#     doc = nlp(word)
#
#     for token in doc:
#         # print(word, ":", token, "&", token.lemma_)
#
#         if token.lemma_ not in words_temp:
#             words_temp.append(token.lemma_)
#
# print("words_temp:", words_temp)

def detect_accident(sentence, target_noun=None):
    # Load the language model
    nlp = spacy.load('en_core_web_sm')

    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Initialize a list to store adjectives for the target noun
    adjectives = defaultdict(list)
    nouns = defaultdict(list)
    verbs = defaultdict(list)

    # Iterate through each token in the sentence
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
    #     #
    #     # # Check if the token is an adjective and its head (parent) is the target noun
    #     # if token.pos_ == 'ADJ' and token.head.text.lower() == target_noun.lower():
    #     #     # Add the adjective to the list
    #     #     adjectives.append(token.text)

    temp = []
    temp_d_and_i = []
    temp_o = []

    chars = re.escape(string.punctuation)
    sentence = re.sub('['+chars+']', ' ',sentence)

    s = sentence.split()

    # for i in range(len(s)):
    #     chars = re.escape(string.punctuation)

    # print("s:", s)

    for word in s:
        if word in words:
            temp.append(word)

        if word in d_and_i:
            temp_d_and_i.append(word)

        if word in others:
            temp_o.append(word)

    # print("temp:", temp)

    t = defaultdict(list)

    dead_and_injured = defaultdict(list)
    otherwise = defaultdict(list)

    for token in doc:
        if token.text in temp_d_and_i:
            # print("token:", token.text)

            if token.head.text:
                dead_and_injured[token.lemma_].append(token.head.lemma_)
                dead_and_injured[token.head.lemma_].append(token.lemma_)

        if token.text in temp_o:
            # print("token:", token.text)

            if token.head.text:
                otherwise[token.lemma_].append(token.head.lemma_)
                otherwise[token.head.lemma_].append(token.lemma_)

    # print("adjectives:", adjectives)
    # print("nouns:", nouns)
    # print("verbs:", verbs)

    # print("t:", t)

    count = 0
    neg = 0

    for key in dead_and_injured:
        val = dead_and_injured[key][0]
        # print("val:", val)

        if val in negating:
            neg -= 1

        count -= 1

    # print("count, neg:", count, neg)

    if neg != 0:
        count *= neg

    if count < 0:
        return True

    else:
        count = 0
        neg = 0

        for key in otherwise:
            val = otherwise[key][0]
            # print("val:", val)

            if val in negating:
                neg -= 1

            count -= 1

        if neg != 0:
            count *= neg

        if count < 0:
            return True

        else:
            return False


# # # Test the function
# # sentence = "The big brown dog is playing in the garden."
# # target_noun = "dog"
# # adjectives_for_noun = find_adjectives_for_noun(sentence, target_noun)
# # print(f"Adjectives for '{target_noun}': {adjectives_for_noun}")
#
#
# def identify_linked_words(sentence):
#     # Load the language model
#     nlp = spacy.load('en_core_web_sm')
#
#     # Process the sentence with spaCy
#     doc = nlp(sentence)
#
#     # Initialize a list to store linked words
#     linked_words = []
#
#     # Iterate through each token in the sentence
#     for token in doc:
#         print("tokens from spacy:", token)
#
#         # Check if the token has a head (parent) and the dependency label is not a punctuation or space
#         if token.head is not token and not token.is_punct and not token.is_space:
#             # Add the linked word and its head to the list
#             linked_words.append((token.text, token.head.text))
#
#     return linked_words
#
#
# # # Test the function
# # sentence = "The quick brown fox jumps over the lazy dog."
# # linked_words = identify_linked_words(sentence)
# # print(linked_words)
#
# import ssl
#
# def detect_accident(text):
#     # text = "Biker fakes rd accident, extorts Rs 22,000 and gold ring"
#
#     tokens = nltk.word_tokenize(text)
#     print("text:", text)
#     # print("tokens:", tokens)
#
#     tagged = nltk.pos_tag(tokens)
#     print("tagged:", tagged)
#
#     NN_list = []
#     VB_list = []
#     CD_list = []
#
#     for word, tag in tagged:
#         if (tag == 'NN') or (tag == 'NNS'):
#             NN_list.append(word)
#
#         if tag[0:2] == 'VB':
#             VB_list.append(word)
#
#         if tag == 'CD':
#             CD_list.append(word)
#
#     print("NN_list:", NN_list)
#     print("VB_list:", VB_list)
#     print("CD_list:", CD_list)
#     print("links:", identify_linked_words(text))
#
#     print("------------------------------")
#
#     return True
#
#
# #
# # nltk.download('vader_lexicon')
# #
# # from nltk.sentiment.vader import SentimentIntensityAnalyzer

filename = "data_cleaner2.csv"

# fields = ['sno', 'heading', 'sub-heading', 'link']
sno = 4992

rows = []

# with open(filename, 'a') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)

H = []

with open('data2.csv', mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    # while sno < 25:
    for i in range(1, len(csvFile)):
        _, h, sub_h, link = csvFile[i]
        # if (h not in H) and (link[36:40] == 'city'):
        if detect_accident(h):
            print(sno, h)
            # H.append(h)

            with open(filename, 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([sno, h, sub_h, link])

            sno += 1

# from nltk.corpus import wordnet
#
# synonyms = []
#
# # for syn in wordnet.synsets("road_accident"):
# #     for i in syn.lemmas():
# #         synonyms.append(i.name())
# #
# # for syn in wordnet.synsets("killed"):
# #     for i in syn.lemmas():
# #         synonyms.append(i.name())
# #
# # for syn in wordnet.synsets("dead"):
# #     for i in syn.lemmas():
# #         synonyms.append(i.name())
# #
# # for syn in wordnet.synsets("injured"):
# #     for i in syn.lemmas():
# #         synonyms.append(i.name())
#
# for syn in wordnet.synsets("fake"):
#     for i in syn.lemmas():
#         synonyms.append(i.name())
#
# print(set(synonyms))

# # import nltk
# # from nltk.sentiment.vader import SentimentIntensityAnalyzer
# #
# #
# # def is_negative_word(word):
# #     # Initialize the SentimentIntensityAnalyzer
# #     sia = SentimentIntensityAnalyzer()
# #
# #     # Get the polarity scores of the word
# #     scores = sia.polarity_scores(word)
# #
# #     # Check if the compound score is negative
# #     print("scores:", scores)
# #     return scores['compound'] < 0
# #
# #
# # # Test the function
# # word = "fake"
# # is_negative = is_negative_word(word)
# # print(f"'{word}' is negative: {is_negative}")
#
# # from textblob import TextBlob
# #
# #
# # def analyze_sentiment(sentence):
# #     # Create a TextBlob object for the input sentence
# #     blob = TextBlob(sentence)
# #
# #     # Get the polarity score of the sentence (-1 to +1)
# #     polarity = blob.sentiment.polarity
# #
# #     # Positive sentiment if polarity is greater than 0, negative if polarity is less than 0
# #     if polarity > 0:
# #         sentiment = "positive"
# #     elif polarity < 0:
# #         sentiment = "negative"
# #     else:
# #         sentiment = "neutral"
# #
# #     return sentiment, polarity
# #
# #
# # # Test the function
# # sentence = "Road accident deaths dip in April-May than in 2022"
# # sentiment, polarity = analyze_sentiment(sentence)
# # print(f"Sentiment: {sentiment}, Polarity: {polarity:.2f}")

# ll = find_adjectives_for_noun("2 killed, 3 injured as car crashes into culvert wall in Rajasthan's Alwar", "killed")
# ll = find_adjectives_for_noun("Four of family dead in Bijnor Road accident", "accident")


# ll = find_adjectives_for_noun("Biker fakes rd accident, extorts Rs 22,000 and gold ring", "accident")
# ll = find_adjectives_for_noun("Four of family dead in Bijnor Road accident", "accident")
# ll = find_adjectives_for_noun("Road accident deaths dip in April-May than in 2022", "accident")
# ll = find_adjectives_for_noun("Youth critically injured in Road accident", "accident")
# ll = find_adjectives_for_noun("63-yr-old killed in Road accident", "accident")'

# ll = accident("Biker fakes rd accident, extorts Rs 22,000 and gold ring")