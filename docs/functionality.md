# Functionality of trinomial-split

Trinomial-split will consist of two classes to begin with: TrinomialSplit and TrinomialLookup.

## TrinomialSplit

Consists of the trinomial itself and the functions to split it in its constituent elements.

Splitting a trinomial is a process that involves doing a basic formatting check first, then splitting it. Initially, there will just be a check for spaces and parens/braces, since those 
are the most common variants, at least judging from summary statistics gathered from the last decade of American Antiquity. 

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


## TrinomialLookup

Will consist of lookup tables for counties and states and the functions to look up trinomial areas. The idea at the moment is to store these as CSV or JSON but this may change as I do 
more research about what would be the most painless way to accomplish this.

