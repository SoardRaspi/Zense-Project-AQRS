# import re
#
# def find_coordinate_strings(text):
#     pattern = r'\[([-+]?\d+\.\d+),\s+([-+]?\d+\.\d+)\]'
#     # pattern = r'(\d+)\s*:'
#     matches = re.findall(pattern, text)
#     return matches
#
# text = """"/Users/soardr/PycharmProjects/Zense Project AQRS/venv/bin/python" /Users/soardr/PycharmProjects/Zense Project AQRS/States/only_related.py
# /Users/soardr/PycharmProjects/Zense Project AQRS/States/only_related.py:11: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#   driver = webdriver.Chrome('./chromedriver')
# /Users/soardr/PycharmProjects/Zense Project AQRS/States/only_related.py:12: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#   driver2 = webdriver.Chrome('./chromedriver')
# sno: 1 soi: ['died in a road accident', 'knocked by a tempo', 'knocked at Nashik Road', 'knocked on Tuesday', 'riding at Nashik Road', 'riding on Monday evening', 'from behind', 'complaint over causing death due to negligent driving', 'received in his head and chest', 'being in the hospital', 'organisations on the road whose CCTV footages are being used to track the details of the vehicle and reach the motorist']
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# 1 : {'coords': [['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214'], ['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/63-yr-old-killed-in-road-accident/articleshow/102371047.cms', 'date': ' Aug 3, 2023'}
# sno: 2 soi: ['collided near Gaikmukh', 'jam on the Mumbai bound lane of Ghodbunder Road and Ahmedabad highway', 'led on Tuesday morning', 'descent on the Thane bound lane', 'spotted in the way that had apparently broken down', 'injured in the mishap']
# address_road: Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070
# address_road: Kapurbawadi Naka, Thane West, Thane, Maharashtra
# 2 : {'coords': [['Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070'], ['Kapurbawadi Naka, Thane West, Thane, Maharashtra']], 'link': 'https://timesofindia.indiatimes.com/city/thane/three-vehicle-collision-hits-gb-rd-traffic/articleshow/102332879.cms', 'date': ' Aug 2, 2023'}
# sno: 3 soi: ['hit near Padgha Khadavali turning point', 'hit on Mumbai Nashik highway', 'hit on Tuesday morning', 'took at around 7.30am', 'took near Lucky hotel on the highway where in the past too many accidents were reported', 'hotel on the highway where in the past too many accidents were reported', 'reported in the past', 'captured on CCTV camera installed on the highway', 'installed on the highway', 'speeding in Mumbai Nashik Highway']
# address_road: Mumbai - Agra National Hwy, Golbhan, Maharashtra 421303
# address_road: Mumbai - Agra National Hwy, Golbhan, Maharashtra 421303
# 3 : {'coords': [['Mumbai - Agra National Hwy, Golbhan, Maharashtra 421303'], ['Mumbai - Agra National Hwy, Golbhan, Maharashtra 421303']], 'link': 'https://timesofindia.indiatimes.com/city/thane/4-dead-5-injured-in-road-accident-on-mumbai-nashik-highway/articleshow/101849590.cms', 'date': 'Jul 18, 2023'}
# sno: 4 soi: ['injured in an accident', 'injured on Tuesday', 'died on Wednesday', 'crossing on Tuesday', 'knocked by a speeding car', 'set on the Gangapur Road', 'set near the site of the incident', 'injuries in head and chest', 'succumbed on Wednesday']
# address_road: Shankaryacharya Sankul, Gangapur Rd, near Jankalyan Blood Bank Shankaracharya Nyas, Nashik, Maharashtra 422005
# 4 : {'coords': [['Shankaryacharya Sankul, Gangapur Rd, near Jankalyan Blood Bank Shankaracharya Nyas, Nashik, Maharashtra 422005']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/senior-citizen-killed-in-nashik-road-accident/articleshow/101559055.cms', 'date': ' Jul 7, 2023'}
# sno: 5 soi: ['killed in two accidents in Nashik city and Chandwad', 'accidents in Nashik city and Chandwad', 'killed on Sunday', 'booked on the charge of causing death due to negligence by the police', 'negligence by the police', 'riding on a bike', 'riding at around 8 pm when they were hit by a car coming from the opposite direction', 'hit by a car coming from the opposite direction', 'was on the wrong side of the road', 'suffered in the accident', 'injuries on his legs', 'hit by an unidentified motorist', 'hit at around 11.30', 'am in Ambad industrial area']
# 5 : {'coords': [[73.789802, 19.997453], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/3-killed-in-road-accidents-in-nashik-district/articleshow/101472219.cms', 'date': ' Jul 4, 2023'}
# sno: 6 soi: ['killed in an accident on the Ramtek Bhandara Road', 'accident on the Ramtek Bhandara Road', 'travelling in rammed into a stationary truck from behind', 'travelling on Sunday', 'temple in Ramtek', '"driven by Himanshu \'s father Rajesh who along with wife Durga is posted with Bhandara police", \'injured in the accident', 'hospital at Ramtek', 'shifted in the city where the three were declared dead by the doctors', 'declared by the doctors', 'parked on the roadside']
# address_road: 7G7C+7MW, Khat Rd, New Shivaji Nagar, Bhandara, Maharashtra 441906
# address_road: Ramtek, Maharashtra 441106
# 6 : {'coords': [['7G7C+7MW, Khat Rd, New Shivaji Nagar, Bhandara, Maharashtra 441906'], ['Ramtek, Maharashtra 441106'], [79.32684, 21.392862], [79.661347, 21.169488], [79.32684, 21.392862]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/2-kids-among-three-dead-in-road-accident/articleshow/101652612.cms', 'date': 'Jul 11, 2023'}
# sno: 7 soi: ['divider near Zero Mile', 'accident on July 6', 'succumbed on Friday', 'storage on old Bhandara road', 'stored at Heliwal Krishi Seetgruha Private Limited Company at Umiya Kapsi Burjug', 'Company at Umiya Kapsi Burjug']
# address_road: Kamptee, Maharashtra 441104
# 7 : {'coords': [['Kamptee, Maharashtra 441104']], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/36-year-old-man-dies-in-road-accident/articleshow/101606564.cms', 'date': ' Jul 9, 2023'}
# sno: 8 soi: ['killed in separate road accidents on Trimbak Road between Sunday and Monday', 'accidents on Trimbak Road', 'accidents between Sunday and Monday', 'hit by a car', 'hit on Monday afternoon', 'opening in the road', 'divider at around 3.30 pm', 'suffered in the accident', 'admitted in the Nashik civil hospital', 'control over his vehicle', 'took at around 9 pm', 'took on Sunday', 'riding on the Trimbak Road', 'control over his scooter', 'suffered in the accident', 'hospital in the city where he succumbed to the injuries on Monday morning', 'succumbed on Monday morning']
# address_road: Trimbak, Maharashtra 422212
# address_road: Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012
# address_road: Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012
# 8 : {'coords': [['Trimbak, Maharashtra 422212'], ['Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012'], [73.778303, 19.996787], ['Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/2-killed-in-separate-accidents-on-trimbak-road/articleshow/101683196.cms', 'date': 'Jul 12, 2023'}
# sno: 9 soi: ['violating in a special drive that began on June 28', 'began on June 28', 'are on the rise in the city', 'rise in the city', 'injured in accidents', 'mandated by teh Motor Vehicles Act', 'lost in road accidents in the city', 'accidents in the city', 'stood at 86', 'provided by the city police', 'died in road accidents', 'died between January and May']
# sno: 10 soi: ['suffering in a road accident in the Upnagar area', 'accident in the Upnagar area', 'suffering on Saturday afternoon', 'riding in the Jail Road area', 'riding on Saturday', 'survived by his parents wife a 14 year old daughter and a 10 year old son', 'joined in Mumbai', 'worked at the police headquarters of the city police']
# address_road: XRFC+FQF, Ayodhya Nagar, Upnagar, Nashik, Maharashtra 422214
# 10 : {'coords': [['XRFC+FQF, Ayodhya Nagar, Upnagar, Nashik, Maharashtra 422214'], [73.822077, 19.973875], [72.877656, 19.075984]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/police-naik-killed-in-bike-accident/articleshow/101623832.cms', 'date': 'Jul 10, 2023'}
# sno: 11 soi: ['rammed on an internal road in the Gangapur Road area', 'road in the Gangapur Road area', 'rammed on Wednesday night', 'sustained in the accident', 'took at around 9 pm in Kale Nagar', 'pm in Kale Nagar', 'took behind the Guruji Hospital in Anandwali area of Gangapur Road', 'Hospital in Anandwali', 'speeding on his bike', 'speeding on the colony road', 'control over his vehicle', 'rammed on the same road', 'speeding by the driver', 'succumbed on Thursday evening', 'are in good condition', 'speed on them', 'registered under Section 304 A', 'registered on the charges of causing death due to negligence', 'roads in the city colonies', 'put on them', 'occur on the smooth roads of the inner colonies']
# address_road: Shankaryacharya Sankul, Gangapur Rd, near Jankalyan Blood Bank Shankaracharya Nyas, Nashik, Maharashtra 422005
# address_road: Shankaryacharya Sankul, Gangapur Rd, near Jankalyan Blood Bank Shankaracharya Nyas, Nashik, Maharashtra 422005
# address_road: Gangapur Rd, Kale Nagar, Anand Vihar Colony, Anandvalli, Nashik, Maharashtra 422013
# 11 : {'coords': [['Shankaryacharya Sankul, Gangapur Rd, near Jankalyan Blood Bank Shankaracharya Nyas, Nashik, Maharashtra 422005'], ['Shankaryacharya Sankul, Gangapur Rd, near Jankalyan Blood Bank Shankaracharya Nyas, Nashik, Maharashtra 422005'], [73.745542, 20.008549], [73.745542, 20.008549], ['Gangapur Rd, Kale Nagar, Anand Vihar Colony, Anandvalli, Nashik, Maharashtra 422013'], [73.7478, 20.012274]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/biker-rams-tree-near-gangapur-rd-at-night-dies/articleshow/101586823.cms', 'date': ' Jul 8, 2023'}
# sno: 12 soi: ['falling on the third floor of Shree Complex in Narendra Nagar area', 'Complex in Narendra Nagar area', 'suffered at around 8.45am', 'suffered on Thursday', 'molested by 20 year old man Powered By Play Unmute', 'molesting by threatening to spread her photos on social media', 'photos on social media', 'befriended on Instagram', 'dies in road accident', 'hit by an unidentified vehicle near HP Gas', 'vehicle near HP Gas', 'hit on June 18', 'treatment on Thursday']
# sno: 13 soi: ['died in a road accident at Girgaum Chowpatty', 'accident at Girgaum Chowpatty', 'died on Wednesday morning', 'driven by a minor', 'be in 10 minutes', 'called at 5 am', 'was on Wednesday midnight', 'cut at midnight', 'inculcated in all schoolchildren', 'coming at a high speed applied brakes', 'rained in the night', 'fell on the road', 'died on the spot', 'died on Wednesday evening', 'Laboratory at Kalina', 'transferred in his name', 'booked under Section 304A', 'causing by negligence', 'riding on a public way', 'hurt by act', 'driving in contravention of Section 3 or Section 4 of the Motor Vehicle Act', 'transfer in his name', '"mourning at Khan \'s residence near Grant Road", \'residence near Grant Road', 'sister in law', 'was in the scrap business', 'worked in a printing company']
# address_road: XR37+WFW, Chowpatty, Girgaon, Mumbai, Maharashtra 400007
# address_road: Krishna Kunj, Grant Road East, Bharat Nagar, Grant Road, Mumbai, Maharashtra 400007
# 13 : {'coords': [['XR37+WFW, Chowpatty, Girgaon, Mumbai, Maharashtra 400007'], [72.816559, 18.951862], ['Krishna Kunj, Grant Road East, Bharat Nagar, Grant Road, Mumbai, Maharashtra 400007']], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/chowpatty-death-cocktail-of-speed-brakes-and-rain/articleshow/101030163.cms', 'date': 'Jun 16, 2023'}
# sno: 14 soi: ['put in place', 'measures at 27 black spots in the city which were identified with the help of a Mumbai based NGO Resilient India', 'spots in the city', 'accident at Mirchi Hotel Chowk', 'accident in October', 'charred in which', 'delay on the part of the civic body', 'delay on the issue', 'measures at the 27 black spots', 'put at the 333 black spots', 'injured in those black spots', 'put in place', 'lost in road accidents', 'prevent at the 27 black spots', 'take at the earliest for the safety of people', 'carry at 27 black spots']
# 14 : {'coords': [[72.817736, 18.961511]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/no-speed-reducing-measures-yet-at-27-black-spots-in-nashik/articleshow/101443916.cms', 'date': ' Jul 3, 2023'}
# sno: 15 soi: ['wall on Samruddhi Expressway', 'hit near Sinnar', 'hit on Monday', 'travelling in a multi - purpose vehicle MPV along the Samruddhi Mahamarg route', 'took near Khambale village near Sinnar', 'village near Sinnar', 'passengers in the MPV', 'control over the vehicle', 'crashed by the roadside', 'died on the spot', 'course at a hospital in Sinnar', 'hospital in Sinnar']
# address_road: Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702
# 15 : {'coords': [['Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702'], [73.988965, 19.847981], [76.138342, 19.990506], [73.988965, 19.847981], [73.988965, 19.847981], [73.988965, 19.847981], [73.988965, 19.847981]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/four-of-family-killed-as-muv-hits-wall-on-samruddhi-expressway/articleshow/100932875.cms', 'date': 'Jun 12, 2023'}
# sno: 16 soi: ['died in a freak mishap', 'died at Ghodbunder road in Thane', 'road in Thane', 'killing on the spot']
# address_road: Kasav Babli, Ghodbandar Road, Mugal Road, Thane
# address_road: Kapurbawadi Naka, Thane West, Thane, Maharashtra
# 16 : {'coords': [['Kasav Babli, Ghodbandar Road, Mugal Road, Thane'], ['Kapurbawadi Naka, Thane West, Thane, Maharashtra']], 'link': 'https://timesofindia.indiatimes.com/city/thane/40-year-old-driver-from-gujarat-dies-in-road-accident-in-thane/articleshow/101772479.cms', 'date': 'Jul 15, 2023'}
# sno: 17 soi: ['lost between January and May', 'lost in road accidents in Nashik city', 'accidents in Nashik city', 'lost in road accidents', 'provided by the city police', 'deaths between January and May', 'accounted in Nashik city', 'spreading among motorists about safe and defensive driving', 'motorists in large numbers', 'installed by the Nashik Municipal Smart City Development Corporation Ltd NMSCDCL', 'provided in the 18 25 age group who apply to the Nashik RTO for driving licences', 'Applicants in this age group', 'programme at the Children ’s Traffic Education Park of Nashik First organisation']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 17 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453], [73.789802, 19.997453], [73.789658, 20.011396], [73.790377, 19.997686]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/80-accident-deaths-between-jan-may-in-23-on-city-roads-slightly-less-than-22/articleshow/101324035.cms', 'date': 'Jun 28, 2023'}
# sno: 18 soi: ['announced on Wednesday', 'announced in Nagpur', 'put at entry gates of all the three RTO offices', 'office at Chikhli Kalamna and rural office near Lal Godam on Kamptee Road', 'office near Lal Godam', 'office on Kamptee Road', 'using in public places', 'ride in a public place', 'officers under your authority', 'visit in the form of a notice', 'visit by placing it in the facade at the main entrance', 'placing in the facade', 'placing at the main entrance', 'aimed at curbing deaths from head injuries in road accidents', 'injuries in road accidents']
# address_road: Army Cantonment, Kamptee, Maharashtra 441001
# address_road: Bhilgaon, Nagpur, Maharashtra 441001
# 18 : {'coords': [[79.088155, 21.1458], ['Army Cantonment, Kamptee, Maharashtra 441001'], ['Bhilgaon, Nagpur, Maharashtra 441001']], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/now-no-entry-for-helmetless-riders-at-rto-offices/articleshow/101176995.cms', 'date': 'Jun 22, 2023'}
# sno: 19 soi: ['hit by a dumper at Alandi', 'dumper at Alandi', 'hit on Sunday night', 'meet at the latter ’s pharmacy', 'Gevrai in Beed district', 'come on Sunday evening', 'came under the dumper', 'killed on the spot', 'booked on the charge of causing death by negligence', 'causing by negligence']
# 19 : {'coords': [[73.895034, 18.678287], [73.895034, 18.678287], [75.754592, 19.260581]], 'link': 'https://timesofindia.indiatimes.com/city/pune/senior-citizen-killed-in-road-accident/articleshow/100608920.cms', 'date': 'May 30, 2023'}
# sno: 20 soi: ['imposed under section 199(A of the MVA 1988', 'allow below 18 years of age', 'person under the age of 18 years', 'drive in any public place', 'driven in public places', 'driven by any person', 'accidents in the state', 'persons in Maharashtra', 'lose in road accidents', 'occurred between January 2022 and December 2022', 'caused by two wheeler drivers in which', 'lost in which', 'issued in this regard', 'drivers in the entire state', 'basis in the entire state', 'person below the age of 20 years', 'drive in public places']
# 20 : {'coords': [[75.713888, 19.75148]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/are-you-a-minor-driving-without-a-licence-be-ready-to-pay-25000/articleshow/101120830.cms', 'date': 'Jun 20, 2023'}
# sno: 21 soi: ['killed in a road accident on Trimbak Road', 'accident on Trimbak Road', 'killed in the early hours of Wednesday', 'speeding on Wednesday', 'speeding on the Trimbak Road', 'control over his two wheeler', 'riding on the bike', 'injuries in the accident']
# address_road: Trimbak, Maharashtra 422212
# address_road: Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012
# address_road: Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012
# 21 : {'coords': [['Trimbak, Maharashtra 422212'], ['Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012'], ['Trambakeshwar Rd, Ashoknagar, Satpur Colony, Nashik, Maharashtra 422012']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/2-youngsters-killed-in-road-accident/articleshow/100516169.cms', 'date': 'May 26, 2023'}
# sno: 22 soi: ['truck in Buldhana district of Maharashtra', 'collided on Tuesday morning', 'took near Sindkhed Raja town', 'took on old Mumbai Nagpur highway in the district', 'highway in the district', 'going in Buldhana', 'hospital in Sindkhed Raja town']
# address_road: Near, Railway Station Rd, Baba Farid Nagar, Sitabuldi, Nagpur, Maharashtra 440001
# 22 : {'coords': [[76.363729, 20.456098], [76.125961, 19.952543], ['Near, Railway Station Rd, Baba Farid Nagar, Sitabuldi, Nagpur, Maharashtra 440001'], [76.18417, 20.529215], [76.125961, 19.952543]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/6-killed-10-injured-in-bus-truck-collision-in-maharashtras-buldhana-mumbai-nagpur-highway/articleshow/100436137.cms', 'date': 'May 23, 2023'}
# sno: 23 soi: ['died in a road accident', 'died near Parsodi', 'dropping at in laws place', 'was on bike', 'trailer on Wardha road', 'registered at Beltarodi police station', 'stolen in separate incidents', 'worth over ₹ 2 lakh', 'worth in separate burglaries in the city', 'burglaries in the city', 'took at Hudco Colony', 'clerk at district collectorate', 'gone on June 10', 'one at home', 'took at Kumbhar Toli in Nandanvan police station area', 'Toli in Nandanvan', 'was at his office', 'registered on Sunday']
# address_road: Wardha Road Ralegaon Nagpur Wardha Road Ralegaon, Nagpur, Maharashtra 440015
# 23 : {'coords': [['Wardha Road Ralegaon Nagpur Wardha Road Ralegaon, Nagpur, Maharashtra 440015'], [79.077932, 21.078296], [79.122689, 21.13672], [79.12764, 21.138791]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/man-dies-after-bike-rams-stationary-trailer/articleshow/100951817.cms', 'date': 'Jun 13, 2023'}
# sno: 24 soi: ['is among the youngest donors in Mumbai', 'donors in Mumbai', 'deaths between hospitals', 'dead in Bombay Hospital near New Marine Lines', 'Hospital near New Marine Lines', 'was in 2001', 'marks in Mumbai', 'given by the National Organ and Tissue Transplant Organisation', 'salute on Sunday evening', 'lagging behind other states', 'lagging in terms of deceased donations']
# 24 : {'coords': [[72.877656, 19.075984], [72.917124, 19.056832], [72.827436, 18.941034], [72.828654, 18.938918], [72.877656, 19.075984]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/brain-dead-3-yr-old-among-youngest-organ-donors-in-city/articleshow/100951572.cms', 'date': 'Jun 13, 2023'}
# sno: 25 soi: ['are among the accused involved in an insurance scam', 'involved in an insurance scam', 'processed by the lawyer', 'signed by the chartered accountant who have been named as accused in the chargesheet submitted before the court', 'accused in the chargesheet submitted before the court', 'died in a road accident', 'died on December 25 2016 in Ahmednagar', 'December in Ahmednagar', 'station in Ahmednagar', 'accident in Bhelwandi', 'submitted in court', 'witness in the case', 'sign in the inquest panchnama or spot panchnama', 'report in court']
# 25 : {'coords': [[74.747979, 19.094829], [74.747979, 19.094829], [74.747979, 19.094829], [73.048291, 19.281255]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/witnesses-in-insurance-claim-fake-finds-probe/articleshow/100925281.cms', 'date': 'Jun 12, 2023'}
# sno: 26 soi: ['was in Nashik', 'was on Saturday', 'organised by the Nashik First organisation at its Children ’s Traffic Education Park', 'organisation at its Children ’s Traffic Education Park', 'others in general', 'die in road accidents in the state', 'accidents in the state', 'motorists on the streets', 'present at the programme', 'spoke at length', 'conducted in the city']
# 26 : {'coords': [[73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/traffic-education-should-be-a-relentless-process-mumbai-cp/articleshow/100908772.cms', 'date': 'Jun 11, 2023'}
# sno: 27 soi: ['decision in this regard', 'lose in road accidents', 'driving on roads', 'units in Ambad Sinnar Dindori', 'visited among others', 'travel on two wheelers or four wheelers', 'wearing in the industrial areas', 'installed at the entrance gate of industrial units', 'lost in road accidents in Nashik city and the rural district', 'accidents in Nashik city and the rural district']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 27 : {'coords': [[73.988965, 19.847981], ['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/rto-tells-150-organizations-to-make-helmets-compulsory/articleshow/100836189.cms', 'date': ' Jun 8, 2023'}
# sno: 28 soi: ['killed in separate road accidents in Narhe and Warje', 'accidents in Narhe and Warje', 'killed on Monday', 'riding on a bike', 'wheeler near the Swaminarayan temple', 'hit on Monday', 'ran at Ambegaon', 'divider in Warje', 'crashed on Monday', 'occurred on the lane', 'control over his vehicle']
# address_road: Service Rd, AtulNagar Phase I, Atul Nagar, Warje, Pune, Maharashtra 411058
# 28 : {'coords': [['Service Rd, AtulNagar Phase I, Atul Nagar, Warje, Pune, Maharashtra 411058'], [73.796834, 18.486473], [73.732678, 19.113234], [73.796834, 18.486473]], 'link': 'https://timesofindia.indiatimes.com/city/pune/two-killed-in-separate-accidents-in-narhe-warje/articleshow/100808234.cms', 'date': ' Jun 7, 2023'}
# sno: 29 soi: ['dashed in a bid to overtake it', 'brother in law', 'brother at Malad village on the Pune Solapur highway', 'village on the Pune Solapur highway', 'happened on Wednesday', 'happened near Daund', 'was in Latur', 'lived in Chakan', 'Waghare in Latur', 'brother in law', 'dashed in an attempt to overtake', 'hit by a dumper at Gunwadi chowk in Baramati', 'dumper at Gunwadi chowk in Baramati', 'chowk in Baramati', 'happened on Tuesday', 'lodged in this regard', 'came under the wheels of the dumper', 'fell on the opposite side']
# address_road: Dhayari, Kasba Peth, Pune, Maharashtra 411011
# address_road: Dhayari, Kasba Peth, Pune, Maharashtra 411011
# 29 : {'coords': [['Dhayari, Kasba Peth, Pune, Maharashtra 411011'], ['Dhayari, Kasba Peth, Pune, Maharashtra 411011'], [74.584049, 18.463118], [76.560383, 18.408793], [73.86132, 18.763208], [76.569004, 18.413402], [74.607797, 18.179179], [74.607797, 18.179179], [74.607797, 18.179179]], 'link': 'https://timesofindia.indiatimes.com/city/pune/two-road-accidents-claim-4-lives-in-daund-baramati/articleshow/100516497.cms', 'date': 'May 26, 2023'}
# sno: 30 soi: ['travelling on a motorbike', '"vehicle on the Mumbai Ahmedabad highway in Maharashtra \'s Palghar district", "highway in Maharashtra \'s Palghar district", \'collided on Thursday', 'were on their way from Harsul', 'were in Nashik district', 'were in Gujarat', 'collided at Sutrakar Phata', 'died on the spot']
# address_road: 7WP3+6QC, Ghodbunder, Thane, Mira Bhayandar, Maharashtra 401107
# 30 : {'coords': [['7WP3+6QC, Ghodbunder, Thane, Mira Bhayandar, Maharashtra 401107'], [74.030012, 20.16235]], 'link': 'https://timesofindia.indiatimes.com/city/thane/3-dead-on-mumbai-ahmedabad-highway-accident-in-palghar/articleshow/100507476.cms', 'date': 'May 25, 2023'}
# sno: 31 soi: ['killed in a road accident', 'hit by a speeding container on the Dwarka flyover', 'container on the Dwarka flyover', 'am on Tuesday', 'stopped on the flyover', 'suffered in the accident', 'brought at the hospital', 'jam on the flyover', 'has on one side of the road']
# sno: 32 soi: ['carried in various parts of Dhule', 'distributed among villagers industrial workers volunteers working as Mrutunjay Doots in various parts of the Dhule highway police unit', 'Doots in various parts of the Dhule highway police unit', 'spread on two national highways and other state highways', 'fatalities in road accidents']
# address_road: National Highway 6, Garud Baag, Navnath Nager, Dhule, Maharashtra 424001
# address_road: National Highway 6, Garud Baag, Navnath Nager, Dhule, Maharashtra 424001
# 32 : {'coords': [[74.774898, 20.90422], ['National Highway 6, Garud Baag, Navnath Nager, Dhule, Maharashtra 424001'], ['National Highway 6, Garud Baag, Navnath Nager, Dhule, Maharashtra 424001']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/highway-cops-distribute-over-100-helmets-in-dhule/articleshow/100389831.cms', 'date': 'May 21, 2023'}
# sno: 33 soi: ['killed in a road accident in the Adgaon area', 'accident in the Adgaon area', 'knocked by an unidentified sports utility vehicle SUV driver', 'knocked on Sunday night', 'taking on Sunday night', 'suffered in the accident']
# address_road: Adgaon Rd, Adgaon, Nashik, Maharashtra 422201
# 33 : {'coords': [['Adgaon Rd, Adgaon, Nashik, Maharashtra 422201'], [73.86356, 20.03347]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/woman-killed-in-hit-and-run-in-adgaon/articleshow/100343312.cms', 'date': 'May 19, 2023'}
# sno: 34 soi: ['couple in Palghar district in Maharashtra', 'district in Maharashtra', 'killed in a motorcycle accident', 'said on Saturday', 'killed in an accident near Bengaluru', 'accident near Bengaluru', 'killed on Friday', 'Committee in Maharashtra IMA', 'donation in the country']
# 34 : {'coords': [[72.993297, 19.786716], [75.713888, 19.75148], [75.713888, 19.75148]], 'link': 'https://timesofindia.indiatimes.com/city/navi-mumbai/maharashtra-doctor-couple-donates-organs-of-son-killed-in-road-accident/articleshow/100385323.cms', 'date': 'May 20, 2023'}
# sno: 35 soi: ['travelling in an autorickshaw', 'divider at Gaimukh', 'divider on the Ghodbunder Road in Thane', 'Road in Thane', 'crashed on Wednesday', 'lost over the vehicle', 'chief at the regional disaster management cell']
# address_road: Kasav Babli, Ghodbandar Road, Mugal Road, Thane
# address_road: Kapurbawadi Naka, Thane West, Thane, Maharashtra
# 35 : {'coords': [[72.938615, 19.28715], ['Kasav Babli, Ghodbandar Road, Mugal Road, Thane'], ['Kapurbawadi Naka, Thane West, Thane, Maharashtra']], 'link': 'https://timesofindia.indiatimes.com/city/thane/woman-charred-to-death-as-autorickshaw-catches-fire-after-crash-in-thane/articleshow/99964612.cms', 'date': ' May 3, 2023'}
# sno: 36 soi: ['killed in separate road accidents in Igatpuri', 'accidents in Igatpuri', 'killed on Sunday', 'died in one accident', 'killed in the other one', 'riding on the wrong side', 'riding on Sunday', 'riding at 6 pm', 'took on the new Samruddhi Highway flyover which passes through Igatpuri', 'speeding on the under construction flyover', 'took at 8.30pm', 'took on Sunday', 'injuries in the accident resulting in their death', 'resulting in their death']
# address_road: Bajrang Wada, Igatpuri, Maharashtra 422402
# address_road: Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702
# 36 : {'coords': [['Bajrang Wada, Igatpuri, Maharashtra 422402'], [73.561107, 19.696326], ['Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/2-killed-in-separate-road-accidents-in-igatpuri/articleshow/99283150.cms', 'date': ' Apr 6, 2023'}
# sno: 37 soi: ['met on April 19', 'died on April 22', 'donated in which', 'witnessed in the city', 'witnessed on April 23', 'work in a private company', 'accident at Kalamba near Kalmeshwar', 'Kalamba near Kalmeshwar', 'admitted at Aureus Hospital', 'admitted on April 19', 'admitted at midnight', 'brain on April 22', 'counseled by Anirudha Koparkar and Dinesh Mandpe', 'Hospital in the city']
# 37 : {'coords': [[78.912019, 21.234449], [78.912019, 21.234449]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/for-the-first-time-post-pandemic-road-accident-victims-all-organs-donated/articleshow/99718582.cms', 'date': 'Apr 24, 2023'}
# sno: 38 soi: ['conducted by Regional Transport Office of Maharashtra government', 'introduce at all entry points of the expressway', 'had on December 31 2022', 'drivers on Samruddhi Expressway', 'inaugurated on December 11', 'decided in the meeting', 'organised at all eight entry points of the expressway', 'be on curbing overspeeding', 'set on the Nagpur Shirdi section', 'one in each district', 'set in the next seven days', 'sessions by RTO officials', 'resulted in the highest number of accidents', 'film on road safety', 'followed by a question paper solving by the driver and a pledge to not indulge in dangerous driving', 'solving by the driver', 'indulge in dangerous driving', 'accidents on the portion of the expressway', 'were among the major causes of accidents on the Samruddhi Mahamarg', 'accidents on the Samruddhi Mahamarg', 'attended by Nagpur rural and city']
# address_road: Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702
# 38 : {'coords': [[75.713888, 19.75148], ['Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702'], [79.088155, 21.1458], [76.138342, 19.990506], [76.138342, 19.990506], [79.088155, 21.1458]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/samruddhi-100-days-900-accidents-31-fatalities/articleshow/98880781.cms', 'date': 'Mar 22, 2023'}
# sno: 39 soi: ['action under the Motor Vehicles Act', 'face under 194C of the Motor Vehicles Act', 'driven in contravention of the provisions of section 128 or', 'deaths in road accidents', 'issued in this regard', 'riders in any government offices', 'issued by the transport commissioner ’s office which had directed all government offices across Maharashtra not to allow any two wheeler riders without helmets', 'come in government offices', 'staff at all the three transport offices of the city', 'killed in two wheeler accidents', 'awareness on the use of helmets in our area of work', 'use in our area of work', 'involved in this campaign']
# sno: 40 soi: ['lease on life', 'injured in a road accident', 'declared in a private city hospital', 'donated on April 12', 'donor in ZTCC Pune', 'done under ZTCC Pune', 'accident on Wednesday', 'took on the same day as the accident']
# 40 : {'coords': [[73.838057, 18.529231], [73.838057, 18.529231]], 'link': 'https://timesofindia.indiatimes.com/city/pune/brain-dead-woman-gives-life-to-three/articleshow/99528160.cms', 'date': 'Apr 16, 2023'}
# sno: 41 soi: ['come by nearly 20 %', 'rise in fatal accidents', 'analysis in the first three months of the year', 'rise in road accidents in Gadchiroli', 'accidents in Gadchiroli', 'increase in plying of vehicles', 'reported in Naxalite affected Gadchiroli district', 'enforcement on roads', 'resulted in an increase in road mishaps in the district', 'increase in road mishaps in the district', 'mishaps in the district', 'occurred on roads between Sironcha and Aheri and Sironcha and Arvi', 'roads between Sironcha and Aheri and Sironcha and Arvi', 'accidents by the transport commissioner', 'died in 52 fatal accidents', 'Roads under Nagpur rural areas', 'died in 97 fatal accidents this year', 'Roads in Wardha district', 'claiming in 2023', 'lost in 61 fatal accidents', 'reduced in Bhandara 45 deaths in 43 fatal accidents in 2022 and 28 deaths in 26 fatal accidents Gondia from 34 deaths 30 fatal accidents in 2022 to 30 deaths in 27 fatal accidents this year and Chandrapur districts from 109 death 96 fatal accidents in 2022 93 deaths in 82 fatal accidents this year', 'deaths in 43 fatal accidents', 'deaths in 2022', 'deaths in 26 fatal accidents', 'accidents in 2022', 'deaths in 27 fatal accidents this year', 'accidents in 2022', 'deaths in 82 fatal accidents this year', 'decline in fatal accidents', 'decline by 13 % 46 % and 40 % respectively']
# address_road: ITI Chowk, Gokul Nagar, Gadchiroli, Maharashtra 442506
# 41 : {'coords': [['ITI Chowk, Gokul Nagar, Gadchiroli, Maharashtra 442506'], [79.994796, 20.184871], [80.276733, 19.496873], [79.961237, 18.847716], [79.088155, 21.1458], [78.566085, 20.804912], [79.657013, 21.177658]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/fatal-accidents-drop-31-in-city-rise-67-in-gadchiroli/articleshow/99527784.cms', 'date': 'Apr 16, 2023'}
# sno: 42 soi: ['accidents in North Maharashtra ’s Jalgaon district', 'rise in the year 2022', 'officials on Friday', 'lost in which', 'rise in number of accidents', 'drop in road accidents', 'drop in fatalities', 'helped in getting expected results', 'dying in road accidents', 'works on the highways', 'spots in Jalgaon', 'install on the highways passing through the crowded areas']
# 42 : {'coords': [[75.562604, 21.007658]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/rise-in-fatal-accidents-in-jalgaon-dist-last-yr/articleshow/99507093.cms', 'date': 'Apr 15, 2023'}
# sno: 43 soi: ['hit by a car at Hinjewadi along the Katraj Dehu Road bypass', 'car at Hinjewadi', 'hit on Wednesday afternoon', 'driving at the time of the incident', 'hit in its rear', 'declared on arrival by the doctors', 'arrival by the doctors', 'ran on February 16', 'ran over a motorcyclist crushing him to death at Dukkkarkhind on Katraj Dehu bypass road', 'crushing at Dukkkarkhind', 'crushing on Katraj Dehu bypass road', 'fallen on the road', 'ran over him', 'injured in this accident', 'collected by the traffic police speeding and rash driving', 'accidents on highways such as the Katraj Dehu bypass road', 'done by the Pune traffic police', 'done in 2020 21']
# address_road: JQ52+X2P, Tathawade, Pimpri-Chinchwad, Maharashtra 411033
# address_road: Pashan Hwy Side Rd, Mohan Nagar Co-Op Society, Mahalunge, Pune, Maharashtra 411045
# address_road: Pashan Hwy Side Rd, Mohan Nagar Co-Op Society, Mahalunge, Pune, Maharashtra 411045
# address_road: Pashan Hwy Side Rd, Mohan Nagar Co-Op Society, Mahalunge, Pune, Maharashtra 411045
# 43 : {'coords': [['JQ52+X2P, Tathawade, Pimpri-Chinchwad, Maharashtra 411033'], [73.738909, 18.591272], ['Pashan Hwy Side Rd, Mohan Nagar Co-Op Society, Mahalunge, Pune, Maharashtra 411045'], ['Pashan Hwy Side Rd, Mohan Nagar Co-Op Society, Mahalunge, Pune, Maharashtra 411045'], ['Pashan Hwy Side Rd, Mohan Nagar Co-Op Society, Mahalunge, Pune, Maharashtra 411045'], [73.856744, 18.52043]], 'link': 'https://timesofindia.indiatimes.com/city/pune/hit-by-car-biker-killed-on-punes-katraj-dehu-road-bypass/articleshow/98529239.cms', 'date': 'Mar 10, 2023'}
# sno: 44 soi: ['died in road accidents in the city', 'accidents in the city', 'died in the first three months of 2023', 'said on Tuesday', 'dead in accidents', 'dead in first 3 months of 2023', 'died in road accidents', 'aged between 18 and 45 years', 'taking in cases of over speeding', 'riding among other offences', 'are on the lookout for motorists riding their bikes without helmets or those indulging in rash driving', 'indulging in rash driving', 'taken by police', 'took at Mirchi Hotel chowk', 'driving by some motorists']
# sno: 45 soi: ['junction in the city', 'fatalities in three years', 'is among 20 high risk intersections that will be redesigned by the BMC to make them safer', 'redesigned by the BMC', 'reported at Kalanagar Junction--', 'deaths in three years--', 'located in the eastern and western suburbs', 'deaths between 2019 and 2021', 'transform by widening pedestrian crossings and footpaths', 'experts on Thursday', 'darted between vehicles', 'putting at risk', 'post at all times', 'said over the constant blaring of horns', 'is at Amar Mahal Junction', 'partner under the Bloomberg Initiative for Global Road Safety BIGRS', 'involved in reworking the road geometry', 'design at Dharavi depot', 'Data on road crashes in Mumbai', 'crashes in Mumbai', 'conflicts between pedestrians and vehicles', 'junctions in south and central Mumbai', 'redesigned under BIGRS including Nagpada Junction Mela Junction at Mahalaxmi Bharatmata at Parel among others', 'Junction at Mahalaxmi Bharatmata at Parel', 'Bharatmata at Parel', 'Junction among others']
# address_road: Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070
# 45 : {'coords': [[72.861085, 19.051833], ['Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070'], [72.877656, 19.075984], [72.877656, 19.075984], [72.828676, 18.967017], [72.837593, 18.997657], [72.837593, 18.997657]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/amar-mahal-other-junctions-to-focus-on-pedestrian-needs/articleshow/99310270.cms', 'date': ' Apr 7, 2023'}
# sno: 46 soi: ['killed in an accident on the road between Khapri Square and Panjri village', 'accident on the road between Khapri Square and Panjri village', 'road between Khapri Square and Panjri village', 'killed on Saturday morning', 'booked by Beltarodi police', 'killed in a hit and run case at Hingna market', 'case at Hingna market', 'killed on Friday', 'hit by a truck on the bridge', 'truck on the bridge', 'hit in front of a cancer hospital near Jamtha', 'hospital near Jamtha', 'hit on Friday', 'hit by a 35 year old biker Sumeet Dehankar on Amravati Road', 'biker on Amravati Road', 'declared at a private hospital', 'declared on Saturday']
# address_road: Mumbai - Kolkata Hwy, Maharashtra 442203
# address_road: Mumbai - Kolkata Hwy, Maharashtra 442203
# 46 : {'coords': [[79.077216, 21.075211], [78.961349, 21.073549], [78.961349, 21.073549], [79.029839, 21.016603], ['Mumbai - Kolkata Hwy, Maharashtra 442203'], ['Mumbai - Kolkata Hwy, Maharashtra 442203']], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/woman-senior-citizen-among-4-killed-in-separate-road-accidents/articleshow/99701464.cms', 'date': 'Apr 23, 2023'}
# sno: 47 soi: ['died on the spot', 'travelling in', 'truck near the Urse toll post around 40 km from Pune on the Pune Mumbai expressway', 'post on the Pune Mumbai expressway', 'crash on Thursday evening', 'traffic on the expressway', 'Dhumal in Pune and his workers', 'was at the high speed', 'halted in the service lane of the expressway', 'hospital in Talegaon']
# address_road: Maharashtra
# address_road: Maharashtra
# 47 : {'coords': [['Maharashtra'], ['Maharashtra'], [73.856744, 18.52043], [73.674663, 18.737576]], 'link': 'https://timesofindia.indiatimes.com/city/pune/4-dead-after-compact-suv-hits-road-divider-before-crashing-into-truck-on-pune-mumbai-expressway/articleshow/99305103.cms', 'date': ' Apr 6, 2023'}
# sno: 48 soi: ['struck by a speeding vehicle', 'walk in Thane', 'resulting in multiple fractures', 'occurred on Monday', 'hit by a speeding car', '"walk in Mumbai \'s Worli area", "walk in Maharashtra \'s Thane city", \'said on Tuesday', 'took on Monday', 'hit by a speeding car', 'walk in Worli area of neighbouring Mumbai', 'Road in Thane', 'was at around 6.30', 'am on Monday when a car hit her at the Yeoor hills gate', 'hit at the Yeoor hills gate', 'suffered in her leg', 'registered under provisions of the Indian Penal Code and the Motor Vehicles Act', 'walk on the Worli sea face promenade', 'walk in Mumbai']
# address_road: Kapurbawadi Naka, Thane West, Thane, Maharashtra
# 48 : {'coords': [[72.97809, 19.218331], [72.81736, 18.998641], [72.81736, 18.998641], ['Kapurbawadi Naka, Thane West, Thane, Maharashtra'], [72.94458, 19.233765], [72.94458, 19.233765], [72.813439, 19.00261], [72.877656, 19.075984]], 'link': 'https://timesofindia.indiatimes.com/city/thane/woman-out-on-morning-walk-suffers-multiple-fractures-as-speeding-car-hits-her-in-thane/articleshow/99234959.cms', 'date': ' Apr 4, 2023'}
# sno: 49 soi: ['truck on the Mumbai Agra highway under the Igatpuri police station', 'highway under the Igatpuri police station', 'rammed in the early hours of Friday', 'admitted in the government rural hospitals', 'Police at Ghoti', 'parked on the side of the road on the Mumbai Nashik lane of the highway', 'road on the Mumbai Nashik lane of the highway', 'rammed at around 4.30 am', 'rushed by the ambulance at the Ghoti toll plaza', 'ambulance at the Ghoti toll plaza', 'travelling by the private bus', 'Those at the incident spot']
# address_road: Khalchi Peth, Girnare, Igatpuri, Maharashtra 422402
# address_road: Khalchi Peth, Girnare, Igatpuri, Maharashtra 422402
# address_road: Mumbai - Agra National Hwy, Golbhan, Maharashtra 421303
# address_road: Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070
# 49 : {'coords': [['Khalchi Peth, Girnare, Igatpuri, Maharashtra 422402'], ['Khalchi Peth, Girnare, Igatpuri, Maharashtra 422402'], ['Mumbai - Agra National Hwy, Golbhan, Maharashtra 421303'], ['Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070'], [73.614707, 19.708766], [73.614707, 19.708766]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/at-least-one-dead-in-road-accident-at-mumbai-agra-highway/articleshow/99317327.cms', 'date': ' Apr 7, 2023'}
# sno: 50 soi: ['compensation under the Motor Vehicles Act MVA', 'death in accident', 'said in his March 3 order uploaded on Thursday', 'uploaded on Thursday', 'appeal by The Iffco Tokio General Insurance Co Ltd', 'incident on May 15 2010', '"rider on a friend Sakharam \'s motorbike", \'were on the Mumbai Pune road going towards Kamshet', 'knocked by an autorickshaw which was being driven in a rash and negligent manner', 'driven in a rash and negligent manner', 'treatment in hospital', '"said at the time of Ganesh \'s death", \'earned in a month', 'ply in Thane district', 'merit in the contention', 'was at the time of accident']
# address_road: Kamshet, Maharashtra 410405
# 50 : {'coords': [['Kamshet, Maharashtra 410405'], [73.37087, 19.269618]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/remarriage-cant-deny-widow-compensation-for-husbands-death-in-road-accident-says-bombay-hc/articleshow/99158309.cms', 'date': ' Apr 1, 2023'}
# sno: 51 soi: ['injured in three separate road accidents in Nashik city and parts of the rural areas on Tuesday and Wednesday', 'accidents in Nashik city and parts of the rural areas', 'accidents on Tuesday and Wednesday', 'people in the accident', 'took in Igatpuri', 'took on Tuesday', 'were on their way home', 'travelling on a bullock cart', 'following on a bike', 'died on spot', 'accident on Wednesday', 'divider on the Untawadi Road', 'going on their bike', 'works in a company in Nashik', 'company in Nashik', 'travelling in a van to Mumbai', 'overturned near Wadivarhe on the Mumbai Agra National Highway', 'Wadivarhe on the Mumbai Agra National Highway', 'overturned on Wednesday morning', 'overturned near the Vaitarna dam', 'overturned on Wednesday afternoon', 'injury in the accident']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 51 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453], [73.561107, 19.696326], [73.789802, 19.997453], [73.789802, 19.997453], [72.877656, 19.075984], [73.29061, 19.670536]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/5-dead-5-hurt-in-3-separate-road-accidents-in-nashik-city-rural/articleshow/96923595.cms', 'date': 'Jan 12, 2023'}
# sno: 52 soi: ['burst in Boisar', 'dropping at around 3 am', 'hit on the Palghar Boisar road in Umroli village', 'road in Umroli village']
# address_road: Plot no. 52, Palghar Taluka Indl. Co-Op Estate Ltd, Boisar Rd, Palghar, 401404
# address_road: QQ45+H9X, Palghar Rd, Umroli, Maharashtra 401404
# 52 : {'coords': [[72.745182, 19.796893], ['Plot no. 52, Palghar Taluka Indl. Co-Op Estate Ltd, Boisar Rd, Palghar, 401404'], ['QQ45+H9X, Palghar Rd, Umroli, Maharashtra 401404']], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/newly-wed-dies-after-tyre-burst/articleshow/98573539.cms', 'date': 'Mar 12, 2023'}
# sno: 53 soi: ['roads in the city', 'eye among other infrastructure necessary for preventing road accidents', 'accident on October 8', 'accident near Mirchi Hotel on the Nashik Aurangabad Road that had claimed 13 lives', 'Hotel on the Nashik Aurangabad Road', 'held between officials from different departments', 'roads in Nashik', 'places on the Mumbai Agra highway', 'Going by the police records', 'occurred in the city in which 182 people had lost their lives', 'lost in which', 'fatalities in the city', 'crossings at all junctions', 'chaos on all the roads in the city', 'roads in the city', 'pedestrians on the streets', 'are in constant touch with the Nashik Municipal Corporation', 'crossings on the roads']
# address_road: Aurangabad Rd, opp. janardhan Swami ashram, kapaleshwar nagar, Nashik, Maharashtra 422001
# address_road: Aurangabad Rd, opp. janardhan Swami ashram, kapaleshwar nagar, Nashik, Maharashtra 422001
# address_road: Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070
# 53 : {'coords': [['Aurangabad Rd, opp. janardhan Swami ashram, kapaleshwar nagar, Nashik, Maharashtra 422001'], ['Aurangabad Rd, opp. janardhan Swami ashram, kapaleshwar nagar, Nashik, Maharashtra 422001'], [73.789802, 19.997453], ['Lower Parel, Kurla West, Kurla, Mumbai, Maharashtra 400070'], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/most-nashik-city-roads-yet-to-get-proper-accident-prevention-features/articleshow/98439470.cms', 'date': ' Mar 6, 2023'}
# sno: 54 soi: ['student on his way to Kolhapur', 'hit by an unidentified vehicle', 'hit at 11', 'died on Saturday', 'residing in Kodoli village of Panhala tehsil', 'was on his way to Kolhapur', 'was on the service road in front of Mahalaxmi earthmovers', 'road in front of Mahalaxmi earthmovers', 'taken on a 108 ambulance', 'registered under relevant sections of the IPC and the Motor Vehicle Act']
# 54 : {'coords': [[74.243253, 16.704987], [74.190207, 16.875181], [74.243253, 16.704987]], 'link': 'https://timesofindia.indiatimes.com/city/kolhapur/17-year-old-student-killed-in-road-accident/articleshow/98056196.cms', 'date': 'Feb 19, 2023'}
# sno: 55 soi: ['injured in Bhiwandi', 'took near Madhavi chowk area', 'took on Friday evening', 'came under the rear wheel of a truck', 'booked under rash driving and negligence charges', 'suffered on a scooter', 'going on Saturday morning', 'drop at Bhiwandi railway station', 'fell on the left side', 'fell on the right side', 'suffered on her back']
# 55 : {'coords': [[73.048291, 19.281255], [73.046265, 19.26865]], 'link': 'https://timesofindia.indiatimes.com/city/thane/transgender-person-dies-two-sisters-injured-in-separate-road-accidents-in-bhiwandi/articleshow/96652280.cms', 'date': 'Dec 31, 2022'}
# sno: 56 soi: ['"truck in Maharashtra \'s Nashik district", \'collided on Friday morning', 'travelling by a luxury bus', 'hospital in Sinnar', 'am on the Nashik Ahmednagar highway', 'passengers in the private tourist bus', 'located in Ambernath', 'spread over the sleepy middle income neighbourhood in Morivali village in Ambernath', 'neighbourhood in Morivali village in Ambernath', 'village in Ambernath', 'organised by a local trader', 'accident on the Nashik Shirdi highway that claimed precious lives mostly of women and children', 'expressed over the loss of life in the incident', 'loss in the incident', 'expressed over the incident', 'helped in reducing the road accidents', 'collided in Nashik']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# address_road: Shop No.1 Near Wadangali, Sinnar - Shirdi Rd, Kirtangali, Maharashtra 422210
# 56 : {'coords': [[74.030012, 20.16235], [73.988965, 19.847981], ['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.192602, 19.182517], [73.200598, 19.201159], [73.200598, 19.201159], [73.192602, 19.182517], ['Shop No.1 Near Wadangali, Sinnar - Shirdi Rd, Kirtangali, Maharashtra 422210'], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/10-pilgrims-killed-in-collision-between-bus-and-truck-in-maharashtras-nashik/articleshow/96955306.cms', 'date': 'Jan 13, 2023'}
# sno: 57 soi: ['died on Friday', 'riding on', 'knocked by a speeding truck driver in Mhasrul area of the city', 'driver in Mhasrul area of the city', 'Based on the complaint of the Jadhav ’s son', 'punishable under section 304 A', 'knocked by the speeding truck', 'suffered in the accident']
# 57 : {'coords': [[73.807953, 20.046649], [73.807953, 20.046649]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/elderly-man-dies-in-road-accident/articleshow/96842711.cms', 'date': ' Jan 9, 2023'}
# sno: 58 soi: ['killed in two separate road accidents in Nashik', 'accidents in Nashik', 'killed on Monday and Tuesday', 'reported at the Gangapur and Panchavati police stations', 'native in the Gaya district of Bihar', 'speeding on the flyover', 'speeding at Mumbai Agra highway', 'speeding at around 1 am on Tuesday', 'am on Tuesday', 'rammed at around 11.30pm', 'rammed on Monday', 'reasons behind the accidents in both these cases', 'accidents in both these cases']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# address_road: Mumbai - Agra National Hwy, Vikhroli, Mumbai, Maharashtra 400042
# 58 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453], [73.791878, 20.009549], ['Mumbai - Agra National Hwy, Vikhroli, Mumbai, Maharashtra 400042']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/two-killed-in-separate-road-accidents/articleshow/96752146.cms', 'date': ' Jan 5, 2023'}
# sno: 59 soi: ['departments in Maharashtra', 'store in a nation wide crash data application which goes by the name of Integrated Road Accident Database IRAD', 'goes by the name of Integrated Road Accident Database IRAD', 'conducted in various districts', 'concluded on Wednesday evening', 'is on scientific investigation of the accident', 'installing at black spots accident prone', 'awareness on traffic rules and road safety', 'creating in areas where mishaps are high', 'accidents at various sites', 'involved in mishap', 'site by various departments', 'collated in the iRAD app which analyses the data scientifically to produce reports on the cause and solutions', 'reports on the cause and solutions', 'registered on an average 2']
# 59 : {'coords': [[75.713888, 19.75148]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/over-1000-officials-from-maharashtra-get-training-to-collect-scientific-data-at-road-crash-sites/articleshow/96628585.cms', 'date': 'Dec 30, 2022'}
# sno: 60 soi: ['refinery in Ratnagiri', 'met on Monday', 'Rajapur in Ratnagiri who had been rushed to hospital in Kolhapur', 'rushed in Kolhapur', 'crashed at the exit of a petrol pump', 'amounting under certain circumstances causing death', 'issue in Parliament', 'threatened at them', 'run over others including the son of a sarpanch who ended up losing the use of both legs', 'made by farmers']
# 60 : {'coords': [[73.312023, 16.990215], [74.243253, 16.704987], [74.243253, 16.704987]], 'link': 'https://timesofindia.indiatimes.com/city/navi-mumbai/hours-after-report-against-maharashtra-refinery-journo-killed/articleshow/97751593.cms', 'date': ' Feb 9, 2023'}
# sno: 61 soi: ['killed in road accidents', 'killed over the past two years', 'killed in Nashik', 'provided by the city traffic police', 'taken on the city roads', 'number in 2021', 'encroached in several parts of the city', 'walk on the roads', 'knocked by overspeeding vehicles on a continuous basis', 'overspeeding on a continuous basis', 'walking on the road', 'knocked by a motorist', 'walking on Madsangvi Road', 'hit by an unidentified motorist', 'walking on the streets', 'populated over the years', 'knocked by vehicles', 'dying in the accidents on the Pune Highway near her locality', 'accidents on the Pune Highway near her locality', 'Highway near her locality', 'dying over the years', 'year in 2021', 'deaths in road accidents']
# address_road: Maharashtra
# address_road: Maharashtra
# 61 : {'coords': [[73.789802, 19.997453], ['Maharashtra'], ['Maharashtra']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/pedestrians-make-up-26-of-road-deaths-in-nashik-city-in-last-2-years/articleshow/97615495.cms', 'date': ' Feb 5, 2023'}
# sno: 62 soi: ['fatalities in rural Nashik', 'died in road accidents', 'died in 10 months', 'killed in accidents in the rural areas', 'accidents in the rural areas', 'died in accidents', 'died in 2020', 'those in the cars buses and pedestrians', 'issued in four days', 'continue in the future', 'inculcate among the motorists', 'going on the other side of the road', 'going by breaking them', 'spots in rural Nashik', 'are in communication with the departments concerned responsible for repair and maintenance of roads', 'accidents on the black spots']
# 62 : {'coords': [[73.789802, 19.997453], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/over-750-killed-this-year-in-rural-nashik-road-accidents/articleshow/95547232.cms', 'date': 'Nov 16, 2022'}
# sno: 63 soi: ['driving on no entry roads', 'routes in a special drive launched between January 20 and 31', 'launched between January 20 and 31', 'driving on the wrong side', 'killed in road accidents in Pimpri Chinchwad that occurred due to rash driving', 'accidents in Pimpri Chinchwad', 'collected in fines']
# address_road: Old Mumbai - Pune Hwy, Anand Nagar, Pimpri Colony, Pimpri-Chinchwad, Maharashtra 411019
# 63 : {'coords': [['Old Mumbai - Pune Hwy, Anand Nagar, Pimpri Colony, Pimpri-Chinchwad, Maharashtra 411019'], [73.799709, 18.629781]], 'link': 'https://timesofindia.indiatimes.com/city/pune/over-5k-traffic-violators-fined-in-pcmc-limits-in-11-days/articleshow/97567321.cms', 'date': ' Feb 3, 2023'}
# sno: 64 soi: ['hit at Charoti', 'hit on the Mumbai Ahmedabad national highway at Dahanu', 'highway at Dahanu', 'hit in Palghar district', 'highway near the Mahalaxmi temple', 'reached at Charoti', 'killed on the spot', 'killed on the spot', 'accident in and around Charoti', 'crashed near the Mahalaxmi temple', 'lost in an accident on the highway near Charoti', 'accident on the highway near Charoti', 'highway near Charoti', 'lost on September 4 last year']
# address_road: XPQQ+XRR, Dahanu - Jawhar Rd, Malyan, Dahanu, Maharashtra 401601
# address_road: XPQQ+XRR, Dahanu - Jawhar Rd, Malyan, Dahanu, Maharashtra 401601
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# 64 : {'coords': [[72.930897, 19.919552], ['XPQQ+XRR, Dahanu - Jawhar Rd, Malyan, Dahanu, Maharashtra 401601'], ['XPQQ+XRR, Dahanu - Jawhar Rd, Malyan, Dahanu, Maharashtra 401601'], [72.993297, 19.786716], [72.930897, 19.919552]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/four-dead-as-car-hits-bus-on-mumbai-ahmedabad-highway-at-charoti-in-palghar/articleshow/97471423.cms', 'date': 'Jan 31, 2023'}
# sno: 65 soi: ['hit in an attempt to overtake it at Bhosari Phata on the Pune Mumbai highway in the early hours of Tuesday', 'overtake at Bhosari Phata', 'overtake on the Pune Mumbai highway', 'overtake in the early hours of Tuesday', 'plying on the same route', 'fell on the road', 'suffered in the accident', 'involving in the recent past', 'hit by a private bus at Mali Mala', 'bus at Mali Mala', 'hit on the Pune Solapur road in Loni Kalbhor', 'road in Loni Kalbhor', 'hit on January 24', 'knocked at Gunjan Chowk on Pune Ahmednagar Road in Yerwada', 'Chowk on Pune Ahmednagar Road in Yerwada', 'Road in Yerwada', 'crossing on October 31 2022']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 66 soi: ['killed in a road accident', 'travelling in', 'knocked by a pickup truck near Wadner Dumala', 'truck near Wadner Dumala', 'knocked on December 6', 'going at about 1.30 pm', 'going on Tuesday', 'travelling on his bike', 'injuries on his head and in his chest']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 67 soi: ['heat on motorists and bikers flouting road rules', 'speaking on cellphone', 'at in such a way that obstructs the traffic', 'took in no parking areas', 'driving in no entry lanes', 'died in road accidents', 'knocked by over speeding motorists', 'spread among bikers on the helmet rule', 'bikers on the helmet rule', 'jumping in 2021', 'speaking on cellphones', 'be on the radar of the traffic police', 'speaking on cellphone', 'hit in 2021']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 68 soi: ['procession at Junoni village along Miraj Pandharpur highway in Solapur district', 'highway in Solapur district', 'rammed on Monday evening', '25 in number', 'taking on November 4', 'is under way', 'village near Kolhapur city', 'admitted in the hospital', 'registered in Solapur']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 69 soi: ['death in 461 accidents in Nashik city', 'accidents in Nashik city', 'reasons in 2022', 'compiled by the Nashik city police', 'than in 2022', 'killed in 470 accidents', 'accounted in 2022', 'speaking on their cellphones', 'accident at the Mirchi hotel chowk', 'accident on October 8', 'set at these blackspots', 'number in the city', 'safety on the streets', 'number on city roads', 'taken in the city']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 70 soi: ['killed in a road accident on the elevated corridor of the Mumbai Agra highway in the Ambad area', 'accident on the elevated corridor of the Mumbai Agra highway in the Ambad area', 'highway in the Ambad area', 'killed on Saturday night', 'riding on the elevated corridor of the Mumbai Agra highway', 'injuries on his head and leg injuries']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 71 soi: ['died in the collision between the bus', 'collision between the bus', 'truck on the Sinnar Shirdi highway', 'travelling on Friday morning', 'issued by the CM ’s office CMO', 'travelling on the way to the temple town of Shirdi', 'hospitals in Sinnar town', 'was on his way to Mumbai from Malegaon', 'went at Sinnar town where the injured were undergoing treatment', 'said in a statement']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 72 soi: ['ratio in Maharashtra', 'Bhimanwar at the inauguration of Road Safety Week at NCPA on Wednesday', 'inauguration at NCPA', 'inauguration on Wednesday', 'campaign on Mumbai Pune route', 'counselled in 40 days', 'speeding over 100kmph', 'speeding on the Expressway and old highway', 'reduction in fatalities', 'reduction in 2022-', 'deaths in road crashes', 'from in 2021', 'were in the age group of 18 45 years', 'died on roads', 'died in 2022', 'take in order to bring down the fatalities', 'reduce by 50 %', 'reduce in five years', 'set by the Centre', 'launch at the NCPA', 'packed at 11.30am with officials NGOs students union members and all stakeholders of road safety', 'inaugurate on his behalf', 'was at the launch', 'fatalities in the state', 'halve in the next few years']
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# error in driver1: []
# sno: 73 soi: ['halted on the corner of the Western Express Highway WEH', 'halted at Malad East in Mumbai', 'East in Mumbai', 'occurred on Sunday', 'booked on charges of negligence', 'gone on Saturday', 'headed on their motorcycles', 'take at 3.45am', 'take near Kurar metro station on the WEH', 'station on the WEH', 'halted on the same stretch', 'Hospital in Kandivali', 'rushed in an auto', 'pronounced by doctors at the hospital', 'doctors at the hospital', 'crash on November 18', 'rammed on the Veer Savarkar flyover at Goregaon', 'flyover at Goregaon', 'spoke at 10.15pm over the phone', '10.15pm over the phone', 'registered on Sunday']
# address_road: Goregaon Flyover East entry, Yashodham, Goregaon West, Mumbai, Maharashtra 400063
# address_road: Sahgadri Building, Aarey Rd, Peru Baug, Jay Prakash Nagar, Goregaon West, Mumbai, Maharashtra 400063
# 73 : {'coords': [[72.858476, 19.185378], [72.877656, 19.075984], [72.851819, 19.202949], ['Goregaon Flyover East entry, Yashodham, Goregaon West, Mumbai, Maharashtra 400063'], ['Sahgadri Building, Aarey Rd, Peru Baug, Jay Prakash Nagar, Goregaon West, Mumbai, Maharashtra 400063']], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/mumbai-2-motorcyclists-killed-in-separate-road-crashes-in-western-suburbs/articleshow/95695892.cms', 'date': 'Nov 22, 2022'}
# sno: 74 soi: ['injured in road accidents in Nashik city', 'accidents in Nashik city', 'indulge in rash driving', 'registered by the city police', 'registered over the past seven days', 'rush on the city streets', 'rise in the road accidents', 'indulge in rash driving', 'are in large numbers on the streets', 'numbers on the streets', 'indulging in rash driving', 'parking on the road side', 'die in road accidents in Nashik city', 'accidents in Nashik city']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 74 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453], ['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/seven-days-into-new-year-4-killed-in-road-accidents/articleshow/96825184.cms', 'date': ' Jan 8, 2023'}
# sno: 75 soi: ['died in a road accident', 'died on Saturday evening', 'hit at Golevadi village', 'hit in Maval Taluka', 'run by the front wheels of the dumper', 'killed on the spot', 'outing on Saturday', 'stopped at Golewadi village along the Mangarul Ambi Road', 'stuck in the front wheels']
# address_road: WPX3+XF2, Golewadi, Maharashtra 412806
# 75 : {'coords': [['WPX3+XF2, Golewadi, Maharashtra 412806']], 'link': 'https://timesofindia.indiatimes.com/city/pune/engineering-student-dies-after-dumper-hits-his-bike/articleshow/96672187.cms', 'date': ' Jan 2, 2023'}
# sno: 76 soi: ['killed in two separate accidents in Nashik', 'accidents in Nashik', 'killed on Friday and Saturday', 'run by a tractor', 'run in a village in the Adgoan area', 'village in the Adgoan area', 'run on Friday', 'arrested on the charge of causing death due to negligence', 'playing on a farm in the Madsangvi area', 'farm in the Madsangvi area', 'came in front of the tractor', 'died on the spot', 'driving on Saturday', 'suffered in the accident']
# 76 : {'coords': [[73.789802, 19.997453], [75.433016, 19.820033], [75.433016, 19.820033], [73.873168, 20.001676]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/2-year-old-girl-among-2-killed-in-separate-road-accidents/articleshow/98076536.cms', 'date': 'Feb 20, 2023'}
# sno: 77 soi: ['away at work', 'murdered in Kashimira', 'murdered in 1994', 'came at 11 pm', 'died in 2006', 'died in a road accident', 'confronted in public', 'booked by the Kashimira police', 'visited in UP', 'visited in June 2021', 'spending in the city', 'working in Qatar', 'Based on the details', 'checkpoints in the country', 'walked at Mumbai airport']
# 77 : {'coords': [[72.885516, 19.279875], [72.874661, 19.097536]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/cops-spent-20-days-in-varanasi-on-killers-trail/articleshow/96634814.cms', 'date': 'Dec 31, 2022'}
# sno: 78 soi: ['died on the spot', 'riding on which', 'came under the wheels of a sugar cane laden trolley pulled by a tractor', 'pulled by a tractor', 'took on Monday evening near Shirol where the deceased Puja Mali lived', 'evening near Shirol where the deceased Puja Mali lived', 'registered in Shirol Police Station']
# 78 : {'coords': [[74.590887, 16.748041], [74.590887, 16.748041]], 'link': 'https://timesofindia.indiatimes.com/city/kolhapur/22-year-old-woman-dies-in-road-accident/articleshow/96386567.cms', 'date': 'Dec 21, 2022'}
# sno: 79 soi: ['led by MPCC president Nana Patole and senior NCP leader Ajit Pawar', 'cornered over potholed roads and growing number of accidents in the state', 'number in the state', 'Speaking on the calling attention motion moved by members Vijay Wadettiar Ashok Chavan Sunil Kedar and others', 'moved by members Vijay Wadettiar Ashok Chavan Sunil Kedar and others', 'measures on roads and highways', 'claimed in accidents due to over speeding', 'due over speeding', 'travelling on it', 'put on speeding vehicles', 'washrooms on Samruddhi Expressway', 'running on this road', 'travelled in a Mercedes which will not be affected', 'happen in summer', 'concern over the rising trend of signal jumping and wrong lane driving', 'blamed on the lack of discipline and meagre penalty against the offenders', 'lights in the tunnels built by the MSRDC', 'built by the MSRDC', 'death in an accident on the Mumbai Pune expressway', 'accident on the Mumbai Pune expressway', 'called on the government', 'accident at Yavatmal', 'accident on October 7', 'hit by a speeding truck', 'concern over private travels taking in more passengers than permitted in their buses', 'permitted in their buses', 'accidents at Yavatmal and other places and chief minister Eknath Khadse', 'created in the last two and half years of Maha Vikas Aghadi MVA tenure and why they were not filled up', 'sustain at 150 km hour', 'fixed at 120km/ hour', 'installed at regular intervals and violators', 'warned at every toll booth', 'stopped at toll booths', 'beef on all exit routes of the state and national highways', 'transportation by passenger bus', 'are in working condition']
# address_road: Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702
# address_road: Maharashtra
# address_road: Maharashtra
# 79 : {'coords': [['Survey No. 115/P , Samrudhi Expressway, Tal, Anantpur, Gangapur, Aurangabad, Maharashtra 423702'], ['Maharashtra'], ['Maharashtra'], [78.130685, 20.389939], [78.130685, 20.389939]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/opposition-corners-govt-on-potholed-roads-accidents-and-samruddhi/articleshow/96380241.cms', 'date': 'Dec 21, 2022'}
# sno: 80 soi: ['Galli in Raviwar Peth', 'found on a road near Kamgar statue', 'road near Kamgar statue', 'found on December 16', 'injured in a road accident', 'hit by an autorickshaw', 'remaining in the hospital', 'spot near Kamgar statue']
# address_road: Sairatna Building, Kapad Ganj, Raviwar Peth, Pune, Maharashtra 411002
# address_road: 58MM+8VQ, Ambekar Nagar, Nanded, Nanded-Waghala, Maharashtra 431605
# address_road: 58MM+8VQ, Ambekar Nagar, Nanded, Nanded-Waghala, Maharashtra 431605
# 80 : {'coords': [['Sairatna Building, Kapad Ganj, Raviwar Peth, Pune, Maharashtra 411002'], ['58MM+8VQ, Ambekar Nagar, Nanded, Nanded-Waghala, Maharashtra 431605'], ['58MM+8VQ, Ambekar Nagar, Nanded, Nanded-Waghala, Maharashtra 431605'], [77.329068, 19.182435]], 'link': 'https://timesofindia.indiatimes.com/city/pune/murder-ruled-out-in-plumber-death-case/articleshow/96584556.cms', 'date': 'Dec 29, 2022'}
# sno: 81 soi: ['compared in 2021', 'died in road accidents in Nashik city', 'accidents in Nashik city', 'reported on the city roads', 'provide on the city roads', 'others on the road', 'spread among motorists', 'putting at the same time', 'taking under the guidance of CP Ankush Shinde and DCP Pournima Chaugule the city traffic branch and the police', 'personnel on the streets', 'survey by the Mumbai', 'spots in the city']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 81 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453], [72.877656, 19.075984]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/fewer-accidents-casualties-same-as-last-year-in-nashik/articleshow/96469941.cms', 'date': 'Dec 24, 2022'}
# sno: 82 soi: ['rammed in Raigad district', 'rammed on Monday', 'took near Khopoli', 'took on the Mumbai Pune Expressway', 'banged on the windscreen that broke and', 'taken in Kamothe where the bus driver was declared brought dead']
# address_road: Maharashtra
# 82 : {'coords': [[73.182162, 18.515752], [73.334643, 18.793905], ['Maharashtra'], [73.096602, 19.016622]], 'link': 'https://timesofindia.indiatimes.com/city/navi-mumbai/bus-driver-killed-10-passengers-injured-in-road-accident-in-raigad/articleshow/96333952.cms', 'date': 'Dec 19, 2022'}
# sno: 83 soi: ['programme on traffic', 'spread among the students', 'indulge in rash', 'people on the road', 'inculcated in minds of students', 'inculcated at a young age', 'lost in road accidents in the district', 'accidents in the district', 'taken by the association of RTO officers', 'taken at the national level', 'undertaken in a few districts', 'undertaken at the initial stage', 'people at a young age']
# sno: 84 soi: ['killed in a road accident', 'killed on Sunday', 'killed at around 8.30', 'am near the Adgaon bridge', 'knocked by a speeding biker', 'punishable under section 304 A of the Indian penal code', 'was in Nashik', 'suffered in the accident']
# 84 : {'coords': [[73.86356, 20.03347], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/nashik-pedestrian-killed-in-road-accident/articleshow/95070294.cms', 'date': 'Oct 25, 2022'}
# sno: 85 soi: ['killed on the spot', 'had on collision with an ST bus coming from the opposite direction in village Loni near Ner tehsil of Yavatmal district on the Nagpur Amravati National Highway on Sunday morning at 11 am', 'direction in village Loni', 'direction near Ner tehsil of Yavatmal district on the Nagpur Amravati National Highway', 'tehsil on the Nagpur Amravati National Highway', 'coming on Sunday morning', 'coming at 11 am', 'gone on Saturday', 'gone in their car', 'returning on Sunday morning', 'head on collision with an ST bus plying from Ralegaon to Amravati', 'were in the ill fated car']
# address_road: Yavatmal Ralegaon Road near Gov ITI Bembla Patbandhare Sub Division No 4 Ralegaon Ralegaon, Pahur, Maharashtra 445402
# address_road: Ner, Maharashtra 445102
# address_road: Near, Railway Station Rd, Baba Farid Nagar, Sitabuldi, Nagpur, Maharashtra 440001
# 85 : {'coords': [['Yavatmal Ralegaon Road near Gov ITI Bembla Patbandhare Sub Division No 4 Ralegaon Ralegaon, Pahur, Maharashtra 445402'], ['Ner, Maharashtra 445102'], ['Near, Railway Station Rd, Baba Farid Nagar, Sitabuldi, Nagpur, Maharashtra 440001'], [77.752304, 20.931982]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/four-dead-six-injured-in-yavatmal-road-accident/articleshow/95986115.cms', 'date': 'Dec 5, 2022'}
# sno: 86 soi: ['rising in the city', 'children below 18 years of age', 'are in the city and on the outskirts', 'offences in court', 'driving on the roads', 'Youngsters in the age group of 16 to 18', 'held in Kolhapur', 'held on Monday', 'rise in road accidents in the district', 'accidents in the district']
# 86 : {'coords': [[74.243253, 16.704987]], 'link': 'https://timesofindia.indiatimes.com/city/kolhapur/cases-against-27-parents-for-giving-2-wheelers-to-underage-children/articleshow/96213858.cms', 'date': 'Dec 14, 2022'}
# sno: 87 soi: ['witnessed in 2022', 'rose in 2022', 'told at Police Bhavan', 'told on Friday', 'movement in the city', 'brought under control', 'brought in 2022', 'came in 2022', 'lowest in the last 21 years', 'cases in 2022', 'decline in crime on all counts', 'crime on all counts', 'booked under MPDA and MCOCA', 'booked in 2022', 'control in the state ’s second capital', 'committed by a family member or a known person', 'reported in 2022', 'was in 2021', 'issues in love affairs or friendships', 'tortured in a friendship or a relationship', 'abuse by relatives and acquaintances', 'incidents by an unknown person', 'increase in cases of vehicle thefts', 'cases in 2021']
# sno: 88 soi: ['travelling in rammed a stationary truck near Nasrapur about 35 km from the city', 'rammed near Nasrapur', 'killed in the early hours of Thursday', 'brother in law', 'were on their way to Pune airport', 'son in law', 'left on Wednesday', 'injuries in the accident', 'putting on the road', 'reached near Nasrapur', 'reached on Thursday when the car rammed the stationary truck', 'was at the back seat']
# 88 : {'coords': [[73.879763, 18.249321], [73.879763, 18.249321], [73.908917, 18.579343], [73.879763, 18.249321]], 'link': 'https://timesofindia.indiatimes.com/city/pune/day-before-girls-wedding-father-killed-in-road-accident/articleshow/96124061.cms', 'date': 'Dec 10, 2022'}
# sno: 89 soi: ['were in different vehicles', 'minor in nature', 'death in the horrific accident involving five vehicles including an MSRTC bus', 'include at the busy Palse village chowk around 20 km from Nashik city', 'include on the Nashik Pune national highway on Thursday morning', 'highway on Thursday morning', 'rammed near the chowk', 'rammed at around 11.45am', 'was on its way from Sinnar to Nashik', 'accidents between April and November', 'was at fault', 'Enquiries in two more cases', 'buses in its fleet for Nashik division district', 'distance on a daily basis', 'courses on a regular basis', 'involved in accidents']
# address_road: Office no 15 Building no A 5 Potnis Parisar, Karve Nagar, Pune:411058, Maharashtra 411058
# 89 : {'coords': [[73.789802, 19.997453], ['Office no 15 Building no A 5 Potnis Parisar, Karve Nagar, Pune:411058, Maharashtra 411058'], [73.988965, 19.847981], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/114-road-accidents-involving-st-buses-in-nashik-district-in-8-months-9-deaths/articleshow/96123894.cms', 'date': 'Dec 10, 2022'}
# sno: 90 soi: ['run by a speeding truck', 'run on Saturday evening', 'riding on the scooter', 'took near Lakshika Hall', 'took on the road from ABB Circle to the City Centre Mall signal', 'registered by Bhave ’s son', 'travelling on their scooter', 'run by the truck', 'died on the spot', 'fell on the other side of the road', 'injuries on her left shoulder and leg', 'punishable under sections 279']
# address_road: Trambakeshwar Rd, Satya Colony, Parijat Nagar, Nashik, Maharashtra 422005
# 90 : {'coords': [[73.760142, 19.991358], ['Trambakeshwar Rd, Satya Colony, Parijat Nagar, Nashik, Maharashtra 422005']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/elderly-man-killed-in-road-accident-in-nashik-city/articleshow/95842798.cms', 'date': 'Nov 29, 2022'}
# sno: 91 soi: ['killed in three separate road accidents across the district', 'killed between Friday and Sunday', 'died in an accident', 'died on Sunday afternoon', 'took on the Sinnar Shirdi Road', 'took near Phule Nagar Phata', 'took at around 12.30 pm', 'Panchavati in Nashik city', 'died on the spot', 'killed in an accident', 'travelling in', 'knocked by a speeding vehicle on the road in front of Prabhat Nagar Mhasrul', 'vehicle on the road in front of Prabhat Nagar Mhasrul', 'road in front of Prabhat Nagar Mhasrul', 'knocked on Friday', 'knocked at around 8 pm', 'killed in a road accident', 'killed on Friday', 'killed at around 11 pm', 'travelling in', 'hit by a speeding four wheeler near the Jail Road water tank', 'wheeler near the Jail Road water tank']
# address_road: Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004
# address_road: Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004
# address_road: Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004
# 91 : {'coords': [[73.823895, 18.622388], [73.791878, 20.009549], ['Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004'], ['Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004'], ['Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/four-people-killed-in-3-separate-road-accidents-in-nashik/articleshow/96161375.cms', 'date': 'Dec 12, 2022'}
# sno: 92 soi: ['killed in three separate road accidents across the district', 'killed between Friday and Sunday', 'died in an accident', 'died on Sunday afternoon', 'took on the Sinnar Shirdi Road', 'took near Phule Nagar Phata', 'took at around 12.30 pm', 'Panchavati in Nashik city', 'died on the spot', 'killed in an accident', 'travelling in', 'knocked by a speeding vehicle on the road in front of Prabhat Nagar Mhasrul', 'vehicle on the road in front of Prabhat Nagar Mhasrul', 'road in front of Prabhat Nagar Mhasrul', 'knocked on Friday', 'knocked at around 8 pm', 'killed in a road accident', 'killed on Friday', 'killed at around 11 pm', 'travelling in', 'hit by a speeding four wheeler near the Jail Road water tank', 'wheeler near the Jail Road water tank']
# address_road: STICE, C 16, Sinnar - Shirdi Rd, Industrial Area, Musalgaon, Maharashtra 422112
# address_road: Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004
# address_road: Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004
# address_road: Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004
# 92 : {'coords': [['STICE, C 16, Sinnar - Shirdi Rd, Industrial Area, Musalgaon, Maharashtra 422112'], [73.823895, 18.622388], [73.791878, 20.009549], ['Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004'], ['Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004'], ['Vaiduwadi, Mhasrul Gaon, Nashik, Maharashtra 422004']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/four-people-killed-in-3-separate-road-accidents-in-district/articleshow/96160479.cms', 'date': 'Dec 12, 2022'}
# sno: 93 soi: ['lost over the vehicle', 'rammed in Khalapur', 'rammed on Monday', 'hospital in Kamothe']
# 93 : {'coords': [[73.284645, 18.830552], [73.096602, 19.016622]], 'link': 'https://timesofindia.indiatimes.com/city/navi-mumbai/maharashtra-5-injured-as-bus-rams-into-median-in-khalapur/articleshow/93996739.cms', 'date': ' Sep 5, 2022'}
# sno: 94 soi: ['killed in separate road accidents in Nashik city', 'accidents in Nashik city', 'killed on Friday', 'knocked by a speeding ghantagadi on the service road along the Mumbai Agra highway', 'ghantagadi on the service road along the Mumbai Agra highway', 'punishable under section 304', 'causing by negligence and rash driving', 'riding on the service road from Pathardi Phata', 'booked on the charges of causing death due to negligence', 'riding on the wrong side of the road', 'riding near a nursery in Adgaon', 'nursery in Adgaon', 'treated at a private hospital where he succumbed to his injuries on October 23', 'succumbed on October 23']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# address_road: Mumbai - Agra National Hwy, Vikhroli, Mumbai, Maharashtra 400042
# address_road: Indiranagar Pathardi Rd, Pathardi Gaon, Pathardi Phata, Nashik, Maharashtra 422010
# 94 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453], ['Mumbai - Agra National Hwy, Vikhroli, Mumbai, Maharashtra 400042'], ['Indiranagar Pathardi Rd, Pathardi Gaon, Pathardi Phata, Nashik, Maharashtra 422010'], [73.86356, 20.03347], [73.86356, 20.03347]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/two-killed-in-separate-road-accidents-in-nashik/articleshow/95174428.cms', 'date': 'Oct 30, 2022'}
# sno: 95 soi: ['lay at Rs 750 crore', 'travel in Shirdi', 'movement on this route', 'inspected in the last week of October', 'start by early 2023', 'made in the new plan', 'undertake at Rs 450 crore', 'project in our fresh proposal', 'included in it', 'was under the state public works department PWD', 'was in a deplorable state', 'lost in road accidents on the road', 'accidents on the road', 'been among local residents about the poor condition of the road', 'is in full swing', 'completed in near future', 'road in some parts']
# 95 : {'coords': [[74.476212, 19.764536]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/ahmednagar-shirdi-nh-to-be-re-laid-at-750-crore/articleshow/95797633.cms', 'date': 'Nov 27, 2022'}
# sno: 96 soi: ['reduce by taking appropriate measures', 'based on the time they took place', 'took between 8 pm and midnight', 'followed by the 4 8pm slot', 'movement on city roads', 'vehicles on the streets', 'out on the roads', 'taken among the six time slots', 'taken between 8 pm and midnight along', 'followed by 81 accidents between 4 and 8 pm', 'accidents between 4 and 8 pm', 'accidents between 8 am and noon', 'accidents between noon and 4 pm', 'presentation on this analysis', 'gave at a recently called parliamentary road safety committee meeting which was chaired by Union minister Bharati Pawar and Nashik city MP Hemant Godse', 'chaired by Union minister Bharati Pawar and Nashik city MP Hemant Godse', 'presentation on accident analysis', 'number in the rural areas', 'took between 4 and 8 pm', 'followed by the 8 pm to midnight time period', 'took between 4 and 8 pm', 'took between 8 pm and midnight', 'took between midnight and 4 am', 'took in the 4 8am slot', 'took between 8 am and noon', 'took between noon and 4 pm']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 96 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/8pm-midnight-is-peak-time-for-nashik-city-road-accidents/articleshow/95797618.cms', 'date': 'Nov 27, 2022'}
# sno: 97 soi: ['injured in 250 accidents reported between January 1 to October 31 this year', 'reported between January 1', 'reported in the 10 months which included 239 fatal 363 serious and 249 minor accidents', 'carried by traffic police', 'was in 153 cases in which 58 people were killed', 'killed in which', 'followed by speeding as the major cause of road accidents', 'penalized in the last 10 months', 'fear in breaking traffic rules']
# sno: 98 soi: ['hit by a dumper at Kashimira', 'dumper at Kashimira', 'hit on Friday', 'seated on the rear seat of the car', 'injuries in his neck and back', 'heading in Palghar district where deaths of two children due to malnutrition were reported', 'occured at around 11.30am', 'reached at Kashimira the dumper that was heading from Kandivli to Kaman in Vasai', 'heading in Vasai', 'Hospital in Andheri', 'ply on the Mumbai Ahmedabad highway']
# address_road:
# 98 : {'coords': [[72.885516, 19.279875], [72.885516, 19.279875], [72.993297, 19.786716], [72.851819, 19.202949], [72.839732, 19.391928], [72.869734, 19.113645], ['']], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/former-maharashtra-health-minister-deepak-sawant-injured-in-road-accident/articleshow/97174887.cms', 'date': 'Jan 20, 2023'}
# sno: 99 soi: ['knocked by an unidentified autorickshaw driver in the Mumbai Naka area', 'driver in the Mumbai Naka area', 'knocked at 11 am on Wednesday', 'am on Wednesday', 'Telpa in Bihar', 'residence in the Bhujbal Farm area', 'area near a water tank', 'injuries on his head and his right hand', 'undergoing on Thursday', 'guard in a restaurant in the Bhujbal Farm area', 'restaurant in the Bhujbal Farm area']
# 99 : {'coords': [[73.784557, 19.987717], [73.784557, 19.987717], [73.774082, 19.978115], [73.774082, 19.978115], [73.774082, 19.978115]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/cyclist-killed-in-road-accident/articleshow/94409008.cms', 'date': 'Sep 24, 2022'}
# sno: 100 soi: ['travelling in rammed into a road divider in the Mohadari Ghat on the Nashik Pune highway near Sinnar', 'divider in the Mohadari Ghat', 'rammed on the Nashik Pune highway near Sinnar', 'highway near Sinnar', 'travelling on Tuesday', 'vehicle in front of him']
# address_road:
# address_road:
# address_road:
# 100 : {'coords': [[''], [73.942228, 19.885642], [''], ['']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/woman-killed-in-road-accident/articleshow/93742384.cms', 'date': 'Aug 24, 2022'}
# sno: 101 soi: ['stand on the enforcement of traffic laws', 'said on Saturday', 'session on Scientific Crash Investigation', 'attended by deputy RTOs assistant RTOs motor vehicle inspectors and assistant motor vehicle inspectors', 'devastation in the affected families', 'adults in the age group of 18 45 years', 'said in foreign countries like Japan', 'is in India', 'rise in road accidents', 'hall at the city RTO premises in Giripeth', 'premises in Giripeth', 'Karpe among others', 'participated in the workshop', 'helps in educating women on motor vehicles along with making them aware of various government schemes', 'educating on motor vehicles', 'formed in other districts', 'enforcement on Mumbai Pune Expressway', 'accidents on the Mumbai Pune Expressway', 'enforcement on these two busy roads', 'here on Friday', 'focus on taking action against vehicles indulging in over speeding and lane cutting which are the two main reasons for accidents on these two highways', 'indulging over speeding and lane cutting which are the two main reasons for accidents on these two highways', 'accidents on these two highways', 'deployed on these roads', 'crackdown on vehicles violating the Motor Vehicles Act', 'work in three shifts', 'keep on violators']
# address_road:
# address_road:
# 101 : {'coords': [[79.067788, 21.143708], [''], ['']], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/enforcement-can-bring-down-road-accidents-transport-commissioner/articleshow/95794464.cms', 'date': 'Nov 27, 2022'}
# sno: 102 soi: ['roads in Nashik city', 'check on the vehicular traffic', 'keeping on these roads', 'growth in terms of new residential and commercial areas', 'burden on the traffic branch', 'provided in mid-2017', 'results in road casualties', 'killed in road accidents in Nashik city', 'accidents in Nashik city']
# 102 : {'coords': [[73.789802, 19.997453], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/just-300-traffic-personnel-struggle-to-man-2200km-of-nashik-city-roads/articleshow/95498609.cms', 'date': 'Nov 14, 2022'}
# sno: 103 soi: ['absence on most of the roads in the city', 'roads in the city', '% in the city', 'deaths in Nashik', 'walking on the streets', 'chaos on the street', 'wait at the nearest junction to cross the road', 'halt on zebra stripes or beyond them', 'killed in road mishaps', 'safety on the roads', 'painted on all the important junctions and crossings for the convenience of pedestrians', 'written in this regard', 'painted at the earliest']
# 103 : {'coords': [[73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/missing-faded-zebra-stripes-strip-pedestrians-of-safety-on-nashik-roads/articleshow/95481703.cms', 'date': 'Nov 14, 2022'}
# sno: 104 soi: ['hit by a yet to be identified vehicle near Chitegaon Phata', 'vehicle near Chitegaon Phata', 'hit on the Nashik Aurangabad state highway', 'hit on Thursday night', 'farm on the state highway', 'centre in Junnar', 'centre in Pune district', 'occurred on Thursday', 'occurred at a place between Chitegaon Phata and Chandori when the leopard was trying to cross the road and was hit by the vehicle', 'place between Chitegaon Phata and Chandori when the leopard was trying to cross the road and was hit by the vehicle', 'hit by the vehicle', 'stayed on the road', 'farm near the state highway', 'trapped in a cage', 'centre in Junnar', 'killed in accidents on the state and national highways passing through the district', 'accidents on the state and national highways passing through the district', 'hit by vehicles', 'hit on highways', 'drowning in wells and road accidents', 'spread over Junnar Ambegaon Shirur and Khed tehsils', 'number in this division', 'concern in the division', 'number in Junnar division', 'are in the sugar cane fields', 'results in accidents']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# address_road: 2XWC+4RH, Kherwadi, Maharashtra 422201
# address_road: 2XWC+4RH, Kherwadi, Maharashtra 422201
# 104 : {'coords': [[73.95463, 20.026936], [73.95463, 20.026936], ['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.87425, 19.203184], [74.030012, 18.683256], ['2XWC+4RH, Kherwadi, Maharashtra 422201'], ['2XWC+4RH, Kherwadi, Maharashtra 422201'], [73.87425, 19.203184], [73.87425, 19.203184], [73.87425, 19.203184]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/vehicle-hits-leopard-on-highway-in-nashik/articleshow/95463434.cms', 'date': 'Nov 12, 2022'}
# sno: 105 soi: ['hit at Ranjangaon', 'hit on the highway', 'hit on Wednesday', 'providing on rent to schools in Panvel', 'schools in Panvel', 'travelled at Shegaon village in Ahmednagar district', 'village in Ahmednagar district', 'started on Tuesday night', 'reopening on Wednesday', 'abandoning on the spot', 'transporter in Dehradun', 'unit at Ranjangaon', 'located at Shirur and Shikrapur', 'declared on arrival', 'travelling on the wrong side of the highway']
# 105 : {'coords': [[74.244849, 18.755018], [73.117516, 18.989401], [73.117516, 18.989401], [74.405661, 19.455502], [74.747979, 19.094829], [74.244849, 18.755018], [74.132313, 18.692369], [74.132313, 18.692369]], 'link': 'https://timesofindia.indiatimes.com/city/pune/maharashtra-5-killed-1-injured-as-truck-hits-bus-in-ranjangaon/articleshow/93613821.cms', 'date': 'Aug 17, 2022'}
# sno: 106 soi: ['collided in Palghar', 'collided on Monday morning', 'took on the ghat section of Jawhar Silvassa road in Palghar', 'section in Palghar', 'hospital in Jawhar', 'was on its way to Jalgaon', 'climbing on the narrow road']
# 106 : {'coords': [[72.769885, 19.696714], [72.769885, 19.696714], [73.231295, 19.905004], [75.562604, 21.007658]], 'link': 'https://timesofindia.indiatimes.com/city/thane/25-passengers-injured-in-collision-between-two-msrtc-buses-in-palghar/articleshow/95349439.cms', 'date': ' Nov 7, 2022'}
# sno: 107 soi: ['road on the Nashik Peth highway in Kotambhi Ghat', 'highway in Kotambhi Ghat', 'skidded on Saturday morning', 'negotiating in the accident prone Kotambhi Ghat', 'accident near Chandwad a truck moving from Nashik towards Satana caught fire on the Mumbai Agra highway near Sogras Phata about 50 km from Nashik', 'caught on the Mumbai Agra highway near Sogras Phata', 'highway near Sogras Phata', 'accident at 8.30 pm', 'gutted in the fire', 'company at Chandwad', 'loss in the fire incident', 'broke at a plastic factory in Dyane in Malegaon taluka', 'factory in Dyane', 'factory in Malegaon taluka', 'broke at around 11 pm', 'broke on Friday', 'gutted in the flame']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# address_road:
# 107 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [''], [74.247278, 20.327128], [74.508946, 20.557903], [74.508946, 20.557903]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/truck-carrying-cans-of-palm-oil-falls-in-kotambhi-ghat/articleshow/95329591.cms', 'date': ' Nov 6, 2022'}
# sno: 108 soi: ['rammed on the Mumbai Pune expressway in Khalapur', 'expressway in Khalapur', 'rammed on Monday', 'parked on the shoulder lane near Khalapur', 'lane near Khalapur', 'accompanied by another person', 'placed behind the car', 'standing near the vehicles', 'taken in the IRB ambulance', 'hospital in Kamothe']
# address_road:
# address_road:
# address_road:
# 108 : {'coords': [[''], [''], [''], [73.096602, 19.016622]], 'link': 'https://timesofindia.indiatimes.com/city/navi-mumbai/six-injured-in-road-accident-on-mumbai-pune-expressway/articleshow/93998178.cms', 'date': ' Sep 5, 2022'}
# sno: 109 soi: ['accident in the Ambad area of Nashik city', 'had on October 13', 'succumbed on Friday', 'FIR in this regard', 'Dang in Igatpuri taluka', 'riding on the Mumbai Agra national highway', 'riding on October 13', 'riding at around 11 pm', 'from near the up ramp of the highway in the Ambad area', 'highway in the Ambad area']
# address_road:
# address_road: 38CV+PJ7, Ambada, Ambad, Madhya Pradesh 413208
# 109 : {'coords': [[73.789802, 19.997453], [73.561107, 19.696326], [''], ['38CV+PJ7, Ambada, Ambad, Madhya Pradesh 413208']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/40-year-old-biker-dies-in-road-accident/articleshow/95057977.cms', 'date': 'Oct 24, 2022'}
# sno: 110 soi: ['died in 44 road accidents in the Jain temple Kasara section of the Mumbai Agra highway', 'accidents in the Jain temple Kasara section of the Mumbai Agra highway', 'driven at high speeds coupled with the bad road conditions', 'lost in 70 accidents between January and December', 'accidents between January and December', 'died in 99 accidents', 'begins in April', 'appear on the highway', 'two in February', 'six in April', 'seven in May', 'eight in June', 'five in July', 'seven in August and September', 'highway in the Ghoti Kasara section']
# address_road: Mumbai - Agra National Hwy, Kasara, Maharashtra 421602
# address_road: Mumbai - Agra National Hwy, Kasara, Maharashtra 421602
# address_road: JFVC+8CW, Old Agra Rd, Kasara, Maharashtra 421602
# 110 : {'coords': [['Mumbai - Agra National Hwy, Kasara, Maharashtra 421602'], ['Mumbai - Agra National Hwy, Kasara, Maharashtra 421602'], ['JFVC+8CW, Old Agra Rd, Kasara, Maharashtra 421602']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/16-road-fatalities-on-ghoti-kasara-section-this-year/articleshow/95191154.cms', 'date': 'Oct 31, 2022'}
# sno: 111 soi: ['schools on the outskirts', 'located in the heart of the city', 'shared by the school', 'schools in Maharashtra', 'blamed on schools', 'driver on a public road', 'point at any school in such incidents', 'school in such incidents', 'play in avoiding an incident like that on Tuesday', 'avoiding on Tuesday', 'commute by school bus', 'happen on city roads', 'case by case', 'accidents in the vicinity of schools', 'exit at the same time', 'is on ensuring that the main gate is not blocked so there ’s no time to manage safety aspect of kids', 'focus on safety of students inside the bus', 'queries on whether they too have such guidelines', 'expertise on school bus issues and education', 'plying in violation of rules', 'are in every 1 km urban and 3 km rural', 'sight in the city', 'sending in overcrowded vehicles', 'engaged in transporting students in city limits', 'transporting in city limits', 'compiled by regional transport office Nagpur city and deputy RTO east office', 'ferry in their vehicles', 'put in place supervisory apparatus', 'headed by the principal', 'work under the state education officer']
# 111 : {'coords': [[75.713888, 19.75148], [79.088155, 21.1458]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/schools-cant-be-held-responsible-for-road-accidents-feel-stakeholders/articleshow/95723489.cms', 'date': 'Nov 24, 2022'}
# sno: 112 soi: ['damaged in a major road accident at Navale bridge area on the Pune Bengaluru highway', 'accident at Navale bridge area', 'accident on the Pune Bengaluru highway', 'damaged on Sunday', 'occurred on Navale bridge', 'injuries in the incident', 'treated at two hospitals', 'vehicles in damaged condition', 'vehicles at the site', 'engaged in rescue efforts', 'pile in accident', 'pile at Navale bridge']
# address_road: Bharati Vidyapeeth Campus, Dhankawadi, Pune, Maharashtra 411043
# 112 : {'coords': [['Bharati Vidyapeeth Campus, Dhankawadi, Pune, Maharashtra 411043'], [73.822208, 18.460924], [73.822208, 18.460924]], 'link': 'https://timesofindia.indiatimes.com/city/pune/at-least-48-vehicles-damaged-in-road-accident-on-pune-bengaluru-highway/articleshow/95645439.cms', 'date': 'Nov 21, 2022'}
# sno: 113 soi: ['aide near Waddhamma', 'aide by rivals on Monday', 'rivals on Monday', 'rivalry over dominating bootlegging trade at Bhivsenkhori', 'dominating at Bhivsenkhori', 'Gondkheri in Kalmeshwar', 'shifted in Nagpur rural from Bhivsenkhori', 'manufactured in Gondkhairi', 'killed on the way back by their rivals on Nagpur Amravati Highway', 'way by their rivals on Nagpur Amravati Highway', 'rivals on Nagpur Amravati Highway', 'captured in one of the CCTVs on the road', 'one on the road', 'riding on which', 'riding at top speed', 'found on the roads', 'attempt by the assailants', 'powder on the bodies of Meshram', 'stuck in his fingers', 'sprinkled in their eyes', 'left on the dividers', 'left by the assailant gang who fled in a white car and an autorickshaw', 'fled in a white car and an autorickshaw', 'masterminded by one Abbas', 'registered at Gittikhadan police station', 'liquor near the bodies']
# address_road: Nagpur - Amravati Hwy, Arjun nagar, Borgaon, Maharashtra 444608
# 113 : {'coords': [[78.912019, 21.234449], [79.000588, 21.152974], [78.905678, 21.137103], ['Nagpur - Amravati Hwy, Arjun nagar, Borgaon, Maharashtra 444608'], [79.060416, 21.173557]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/rivals-bump-off-2-bootleggers-make-it-look-like-road-accident/articleshow/96352427.cms', 'date': 'Dec 20, 2022'}
# sno: 114 soi: ['passerby on road', 'passerby in Dombivli', 'passerby on Tuesday morning', 'captured on CCTV footage', 'captured near a shop which now has gone viral on social media', 'gone on social media', 'going by walking on road when suddenly a tempo traveller passing from Dombivli East towards West side near bridge lost control of his vehicle and dashed to two auto rickshaw and one motorcycle', 'walking on road', 'side near bridge', 'hit by tempo', 'passing on road', 'treatment at hospital', 'booked under negligent rash driving charges', 'injured in road accident', 'injured in Kalyan']
# address_road: Shop # 48, 1st Floor, P P Chambers, near KDMC Office, Banu Nagar, Dombivli East, Dombivli, Maharashtra 421201
# 114 : {'coords': [[73.093948, 19.209401], ['Shop # 48, 1st Floor, P P Chambers, near KDMC Office, Banu Nagar, Dombivli East, Dombivli, Maharashtra 421201'], [73.13054, 19.240331]], 'link': 'https://timesofindia.indiatimes.com/city/thane/maharashtra-four-including-three-students-injured-in-road-accident-in-kalyan/articleshow/94946090.cms', 'date': 'Oct 19, 2022'}
# sno: 115 soi: ['tossed in the air', 'rammed in Nagpur city of Maharashtra', 'took in Sakkardara area of the city', 'took on Friday', 'arrested by the police', 'driving at a great speed', 'going on one of the motorcycles', 'tossed in the air', 'fell on the road below from the flyover', 'injured in the incident']
# 115 : {'coords': [[79.088155, 21.1458], [79.118009, 21.118017]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/four-of-family-killed-after-falling-off-flyover-as-suv-hits-their-motorcycle-in-nagpur-driver-held/articleshow/94111273.cms', 'date': 'Sep 10, 2022'}
# sno: 116 soi: ['killed in separate road accidents in the city', 'accidents in the city', 'killed between Tuesday and Wednesday', 'travelling by an autorickshaw', 'killed in an accident between a car and autorickshaw in the Mumbai Naka area', 'accident between a car and autorickshaw in the Mumbai Naka area', 'car in the Mumbai Naka area', 'killed in another accident on the Dwarka flyover', 'accident on the Dwarka flyover', 'hit by an unidentified motorist', 'punishable under sections']
# 116 : {'coords': [[73.784557, 19.987717], [73.784557, 19.987717]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/nashik-two-killed-in-road-accidents/articleshow/92447359.cms', 'date': 'Jun 25, 2022'}
# sno: 117 soi: ['arrested on the charge of causing the death of a person due to negligence and injury to 45 others owing to rash driving near Dogheshwar Ghat on the Satana Dogheshwar road', 'driving near Dogheshwar Ghat', 'driving on the Satana Dogheshwar road', 'institute in Satana', 'people in the vehicle', 'suffered in the accident']
# 117 : {'coords': [[74.203258, 20.598224]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/tractor-driver-held-in-road-accident-case/articleshow/93335761.cms', 'date': ' Aug 4, 2022'}
# sno: 118 soi: ['ordered on Wednesday', '"probe by the state police \'s Crime Investigation Department CID", \'death in a road accident', 'hit on the Mumbai Pune Expressway', 'hit on Sunday', 'occurred on the Mumbai Pune Expressway', 'occurred on Sunday morning', 'told by officials', 'Avoiding among reasons for most fatalities on expressway', 'fatalities on expressway', 'being in sleep', 'spectrum in Maharashtra', 'elected on an NCP ticket', 'reservation in government jobs and education', 'was on his way to Mumbai', 'meeting on the quota issue', 'was on his way to Mumbai', 'meeting on the quota issue']
# address_road: Maharashtra
# address_road: Maharashtra
# 118 : {'coords': [['Maharashtra'], ['Maharashtra'], [72.877656, 19.075984], [72.877656, 19.075984]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/maharashtra-cid-to-probe-ex-mlc-vinayak-metes-death-in-road-accident/articleshow/93621246.cms', 'date': 'Aug 17, 2022'}
# sno: 119 soi: ['Traffic on Ghodbunder road', 'affected on Wednesday', 'injured in the accident', 'was on its way to Ratnagiri from Gujrat', 'hit on Wednesday', 'oozing on the road', 'halted on the stretch', 'sprayed on the spilled diesel', 'started on the stretch']
# address_road: 903, Queensgate CHS Ltd, off Ghodbunder Road, Hiranandani Estate, Thane West, Mumbai, Mira Bhayandar, Maharashtra 400607
# 119 : {'coords': [['903, Queensgate CHS Ltd, off Ghodbunder Road, Hiranandani Estate, Thane West, Mumbai, Mira Bhayandar, Maharashtra 400607'], [73.312023, 16.990215]], 'link': 'https://timesofindia.indiatimes.com/city/thane/thane-chemical-tanker-hits-median-on-ghodbunder-road-traffic-affected-temporarily/articleshow/91630053.cms', 'date': 'May 18, 2022'}
# sno: 120 soi: ['rammed on the Western Express Highway WEH', 'rammed at Borivali east', 'driver under section 304 A of the IPC', 'broke in the middle of the road at Devipada', 'road at Devipada', 'broke on WEH', 'broke on August 26', 'was in the truck']
# address_road: 204, Gora Kumbhar Rd, Khodiyar Nagar, Sadguru Nagar, Devipada, Borivali, Mumbai, Maharashtra 400066
# address_road: 204, Gora Kumbhar Rd, Khodiyar Nagar, Sadguru Nagar, Devipada, Borivali, Mumbai, Maharashtra 400066
# 120 : {'coords': [[72.860856, 19.229781], ['204, Gora Kumbhar Rd, Khodiyar Nagar, Sadguru Nagar, Devipada, Borivali, Mumbai, Maharashtra 400066'], ['204, Gora Kumbhar Rd, Khodiyar Nagar, Sadguru Nagar, Devipada, Borivali, Mumbai, Maharashtra 400066']], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/mumbai-1-killed-1-injured-in-road-accident-on-western-express-highway/articleshow/94279743.cms', 'date': 'Sep 18, 2022'}
# sno: 121 soi: ['wheeler on the Nashik Peth highway', 'hit by a speeding truck', 'hit on Tuesday afternoon', 'registered on the charge of death', 'punishable under section 304(A', 'Nalshet in Peth taluka', 'Kaprada in Valsad Gujrat', 'Hatipada in Peth taluka', 'accidents on the stretch']
# address_road: Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001
# 121 : {'coords': [['Lokhand Bazar, Gotane Wada, Nashik, Maharashtra 422001'], [73.505666, 20.258113]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/3-killed-in-road-accident-on-nashik-peth-highway/articleshow/92609914.cms', 'date': ' Jul 2, 2022'}
# sno: 122 soi: ['died in a road accident in the Charanmal Ghat of Nandurbar district', 'accident in the Charanmal Ghat of Nandurbar district', 'died on Saturday night', 'suffered in the accident', 'are in the process of registering an FIR in this regard', 'registering in this regard', 'passengers on the bus', 'hospitals in Navapur', 'Pimpalner in Dhule district', 'passengers on the bus', 'work in sugar cane fields', 'road in Charanmal Ghat', 'treatment at the Navarpur rural hospital', 'was in critical condition', 'died in the ambulance', 'died on his way to Surat']
# address_road: XVV9+X8X, Charanmal, Maharashtra 424306
# 122 : {'coords': [[73.86837, 20.994979], [73.79464, 21.161653], [74.121877, 20.949655], ['XVV9+X8X, Charanmal, Maharashtra 424306']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/private-bus-driver-18-month-old-girl-killed-in-road-accident/articleshow/94141413.cms', 'date': 'Sep 12, 2022'}
# sno: 123 soi: ['died in Nashik rural taluka', 'hit by a speeding vehicle', 'hit on Monday night', 'took on Monday night', 'hit near the Mungasare village on the Makhmalabad Matori road', 'village on the Makhmalabad Matori road', 'died by the time they reached', 'found on a farm at Lahavit near Nashik city', 'farm at Lahavit', 'farm near Nashik city', 'deaths in accidents on the Nashik Trimbakeshwar and Nasik Sinnar roads', 'accidents on the Nashik Trimbakeshwar and Nasik Sinnar roads', 'spotted in Niphad Sinnar and Nashik taluka and other parts of the district', 'presence in these talukas', 'fallen at Daregaon village of Satana taluka', 'rescued by the forest officials']
# address_road: Gandhi Nagar, Ramkrishna Nagar, Makhmalabad, Nashik, Maharashtra 422003
# address_road: Gandhi Nagar, Ramkrishna Nagar, Makhmalabad, Nashik, Maharashtra 422003
# 123 : {'coords': [[73.789802, 19.997453], ['Gandhi Nagar, Ramkrishna Nagar, Makhmalabad, Nashik, Maharashtra 422003'], ['Gandhi Nagar, Ramkrishna Nagar, Makhmalabad, Nashik, Maharashtra 422003'], [73.813234, 19.850965], [73.813234, 19.850965], [73.789802, 19.997453], [73.988965, 19.847981], [74.015215, 19.856577], [74.109441, 20.077145]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/4-year-old-leopard-dies-in-road-accident-cremated/articleshow/93147428.cms', 'date': 'Jul 27, 2022'}
# sno: 124 soi: ['killed in a road accident on the Ambad Link Road', 'accident on the Ambad Link Road', 'killed on Wednesday morning', 'are in the process of registering an FIR against the car driver for causing death due to negligence', 'walking on the Ambad Link Road', 'hit by a speeding car', 'suffered in the accident', 'making in the Shivaji Nagar area of Satpur']
# address_road: 90, Ambad CIDCO Link Rd, Mhasoba Nagar, Modkeshwar Nagar, Nashik, Maharashtra 422007
# address_road: 90, Ambad CIDCO Link Rd, Mhasoba Nagar, Modkeshwar Nagar, Nashik, Maharashtra 422007
# address_road: 90, Ambad CIDCO Link Rd, Mhasoba Nagar, Modkeshwar Nagar, Nashik, Maharashtra 422007
# 124 : {'coords': [['90, Ambad CIDCO Link Rd, Mhasoba Nagar, Modkeshwar Nagar, Nashik, Maharashtra 422007'], ['90, Ambad CIDCO Link Rd, Mhasoba Nagar, Modkeshwar Nagar, Nashik, Maharashtra 422007'], ['90, Ambad CIDCO Link Rd, Mhasoba Nagar, Modkeshwar Nagar, Nashik, Maharashtra 422007'], [73.709537, 20.013916]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/17-year-old-killed-in-road-accident/articleshow/92400686.cms', 'date': 'Jun 23, 2022'}
# sno: 125 soi: ['ambulance at Rajgurunagar on the Pune Nashik highway', 'Rajgurunagar on the Pune Nashik highway', 'collided on Friday', 'heading in the opposite direction', 'register in this regard', 'travelling in its lane', 'overtook on the highway', 'ambulance in front of the Khed rest house']
# address_road: Nearest To Market Yard, Pune - Nashik Hwy, Rajgurunagar, Maharashtra 410505
# address_road: Nearest To Market Yard, Pune - Nashik Hwy, Rajgurunagar, Maharashtra 410505
# 125 : {'coords': [['Nearest To Market Yard, Pune - Nashik Hwy, Rajgurunagar, Maharashtra 410505'], ['Nearest To Market Yard, Pune - Nashik Hwy, Rajgurunagar, Maharashtra 410505'], [73.398632, 17.724448]], 'link': 'https://timesofindia.indiatimes.com/city/pune/two-bike-borne-men-killed-in-road-accident-on-pune-nashik-highway/articleshow/93974013.cms', 'date': ' Sep 3, 2022'}
# sno: 126 soi: ['witnessed in May', 'accidents in the city', 'Going by these figures', 'lost in road accidents', 'lost in Nashik city', 'died in road accidents', 'died in January', 'followed by 17', 'followed in February', 'followed in March', 'followed in April', 'highest in May', 'died in road accidents in the city', 'accidents in the city', 'parking on the sides of roads or motorists', 'driving on the wrong side', 'solving in the city', 'taken by the city police']
# 126 : {'coords': [[73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/20-road-accident-deaths-in-nashik-city-in-may/articleshow/92240225.cms', 'date': 'Jun 16, 2022'}
# sno: 127 soi: ['died in a road accident', 'died in 2020', 'hit by a truck', 'hit on February 5', 'died in a hospital', 'was at the time', 'earning in their home in Dunge in Bhiwandi', 'home in Dunge', 'home in Bhiwandi']
# 127 : {'coords': [[73.048291, 19.281255], [73.048291, 19.281255]], 'link': 'https://timesofindia.indiatimes.com/city/thane/thane-kin-of-man-killed-in-road-accident-in-2020-get-rs-20-lakh-as-compensation/articleshow/94622952.cms', 'date': ' Oct 3, 2022'}
# sno: 128 soi: ['caused by road accidents in the city', 'accidents in the city', 'went by 11 %', 'went in 2021', 'witnessed in five years', 'deaths on roads across the state', 'highest in recent years', 'rose in 2021', 'topped in 2021', 'slipped in a year', '"rank among Maharashtra \'s districts", \'slipped in 2021', 'followed by drunk driving and lane cutting', 'released by the transport department', 'released on Monday', 'reduce by 50 %', 'reduce in five years', 'review in the city as well as across the state', 'study on 35 black spots', 'implemented at all crash prone spots across Maharashtra', 'is on the safety of two wheeler riders pedestrians', 'lockdowns in the past two years', 'occurred at intersections', 'imposing on offenders', 'create on road safety', 'encourage at the same time', 'be in order to save lives during the crucial golden hour after an accident']
# 128 : {'coords': [[75.713888, 19.75148], [75.713888, 19.75148]], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/mumbais-road-mishap-deaths-rise-11-in-1-year-maharashtras-maximum-in-5-years/articleshow/92348506.cms', 'date': 'Jun 21, 2022'}
# sno: 129 soi: ['killed in separate accidents that took place in Nashik Road and Adgaon areas of the city between Friday and Sunday', 'took in Nashik Road and Adgaon areas of the city', 'took between Friday and Sunday', 'booked on charges of causing death by negligence', 'causing by negligence', 'registered by Nashik Road police 33 year old Sambhaji Shivaji Pavle a resident of Male Vasti in Eklahara', 'Vasti in Eklahara', 'parked on the road near Shinde Palse village', 'road near Shinde Palse village', 'pm on Friday', 'parked on the road', 'Chitegaon in Niphad', 'killed in a collision between two motorbikes in the Nashik Road area', 'collision between two motorbikes in the Nashik Road area', 'motorbikes in the Nashik Road area', 'was on his way towards Bytco Point in Nashik Road from the Deolali Gaon area on Sunday', 'Point in Nashik Road', 'way on Sunday', 'was at 7.30 am', 'injuries in the accident']
# address_road: Adgaon, Nashik, Maharashtra
# address_road: Shop No 9, Lakhan Socity, Adgaon Rd, Vasantdadanagar, Panchavati, Nashik, Maharashtra 422003
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# address_road: Palse, Palase, Maharashtra 422102
# address_road: Palse, Palase, Maharashtra 422102
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# address_road: Canal Rd, Gosavi Nagar, Mangalmurti Nagar, Nashik, Maharashtra 422006
# address_road: Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214
# 129 : {'coords': [['Adgaon, Nashik, Maharashtra'], ['Shop No 9, Lakhan Socity, Adgaon Rd, Vasantdadanagar, Panchavati, Nashik, Maharashtra 422003'], ['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214'], [73.88601, 19.978375], ['Palse, Palase, Maharashtra 422102'], ['Palse, Palase, Maharashtra 422102'], [74.109441, 20.077145], ['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214'], ['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214'], ['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214'], ['Canal Rd, Gosavi Nagar, Mangalmurti Nagar, Nashik, Maharashtra 422006'], ['Matoshri Nagar, Upnagar, Nashik, Maharashtra 422214']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/2-killed-in-separate-road-accidents-in-nashik-city/articleshow/91775755.cms', 'date': 'May 25, 2022'}
# sno: 130 soi: ['died on June 15', 'accident on the Mumbai Agra highway near Adgaon', 'highway near Adgaon', 'following on June 12', 'riding on his 21 year old friend ’s bike', 'registered on June 18', 'Based on the complaint of Garad ’s mother', 'registered under sections 304 A', 'riding on the night of June 12', 'riding on the two wheeler', 'speeding on the road towards Bali Mandir from Shivnagar', 'was under treatment', 'was at a private hospital', 'died on June 15', 'is under medical treatment']
# address_road: Shree Samarth Nagar, Vasantdadanagar, Adgaon, Nashik, Maharashtra 422207
# address_road:
# 130 : {'coords': [['Shree Samarth Nagar, Vasantdadanagar, Adgaon, Nashik, Maharashtra 422207'], ['']], 'link': 'https://timesofindia.indiatimes.com/city/nashik/17-year-old-pillion-rider-dies-in-road-accident/articleshow/92349523.cms', 'date': 'Jun 21, 2022'}
# sno: 131 soi: ['killed in a road accident in Wani', 'accident in Wani', 'killed in the wee hours of Saturday', 'negligence under Section 304 A of the Indian Penal Code and other sections for rash driving', 'returning on their bike', 'village in Dindori taluka', 'lost over the bike', 'taking in a village']
# address_road:
# 131 : {'coords': [[''], [78.952521, 20.056075], [73.827203, 20.204166]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/two-bikers-killed-in-road-accident-in-wani/articleshow/90923285.cms', 'date': 'Apr 19, 2022'}
# sno: 132 soi: ['were in', 'rammed on Gangapur Road', 'rammed on Wednesday evening', 'occupants in the multi - utility vehicle MUV that rammed a wall near the Hotel Gammat Jammat in Nashik taluka', 'rammed near the Hotel Gammat Jammat in Nashik taluka', 'Jammat in Nashik taluka', 'returning at 6 pm when the accident occurred', 'was in the front seat', 'died in the early hours of Thursday', 'treatment at various hospitals', 'are in stable condition', 'reasons behind the accident']
# address_road:
# 132 : {'coords': [[''], [73.688758, 20.034234], [73.688758, 20.034234], [73.789802, 19.997453]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/18-yr-old-girl-killed-in-road-accident-6-seriously-injured/articleshow/93359998.cms', 'date': ' Aug 5, 2022'}
# sno: 133 soi: ['killed in as many accidents that recently took place in Nashik city', 'took in Nashik city', 'knocked by an unidentified vehicle', 'occurred at 1.45 am on Saturday', 'am on Saturday', 'took at a crossroads in Mhasrul', 'crossroads in Mhasrul', 'resident in Dindori', 'out on morning walk', 'knocked by a four wheeler in Bhadrakali police station area', 'wheeler in Bhadrakali', 'knocked on Saturday', 'knocked by a speeding vehicle', 'knocked by a speeding motorcycle', 'crossing on May 7']
# 133 : {'coords': [[73.789802, 19.997453], [73.789802, 19.997453], [73.807953, 20.046649], [73.807953, 20.046649], [73.789208, 19.997799]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/3-killed-in-different-road-accidents-in-nashik-city/articleshow/91583575.cms', 'date': 'May 16, 2022'}
# sno: 134 soi: ['suffered in a road accident on the Yeola Manmad Road', 'accident on the Yeola Manmad Road', 'suffered at around 1', 'am on Wednesday', 'treatment in Malegaon', 'went by car', 'Manmad near Anakwade', 'died on spot', 'damaged by the impact of the accident', 'reported by the passers by on the road', 'by on the road', 'worked in a food catering firm', 'worked in a mobile repair shop']
# address_road:
# 134 : {'coords': [[''], [74.508946, 20.557903], [74.434976, 20.205171]], 'link': 'https://timesofindia.indiatimes.com/city/nashik/4-killed-1-injured-in-road-accident-in-manmad/articleshow/91503189.cms', 'date': 'May 12, 2022'}
# sno: 135 soi: ['killed on the spot', 'from near Umargaon', 'rammed on Umrer Road', 'present at the spot', 'reason behind the accident', 'be on top speed', 'were at the spot after the accident', 'clearing on the state highway']
# sno: 136 soi: ['collision between a tanker and a truck on the outskirts of Chandrapur in Maharashtra', 'truck on the outskirts of Chandrapur in Maharashtra', 'Chandrapur in Maharashtra', 'said on Friday', 'occurred on Thursday', 'occurred on Chandrapur Mul Road', 'logs near Chandrapur', 'charred in which', 'charred on the spot', 'sources in the forest department', 'brought under control']
# address_road:
# 136 : {'coords': [[79.296147, 19.96154], [79.296147, 19.96154], [''], [79.296147, 19.96154]], 'link': 'https://timesofindia.indiatimes.com/city/nagpur/maharashtra-nine-charred-to-death-as-fire-breaks-out-after-tanker-truck-collision-in-chandrapur/articleshow/91682443.cms', 'date': 'May 20, 2022'}
# sno: 137 soi: ['overturned on Mumbai Ahmedabad national highway in Palghar district', 'highway in Palghar district', 'overturned on Thursday', 'heading on the Mumbai road', 'traffic on the highway', 'diverted on one lane of the Mumbai road', 'are on', 'present at the spot', 'hit on Mumbai Ahmedabad Highway', 'hit near Palghar']
# address_road:
# address_road:
# address_road:
# address_road:
# address_road:
# 137 : {'coords': [[''], [''], [''], [''], [''], [72.769885, 19.696714]], 'link': 'https://timesofindia.indiatimes.com/city/thane/tanker-overturns-on-mumbai-ahmedabad-highway-in-palghar/articleshow/91659565.cms', 'date': 'May 20, 2022'}
# sno: 138 soi: ['payouts in an accident claims case', 'vehicle on Mumbai Ahmedabad Highway', 'rammed in 2016', 'stayed in the car', 'visit in a village on the highway', 'village on the highway', 'was on their way to Palghar', 'travelling in which', 'parked on the side of a National Highway', 'park by the side of National Highway on which the vehicle is being driven at high speed', 'driven on which', 'driven at high speed', 'parked by the side of National Highway', 'took in daylight', 'took at about 8:30am', 'was at high speed', 'occurred on part of driver of Innova Car', 'occurred by parking on National Highway', 'parking on National Highway', 'sitting in the car', 'died in a car crash on the Western Express Highway', 'crash on the Western Express Highway', 'died in 2015']
# address_road:
# 138 : {'coords': [['']], 'link': 'https://timesofindia.indiatimes.com/city/mumbai/mumbai-insurance-companies-to-pay-rs-3-crore-in-2016-road-accident-case/articleshow/93488749.cms', 'date': 'Aug 11, 2022'}
# sno: 139 soi: ['members on the Western Express Highway at Dahisar', 'Highway at Dahisar', 'rammed on Thursday evening', 'driving under IPC provisions against the truck driver', 'is in the ICCU', 'live at Naigaon', 'live near Vasai', 'train at Borivali station', 'head in an auto from Borivali']
# sno: 140 soi: ['rammed in the traffic snarl in Bhor ghat', 'snarl in Bhor ghat', 'rammed near Khopoli', 'rammed on Tuesday', 'travelling in their Maruti Swift car', 'one behind the other', 'caused in two other cars', 'people in a car', 'aide in the IRB ambulance', 'people in a tempo', 'snarl in the Bhor ghat', 'parked on the first lane', 'km on the Mumbai lane', '"was at snail \'s pace", \'rammed on the downward gradient in the Bhor ghat', 'gradient in the Bhor ghat', 'crushed between the truck and a tempo', 'people in the car', 'killed on the spot']
# sno: 141 soi: ['killed in separate road accidents in the Mhasrool and Indiranagar areas of Nashik city', 'accidents in the Mhasrool and Indiranagar areas of Nashik city', 'killed on Saturday', 'suffered in the accident along Dindori Road', 'suffered on April 18', 'suffered in the accident', 'succumbed on Friday', 'died in a hit and run case', 'travelling on his bike', 'travelling on Wednesday night', 'succumbed on Friday']
# sno: 142 soi: ['hit on Nagpur Amravati highway', 'said on Sunday', 'took at 3 pm on Saturday near Kondhali', 'pm on Saturday', 'pm near Kondhali', 'travelling on a motorcycle', 'wheeler near Dudhala village', 'declared on arrival', 'arrested in connection with the accident']
# sno: 143 soi: ['flyover in Nashirabad', 'collided at around 6.45am', 'collided on Wednesday', 'treated in a private hospital in Nashirabad and Jalgaon civil hospital', 'hospital in Nashirabad and Jalgaon civil hospital', 'took on the railway flyover in Nashirabad', 'flyover in Nashirabad', 'travelling by two pick up vehicles', 'market in Savda', 'travelling in Faizpur', 'some on their roofs', 'moving in tandem', 'moving in the opposite direction towards the Bhusawal side', 'died on the spot', 'admitted in Nashirabad and at the Jalgaon civil hospital', 'are in the process of registering an offence against the truck driver']
# sno: 144 soi: ['hit in Ahmednagar district of Maharashtra', 'hit on Friday', 'am near Masudpur Phata', 'occurred under the jurisdiction of Kopargaon city police station', 'died in the accident']
# sno: 145 soi: ['here on Monday', 'causing in an accident', 'causing in April 2019', 'held at the site of cable laying works undertaken by power distribution company MSEDCL', 'undertaken by power distribution company MSEDCL', 'accused under IPC section 304 a', 'driving on Central Avenue', 'driving between Adamshah Chowk and Telephone Exchange Square', 'prosecutor in this case', 'work by MSEDCL', 'negligence on the part of officials and contactors', 'crushed under a tipper', 'concerned in the matter', 'offence under 304(a', 'accused under section 304a', 'assisted by advocates Saket Narasapurkar Sanket Puranik and Akanksha Wanjari', 'came under whose wheels', 'done by the sub - contractor', 'imposed on all the accused']
# sno: 146 soi: ['met on Thursday evening', 'Bhujbal in his condolence message', 'link between the government and the news media', 'work in Malegaon', 'finishing on Thursday evening', 'accident near Devarpada Phata', 'survived by his parents two brothers wife and two children']
# sno: 147 soi: ['claimed in fatal accidents in the city', 'accidents in the city', 'claimed in 2021', 'died on the Katraj Dehu Road bypass', 'died on the Pune Ahmednagar highway', 'died on the Pune Solapur highway', 'study in detail', 'demarcate on these roads', 'accidents on the city roads and the highways', 'are under the Pune city police and vehicles on these highways', 'police on these highways', 'travel at a high speed', 'taken in the old parts of the city', 'taken in Vimannagar Aundh Baner Khadki Wanowrie Katraj Phursungi Road Kharadi Mundhwa Road Kondhwa Road Pune Satara Road old Mumbai Pune Road Alandi Road and other areas', 'driving by heavy vehicles', 'driving on the long slope', 'driving by the light motor vehicles and two wheeler riders and drowsiness', 'points on the stretch of the Pune Solapur highway which passes from Pune city', 'resulted in fatal accidents']
# sno: 148 soi: ['killed in two separate road accidents in the city', 'accidents in the city', 'killed on Thursday and Friday', 'travelling on their bike', 'travelling near the Old Adgaon Naka', 'travelling on Thursday night', 'gap in one of the road dividers', 'suffered in the accident', 'killed in a road accident', 'travelling in a scooter', 'travelling in the Jail Road area', 'travelling on Friday night', 'travelling at around 10.30 pm', 'injuries in the accident']
# sno: 149 soi: ['released by police', 'killed in road accidents', 'killed between January and November', 'was in 2020', 'driving at high speed', 'causes behind the accidents', 'reported in areas such as Deccan Gymkhana and Shivajinagar', 'signals on the city roads', 'involved in rash and negligent driving']
# sno: 150 soi: ['released by the police', 'released on Thursday', '% in Mumbai', 'decreased by 45 %', 'is at the heart of the Motor Vehicles Amendment Act', 'occurred among young men between 20 and 34 years of age', 'men between 20 and 34 years of age', 'crashes by researchers with the Bloomberg Philanthropies Initiative for Global Road Safety BIGRS', 'corridor in the city', 'Junction at Ghatkopar', 'was at risk with 23 fatalities within a 250 metre radius between 2018 and 2020', 'radius between 2018 and 2020', 'go in a big way', 'occurred on Saturday evenings', 'seen in many cities', 'occurred between 8 pm and midnight', 'killed in crashes', 'passengers in two and three wheelers 10 %', 'be at fault', 'be in crash related deaths', 'Going by location of crashes', 'observed in 2020', 'observed by 22 % for fatalities and 41 % for injuries', 'BIGRS in their data analysis report launched by the police on Tuesday', 'launched by the police', 'launched on Tuesday']
# sno: 151 soi: ['wall in Bhot Ghat', 'wall near Khopoli', 'crashed on Tuesday morning', 'Decorators in Vile Parle', 'event at Aamby Valley near Pune', 'Valley near Pune']
# sno: 152 soi: ['rammed behind another dumper', 'halted in the middle of the Sion Panvel highway', 'climbing on Friday', 'occurred at Nerul', 'Acting on a complaint by the injured dumper ’s cleaner Gopichand Gautam 30', 'complaint by the injured dumper ’s cleaner Gopichand Gautam 30', 'halted in the middle of the highway', 'plying on the highway', 'hospital in Nerul', 'hospital in Vashi where he was declared brought dead']
# sno: 153 soi: ['died on the Karad Wathar stretch of the Pune Bengaluru National Highway', 'hit by a vehicle', 'hit in the early hours of Sunday', 'area in Koyna or Bamnoli', 'highway near Karad', 'attacks in the region', 'killed in a leopard attack in the Yenke village of Karad tehsil', 'attack in the Yenke village of Karad tehsil', 'released in the wild', 'released by the forest department', 'occurred between 5 am and 6 am', 'cremated in presence of forest officials and honorary wild life warden Rohan Bhate']
# sno: 154 soi: ['patted in February', 'witnessed in the first two months of 2022', 'Analysis in January and February', 'Analysis by traffic police', 'fault in vehicles', 'occurred between 9 pm and 7 am', 'reported in these two months', 'occurred between 9 pm and 7 am', 'policing on city roads', 'improvement in traffic policing', 'motorists on city roads', 'stressed on the need', 'curtail by intensifying drive across the city', 'rise in fatal accidents on poor traffic policing', 'accidents on poor traffic policing', 'seen on roads', 'than in office', 'Admitting in the number of road accidents', 'overspeeding by heavy vehicles which are responsible for most such incidents', 'working on it']
# sno: 155 soi: ['died in three separate accidents in the city between Sunday and Monday', 'accidents in the city', 'accidents between Sunday and Monday', 'Road in Nashik Road area', 'came under the rear tyre of the truck', 'killed on the spot', 'survived by two children aged 13 years and seven years', 'killed in the second accident', 'killed on Sunday', 'knocked by an unidentified vehicle', 'took at 6.30 pm', 'took on the Mhasrool Makhmabad Link Road', 'knocked by the unidentified motorist who managed to escape from the scene', 'knocked by an unidentified motorist near Papaya Nursery Road on Sunday', 'motorist near Papaya Nursery Road', 'motorist on Sunday', 'knocked at around 12.30 pm', 'hit by a speeding vehicle']
# sno: 156 soi: ['killed in three separate road accidents in Kolhapur district', 'accidents in Kolhapur district', 'killed on Saturday', 'riding on a scooter', 'fall on the road', 'came under the wheels of a speeding truck', 'died on spot', 'took at around 8 pm along the Shiroli stretch of Pune Bengaluru National Highway', 'moving at high speed', 'worked in Gandhinagar shop', 'stepped in the evening', 'hit by a four wheeler coming from the back at Gadmudshingi along Kolhapur to Hupari road', 'back at Gadmudshingi along Kolhapur', 'called by the state transportation staffers', 'was on her scooter', 'hit by a vehicle along Yalgud Hupari road', 'died on the spot']
# sno: 157 soi: ['witnessed in 2019', 'injured in road related mishaps', 'conducted by Nagpur city traffic police', 'lockdown in 2020', 'decline in road accidents', 'occurred in 2021', 'reported in 2019', 'reduced by 49 but fatal accidents', 'accidents in 2021', 'presence on roads', 'cops on roads', 'indulged in road accidents including fatal serious and minor', 'involved in road mishaps which was followed by 177 heavy vehicles 47 autorickshaws and 22 buses including Aapli ST and private buses respectively', 'followed by 177 heavy vehicles 47 autorickshaws and 22 buses including Aapli ST and private buses respectively', 'study under the leadership of joint commissioner of police Aswati Dorje and deputy commissioner of police traffic', 'thoroughfares in the city', 'roads in the city', 'rise in road accidents', 'involved in', 'involved over speeding 2', 'cases in 2021', 'booked by traffic police', 'discipline among drivers', 'camps in and around the city']
# sno: 158 soi: ['knocked near Green Plaza hotel in Malegaon The deceased identified as Sagar Thakre 25 and Swapnil Thakre 25', 'hotel in Malegaon', 'ran at Chandwad', 'wason on Saturday']
# sno: 159 soi: ['riding on', 'hit in Ulhasnagar', 'hit on Friday afternoon', 'lying on road', 'injured at a private hospital', 'gone on social media platforms', 'injured in mishap']
# sno: 160 soi: ['injured in an accident involving multiple vehicles on the Mumbai Pune expressway in Bhor Ghat near Khopoli on Thursday evening', 'vehicles on the Mumbai Pune expressway', 'involving in Bhor', 'involving near Khopoli', 'involving on Thursday evening', 'occurred at the accident prone black spot of Dheku village', 'halting on the third lane', 'truck behind the goods vehicle', 'road on the left', 'standing near his vehicle', 'crushed by the coconut laden truck']
# sno: 161 soi: ['died on the Karad Wathar stretch of the Pune Bengaluru National Highway', 'hit by a vehicle', 'hit in the early hours of Sunday', 'declared on the spot']
# sno: 162 soi: ['died in road accident', 'died on late Friday night', 'died in Ulhasnagar', 'dashed by another vehicle near Rayta', 'vehicle near Rayta', 'dashed on Kalyan Murbad road', 'treatment at private hospital']
# sno: 163 soi: ['crashes on Mumbai streets', 'lull in 2020', 'reported between January and June 2019', 'reduced by 39 % to 141 fatalities', 'reduced in the same period last year', 'rose between January and June 2021', 'increase in personal vehicles', 'increase on streets post lockdown', 'implemented in Maharashtra and', 'surged by 41 %', 'surged in January June 2020', 'burden on the survivors', 'worked on road safety projects', 'worked in Mumbai', 'worked in partnership with the Bloomberg Initiative for Global Road Safety BIGRS', 'invest in public transport', 'spike in fatalities', 'train in basic trauma care skills']
# sno: 164 soi: ['were in 2021', 'year in Nashik city', 'killed in 470 road accidents', 'killed in 2021', 'died in 416 accidents', 'died in 2020', 'rise in road accidents and fatalities', 'were in 2020', 'killed in road accidents', 'riding on two wheelers', 'involved in the fatal accidents', 'died in the accident', 'indulge in rash driving', 'stopping at signals', 'driving on the wrong side of the road', 'parked on blind spots', 'halting on the highways', 'left in 2021', 'killed in road accidents', 'high on the highways due to which pedestrians get killed', 'raise among residents of the city', 'conditions on the road']
# sno: 165 soi: ['riding on an Activa scooter', 'killed in a hit and run incident', 'killed on the Palm Beach road near Aspire building junction in Nerul', 'road near Aspire building junction in Nerul', 'junction in Nerul', 'knocked by a speeding car', 'am on Monday', 'hospital in Vashi', 'was in a relationship with Gore', 'booked under relevant IPC sections and Motor Vehicle Act', 'recorded at the civic hospital', 'installed by NMMC', 'initiated in 2016', 'delay in CCTV camera installation', 'supervisor at the APMC grain market', 'stated in the FIR', 'gone on Sunday', 'gone at around 11', 'am on his scooter', 'were near Aspire building junction', 'am at around 1', 'am on Monday', 'hospital in Nerul where the doctors declared her brought dead on arrival', 'brought on arrival']
# sno: 166 soi: ['killed in separate accidents in the city', 'accidents in the city', 'killed on Monday', 'hit at Kawadipat toll plaza near Kadamvak Vasti', 'plaza near Kadamvak Vasti', 'working in a private company', 'heading on his two wheeler', 'rammed at a high speed', 'knocked by a speeding tempo at Kharadi', 'tempo at Kharadi', 'knocked on Monday evening', 'gathered at the spot']
# sno: 167 soi: ['injuries in an accident between a car and truck that occurred at 1.30 am on Wednesday along the Phaltan Dahiwadi road', 'accident between a car and truck that occurred at 1.30 am on Wednesday along the Phaltan Dahiwadi road', 'occurred at 1.30 am on Wednesday', 'am on Wednesday', 'rammed by a speeding truck', 'treatment at the hospital']
# sno: 168 soi: ['killed in two separate road accidents in the city', 'accidents in the city', 'killed on October 10 and 14', 'collision between two motorcycles in the Carbon Naka Satpur area', 'motorcycles in the Carbon Naka Satpur area', 'speeding on the road', 'speeding at around 7 pm', 'speeding on Sunday', 'hospital in Mumbai Naka where he succumbed to the injuries on Monday', 'succumbed on Monday', 'knocked by a biker', 'knocked on Thursday morning', 'walking at around 7.30', 'am on Thursday']
# sno: 169 soi: ['period in 2020 when 598 accidents were reported', 'carried by Nagpur traffic police', 'relaxations in Covid curbs', 'period in 2020', 'killed in 145 accidents that had left another 51 injured', 'occurred on internal roads', 'traffic on inner ring road', 'occurred on inner ring road', 'were in 2020', 'Accidents on Wardha Road Jabalpur Road Amravati Road Chhindwara Road and Hingna Road', 'carried by Nagpur traffic police']
# sno: 170 soi: ['lost on Ghodbunder road', 'collided on Tuesday morning', 'occured near Gaimukh Jakat naka TMC school no.97', 'driven by Shabuddin Khan', 'was on its way from Valsad Gujrat to Balkum Thane', 'jam on the stretch']
# sno: 171 soi: ['accidents in the city', 'from over speeding', 'reported between January and August', 'recorded in 2020', 'recorded in 2019', 'occurred on the Pune Solapur and Pune Ahmednagar highways and the Katraj Dehu Road bypass', 'city in the past eight months', 'died in which', 'reported in accidents on the city roads', 'accidents on the city roads', 'said over speeding', 'fatalities on these stretches', 'fatalities on the Pune Ahmednagar highway', 'fatalities on the Pune Solapur highway', 'died on the Katraj Dehu road bypass', 'highway in Hadapsar', 'accidents in the areas of the Cantonment']
# sno: 172 soi: ['rammed on the Katraj Dehu road bypass', 'rammed on Monday afternoon', 'from behind', 'from near D Mart', 'crushed under the wheels']
# sno: 173 soi: ['hit at Sategaon near Kamshet', 'Sategaon near Kamshet', 'hit on the old Pune Mumbai highway at 6.15 am on Saturday', 'highway at 6.15 am on Saturday', 'am on Saturday', 'lost over the wheel', 'driving in the night which led to the accident', 'was at the time of accident', 'sitting in a tractor trolley which was part of the group', 'hit at a high speed', 'located at Somatne Phata Kamshet and Kanhe']
# sno: 174 soi: ['killed in separate road accidents in the Adgaon and Mhasrool area of the city', 'accidents in the Adgaon and Mhasrool area of the city', 'killed on Tuesday and Wednesday', 'highway near Guru Nanak Petrol Pump in Adgaon', 'Pump in Adgaon', 'crossing at around 8 pm', 'crossing on Tuesday', 'filed by the deceased ’s father', 'knocked by an unidentified truck driver']
# sno: 175 soi: ['causing by negligence', 'suffered in an accident in the Ambad area', 'accident in the Ambad area', 'suffered on September 21', 'Nagar in Ambad', 'knocked by a speeding four wheeler', 'knocked at 4.40 pm', 'knocked on September 21', 'course on September 27', 'succumbed at the Nashik civil hospital', 'rise in the number of cases of causing death due to negligence this year', 'died in road accidents', 'died in fatal accidents in the city', 'accidents in the city']
# sno: 176 soi: ['cars at Gaimukh ghat', 'rammed on Sunday', 'jam on Ghodbunder road', 'stuck on Monday morning', 'stuck in the long queue of traffic jam', 'movement on Gujarat bound lane of Ghodbunder road', 'movement on Monday', 'occurred at 10:20 pm near Nagla bunder along the city fringes and the pileup of traffic spread for nearly eight kms till Majiwada in the city', 'pm near Nagla', 'Majiwada in the city', 'injured in the accident', 'injured in the mishap', 'officials in Thane', 'present on the spot upon receiving the information with one fire engine one crane three Hydra one JCB and three ambulances', 'spill on road', 'jam on']
# sno: 177 soi: ['peon at the Panvel RTO office', 'hit by a tanker', 'crossing near a flyover along the Mumbra Panvel highway', 'crossing on Wednesday', 'caught by the passersby', 'informed at around 2.50pm', 'residing in Khanda Colony who was chatting with other auto drivers near the Panvel RTO office gate', 'drivers near the Panvel RTO office gate', 'informed by a passerby that a RTO official had met with an accident near the flyover abutting the steel market', 'accident near the flyover', 'peon at Panvel RTO office', 'resided at Navade village in Panvel taluka', 'village in Panvel taluka', 'gathered at the spot', 'road near the flyover', 'rushed in an auto rickshaw to MGM hospital Kamothe where Parkar succumbed to his injuries during treatment at around 6.30pm', 'succumbed at around 6.30pm', 'Acting on a complaint by Jagdale', 'complaint by Jagdale', 'caught by the passersby', 'booked under relevant IPC sections and Motor vehicle Act for rash and negligent driving causing death of Parkar']
# sno: 178 soi: ['killed in a road accident', 'killed on Monday', 'killed in Shahapur taluka of Thane district', 'treatment at a hospital', 'travelling on his bike', '"hit by Pansare \'s bike", \'died on the spot']
# sno: 179 soi: ['rickshaw on Kapurbawdi Nashik flyover bridge', 'rammed in the early hours of Tuesday', 'occurred at around 1 am on Kapurbawdi Nashik flyover bridge towards Nashik lane', 'am on Kapurbawdi Nashik flyover bridge towards Nashik lane', 'circle in Thane', 'restored on Mumbai Nashik highway', 'injuries on both legs and head and Tarnumun 30', 'injuries on her back']
# sno: 180 soi: ['ordered on Friday', 'ordered by the state PWD and 315', 'ordered by urban local bodies across Maharashtra .', 'meeting at Sahyadri guest house', 'focus on saving lives and reducing fatalities on the road', 'fatalities on the road', 'said at the meeting', 'seek in curbing mishaps on highways', 'mishaps on highways', 'completed at 931 locations', 'completed at 359 locations', 'signs on traffic rules', 'limits at various locations', 'have on the rear side', 'present at the road safety council meeting', 'dip in the number of mishaps across the state', 'fatalities in road crashes', 'taken at the meeting', 'updates on crashes on the road', 'crashes on the road', 'roles in road safety', 'attended by representatives from PWD the health and transport departments MSRTC and non - profit organisations such as SAVELife Foundation']
# sno: 181 soi: ['court in Mumbai', 'causing by negligence', 'causing in a case involving a 60 year old woman who died allegedly after being hit by his motorcycle while she was trying to cross a highway in 2017', 'hit by his motorcycle', 'cross in 2017', 'acquitted on August 28', 'made on Wednesday', 'hit by Hatkar who was going on his two wheeler', 'going on his two wheeler', 'cross near suburban Chembur in Mumbai', 'Chembur in Mumbai', 'place on record', 'hit by his vehicle', 'placed on record', 'took on the Eastern Express Highway that goes towards Mumbai', 'was at a distance of 35 feet towards the eastern side', 'divider at a distance of 15 feet', 'occurred in the middle of the road', 'nothing on record', 'was at the spot of incident']
# sno: 182 soi: ['"vehicle in Maharashtra \'s Amravati district", \'said on Saturday', 'took near Paratwada', 'took under Aasegaon police station', 'ridden by Sarthak Vaidya 17 and Nivrutti Salav 15', 'collided on Friday evening', 'friction on the road', 'blast in the petrol tank of the two wheeler', 'engulfed in flames', 'died on the spot', 'studying in Class 8', 'offence under relevant sections of the IPC and Motor Vehicles Act', 'registered at Aasegaon police station']
# sno: 183 soi: ['killed in a hit- and run accident in Kapurbawdi area of Thane city', 'accident in Kapurbawdi area of Thane city', 'said on Saturday', 'traveling on a motorcycle', 'hit on Y Bridge here', 'hit on Friday afternoon', 'died in the spot', 'are on']
# sno: 184 soi: ['station in Ambernath', 'died in road accident', 'died on Thursday', 'took on Badlapur Dombivli pipeline road', 'fill at petrol pump situated near Nevali naka', 'situated near Nevali naka', 'died on the spot', 'was in full speed and', 'travelling in car', 'arrested under negligence causing death and rash driving charges']
# sno: 185 soi: ['is on the rise', 'were in April', 'rush on the roads', 'rise in the number of accidents', 'indulge in rash driving', 'claimed in Nashik city', 'accidents on city roads']
# sno: 186 soi: ['operated by Maharashtra State Road Transport Corporation MSRTC', 'toppled in Dindoshi area', 'taken on a lease from MSRTC', 'took in the middle of the road', 'driver at Kurar police station']
# sno: 187 soi: ['rammed in the early hours of Wednesday', '"rammed in Maharashtra \'s Thane city", \'travelling at around 5.30am when the car rammed into a tree near a footpath in Upavan area chief of the RDMC of the TMC Santosh Kadam', 'rammed near a footpath in Upavan area chief of the RDMC of the TMC Santosh Kadam', 'footpath in Upavan area chief of the RDMC of the TMC Santosh Kadam', 'died on the spot', 'treatment at a private hospital', 'came in front of the car']
# sno: 188 soi: ['collided on the Mumbai Nashik highway', 'collided on Wednesday', 'coming on the Mumbai Nashik highway in Thane', 'highway in Thane']
# sno: 189 soi: ['knocked by a speeding car coming from the opposite direction on the Wani Dindori Road on Friday afternoon', 'direction on the Wani Dindori Road', 'coming on Friday afternoon', 'parked by the roadside', 'suffered in the accident a woman who was standing near the other bike', 'standing near the other bike', 'saved by jumping out of the path of the speeding car', 'took at around 4.30 pm', 'took near Lakhmapur Phata on the Wani Dindori Road', 'Phata on the Wani Dindori Road', 'got on the wrong lane']
# sno: 190 soi: ['collided at a village in Akola district of Maharashtra', 'village in Akola district of Maharashtra', 'collided in the wee hours of Friday', 'residents in neighbouring Washim district', 'visiting at Shegaon in Buldhana district', 'Shegaon in Buldhana district', 'were in the age group of 28 to 34', 'village in Akola district', 'going in the opposite direction towards Khamgaon in Buldhana', 'Khamgaon in Buldhana', 'died on the spot', 'hospital in Akola where he was declared dead']
# sno: 191 soi: ['"injured in a road accident that took place near Sakwar village in Maharashtra \'s Palghar district early on Friday", "took near Sakwar village in Maharashtra \'s Palghar district", "village in Maharashtra \'s Palghar district", \'rammed in which', 'autorickshaw on the Mumbai- Ahmedabad highway', 'parked by the roadside', 'sitting in the tempo', 'killed on the spot', 'injuries in the mishap', 'bottles in the tempo', 'hailed in the district']
# sno: 192 soi: ['modes in the city', 'modes in last 17 months', 'involved in road accidents in the jurisdiction of Nagpur city police commissionerate which claimed lives of 102 people', 'accidents in the jurisdiction of Nagpur city police commissionerate which claimed lives of 102 people', 'shared by Nagpur city traffic police', 'shared in a reply to an RTI query filed by activist Abhay Kolarkar', 'filed by activist Abhay Kolarkar', 'involved in 29 road accidents that claimed lives of five people', 'Roads in the city', 'reply in the city', 'killed in which', 'from in the last 17 months', 'paid in fines', 'Honking in silent zones']
# sno: 193 soi: ['located near the popular Lalbaugcha Raja mandal', 'crashes over three years', 'dart at will', 'dart at Jagnade Chowk in Lalbaug', 'Chowk in Lalbaug', 'Chowk at Lalbaug', 'trips in the city', 'are on foot', 'travelling by foot', 'junction at Kandivali', 'sprint at Jagnade Chowk', 'halt at times', 'used by', 'radius between 2016 and 2019', 'made by aligning traffic lanes shortening turning radii and creating refuge areas out of unutilised spaces for pedestrians to halt before crossing', 'reduced by almost 30 %', 'kept in check', 'fitted at the junction', 'casualties between 2015 and 2019', 'zones in pre - Covid times', 'Located at a three arm intersection of the Khan Abdul Gaffar Khan Road and Annie Besant Road in Worli', 'Road in Worli', 'identified by BMC', 'identified in its Comprehensive Mobility Plan', 'improved by providing 11 wheelchair accessible ramps on footpaths', 'providing on footpaths', 'ramps in the two refuge islands']
# sno: 194 soi: ['station in Thane', 'died in an accident', 'died on Sunday evening', 'travelling in', 'truck on the Mumbai Agra highway', 'injuries in the accident that took place at 7.45 pm', 'took at 7.45 pm', 'took between their car and an unidentified truck in the Raigad Nagar area', 'truck in the Raigad Nagar area', 'were on the same lane', 'victims in the accidents', 'are in a position to give any statement', 'village in Surgana', 'were on their way back to Mumbai', 'were on Sunday']
# sno: 195 soi: ['injuries in separate accidents that happened near Pune in the early hours of Monday', 'happened near Pune', 'happened in the early hours of Monday', 'travelling in', 'truck near Wakad', 'crashed on Katraj Dehu Road bypass', 'happened in the early hours of Monday', 'treated at a Aundh hospital', 'treatment in a private hospital', 'heading in Latur district', 'happened near Narhe', 'crashed in the rear of a truck transporting liquor bottles', 'injured in 4 different road accidents near Pune', 'accidents near Pune']
# sno: 196 soi: ['fatalities in April and May', 'was in effect', 'down by 50 %', 'casualties in the corresponding months in 2019', 'months in 2019', 'casualties in Pune city', 'lost in road accidents', 'lost in April and May', 'lost in the city', 'reported in those two months', 'was in effect', 'died in road accidents on the city roads', 'accidents on the city roads', 'fatalities in Pune city', 'were in the same period', 'fatalities in those four months of the Covid hit year', 'was in 2019', 'reported in Pune city', 'reported in 2020', 'casualties in 2019', 'lockdown between the last week of March', 'decline in the numbers', 'was in 2019', 'witnessed in 2020', 'suffered in which', 'provided by traffic police', 'fatalities in a month', 'fatalities in 2020', 'reported in four months from March to June', 'reported in six months from July to December', 'were on the city roads', 'were in that period', 'resulting in fewer accidents', 'accidents on Katraj Dehu Road bypass and the Solapur highway', 'casualties in November and December', 'is in the jurisdiction of the Pune city police', 'recorded in the highway section', 'recorded in November 2020', 'five in December', 'witnessed in November', 'deaths in December', 'studies in the city', 'number in the city', 'study by visiting the spots', 'accidents on those particular spots']
# sno: 197 soi: ['injured in separate incidents on the Mumbai- Ahmedabad highway', 'incidents on the Mumbai- Ahmedabad highway', 'injured on Sunday morning', 'died on the spot', 'flyover near Dahanu', 'fell in nighbouring Palghar district', 'container near Ahura hotel in Amboli on the highway', 'hotel in Amboli', 'hotel on the highway']
# sno: 198 soi: ['killed in a hit and run on Rajura Virur road near village Shirshi', 'hit on Rajura Virur road near village Shirshi', 'road near village Shirshi', 'came on Wednesday morning when a forest guard Chandrashekar Medpalliwar discovered the carcass close to the road', 'hit by a speeding vehicle', 'rising in Chandrapur district', 'measures on the road passing through the wildlife corridors']
# sno: 199 soi: ['killed in a road accident at Bhigwan in Pune district', 'accident at Bhigwan in Pune district', 'Bhigwan in Pune district', 'killed on Thursday morning', 'place in Pune', 'Accompanied by three other relatives', 'returning on Thursday morning', 'died on the spot', 'resume at 10 am at Kalamboli headquarters', 'am at Kalamboli headquarters']
# sno: 200 soi: ['crushed under the wheels of unidentified vehicle in MIDC area of Nagbhid', 'wheels in MIDC area of Nagbhid', 'recovered on Friday morning']
# sno: 201 soi: ['been at Sakegaon village in Jalgaon', 'village in Jalgaon', 'toppled near the Tarsod Phata', 'toppled over 300 km from Nashik', 'killed at 3 am on Thursday', 'am on Thursday', 'died on the spot', 'succumbed in a private hospital', 'accompanied by his friend Bagul who wanted to pick up his wife from Malegaon', 'left on Thursday morning', 'reach by evening', 'Phata in Nashirabad', 'lost on a road where construction activity was going on']
# sno: 202 soi: ['bus on Mumbai Nashik highway', 'dashed on Monday wee hours', 'took near Pimplas area in Bhiwandi taluka on Mumbai Nashik highway', 'area in Bhiwandi taluka on Mumbai Nashik highway', 'taluka on Mumbai Nashik highway', 'residents in Nashik', 'police in Bhiwandi', 'come on Sunday', 'purchasing on Monday wee hours', 'returning in their old car', 'heading in Nashik', 'hit by a speeding bus', 'resulting in the death of all the four friends', 'resulting on the spot']
# sno: 203 soi: ['accidents on highways', 'cut by half', 'cut in four years', 'hosted by the International Institute of Security & Safety Management IISSM', 'die over 1.5 lakh', 'injured in the country in road accidents', 'country in road accidents', 'reduce by 2030', 'adopted at the 3rd global ministerial conference on road safety in Sweden held in February 2020', 'conference on road safety in Sweden', 'safety in Sweden', 'held in February 2020', 'reduction by 50 %', 'reduction by 2030', 'achieve by 2025', 'focusing on engineering effective implementation training and strengthening of emergency services', 'deaths on the world ’s roads', 'percentage between 18 45 years', 'implementing by creating awareness among drivers road safety drives at school levels', 'creating among drivers', 'drives at school levels', 'drives on road safety']
# sno: 204 soi: ['killed in a road accident in Ambernath', 'accident in Ambernath', 'killed on Sunday', 'returning in Ulhasnagar', 'took on Sunday', 'took on the new MIDC road at Palegaon area in Ambernath taluka', 'road at Palegaon area in Ambernath taluka', 'area in Ambernath taluka', 'damaged in the mishap', 'travelling in the auto rickshaw', 'travelling in two separate auto rickshaws for Ganesh immersion', 'travelling in which', 'died on the spot The Shivaji Nagar police have registered an FIR against the driver of the car and have arrested him in the case', 'arrested in the case', 'sent in Ulhasnagar', 'investigated by the Shivaji Nagar Police Station']
# sno: 205 soi: ['lost in three separate incidents between Monday evening and Wednesday morning', 'incidents between Monday evening and Wednesday morning', 'killed on the spot in a road accident on the Mumbai Agra highway near the Wadivarhe police station', 'spot in a road accident on the Mumbai Agra highway near the Wadivarhe police station', 'accident on the Mumbai Agra highway near the Wadivarhe police station', 'highway near the Wadivarhe police station', 'killed on Wednesday morning', 'killed in a collision between two trucks', 'collision between two trucks', 'killed at 5.30 am', 'was in the truck', 'suffered in this accident', 'jam on the highway', 'early in the morning', 'killed in separate road accidents in Nashik city', 'accidents in Nashik city', 'killed on Monday', 'one in the Upnagar area', 'killed in the Mhasrool area', 'registered by the Upnagar police the two bikers Kiran Mali and Amit Wagh', 'collided near Pimpalgaon Phata', 'collided on Monday', 'collided at 11.30 pm', 'riding in the opposite direction', 'bikers under relevant sections of the Indian Penal Code IPC', 'causing by negligence', 'killed in an accident near the old octroi naka in Mhasrool', 'accident near the old octroi naka in Mhasrool', 'naka in Mhasrool', 'from near the old octroi naka', 'riding at 5.30 pm', 'riding on Monday', 'knocked by an unidentified motorist']
# """
#
# sentences = text.split("\n")
# arr = []
#
# for sentence in sentences:
#     if " : {'coords':" in sentence:
#         arr.append(sentence)

