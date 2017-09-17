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
### Pseudocode

```

declare a copy of the ST for formatting and splitting purposes in the class definition

check for parens
check for separators

if the ST has parens
   remove them and return the version of the ST with removed parens
if the ST has separators:
   remove them and return the version of the ST withh removed parens

send ST copy to splitters

```

#### Splitting function

```
for each character in the trinomial

   if trinomial[character] < 3
      trinomial[character] += statenumber
   
   if trinomial[character] < 5
      trinomial[character] += countycode

   else
      trinomial[character] += sitecode
```

## TrinomialLookup

Will consist of lookup tables for counties and states and the functions to look up trinomial areas. The idea at the moment is to store these as CSV or JSON but this may change as I do 
more research about what would be the most painless way to accomplish this.

