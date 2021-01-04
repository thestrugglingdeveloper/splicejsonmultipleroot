import splicejsonmultipleroots
import json
input_text = '{"data": { "id": 1}}{"data": { "id": 2}}{"data": { "id": 3}}'

# List of strings representing each a stringified json string
my_list = splicejsonmultipleroots.splice_json(input_text)

for entry in my_list:
    # Parse with json to get an object
    print(json.loads(entry))
