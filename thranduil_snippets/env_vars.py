#! /usr/bin/env python3

import os
import re
import json

# get variable from Bash variable
a = os.getenv("SALES_DATA").strip()
print("SALES_DATA (raw):")
print(a)
print("")

# regex to clean up new lines
a = re.sub(r'\s*{\s*', '{', a)
a = re.sub(r'\s*}\s*', '}', a)
a = re.sub(r'\s*"\s*', '"', a)
a = re.sub(r'\s*\n\s*', ',', a)
print("SALES_DATA (cleaned):")
print(a)
print("")

# convert to json
j = json.loads(a)
print("SALES_DATA (dict):")
print(json.dumps(j, indent=2))
print("")

# write it to a JSON file
f = "my_sales.json"
with open(f, "r", encoding="utf-8") as file:
    my_sales = json.load(file)

my_sales["sales_history"].append(j)

with open(f, "w", encoding="utf-8") as file:
    json.dump(my_sales, file, indent=4)
