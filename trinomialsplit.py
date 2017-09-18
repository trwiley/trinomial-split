# Name: trinomialsplit.py
# Description: class that stores an ST and its split-up version
# Attributes:
#   Variables:
#       trinomial - string containing an instance of an ST.
#       statenumber - contains the state code. 1 - 50, alphabetical except for Alaska and Hawaii
#       countycode - contains alphabetical county code string.
#       sitenumber - contains actual site number.#

class TrinomialSplit:

    trinomial = ""
    statenumber = ""
    countycode = ""
    sitenumber = ""


    def __init__(self, trinomialinstance):
        self.trinomial = trinomialinstance
        self.split_trinomial()



    # see if the trinomial has dashes or spaces
    def has_dashes_or_spaces(self):
        for i in range(0, len(self.trinomial)):
            if (self.trinomial[i] == " ") or (self.trinomial[i] == "-"):
                return True

        return False

    # strip dashes or spaces
    def strip_dashes(self):
        strippedtrinomial = ""
        for i in range(0, len(self.trinomial)):
            # if the character is not a space or dash, copy it over.
            if (self.trinomial[i] != " ") and (self.trinomial[i] != "-"):
                strippedtrinomial += self.trinomial[i]
        self.trinomial = strippedtrinomial

    # see if the trinomial has parentheses or brackets, return true if the case.
    def has_parens_or_brackets(self):
        if (self.trinomial[0] == "(") and (self.trinomial[len(self.trinomial) - 1] == ")"):
            return True
        elif (self.trinomial[0] == "[") and (self.trinomial[len(self.trinomial) - 1] == "]"):
            return True
        else:
            return False

    # Strip trinomial of brackets or parens
    def strip_parens(self):
        strippedtrinomial = ""
        for i in range(0, len(self.trinomial)):
            # If not the first or last character (the spaces, in other words), copy over.
            if (i != 0) and (i != len(self.trinomial) - 1):
                strippedtrinomial += self.trinomial[i]

        # store the stripped version back into the original.
        self.trinomial = strippedtrinomial

    def split_trinomial(self):

        if self.has_parens_or_brackets():
            self.strip_parens()

        if self.has_dashes_or_spaces():
            self.strip_dashes()

        if self.is_lowercase():
            self.change_toupper()

        for i in range(0, len(self.trinomial)):

            #If the state number is two digits long:
            if self.trinomial[1].isdigit():
                # Stuff the first two characters into the state number
                if i < 2:
                    self.statenumber += self.trinomial[i]

                # Stuff the next two characters into the county code
                elif i < 4:
                    self.countycode += self.trinomial[i]

                # Stuff the rest into the site number
                else:
                    self.sitenumber += self.trinomial[i]
            #if the state number is one digit long
            else:
                # Stuff the first character into the state number
                if i < 1:
                    self.statenumber += self.trinomial[i]

                # Stuff the next two characters into the county code
                elif i < 3:
                    self.countycode += self.trinomial[i]
                # Stuff the rest into the site number
                else:
                    self.sitenumber += self.trinomial[i]

    # Test function to print out the trinomial elements.
    def print_elements(self):
        print(self.statenumber + " " + self.countycode + " " + self.sitenumber)
     # test function
    def print_trinomial(self):
        print(self.trinomial)

    # checks if any of the letters are lower case, and, if so, returns true.
    def is_lowercase(self):
        for i in range(0, len(self.trinomial)):
            if self.trinomial[i].isalpha():
                if self.trinomial.islower():
                    return True

        return False

    #changes any lowercase letters to uppercase.
    def change_toupper(self):
        temp = ""
        for i in range(0, len(self.trinomial)):
            if  self.trinomial[i].isalpha() and self.trinomial[i].islower():
                temp += self.trinomial[i].upper()
            else:
                temp += self.trinomial[i]
        self.trinomial = temp
        