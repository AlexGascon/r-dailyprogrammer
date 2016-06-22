"""
DESCRIPTION

Scrabble is a popular word game where players remove tiles with letters on them
from a bag and use them to create words on a board. The total number of tiles as
well as the frequency of each letter does not change between games.
For this challenge we will be using the tile set from the English edition, which
has 100 tiles total. Here's a reference for the distribution and point value of 
each tile: http://scrabblewizard.com/scrabble-tile-distribution/
Each tile will be represented by the letter that appears on it, with
the exception that blank tiles are represented by underscores _.


INPUT DESCRIPTION
The tiles already in play are inputted as an uppercase string. For example, if 14
tiles have been removed from the bag and are in play, you would be given an input
like this:

AEERTYOXMCNB_S


OUTPUT DESCRIPTION
You should output the tiles that are left in the bag. The list should be in 
descending order of the quantity of each tile left in the bag, skipping over 
amounts that have no tiles. In cases where more than one letter has the same
quantity remaining, output those letters in alphabetical order, with blank tiles
at the end.

10: E
9: I
8: A
7: O
5: N, R, T
4: D, L, U
3: G, S
2: F, H, P, V, W
1: B, C, J, K, M, Q, Y, Z, _
0: X

If more tiles have been removed from the bag than possible, such as 3 Qs, you
should give a helpful error message instead of printing the list.
Example: 
"Invalid input. More Q's have been taken from the bag than possible."

"""

    def whatsinbag(tiles_played):

        #PART 1: GETTING THE DISTRIBUTION
        #Tile distribution of the English version of Scrabble 
        tile_distribution = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 
                            'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 
                            'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
                            'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2}

        #Removing the played tiles out of the total distribution
        for tile in tiles_played:
            tile_distribution[tile] -= 1

            #Checking if we've taken more units of that tile than available
            #If that's the case, we'll stop the loop
            if tile_distribution[tile] < 0:
                print("Invalid input. More {}'s have been taken from the bag than possible.".format(tile))
                return None


        #PART 2: PREPARING THE RESULT
        results = {}
        for letter in tile_distribution:
            amount_left = tile_distribution[letter]

            #Adding a letter to the result dictionary
            try:
                results[amount_left] += letter
            
            except KeyError:
                results[amount_left] = letter

        appearances = results.keys()
        appearances.sort(reverse = True)

        #PART 3: PRINTING THE RESULT
        separator = ", "
        for num in appearances:
            print( str(num) + ": " + separator.join(results[num]))




    


input1 = "PQAREIOURSTHGWIOAE_"
input2 = "LQTOONOEFFJZT"
input3 = "AXHDRUIOR_XHJZUQEE"

whatsinbag(input1)
print("\n\n\n")
whatsinbag(input2)
print("\n\n\n")
whatsinbag(input3)