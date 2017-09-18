# read_json.py
#
# Simple  script that loads the external json files needed for trinomial lookup.
# This was implemented as a separate file so that trinomiallookup  would not have to
# load the file for every instance ot itself.

import json

statefile = "states.json"

def read_json_file(filename):
    with open(filename, 'r') as f:
        datastore = json.load(f)

    return datastore

statebase = read_json_file("states.json")