# arr = []
#
# for item in find_coordinate_strings(text):
#     item_t = [float(item[0]), float(item[1])]
#     if item_t not in arr:
#         arr.append(item_t)

# print(arr)

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import haversine_distances
from math import radians
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.spatial import ConvexHull

# Function to calculate Haversine distance between two sets of coordinates
def haversine_distance(coord1, coord2):
    coord1_rad = np.radians(coord1)
    coord2_rad = np.radians(coord2)

    d_lat = coord2_rad[0] - coord1_rad[0]
    d_lon = coord2_rad[1] - coord1_rad[1]

    a = np.sin(d_lat / 2) ** 2 + np.cos(coord1_rad[0]) * np.cos(coord2_rad[0]) * np.sin(d_lon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    return c * 6371000  # Earth's radius in meters


# Sample GPS coordinates (latitude, longitude)
coordinates = np.array([[79.75155, 20.480224], [79.602053, 21.434709], [78.774455, 20.88056], [78.458147, 21.490189],
                        [72.877393, 19.07599], [72.871827, 19.131244], [72.837652, 18.987975], [72.895574, 19.288213],
                        [72.970178, 19.194329], [80.313806, 21.353921], [79.547796, 21.150519], [79.511302, 20.633333],
                        [79.493825, 20.902994], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293], [72.853977, 19.080113],
                        [73.216962, 19.350197], [73.569968, 17.576538], [73.448218, 16.722566], [73.412121, 16.817984],
                        [73.9879578, 20.3315982], [72.877393, 19.07599], [73.790236, 20.011248], [72.851341, 19.229631],
                        [72.87162, 19.061034], [72.851251, 19.173014], [72.563592, 23.027848], [72.563592, 23.027848],
                        [72.851341, 19.229631], [73.93947, 19.847113], [73.896447, 18.562624], [72.563592, 23.027848],
                        [72.90555, 19.676744], [72.851341, 19.229631], [72.87162, 19.061034], [72.940244, 19.049643],
                        [72.833414, 19.208385], [73.9879578, 20.3315982], [73.87257, 18.500972], [72.862086, 19.052074],
                        [72.563592, 23.027848], [72.914851, 20.076293], [72.811727, 19.359214], [72.86313, 19.259786],
                        [74.7369665, 19.9203238], [73.7350917, 20.0101404], [75.012441, 19.697762],
                        [79.995177, 19.649775], [78.750678, 20.409617], [73.612717, 18.755392], [73.402165, 18.357924],
                        [74.537284, 17.271977], [74.238723, 20.327815], [73.790236, 20.011248], [75.633651, 18.600976],
                        [72.850846, 19.965672], [74.238723, 20.327815], [73.790236, 20.011248], [75.633651, 18.600976],
                        [72.850846, 19.965672], [74.182473, 15.941017], [72.8367076, 19.1940346],
                        [72.855282, 19.229694], [73.865477, 18.431897], [74.0042871, 18.5840622], [73.934888, 18.51884],
                        [72.823974, 19.066737], [73.851252, 18.53572], [72.894767, 19.088615], [72.811727, 19.359214],
                        [72.86313, 19.259786], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.834672, 19.133393], [72.944435, 19.156697], [73.822211, 18.444098], [79.179558, 21.142308],
                        [79.2838532, 21.1366894], [79.0902147, 21.1532586], [79.0845449, 21.1543698],
                        [79.325747, 21.395752], [79.65658, 21.17067], [79.325747, 21.395752], [79.65658, 21.17067],
                        [77.623548, 20.70566], [77.536479, 20.780511], [77.35641, 21.351964], [72.862086, 19.052074],
                        [72.563592, 23.027848], [72.914851, 20.076293], [72.851341, 19.229631],
                        [72.8367076, 19.1940346], [72.855282, 19.229694], [73.865477, 18.431897],
                        [79.325747, 21.395752], [77.623548, 20.70566], [77.536479, 20.780511], [77.35641, 21.351964],
                        [79.3827754, 21.3369123], [79.65658, 21.17067], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [79.325747, 21.395752], [77.623548, 20.70566], [77.536479, 20.780511],
                        [77.35641, 21.351964], [79.3827754, 21.3369123], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.87162, 19.061034], [73.88966, 18.482555], [73.876515, 18.531233], [73.870853, 18.491833],
                        [72.911817, 19.075386], [72.902559, 19.062799], [79.080832, 21.149727], [75.138365, 17.861267],
                        [74.168579, 16.840114], [74.04449, 16.981518], [73.897224, 16.947115], [79.1045821, 21.1558356],
                        [79.2838532, 21.1366894], [79.0902147, 21.1532586], [79.0845449, 21.1543698],
                        [79.65658, 21.17067], [79.937068, 20.069455], [78.597507, 20.439142], [78.159031, 20.050373],
                        [76.876962, 19.002491], [75.231344, 18.954419], [73.7427012, 19.9917339],
                        [73.6012531, 19.9555426], [73.529827, 19.935071], [73.516763, 16.217019],
                        [73.530177, 19.935386], [73.7427012, 19.9917339], [73.6012531, 19.9555426],
                        [73.933942, 18.5166069], [73.529827, 19.935071], [73.516763, 16.217019], [72.855282, 19.229694],
                        [73.865477, 18.431897], [72.901235, 19.134288], [72.811727, 19.359214], [72.86313, 19.259786],
                        [72.908806, 19.090445], [73.933942, 18.5166069], [75.9730232, 18.0656319],
                        [74.4315767, 16.2167242], [74.3392054, 20.3013233], [72.862086, 19.052074],
                        [72.563592, 23.027848], [72.914851, 20.076293], [74.5692178, 16.8534763],
                        [73.790236, 20.011248], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.8367076, 19.1940346], [72.855282, 19.229694], [73.865477, 18.431897],
                        [73.7427012, 19.9917339], [73.6012531, 19.9555426], [73.529827, 19.935071],
                        [73.516763, 16.217019], [73.530177, 19.935386], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [72.563592, 23.027848], [72.851341, 19.229631], [72.87162, 19.061034],
                        [74.293571, 18.34668], [72.563592, 23.027848], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [72.851341, 19.229631], [73.879327, 18.516428], [75.468659, 19.170391],
                        [73.776578, 16.676929], [73.303459, 18.125034], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.87162, 19.061034], [73.961647, 18.479429], [72.563592, 23.027848], [73.933942, 18.5166069],
                        [75.9730232, 18.0656319], [74.4315767, 16.2167242], [74.3392054, 20.3013233],
                        [74.2686431, 16.4500817], [72.888761, 19.085913], [72.833601, 19.0686],
                        [73.7498159, 19.9962035], [72.8254578, 18.9342776], [73.822915, 19.973191],
                        [73.822915, 19.973191], [72.563592, 23.027848], [72.851341, 19.229631], [72.87162, 19.061034],
                        [72.814695, 18.978485], [72.862086, 19.052074], [72.833094, 18.92171], [72.82595, 19.057433],
                        [72.87162, 19.061034], [72.865397, 18.925851], [75.012441, 19.697762], [79.995177, 19.649775],
                        [75.012441, 19.697762], [79.995177, 19.649775], [78.750678, 20.409617], [78.936725, 20.924385],
                        [78.428752, 20.49789], [73.000727, 19.065713], [73.08199, 19.119022], [72.862086, 19.052074],
                        [72.563592, 23.027848], [72.914851, 20.076293], [72.848509, 19.05467], [73.783982, 19.973567],
                        [74.580383, 16.876906], [73.857171, 18.462287], [72.82595, 19.057433],
                        [73.8770045, 18.533583999999998], [72.916633, 19.120386], [72.878695, 19.117477],
                        [73.876617, 18.5303865], [73.832128, 18.502214], [78.167148, 21.123817], [76.871478, 18.566991],
                        [76.85494, 18.939367], [75.759948, 19.01965], [75.027498, 18.5262], [73.934888, 18.51884],
                        [73.851252, 18.53572], [72.894767, 19.088615], [72.890607, 19.119814], [73.878127, 18.53303],
                        [73.7872931, 20.0126153], [73.7971644, 20.004924], [79.149898, 21.647061],
                        [73.828473, 18.53297], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [77.317324, 19.151038], [72.563592, 23.027848], [72.851341, 19.229631],
                        [73.9262112, 18.5298039], [73.9834356, 18.5719686], [74.0006199, 18.5900666],
                        [73.9332005, 18.588404], [79.077974, 21.104038], [79.077974, 21.104038], [75.929023, 17.651924],
                        [74.656808, 17.670441], [76.978986, 18.419328], [72.86038, 19.042796], [73.933942, 18.5166069],
                        [75.9730232, 18.0656319], [74.4315767, 16.2167242], [74.3392054, 20.3013233],
                        [74.2686431, 16.4500817], [73.873363, 18.480841], [72.845995, 19.195694],
                        [72.856841, 19.233802], [73.862844, 18.529218], [73.835668, 18.494205],
                        [72.8254578, 18.9342776], [72.813201, 18.954341], [72.814771, 18.952757],
                        [72.8125885, 18.9532025], [72.818686, 18.955719], [72.814771, 18.952757],
                        [72.813201, 18.954341], [72.833094, 18.92171], [72.9192, 19.721501], [72.909615, 19.722766],
                        [75.349147, 19.897968], [73.8355212, 18.5153029], [73.8107315, 18.4966112],
                        [73.7663651, 18.6062692], [72.934212, 19.717669], [72.862086, 19.052074],
                        [72.914851, 20.076293], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.851341, 19.229631], [77.088937, 19.374013], [73.000727, 19.065713], [73.08199, 19.119022],
                        [72.863629, 19.070934], [72.861267, 19.079273], [72.9273089, 19.1407116],
                        [72.8334568, 19.0681994], [74.84221, 20.676082], [74.648443, 20.600519], [73.964911, 17.340594],
                        [73.550023, 18.769998], [73.422349, 17.109176], [77.317324, 19.151038], [73.899193, 18.533169],
                        [74.0042871, 18.5840622], [74.84221, 20.676082], [74.648443, 20.600519], [73.964911, 17.340594],
                        [73.550023, 18.769998], [73.422349, 17.109176], [72.817039, 18.959424],
                        [73.9550925, 18.5595171], [72.817039, 18.959424], [72.817058, 18.9588476],
                        [72.8160225, 18.963334500000002], [72.815789, 18.962539], [72.864001, 19.071018],
                        [72.927837, 19.128196000000003], [72.875164, 19.04098], [72.863997, 19.065174],
                        [72.853444, 19.145536], [73.9499365, 18.5511925], [72.855502, 19.152408], [73.932336, 18.52036],
                        [72.882668, 19.093662], [73.952873, 18.491514], [72.870534, 19.104835], [74.000024, 19.845314],
                        [78.376734, 21.356585], [76.375451, 17.322669], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [74.123431, 19.796033], [74.000024, 19.845314], [75.070318, 21.445287],
                        [73.152013, 19.431964], [72.778969, 19.878293], [74.000024, 19.845314], [78.376734, 21.356585],
                        [76.375451, 17.322669], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [74.000024, 19.845314], [77.088937, 19.374013], [74.000024, 19.845314], [78.376734, 21.356585],
                        [76.375451, 17.322669], [72.862086, 19.052074], [74.0042871, 18.5840622],
                        [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293], [72.895574, 19.288213],
                        [72.9752205178309, 19.2391651], [72.970178, 19.194329], [72.851341, 19.229631],
                        [72.87162, 19.061034], [72.970178, 19.194329], [72.973395, 19.216319], [72.974023, 19.195153],
                        [72.976053, 19.246349], [72.96381, 19.207368], [72.888761, 19.085913], [72.833601, 19.0686],
                        [73.790236, 20.011248], [73.761528, 19.990662], [73.7242455, 19.6386918],
                        [73.5290626, 19.8971538], [73.790236, 20.011248], [73.761464, 19.958512],
                        [73.933942, 18.5166069], [75.9730232, 18.0656319], [74.4315767, 16.2167242],
                        [74.3392054, 20.3013233], [74.2686431, 16.4500817], [72.888761, 19.085913],
                        [72.833601, 19.0686], [73.761528, 19.990662], [73.7242455, 19.6386918],
                        [73.5290626, 19.8971538], [73.790236, 20.011248], [73.761464, 19.958512],
                        [76.992355, 21.217684], [76.154286, 20.223361], [74.166009, 21.619727], [79.149898, 21.647061],
                        [75.246887, 17.481415], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.851341, 19.229631], [73.790236, 20.011248], [72.877029, 19.170836], [79.117798, 21.101914],
                        [73.853463, 18.534785], [73.790236, 20.011248], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.87162, 19.061034], [73.961647, 18.479429], [73.790236, 20.011248], [75.154085, 19.700288],
                        [80.007822, 19.421892], [79.0821, 21.1498], [79.247932, 20.025035], [75.836022, 19.051696],
                        [74.434933, 21.044272], [79.0902431, 21.1101179], [73.863296, 18.529799],
                        [73.123831, 19.622296], [73.003725, 19.077644], [73.010522, 19.084868], [79.196418, 21.217065],
                        [76.252499, 20.349113], [79.671832, 21.30442], [79.432443, 19.816122], [78.070708, 19.295621],
                        [79.1316894, 21.1942105], [73.933942, 18.5166069], [79.196418, 21.217065],
                        [75.9730232, 18.0656319], [74.4315767, 16.2167242], [73.899193, 18.533169],
                        [72.563592, 23.027848], [72.851341, 19.229631], [72.87162, 19.061034], [72.563592, 23.027848],
                        [72.851341, 19.229631], [72.87162, 19.061034], [77.317324, 19.151038], [72.563592, 23.027848],
                        [72.851341, 19.229631], [73.65308, 16.330292], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [73.65308, 16.330292], [73.933942, 18.5166069],
                        [75.9730232, 18.0656319], [73.933942, 18.5166069], [75.9730232, 18.0656319],
                        [74.4315767, 16.2167242], [74.3392054, 20.3013233], [74.2686431, 16.4500817],
                        [73.898113, 18.677245], [77.568636, 18.679603], [73.898113, 18.677245],
                        [73.89683600000001, 18.676327999999998], [77.568636, 18.679603], [72.8367076, 19.1940346],
                        [73.000727, 19.065713], [73.08199, 19.119022], [72.855282, 19.229694], [73.875401, 18.480498],
                        [73.85293, 18.529587], [72.910164, 19.116919], [73.905001, 18.546017], [72.872087, 19.094735],
                        [73.919251, 18.463242], [73.935453, 18.518384], [73.887023, 18.539651], [73.829564, 18.532077],
                        [73.879993, 18.510672], [72.8367076, 19.1940346], [72.855282, 19.229694],
                        [77.317324, 19.151038], [73.899193, 18.533169], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [73.899193, 18.533169], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.87162, 19.061034], [73.612717, 18.755392], [72.862086, 19.052074], [72.914851, 20.076293],
                        [72.851341, 19.229631], [73.81511850000001, 18.517729000000003], [72.82595, 19.057433],
                        [73.933942, 18.5166069], [75.9730232, 18.0656319], [74.4315767, 16.2167242],
                        [74.3392054, 20.3013233], [74.2686431, 16.4500817], [72.888761, 19.085913],
                        [72.833601, 19.0686], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.851341, 19.229631], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.851341, 19.229631], [73.612717, 18.755392], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [73.612717, 18.755392], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [73.899193, 18.533169], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.87162, 19.061034], [73.529827, 19.935071], [73.516763, 16.217019], [73.530177, 19.935386],
                        [73.7427012, 19.9917339], [73.6012531, 19.9555426], [73.933942, 18.5166069],
                        [73.529827, 19.935071], [73.516763, 16.217019], [72.563592, 23.027848], [72.851341, 19.229631],
                        [72.87162, 19.061034], [73.961647, 18.479429], [73.7427012, 19.9917339],
                        [73.6012531, 19.9555426], [73.529827, 19.935071], [73.516763, 16.217019],
                        [73.530177, 19.935386], [72.968687, 19.263131], [73.934888, 18.51884], [72.823974, 19.066737],
                        [73.851252, 18.53572], [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [72.851341, 19.229631], [72.87162, 19.061034], [73.961647, 18.479429], [73.896447, 18.562624],
                        [72.940244, 19.049643], [76.125496, 19.955914], [77.946268, 20.490737], [75.940619, 17.492105],
                        [76.040523, 19.456594], [76.03377, 20.736771], [72.877393, 19.07599], [79.0821, 21.1498],
                        [72.851341, 19.229631], [72.87162, 19.061034], [79.247932, 20.025035], [72.563592, 23.027848],
                        [72.851341, 19.229631], [76.179911, 20.53208], [76.179911, 20.53208], [72.862086, 19.052074],
                        [72.563592, 23.027848], [76.125496, 19.955914], [77.946268, 20.490737], [75.940619, 17.492105],
                        [76.040523, 19.456594], [76.03377, 20.736771], [73.933942, 18.5166069],
                        [73.7498159, 19.9962035], [72.8254578, 18.9342776], [75.9730232, 18.0656319],
                        [79.149241, 21.44512], [79.03708, 21.117335], [80.372482, 20.961047], [79.555257, 20.844677],
                        [79.491461, 19.714298], [73.934888, 18.51884], [73.851252, 18.53572], [72.894767, 19.088615],
                        [72.890607, 19.119814], [73.878127, 18.53303], [79.0664632, 21.0974671],
                        [79.0707769, 21.1154412], [73.933942, 18.5166069], [78.599792, 20.746494],
                        [78.218251, 21.067548], [72.914253, 19.079184], [72.89975, 19.119578], [72.850127, 19.065403],
                        [72.841556, 19.469991], [72.832699, 18.944442], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [72.851341, 19.229631], [72.91229, 19.123823], [72.915411, 19.128146],
                        [72.897991, 19.123512], [77.138692, 19.631705], [75.480858, 20.725403], [72.563592, 23.027848],
                        [72.563592, 23.027848], [73.756248, 20.011207], [73.7872931, 20.0126153],
                        [72.917193, 19.099035], [72.920982, 19.123803], [73.937066, 18.51583], [73.894472, 18.556153],
                        [73.852322, 18.533981], [72.914253, 19.079184], [72.89975, 19.119578], [73.939629, 18.500343],
                        [73.875829, 18.521527], [72.844412, 19.183743], [73.023178, 19.034073], [79.122682, 21.137562],
                        [79.121366, 21.134273], [77.310745, 18.884698], [72.927837, 19.128196000000003],
                        [73.913521, 18.530886], [72.87531, 19.034204], [73.875884, 18.521377], [73.863296, 18.529799],
                        [72.8367076, 19.1940346], [72.855282, 19.229694], [73.865477, 18.431897],
                        [72.862086, 19.052074], [72.865397, 18.925851], [72.869891, 19.109283], [72.835429, 19.158232],
                        [72.82625, 19.227456], [72.862086, 19.052074], [72.833094, 18.92171], [72.82595, 19.057433],
                        [72.87162, 19.061034], [72.865397, 18.925851], [73.8770045, 18.533583999999998],
                        [72.916633, 19.120386], [72.878695, 19.117477], [73.876617, 18.5303865], [73.832128, 18.502214],
                        [72.828326, 18.940915], [72.828535, 18.938918], [72.826795, 18.943564], [72.818067, 18.952527],
                        [72.80459400000001, 18.9731795], [72.828535, 18.938918], [72.8275945, 18.9413633],
                        [72.826795, 18.943564], [72.833094, 18.92171], [72.82831, 18.923183], [72.862086, 19.052074],
                        [72.563592, 23.027848], [72.914851, 20.076293], [72.851341, 19.229631], [72.862086, 19.052074],
                        [72.833094, 18.92171], [72.82595, 19.057433], [72.87162, 19.061034], [72.865397, 18.925851],
                        [72.888761, 19.085913], [72.833601, 19.0686], [72.839141, 19.056546], [72.836896, 18.935112],
                        [72.8367076, 19.1940346], [72.855282, 19.229694], [72.828599, 19.230355],
                        [72.821526, 18.924562], [72.830546, 18.997146], [72.862086, 19.052074], [72.563592, 23.027848],
                        [72.914851, 20.076293], [72.851341, 19.229631], [73.87257, 18.500972], [72.808884, 18.957492],
                        [72.864001, 19.071018], [72.563592, 23.027848], [72.851341, 19.229631], [72.87162, 19.061034],
                        [73.8553706, 18.5268581], [73.933942, 18.5166069], [73.7498159, 19.9962035],
                        [72.8254578, 18.9342776], [75.9730232, 18.0656319], [73.961647, 18.479429],
                        [74.749345, 19.092952], [78.567262, 21.177502], [75.0127868, 18.6833661],
                        [75.0066984, 18.5683173], [73.996737, 19.4030717], [74.749345, 19.092952],
                        [78.567262, 21.177502], [75.0127868, 18.6833661], [75.0066984, 18.5683173],
                        [73.996737, 19.4030717], [74.749345, 19.092952], [78.567262, 21.177502], [74.594837, 18.718692],
                        [72.862086, 19.052074], [72.563592, 23.027848], [72.914851, 20.076293],
                        [73.8553706, 18.5268581], [76.1850939, 20.5358974], [72.862086, 19.052074],
                        [72.563592, 23.027848], [73.912025, 18.559873], [72.563592, 23.027848],
                        [73.8553706, 18.5268581], [76.1850939, 20.5358974], [72.862086, 19.052074],
                        [72.563592, 23.027848]])

