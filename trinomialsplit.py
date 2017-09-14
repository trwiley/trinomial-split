# Name: trinomialsplit.py
# Description: class that stores an ST and its split-up version
# Attributes:
#   Variables:
#       trinomial - string containing an instance of an ST.
#       statenumber - contains the state code. 1 - 50, alphabetical except for Alaska and Hawaii
#       countycode - contains alphabetical county code string.
#       sitenumber - contains actual site number.#



class TrinomialSplit:

    trinomial = None

    statenumber = None
    countycode = None
    sitenumber = None

    def __init__(self, trinomialinstance):
        self.trinomial = trinomialinstance
