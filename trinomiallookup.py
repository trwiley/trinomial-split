# trinomiallookup.py
# Set of functions for reading through a JSON files containing states and counties and
# mapping those counties to states.

import json


statefile = "states.json"

#Read a JSON file.
def read_json_file(filename):
    with open(filename, 'r') as f:
        datastore = json.load(f)

    return datastore

statebase = read_json_file("states.json")

#Go through the JSON file and search for the state. If it is found, return it.
def lookup_state(trinomial):
  for i in statebase['ST_states']:
      if i.get('Tri') == trinomial.statenumber:
          return i.get('state')
  return "Not found."