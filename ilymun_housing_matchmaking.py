import csv
import json

# Organise the delegate data
csvfile = open('delegates.csv', 'r')
jsonfile = open('delegates.json', 'w')
fieldnames = ('id', 'school', 'city', 'first_name', 'last_name', "sex", "dob", "nationality", "special_req", "day1", "day2", "day3", "day4")
reader = csv.DictReader( csvfile, fieldnames)
delegates_data = []
row_number = 0
for row in reader:
    days = []
    if row["day1"] == 1:
        days.push(1)
    if row["day2"] == 1:
        days.push(2)
    if row["day3"] == 1:
        days.push(3)
    if row["day4"] == 1:
        days.push(4)

    if row["sex"] == "M":
        sex = "male"
    elif row["sex"] == "F":
        sex = "female"
    delegate = {
        "id": row["id"],
        "first_name": row["first_name"],
        "last_name": row["last_name"],
        "sex": sex,
        "days": days
    }

    # Dump the selected delegate_data into the json file
    if row_number != 0:
        delegates_data.append(delegate)
    row_number += 1

json.dump(delegates_data, jsonfile)
jsonfile.write('\n')

# .json file format must be the following
# [
#     {
#         name: "Gamito",
#         student: "Pablo Gamito",
#         capacity: 2,
#         sex_preference: "female", # "none" or "male"
#         can_host_on_days: [1, 2, 3, 4, 5]
#     },
#     {
#         name: "Gillet",
#         student: "Martin Gillet",
#         capacity: 69,
#         sex_preference: "none", # "none" or "male"
#         can_host_on_days: [4, 5]
#     }
# ]

# matches = []
# delegates_with_no_preference_data = []
#
# with open('hosts_data.json') as data_file:
#     hosts_data = json.load(data_file)
#
# with open('delegates_data.json') as data_file:
#     delegates_data = json.load(data_file)

# for host in host_data:
#     available_capacity = host.capacity
#     sex_preference = host.sex_preference
#     for delegate in delegates_data:
#         if sex_preference == "none":
#             # keep for the end
#             delegates_with_no_preference_data.push(delegate)
#         elif sex_preference == "male":
#
#         elif sex_preference == "female":
#
#
#
# pprint(data)
