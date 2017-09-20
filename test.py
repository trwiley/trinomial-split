#Name: test.py
#Purpose; test the TrinomialSplit class.


import trinomialsplit as ts
import trinomiallookup as tl

t = input("Enter a ST: ")

trinomial = ts.TrinomialSplit(t)
state = tl.lookup_state(trinomial)
print(state)

