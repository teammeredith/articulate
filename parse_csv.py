import csv
import json
import re

words = {
    "Object":[],
    "Nature": [],
    "World": [],
    "Person": [],
    "Action": [],
    "Random": []
}

with open('Articulate.csv', "rt", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for key, value in row.items():
            if key == "Spade" or len(value) == 0: 
                continue
            pattern = r'[^A-Za-z0-9 \'\"]+'
            value = re.sub(pattern, '', value)
            words[key].append(value)
            

with open('words.js', "wt") as js_file:
    js_file.write("words = {\n")
    for key in words.keys():
        js_file.write("  "+key+": [\n")
        for value in words[key]:
            js_file.write("    \""+value+"\",\n")
        js_file.write("  ],\n")
    js_file.write("}\n")
