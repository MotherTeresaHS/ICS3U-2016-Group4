import json

item_to_load = [['MAT - ', 1000000], ['MAT - ', 100000], ['MAT - ', 10000], ['MAT - ', 1000], ['MAT - ', 100], ['MAT - ', 10]]

high_scores_list = open('./high_scores.txt', 'r+')

high_scores_list.truncate(0)

json.dump(item_to_load, high_scores_list)

high_scores_list.close()
