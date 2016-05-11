"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""

# read from keyboard
print ("Enter your string:")
input_str = raw_input()
print (input_str)

# write to a files
sample_file = open("new_file.txt", "w")
sample_file.write("Hi\nThis is a file!\n1\n2\n3")
sample_file.close()

# append some information to file
sample_file = open("new_file.txt", "a")  # w mode overwrites file. a: appending mode
sample_file.write("\n4\n5\n6")
sample_file.close()

# read mode
sample_file = open("new_file.txt", "r")
lines = sample_file.readlines()
for line in lines:
    print (line)
sample_file.close()

import requests
import json

# json: get country and city of a street
print ("Enter the street:")
street = raw_input()
google_url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + street
response = requests.get(google_url)
json_response = response.text
decoded_json = json.loads(json_response)
description = decoded_json["results"][0]["formatted_address"]
print (description)
