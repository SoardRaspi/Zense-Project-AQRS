from flask import Flask
import csv
import json
import os
# from flask_ngrok import run_with_ngrok

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.spatial import ConvexHull
from scipy.cluster.hierarchy import linkage, fcluster
from geopy.distance import geodesic

import numpy as np
from scipy.spatial import ConvexHull
# import matplotlib.pyplot as plt

# coords2 = []
# fences = None

with open("server_data.json", 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    coords2 = json_object['coords']
    fences = json_object['fences']
    counts = json_object['counts']

# Function to calculate Haversine distance between two sets of coordinates
def haversine_distance(coord1, coord2):
    coord1_rad = np.radians(coord1)
    coord2_rad = np.radians(coord2)

    d_lat = coord2_rad[1] - coord1_rad[1]
    d_lon = coord2_rad[0] - coord1_rad[0]

    a = np.sin(d_lat / 2) ** 2 + np.cos(coord1_rad[1]) * np.cos(coord2_rad[1]) * np.sin(d_lon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    return c * 6371000  # Earth's radius in meters

# coordinates = np.array(coords2)
#
# max_grouping_distance = 20000  # Adjust this threshold as needed
#
# # Create a list to store groups of coordinates
# coordinate_groups = []
#
# # Loop through each coordinate and group them based on distance
# for coord in coordinates:
#     added_to_group = False
#     for group in coordinate_groups:
#         if all(haversine_distance(coord, existing_coord) <= max_grouping_distance for existing_coord in group):
#             group.append(coord)
#             added_to_group = True
#             break
#     if not added_to_group:
#         coordinate_groups.append([coord])
#
# # Visualize the coordinate groups on a map
#
# temp = []
#
# # plt.figure(figsize=(4, 4))
# for i, group in enumerate(coordinate_groups):
#     group_coords = np.array(group)
#     temp.append(group_coords)

    # print(i, ":", group)

app = Flask(__name__)
# run_with_ngrok(app)


@app.route('/request')
def request():
    result_fences = {}
    count_fence = {}

    # if True:
    #     coords = {1: {"v1": {"lat": -27.457, "long": 153.040}, "v2": {"lat": -33.852, "long": 151.211},
    #                   "v3": {"lat": -37.813, "long": 144.962}, "v4": {"lat": -34.928, "long": 138.599}},
    #               2: {"v1": {"lat": -31.673, "long": 128.892}, "v2": {"lat": -31.952, "long": 115.857},
    #                   "v3": {"lat": -17.785, "long": 122.258}, "v4": {"lat": -12.4258, "long": 130.7932}}}

    if fences[0]:
        for key in fences[0]:
            result_fences[key] = {}
            count_fence[key] = {}

            count = 1
            for coord_f in fences[0][key]:
                result_fences[key]["v" + str(count)] = {"lat": coord_f[1], "long": coord_f[0]}
                count_fence[key] = counts[0][key]

                count += 1

    return {"0": result_fences, "1": count_fence}
    # return {"data": coords}

@app.route('/process/radius=<rad>')
def process(rad):
    coordinates = np.array(coords2)

    max_grouping_distance = int(rad)  # Adjust this threshold as needed

    # Create a list to store groups of coordinates
    coordinate_groups = []

    # Loop through each coordinate and group them based on distance
    for coord in coordinates:
        added_to_group = False
        for group in coordinate_groups:
            if all(haversine_distance(coord, existing_coord) <= max_grouping_distance for existing_coord in group):
                group.append(coord)
                added_to_group = True
                break
        if not added_to_group:
            coordinate_groups.append([coord])

    # Visualize the coordinate groups on a map

    temp = []

    # plt.figure(figsize=(4, 4))
    for i, group in enumerate(coordinate_groups):
        # group_coords = np.array(group)
        # temp.append(list(group_coords))
        # print("type", type(group))

        group_list = []

        for item in group:
            group_list.append([item[0], item[1]])
        temp.append(group_list)

    print("temp:", temp)

    return {"data": temp}

def distance(coord1, coord2):
    return geodesic([coord1[1], coord1[0]], [coord2[1], coord2[0]]).meters

@app.route('/process/point=<lat>,<long>&radius=<r>&status=<stat>')
def process_new(lat, long, r, stat):
    latitude = float(lat)
    longitude = float(long)
    radius = int(r)

    fences2 = fences.copy()
    counts_data = counts.copy()

    coordinates = coords2.copy()
    coordinates.append([longitude, latitude])

    if stat == "y":
        num_coords = len(coordinates)
        dist_matrix = np.zeros((num_coords, num_coords))

        for i in range(num_coords):
            for j in range(num_coords):
                dist_matrix[i][j] = distance(coordinates[i], coordinates[j])

        # Convert the distance matrix to condensed form
        dist_condensed = pdist(np.array(coordinates), metric=distance)

        # Perform hierarchical clustering
        linkage_matrix = linkage(dist_condensed, method='complete')  # You can choose a different method if needed
        max_distance_threshold = radius  # Maximum distance threshold for grouping

        # Get cluster assignments
        clusters = fcluster(linkage_matrix, t=max_distance_threshold, criterion='distance')

        ans = {}
        count = 1

        # Organize coordinates into clusters
        clustered_coordinates = {}
        for i, cluster_id in enumerate(clusters):
            if cluster_id not in clustered_coordinates:
                clustered_coordinates[cluster_id] = []
            clustered_coordinates[cluster_id].append(coordinates[i])

        for key in clustered_coordinates:
            temp_coords_fence = []

            for coord in clustered_coordinates[key]:
                if coord not in temp_coords_fence:
                    temp_coords_fence.append(coord)

            if len(temp_coords_fence) > 2:
                print("cluster", key, ":")

                for coord in temp_coords_fence:
                    print(coord)

                hull = ConvexHull(temp_coords_fence)

                print("hull coordinates for cluster:", key)
                print(hull.vertices)

                temp_coords = []

                for index in hull.vertices:
                    temp_coords.append(temp_coords_fence[int(index)])

                ans[count] = temp_coords
                count += 1

        fences2 = [ans]

    json.dump({"coords": coordinates, "fences": fences2, "counts": counts_data}, openfile)

app.run(debug=True, port=8001)
