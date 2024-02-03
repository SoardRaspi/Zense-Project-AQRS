import os
import csv
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

import spacy
from spacy import displacy

# text = """Nashik: A motorist died in a road accident when his vehicle was knocked down by a tempo at Mumbai Nashik Hwy on
# Tuesday The victim, Dinkar Tajanpure (63), was riding his motorcycle at Nashik Road on Monday evening when a tempo
# coming from behind allegedly hit him, causing him to fall down. The driver fled the scene.A complaint over causing
# death due to negligent driving was registered with Nashik Road police station “Tajanpure’s condition was critical. He
# received grievous injuries in his head and chest. He succumbed to treatment while being in the hospital,” said an
# officer. The police said that though the motorist has fled the scene along with the vehicle, CCTV footage will help
# track him. “We have various organisations on the road whose CCTV footages are being used to track the details of the
# vehicle and reach the motorist,” the officer said."""
#
# # text = """Nashik: A 41-year-old police naik attached with the Upnagar police station died after suffering serious injuries
# # in a road accident in the Upnagar area on Saturday afternoon.The deceased has been identified as Sachin Vatane, a
# # resident of Dwarka Nagari, Old Saikheda Road, Nashik Road.The Upnagar police said Vatane was riding his bike in the Jail
# # Road area around 4.30pm on Saturday when he fell off the bike and suffered serious injuries. He was immediately shifted
# # to a private hospital where he was declared brought dead. He is survived by his parents, wife, a 14-year-old daughter
# # and a 10-year-old son.Police said Vatane had joined the police force in Mumbai, and after a few years, he got a transfer
# # to Nashik city. Before joining the Upnagar police station, he worked at the police headquarters of the city police and
# # then the Nashik Road police station."""
# #
# # text = """MUMBAI: Akbar Khan (42), who died in a road accident at Girgaum Chowpatty on Wednesday morning after a
# # speeding car driven by a minor rammed his bike, had told his wife he would be home in 10 minutes when she called at 5am.
# # Half an hour later, when she called him again, she was told about the accident. Khan was out on Wednesday midnight to
# # celebrate his 42nd birthday with friends. He had dinner with them and even cut a cake at midnight.  The 17-year-old boy,
# # who was driving his father's car, came from Parel with a friend. Khan and his friend, Kiran (35), were returning around
# # 5.30am from Marine Drive. As Khan was taking a right turn, the boy, who was coming at a high speed, applied brakes.
# # Since it had rained in the night, the car skidded and it rammed the bike. The impact was so high that the victims were
# # flung into the air and fell on the road. While Khan died on the spot, Kiran was admitted to JJ Hospital, where she died
# # on Wednesday evening. The teenaged driver and his friend did not sustain any injury as the airbags opened when their car
# # hit the bike. We have collected his (boy's) blood samples and sent it to the Forensic Science Laboratory at Kalina
# # for examination to find out if he was drunk, an officer said. The police said the boy, who used to go cycling every
# # morning, took the keys of the car while his father was asleep. He left home saying he was going cycling. He along with a
# # friend came to Chowpatty, where the accident took place, said the police. The boy's father, a bank employee, had bought
# # the car from another person last month and the car is yet to be transferred in his name, said an officer. We have
# # submitted a report to the Child Welfare Committee, an officer said.The police booked the minor and his father under
# # Section 304A (causing death by negligence), Section 279 (rash driving or riding on a public way) and Section 338
# # (causing grievous hurt by act endangering life or personal safety of others) of the IPC and invoked Section 181 (driving
# # vehicles in contravention of Section 3 or Section 4) of the Motor Vehicle Act.The police recorded the father's statement
# # and issued him a notice. He reportedly told the police that he had undergone a bypass surgery and that is why he could
# # not transfer the car in his name.Relatives were mourning at Khan's residence near Grant Road. Khan had two sons, 17
# # and 15 years old. The elder one wanted to join the IATA course and his father had assured him that he would make all the
# # arrangements for his fees, Nishat, Khan's sister in-law, said. Khan was in the scrap business. We learnt about
# # the accident only after Khan's wife called him up again around 5.30am. Someone else picked up the call and informed them
# # about the accident. We reached the spot and then went to JJ Hospital. After half an hour, we were told that Khan had
# # passed away, Khan's niece, Tasleem, said. A relative of Kiran's said she worked in a printing company and her daughter
# # had passed Class XII."""
#
# # text = text.lower()
#
# # text = """PUNE: For a city that has a high number of fatalities in road accidents every year, the least that citizens
# # would expect is prompt remedial measures from the civic authorities when they are alerted about accident-prone spots.
# # The traffic branch came up with a comprehensive report on road accidents last year identifying as many as 51 accident-
# # prone spots in the city and neighbouring Pimpri-Chinchwad. However, fresh data showed that the number of fatal accidents
# # have increased at nine places and remedial work at eight of these nine spots has either not begun or is still going on
# # while the number of fatal mishaps at 11 other spots remained unchanged. On the positive side, the number of fatal
# # mishaps at 31 spots has reduced while the number of serious accidents at 31 spots has also fallen. However, at eight
# # spots the number of serious mishaps have increased and at 12 other spots the figure has remained unchanged. The report
# # had statistics about fatal and serious mishaps at these spots in 2007 and 2008. The report, published by police
# # commissioner Satya Pal Singh, had also suggested accident-prevention remedial measures at each spot. These works were to
# # be taken up and completed by the Pune and Pimpri-Chinchwad municipal corporations. A reality check also revealed that
# # work is in progress at 25 junctions, improvement plans have been finalised for a mere three chowks and no work has been
# # done at 15 accident spots and steps to improve traffic has been completed at eight junctions. Of the 15 spots where
# # there is no work done, 12 are in the PMC limits, while three are in the PCMC limits. The PMC is to be largely to be
# # blamed for the slow pace of work. Additional city engineer and traffic planner Shriniwas Bonala cited certain reasons
# # for the delay in work. "Some works require budgetary provisions, and some may have been delayed because of technical
# # reasons. Other works are not related to one particular department in the civic body. The ward offices, JNNURM department
# # , road department are all involved in road improvement works, " he said. Road traffic safety activist Chandmal Parmar
# # said both civic bodies should prioritise the work on the 51 accident spots. "The police should pursue the matter and get
# # the works done. The traffic mobility committee of the PMC has not conducted its meeting for the past two years, while
# # the PCMC held it two months ago. I have written to the two corporations to take necessary accident-prevention measures,"
# # he said. Deputy commissioner of police (traffic) Manoj Patil said that the remedial work has begun at a number of
# # accident-prone spots, and hoped that work will start at spots where nothing has been done. "We are continuously
# # monitoring the works at all these spots," he said. Patil said that while improvement works at some identified junctions
# # has been completed or is in progress, new sites have become accident prone. "The traffic branch will compile a
# # comprehensive list of junctions likely to face traffic congestion in the next three to four years. The list will
# # identify the corridors where the traffic is going to increase," he said. According to Patil, some road stretches like
# # the one between Hinjewadi and Indira Institute at Wakad continues to be accident prone. He also said that the number of
# # accidents in the city was down, but Pune was ahead of Mumbai in fatal accidents. "Mumbai has about 800 fatalities every
# # year while Pune has 450 deaths. But if we consider the number of fatalities per lakh population in the two cities, the
# # number of fatalities in Pune is high," he said."""

