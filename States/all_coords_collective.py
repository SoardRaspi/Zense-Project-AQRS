import os
import csv

curr_path = os.path.join(os.getcwd(), 'Maharashtra')

coords_grouping = []

with open(os.path.join(curr_path, 'content3_data.csv'), mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
    # for i in range(1, 10):
        sno, coords, link, date = csvFile[i]

        coords_t = coords[1:-1]
        coords_t_list = coords_t.split(', ')

        count = 0
        temp = []

        for item in coords_t_list:
            item_t = item.strip()

            if item_t != '':
                if item_t[0] == '[':
                    item_tt = item_t[2:]

                elif item_t[0] == "'":
                    item_tt = item_t[1:]

                if item_tt[-1] == ']':
                    item_tt = item_tt[:-2]

                elif item_tt[-1] == "'":
                    item_tt = item_tt[:-1]

                if len(item_tt.split()) == 1:
                    temp.append(float(item_tt))

                    if count == 1:
                        count = 0
                        coords_grouping.append(temp)
                        temp = []

                    else:
                        count += 1

print(coords_grouping)
print(len(coords_grouping))