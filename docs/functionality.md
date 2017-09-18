# Functionality of trinomial-split

trinomial-split has 2 classes: TrinomialSplit and TrinomialLookup
## TrinomialSplit

Consists of the trinomial itself and the functions to split it in its constituent elements.

Splitting a trinomial is a process that involves doing a basic formatting check first, then splitting it. 
Checks for parentheses or braces and dashes or spaces are implemented, since these are the most common trinomial
formats other than the trinomial having no spaces or anything surrounding it other than whitespace, at least according 
to the data from the last 10 years of American Antiquity. 

The constructor for TrinomialSplit takes a string argument with a trinomial:

```buildoutcfg
exampletrinomial = trinomialsplit.TrinomialSplit("20MA12")
```

In the constructor, the splitting function is called.

### split_trinomial

Called in the the constructor and splits the trinomial into the state number, county code, and site digits. First, it
checks to see whether there are parentheses by calling has_parens_or_brackets, and if so it calls strip_parens.
Next, it does a similar process with dashes or spaces, only it calls has_dashes_or_spaces and if it does have dashes
or spaces, it calls strip_dashes. 

After the formatting is stripped, the function checks whether the trinomial has a state code that is one or two
characters long. Depending on which it is, the locations where the trinomial is split is different. Either way, each of
the parts is stored in its respective variable.

### has_dashes_or_spaces

Boolean function. Checks whether the trinomial has dashes or spaces or not. If so, return true.

### strip_dashes

Strips dashes or spaces from a trinomial. Does so by going through the original trinomial input, and storing the non
dash or space characters into a temporary string variable. This temp is stored into the trinomial class member.

### has_parens_or_brackets

Boolean function. Checks whether the trinomial has parentheses or brackets. if so, return true.

### strip_parens

Strips the parentheses or brackets off of a trinomial. Does so by copying all of the characters in the trinomial that 
are not at the beginning or at the end.



## TrinomialLookup

The constructor of TrinomialLookup makes an instance of TrinomialSplit. More to be added in the future.

## read_json

Simple script that loads in the state (and eventually county) JSON files. This functionality was implemented
a separate from TrinomialLookup so that a new instance of the state and county lookup would not be created 
everytime a new lookup object is made.

