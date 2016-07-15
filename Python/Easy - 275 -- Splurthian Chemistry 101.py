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
Given an element name, find the valid symbol for that name that's first in 
alphabetical order. E.g. Gozerium -> Ei, Slimyrine -> Ie.
"""

#Import needed for bonus
import string

def checksymbol(elementName, symbol):
    print(elementName)

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

def findFirstSymbol(elementName):
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