curr_path = os.path.join(os.getcwd(), 'Maharashtra')
file_target = 'content3_data.csv'


def traverse(text, head_graph, token_l, curr_id):
    direct_children = []
    overall = []
    children = []
    result = []

    direct_children = head_graph[curr_id]
    list_id = [0]

    def dfs(curr, arr):
        if (curr not in children) and (token_l[curr]['pos'] != 'SPACE'):
            if token_l[curr]['dep'] != 'cc':
                children.append([curr, ent_graph[curr], list_id[0]] if curr in ent_graph else [curr, None, list_id[0]])

        for c in arr:
            # if flag_cc is False:
            if True:
                if ((token_l[c]['dep'] == 'compound') or (token_l[c]['dep'] == 'conj') or
                        (token_l[c]['dep'] == 'appos') or (token_l[c]['dep'] == 'amod')) and \
                        (token_l[c]['pos'] != 'SPACE'):
                    dfs(c, head_graph[c])

            if True:
                # if (token_l[c]['dep'] == 'conj') and (token_l[c]['pos'] != 'SPACE'):
                if (token_l[c]['dep'] == 'cc') and (token_l[c]['pos'] != 'SPACE'):
                    list_id[0] += 1
                    dfs(c, head_graph[c])

    for direct_children_index in direct_children:
        dfs(direct_children_index, head_graph[direct_children_index])
        children.sort()

        result.append(children)

    result_t = []
    for item in result:
        if item not in result_t:
            result_t.append(item)

    result = result_t
    del result_t

    # print(result)

    if len(result) != 0:
        return result[0]

    else:
        return None

# with open(os.path.join(curr_path, file_target), 'a') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(['sno', 'data', 'link', 'date'])