# coordinates = np.array([
#     [42.123, -73.456],
#     [34.567, -45.678],
#     [40.789, -80.123],
#     [37.890, -95.678],
#     [30.456, -100.987],
#     [32.123, -76.543]
# ])

max_distance_threshold = 2000

# Maximum Haversine distance threshold (in meters)
close_coordinates = []

# Calculate pairwise Haversine distances and identify close coordinates
for i, coord1 in enumerate(coordinates):
    close_indices = [j for j, coord2 in enumerate(coordinates) if haversine_distance(coord1, coord2) <= max_distance_threshold]
    close_coordinates.append(close_indices)

# Combine close coordinates to create the adjacency matrix
adjacency_matrix = np.zeros((len(coordinates), len(coordinates)), dtype=int)
for i, indices in enumerate(close_coordinates):
    adjacency_matrix[i, indices] = 1

# Create KMeans instance
n_clusters = 50
kmeans = KMeans(n_clusters=n_clusters)

# Fit the model using adjacency matrix
kmeans.fit(adjacency_matrix)

# Get cluster labels
labels = kmeans.labels_

# Print cluster assignments
for i, label in enumerate(labels):
    print(f"Coordinate {coordinates[i]} belongs to cluster {label + 1}")

plt.figure(figsize=(8, 8))

