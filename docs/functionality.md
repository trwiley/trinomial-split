# Functionality of trinomial-split

trinomial-split is a repo containing classes and functions to split up trinomials into their constituent parts and
use those parts to lookup the state and county the trinomial is associated with. It consists of the following scripts:
## trinomialsplit

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

Then, it calls three functions that grab the state number, county code, and site code specifically. The state number 
grabber adds characters to the state number until it hits an alphabetical character, at which point it returns. The site
number grabber starts from the point the other two functions left off and stuffs the rest of the characters into
its variable.

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

### has_leading

Checks whether the site number has leading zeroes or not

### leadingzeros

Counts and returns the number of leading zeroes in the site number.

### removeleading

Removes leading zeros from a trinomial



## trinomiallookup

Script that reads in JSON files containing state data and contains functions for returning the state
and county of a trinomial by passing in its elements.