place_prep = ['in', 'on', 'at', 'by', 'under', 'over', 'beside', 'between', 'among', 'above', 'below', 'behind',
              'in-front-of', 'near']
woi_cue = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure', 'kill',
           'wound', 'injury', 'victims',

           'accident', 'crash', 'hit', 'smash', 'crush', 'collision', 'accidents', 'mishap', 'explosion', 'crashes',
           'crashed', 'collapsed', 'wreck', 'knocked',

           'cycling', 'biking', 'driving', 'motorcycling', 'racing', 'gliding', 'riding', 'walking', 'strolling',
           'roaming']
roads = ["road", "highway", "expressway", "street", "lane", "avenue", "boulevard", "marg", "flyover", "walkover",
         "expy", "rd", "galli", "gali", "hwy", "rasta", "maarg", "path"]

def is_road(sentence, nlp):
    for word_sent in sentence:
        for word_road in roads:
            if nlp(word_sent).similarity(nlp(word_road)) > 0.5:
                return True

    return False

def get_coords(sentence):
    q = "https://apihub.latlong.ai/v4/geocode.json?address=" + sentence
    r = requests.get(q, headers={
        'X-Authorization-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUb2tlbklEIjoiY2Q2ZmEzZjQtNjI2NC00Yjc5LWEwMjctOTNkZWUwZjdjMzYxIiwiQ2xpZW50SUQiOiIxNGI0MTVhYS01NjVkLTRjZWEtYjFlNC05ZTJiNTU0NmEzMWYiLCJCdW5pdElEIjoxMDMxNCwiQXBwTmFtZSI6InNvYXJkcihzb2FyZC5yYXNwaUBnbWFpbC5jb20pIC0gU2lnbiBVcCIsIkFwcElEIjoxMDI4MiwiVGltZVN0YW1wIjoiMjAyMy0wOC0xNiAxMDo0NjoxMyIsImV4cCI6MTY5NDc3NDc3M30.1xVUOfkoj5nl9Vvrtx6BBXV0ntusYBmqd4iSl53-wgk'})

    r = r.json()
    return [r['data']['longitude'], r['data']['latitude']]

driver = webdriver.Chrome('./chromedriver')

