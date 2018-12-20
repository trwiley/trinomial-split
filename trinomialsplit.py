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
    count = 0
    countycount = 0


    def __init__(self, trinomialinstance):
        self.trinomial = trinomialinstance
        self.split_trinomial()

    def has_dashes(self):
        if self.trinomial.find("-") != -1:
            return True
        else:
            return False

    def has_spaces(self):
        if self.trinomial.find(" ") != -1:
            return True
        else:
            return False


    def has_state_no(self):
        if self.statenumber == "00":
            return False
        else:
            return True

    # strip dashes
    def strip_dashes(self):
        self.trinomial = self.trinomial.replace("-", "")

    #strip spaces
    def strip_spaces(self):
        self.trinomial = self.trinomial.replace(" ", "")

    def has_parens(self):
        if ((self.trinomial.find("(") != -1) or (self.trinomial.find(")") != -1)):
            return True
        else:
            return False

    def has_brackets(self):
        if ((self.trinomial.find("[") != -1) or (self.trinomial.find("]") != -1)):
            return True
        else:
            return False


    

    # Strip trinomial of brackets or parens
    def strip_parens(self):
        self.trinomial = self.trinomial.replace("(", "")
        self.trinomial = self.trinomial.replace(")", "")
    
    def strip_brackets(self):
        self.trinomial = self.trinomial.replace("]", "")
        self.trinomial = self.trinomial.replace("[", "")



    #Grabs the state code.

    def get_state_code(self):
        self.statenumber = self.trinomial[self.count:2]
        self.count += 2

    #Grabs the county code
    def get_county_code(self):
        # If there is a state number, the starting off point for the loop should be its length.
        # else, it should be 0.

        #keep track of what the length of the county code is.
        countylen = 0

        for char in self.trinomial:
            if char.isalpha():
                countylen += 1

        #county code spans from the current count to the end of the code
        self.countycode = self.trinomial[self.count:self.count + countylen]
        self.count += countylen


    #grabs the site number
    def get_site_number(self):
        self.sitenumber = self.trinomial[self.count:]

    # see if the site number has leading zeros
    def has_leading(self):
        if self.sitenumber[0] == "0":
            return True
        else:
            return False

    #count and return the number of leading zeros
    def leadingzeros(self):
        leading = 0
        for n in self.sitenumber:
            if n == "0":
                leading += 1
            else:
                return leading

    # remove the leading zeroes
    def remove_leading(self):
        self.sitenumber = self.sitenumber[self.leadingzeros():]




    def split_trinomial(self):

        if self.has_parens():
            self.strip_parens()
        if self.has_brackets():
            self.strip_brackets()

        if self.has_dashes():
            self.strip_dashes()
        if self.has_spaces():
            self.strip_spaces()
        

        if self.is_lowercase():
            self.change_toupper()

        if self.has_state_no():
             self.get_state_code()
        else:
            self.statenumber = "00"
        self.get_county_code()
        self.get_site_number()

        if self.has_leading():
            self.remove_leading()


    # Test function to print out the trinomial elements.
    def print_elements(self):
        print(self.statenumber + " " + self.countycode + " " + self.sitenumber)
     # test function
    def print_trinomial(self):
        print(self.trinomial)

    # checks if any of the letters are lower case, and, if so, returns true.
    def is_lowercase(self):
        for char in self.trinomial:
            if char.islower():
                return True
        return False

    #changes any lowercase letters to uppercase.
    def change_toupper(self):
        temp = ""
        for char in self.trinomial:
            if char.islower():
                temp += char.upper()
            else:
                temp += char

        self.trinomial = temp
        
