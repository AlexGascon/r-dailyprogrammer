"""
DESCRIPTION

The inhabitants of the planet Splurth are building their own periodic table of
the elements. Just like Earth's periodic table has a chemical symbol for each 
element (H for Hydrogen, Li for Lithium, etc.), so does Splurth's. However, 
their chemical symbols must follow certain rules:

    - All chemical symbols must be exactly two letters, so B is not a valid symbol
    for Boron.
    - Both letters in the symbol must appear in the element name, but the first
    letter of the element name does not necessarily need to appear in the symbol.
    So Hg is not valid for Mercury, but Cy is.
    - The two letters must appear in order in the element name. So Vr is valid 
    for Silver, but Rv is not. To be clear, both Ma and Am are valid for 
    Magnesium, because there is both an a that appears after an m, and an m that
    appears after an a.
    - If the two letters in the symbol are the same, it must appear twice in the
    element name. So Nn is valid for Xenon, but Xx and Oo are not.

As a member of the Splurth Council of Atoms and Atom-Related Paraphernalia, you 
must determine whether a proposed chemical symbol fits these rules.


DETAILS
Write a function that, given two strings, one an element name and one a proposed
symbol for that element, determines whether the symbol follows the rules. If you
like, you may parse the program's input and output the result, but this is not 
necessary.

The symbol will have exactly two letters. Both element name and symbol will 
contain only the letters a-z. Both the element name and the symbol will have 
their first letter capitalized, with the rest lowercase. (If you find that too 
challenging, it's okay to instead assume that both will be completely lowercase.)


EXAMPLES
Spenglerium, Ee -> true
Zeddemorium, Zr -> true
Venkmine, Kn -> true
Stantzon, Zt -> false
Melintzum, Nn -> false
Tullium, Ty -> false


BONUS
1. Given an element name, find the valid symbol for that name that's first in 
alphabetical order. E.g. Gozerium -> Ei, Slimyrine -> Ie.

2. Given an element name, find the number of distinct valid symbols for that
name. E.g. Zuulon -> 11.

3. The planet Blurth has similar symbol rules to Splurth, but symbols can be 
any length, from 1 character to the entire length of the element name. Valid 
Blurthian symbols for Zuulon include N, Uuo, and Zuuln. Complete challenge #2 
for the rules of Blurth. E.g. Zuulon -> 47.
"""

#Import needed for bonus
import string

def checksymbol(elementName, symbol):
    """Function that gets two string parameters: an element name and a symbol
    used to represent it, and outputs a boolean indicating if the symbol is
    valid for the given element"""

    #Rule 1: Two letters per symbol
    if len(symbol) != 2:
        return False

    #Rule 2: only letters
    if not symbol.isalpha():
        return False

    #Rule 3: first uppercase, second lowercase
    if symbol[0].islower() or symbol[1].isupper():
        return False

    #Rule 4 + 5: Letter must appear and in same order
    # We have to lowercase both elements to compare in order to avoid case mismatch
    # We'll start looking for the second letter from the end (rfind), in order to 
    # avoid finding an earlier coincidence
    firstindex = elementName.lower().find(symbol[0].lower())
    secondindex = elementName.lower().rfind(symbol[1].lower())
    if secondindex <= firstindex and firstindex != -1:
        return False

    return True

# Function created for Bonus 1
def findFirstSymbol(elementName):
    """Function that gets a string parameter representing an element name and
    returns a string representing the first symbol in alphabetical order for
    that element. """

    alphabet = string.lowercase
    #Getting the order of each letter in the alphabet
    # We discard the last letter of the name when getting the first char because,
    # as we need two letters, we don't care about the position of the last one 
    letterOrder = [alphabet.index(letter) for letter in elementName[:-1].lower()]
    firstLetterIndex = letterOrder.index(min(letterOrder))
    firstLetter = elementName[firstLetterIndex]

    # Now we do care about the last letter, but not about the ones prior to the
    # first letter of the symbol
    letterOrderRemaining = letterOrder[(firstLetterIndex + 1) :] + [alphabet.index(elementName[-1])]
    secondLetterIndex = letterOrderRemaining.index(min(letterOrderRemaining))
    secondLetter = elementName[secondLetterIndex + (firstLetterIndex + 1)]

    return (firstLetter.upper() + secondLetter)

# Function created for Bonus 2
def countPossibleSymbols(elementName):
    """Function that given an element name returns an integer representing the
    amount of possible symbols available for it, according to the rules
    previously stated"""

    #Finding repeated consecutive letters (most of the symbols will appear twice) 
    charsElemName = list(elementName)
    repeatedLetters = [charsElemName[i+1] == charsElemName[i] for i in range(0, len(charsElemName)-1)]
    #Taking the repeated letters out
    #For each repeted letter, we can take out the letter and add to the count
    #a +1, representing the repeated-letter symbol
    #Ex: "Zuulon" will have the same symbols as "Zulon" + 1 ("Uu" symbol)
    if True in repeatedLetters:
        charsElemName.pop(repeatedLetters.index(True))
        return countPossibleSymbols("".join(charsElemName)) + 1
    else:
        possibleSymbols = 


print(countPossibleSymbols)