with open(os.path.join(curr_path, 'content3.csv'), mode='r') as file:
    nlp = spacy.load('en_core_web_md')

    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for content_i in range(1089, len(csvFile)):
    # for content_i in range(1, 2):
        sno, _c_, link, date = csvFile[content_i]

        driver.get(link)
        try:
        # if True:
            content = driver.find_elements(By.XPATH, '//div[@class="_s30J clearfix  "]')[0]
            text = content.get_attribute('innerText')

            try:
                extra = driver.find_elements(By.XPATH, '//div[@class="coronaaswidget"]')[0].get_attribute('innerText')

                # print("extra:", extra)

                if (extra.strip() != '') and (extra in text):
                    text = text[:text.index(extra)]

            except Exception as e:
                print("error in extra, but text intact:", text)

            # print("text:", text)

            # text = """Nashik: Three bikers were killed in two accidents in Nashik city and Chandwad on Sunday. Motorists
            # responsible for both the accidents escaped from the scene and are booked on the charge of causing death due
            # to negligence by the police.In Chandwad, three people were riding on a bike to Ganur village at around 8 pm,
            # when they were hit by a car coming from the opposite direction. The police said that the car driver was on
            # the wrong side of the road while trying to overtake a car ahead of him, when he ended up hitting the bikers.
            # All the three bikers suffered serious injuries in the accident. Two of them, Balu Devram Jadhav (53) and
            # Arun Uttam Gangurde (31) of Ganur village succumbed to the injuries whereas Sagar Thombre (25) of Parsul
            # village, who was riding the bike escaped with injuries on his legs.In another incident, Bhimkumar Singh of
            # Pathardi Phata was killed after he was hit by an unidentified motorist at around 11.30 am in Ambad
            # industrial area. Police said the victim was returning home when he met with the accident. Singh suffered
            # from serious injuries to his stomach and succumbed to them."""

            doc = nlp(text)

            collection = {}

            token_l = doc.to_json()['tokens']
            ent_graph = {}

            count = 0
            for token in doc:
                if token.ent_type_ != '':
                    ent_graph[count] = token.ent_type_

                    # print(token, ":", token.ent_type_)

                count += 1

            print("ent_graph:", ent_graph)

            head_graph = {i: [] for i in range(len(token_l))}
            accident_list = []

            for token_info in token_l:
                if (token_info['dep'] != 'punct') and (token_info['dep'] != 'ROOT') and (token_info['pos'] != 'morph'):
                    head_graph[token_info['head']].append(token_info['id'])

            for token in token_l:
                if token['pos'] == 'ADP':
                    curr_word = text[token['start']:token['end']]
                    curr_word_head = text[token_l[token['head']]['start']:token_l[token['head']]['end']]
                    prep_curr = token['id']

                    for word in place_prep:
                        if nlp(word).similarity(nlp(curr_word)) > 0.7:
                            flag_poi = False

                            for word_oi in woi_cue:
                                if flag_poi is False:
                                    if nlp(curr_word_head).similarity(nlp(word_oi)) > 0.5:
                                        flag_poi = True

                            if flag_poi is not False:
                                collection[prep_curr] = {(curr_word_head, token_l[token['head']]['id']):
                                                             traverse(text, head_graph, token_l, prep_curr)}

            print("head_graph:", head_graph)
            print("token_l:", token_l)
            print("collection:", collection)

            collection_t = {}

            for key_t in collection:
                dict_temp = collection[key_t]

                for k_t in dict_temp:
                    arr = dict_temp[k_t]

                if arr:
                    flag_present = False
                    max_length = 0

                    for token_index, token_entity, __ in arr:
                        if flag_present is False:
                            if (token_entity == 'ORG') or (token_entity == 'GPE') or (token_entity == 'FAC') or \
                                    (token_entity == 'LOC') or (token_entity == 'PRODUCT') or (token_entity == 'NORP') \
                                    or (token_entity == 'PERSON'):
                                flag_present = True

                        max_length += 1

                    # print("arr:", arr)
                    # print("max_length:", max_length)

                    if flag_present is True:
                        # final_sent = ""
                        final_sents = []

                        for ____ in range(max_length):
                            final_sents.append("")

                        for token_index, _, ___ in arr:
                            final_sents[___] += text[token_l[token_index]['start']:token_l[token_index]['end']] + " "

                        for final_sents_i in range(len(final_sents)):
                            final_sents[final_sents_i] = str(final_sents[final_sents_i]).strip()

                        for final_sents_i in range(len(final_sents)):
                             final_sents[final_sents_i] = text[token_l[key_t]['start']:token_l[key_t]['end']] + " " + \
                                                          final_sents[final_sents_i]

                        # collection_t[key] = [text[token_l[key]['start']:token_l[key]['end']] + " " + final_sent[:-1], arr]
                        collection_t[key_t] = {k_t: [final_sents, arr]}

            collection = collection_t
            del collection_t

            print("collection_t:", collection)

            result_csv = []

            collection_tt = {}

            for key in collection:
                dict_temp = collection[key]
                collection_tt[key] = [[], []]

                # print(dict_temp)

                for k_t in dict_temp:
                    arr_temp = dict_temp[k_t]
                    sentences = arr_temp[0]
                    ents = arr_temp[1]

                    # print(sentences, ents)

                    for arr_index in range(len(sentences)):
                        if (len(sentences[arr_index].split()) > 1) and \
                                ((ents[arr_index][1] == 'ORG') or (ents[arr_index][1] == 'GPE') or
                                 (ents[arr_index][1] == 'FAC') or (ents[arr_index][1] == 'LOC') or
                                 (ents[arr_index][1] == 'PRODUCT') or (ents[arr_index][1] == 'NORP') or
                                 (ents[arr_index][1] == 'PERSON')):
                            collection_tt[key][0].append(sentences[arr_index])
                            collection_tt[key][1].append(ents[arr_index])



                # arr_result = collection[key][k_t][0]
                # result_csv.append(arr_result)
                #
                # # arr_result = collection[key][0]
                # #
                # # for sent in arr_result:
                # #     result_csv.append(sent)

            collection = {key: value for key, value in collection_tt.items() if len(value[0]) != 0}
            del collection_tt

            print("collection final:", collection)

            for key in collection:
                sentences = collection[key][0]
                sent_ents = collection[key][1]

                for index in range(len(sentences)):
                    sentence_curr = sentences[index]
                    sent_ent_curr = sent_ents[index]

                    if (sent_ent_curr[1] == 'FAC') or is_road(sentence_curr, nlp):
                        result_csv.append(sentence_curr)

                    else:
                        result_csv.append(get_coords(sentence_curr))

            result_csv_t = []
            for item in result_csv:
                if item not in result_csv_t:
                    result_csv_t.append(item)

            result_csv = result_csv_t
            del result_csv_t

            with open(os.path.join(curr_path, file_target), 'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([sno, result_csv, link, date])

            # displacy.serve(doc, style="dep", auto_select_port=True)

        except Exception as ee:
            print("error in getting article", ee)
