import trinomialsplit as ts
import json
import read_json as rj

class TrinomialLookup:

    state = ""
    county = ""



    def  __init__(self,  trinomialinstance):
        trinomial = ts.TrinomialSplit(trinomialinstance)

