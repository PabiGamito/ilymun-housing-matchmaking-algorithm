import csv
import json

# ##################### #
# GET THE DELEGATE DATA #
# ##################### #
csvfile = open('delegates.csv', 'r')
jsonfile = open('delegates.json', 'w')
# Convert .csv to arry
fieldnames = ('id', 'school', 'city', 'first_name', 'last_name', "sex", "dob", "nationality", "allergies", "special_req", "day1", "day2", "day3", "day4")
reader = csv.DictReader( csvfile, fieldnames)
delegates_data = []
row_number = 0
# Parse the needed data into usable format
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

    if row["allergies"] != "":
        alergies = True
    else:
        alergies = False

    delegate = {
        "id": row["id"],
        "first_name": row["first_name"],
        "last_name": row["last_name"],
        "sex": sex,
        "days": days,
        "alergies": alergies
    }

    # Add the parsed delegate data into the delegate data array
    if row_number != 0:
        delegates_data.append(delegate)
    row_number += 1

# Dump the selected delegate_data into the json file
json.dump(delegates_data, jsonfile)
jsonfile.write('\n')

# #################### #
# GET THE HOSTING DATA #
# #################### #
csvfile = open('hosts.csv', 'r')
jsonfile = open('hosts.json', 'w')
# Convert .csv to arry
fieldnames = ('horodateur', 'last_name', 'first_name', 'adresse', 'phone', "email", "capacity", "sex_preference", "day1", "day2", "day3", "day4")
reader = csv.DictReader( csvfile, fieldnames)
delegates_data = []
row_number = 0
# Parse the needed data into usable format
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

    if row["sex_preference"] == "Boys":
        sex_preference = "male"
    elif row["sex_preference"] == "Girls":
        sex_preference = "female"
    else:
        sex_preference = "none"
    delegate = {
        "id": row["id"],
        "first_name": row["first_name"],
        "last_name": row["last_name"],
        "sex_preference": sex_preference,
        "days": days,
        "capacity": capacity
    }

    # Add the parsed delegate data into the delegate data array
    if row_number != 0:
        delegates_data.append(delegate)
    row_number += 1

# Dump the selected delegate_data into the json file
json.dump(delegates_data, jsonfile)
jsonfile.write('\n')

# TODO: Treat student with alergies independently later

matches = []
hosts_with_no_preference_data = []

with open('hosts.json') as data_file:
    hosts_data = json.load(data_file)

with open('delegates.json') as data_file:
    delegates_data = json.load(data_file)

for host in host_data:
    available_capacity = host["capacity"]
    sex_preference = host["sex_preference"]
    for delegate in delegates_data:
        if sex_preference == "none":
            # keep for the end
            hosts_with_no_preference_data.append(delegate)
        elif sex_preference == delegate["sex"]:
            # Found match
            matches.append({
                "host": host
                "delegate": delegate
            })
            # TODO: Remove delegate from list
            host["capacity"] = host["capacity"] - 1



pprint(data)