# Plot clusters
for i in range(n_clusters):
    cluster_points = coordinates[labels == i]
    plt.scatter(cluster_points[:, 1], cluster_points[:, 0], label=f"Cluster {i + 1}")

# Plot convex hulls
# for i in range(n_clusters):
#     cluster_points = coordinates[labels == i]
#     hull = ConvexHull(cluster_points)
#     hull_polygon = Polygon(cluster_points[hull.vertices], fill=None, edgecolor='black', linewidth=2)
#     plt.gca().add_patch(hull_polygon)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("K-means Clustering with Convex Hulls")
plt.legend()
plt.show()

# n_clusters = 30
#
# # Create KMeans instance
# kmeans = KMeans(n_clusters=n_clusters)
#
# # Fit the model
# kmeans.fit(coordinates)
#
# # Get cluster labels and cluster centers
# labels = kmeans.labels_
# centers = kmeans.cluster_centers_
#
# # Get a list of coordinates for each cluster
# cluster_coordinates = [[] for _ in range(n_clusters)]
# for i, label in enumerate(labels):
#     cluster_coordinates[label].append(coordinates[i])
#
# coords = []
#
# for i, cluster_coords in enumerate(cluster_coordinates):
#     temp = []
#
#     # print(f"Cluster {i + 1} Coordinates:")
#     for coord in cluster_coords:
#         temp.append([coord[1], coord[0]])
#         # print(f"[{coord[1]},{coord[0]}],")
#
#     # print("temp:", np.array(temp))
#     coords.append(np.array(temp))
#
# coordinates = np.array([[20.480224, 79.75155],
#                         [21.353921, 80.313806],
#                         [21.150519, 79.547796],
#                         [20.633333, 79.511302],
#                         [20.902994, 79.493825],
#                         [21.17067, 79.65658],
#                         [21.17067, 79.65658],
#                         [21.17067, 79.65658],
#                         [21.17067, 79.65658],
#                         [21.30442, 79.671832],
#                         [20.961047, 80.372482],
#                         [20.844677, 79.555257]])
#
# # for coordinates in coords:
# if True:
#     hull = ConvexHull(coordinates)
#
#     # Print the coordinates of the convex hull vertices
#     convex_hull_coordinates = coordinates[hull.vertices]
#     for coord in convex_hull_coordinates:
#         print([coord[1],coord[0]])
#
#     # Plot the convex hull and the points
#     plt.plot(coordinates[:, 1], coordinates[:, 0], 'o', label='Points')
#     for simplex in hull.simplices:
#         plt.plot(coordinates[simplex, 1], coordinates[simplex, 0], 'k-')
#     plt.plot(coordinates[hull.vertices, 1], coordinates[hull.vertices, 0], 'r--', lw=2, label='Convex Hull')
#     plt.xlabel("Longitude")
#     plt.ylabel("Latitude")
#     plt.title("Convex Hull of GPS Coordinates")
#     plt.legend()
#
# plt.show()
