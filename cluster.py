import csv
import os
import requests

# states = {'Andhra Pradesh': 156, 'Arunachal Pradesh': 1, 'Assam': 28, 'Bihar': 95, 'Chandigarh': 79,
#           'Chhattisgarh': 41, 'Delhi': 46, 'Goa': 53, 'Gujarat': 115, 'Himachal Pradesh': 31,
#           'Jammu & Kashmir': 17, 'Jharkhand': 35, 'Karnaatak': 36, 'Karnataka': 101, 'Kerala': 51,
#           'Madhya Pradesh': 145, 'Maharashtra': 294, 'Manipur': 1, 'Meghalaya': 1, 'Odisha': 36,
#           'Punjab': 85, 'Rajasthan': 148, 'Tamil Nadu': 312, 'Telangana': 150, 'Tripura': 1,
#           'Uttar Pradesh': 401, 'Uttarakhand': 75, 'West Bengal': 50}

states = {}
others = 1

curr_path = os.path.join(os.getcwd(), 'States')

with open('all_articles_raw.csv', mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for ii in range(19922, len(csvFile)):
    # for ii in range(1, len(csvFile)):
        _, h, sub_h, link = csvFile[ii]
        link_t = link[41:]
        city = link_t[:link_t.index('/')]

        q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=heKhoAMtNGoYcTVKb8ycW7ZqkLRC671U"
        # q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=GgCKUCUAfIvT6II7JHgqUWm5IGMGxFce"
        # q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=oYGVNAkoLnoKGwJCaUFSEkDQPDRESJY8"
        # q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=8MHKZIkJiGg7k6zvLJOtjVP9SW7K6dWa"
        # q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=8xDLu7MzgNCM8G1jOxuEBArbqSTbqPaxC"
        # q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=2WJFCxoPdcwGALqFHMGUkqRWWGP4mT12"
        # q = "https://api.tomtom.com/search/2/geocode/" + city + ".json?key=WL9VamAibOw1G1KoHFqeuDOsUcVGlbJJ"

        r = requests.get(q, headers=None)

        # print(city)

        flag_country = False
        for i in range(len(r.json()['results'])):
            try:
                state = r.json()['results'][i]['address']['countrySubdivision']
                country = r.json()['results'][i]['address']['countryCodeISO3']
                # lat = r.json()['results'][i]['position']['lat']
                # lon = r.json()['results'][i]['position']['lon']

                if (flag_country is False) and (country == 'IND'):
                    flag_country = True
                    new_path = os.path.join(curr_path, state)

                    if state not in states:
                        states[state] = 1

                        # os.mkdir(new_path)

                        with open(new_path + '/' + 'data.csv', 'a') as csvfile:
                            csvwriter = csv.writer(csvfile)
                            csvwriter.writerow(['sno', 'h', 'sub_h', 'link'])
                            csvwriter.writerow([states[state], h, sub_h, link])

                    else:
                        states[state] += 1

                        with open(new_path + '/' + 'data.csv', 'a') as csvfile:
                            csvwriter = csv.writer(csvfile)
                            csvwriter.writerow([states[state], h, sub_h, link])

            except Exception as e:
                print("error in ::", r.json()['results'][i]['address'])

                new_path = os.path.join(curr_path, 'Others')

                if others == 1:
                    # os.mkdir(new_path)

                    with open(new_path + '/' + 'data.csv', 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(['sno', 'h', 'sub_h', 'link'])
                        csvwriter.writerow([others, h, sub_h, link])

                else:
                    with open(new_path + '/' + 'data.csv', 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow([others, h, sub_h, link])

                others += 1

        print("Operated on", ii)

print("states:", states)