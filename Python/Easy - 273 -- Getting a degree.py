"""
DESCRIPTION
Welcome to DailyProgrammer University. Today you will be earning a degree in 
converting degrees. This includes Fahrenheit, Celsius, Kelvin, Degrees (angle),
and Radians.


INPUT DESCRIPTION
You will be given two lines of text as input. On the first line, you will receive
a number followed by two letters, the first representing the unit that the number
is currently in, the second representing the unit it needs to be converted to.

Examples of valid units are:
    d for degrees of a circle
    r for radians


OUTPUT DESCRIPTION
You must output the given input value, in the unit specified. It must be followed
by the unit letter. You may round to a whole number, or to a few decimal places.


CHALLENGE INPUT
3.1416rd
90dr


CHALLENGE OUTPUT
180d
1.57r


BONUS
Also support these units:
    c for Celsius
    f for Fahrenheit
    k for Kelvin
If the two units given are incompatible, give an error message as output.
"""
import math

def getting_degree(conversion_string):
	
	#This dictionary contains 
	conversion_dict = {
		"r":
			{
			"d": lambda a: a * 180/math.pi
			},
		"d":
			{
			"r": lambda a: a * math.pi/180
			},
		"k":
			{
			"c": lambda t: t - 273.15,
			"f": lambda t: t * 9/5 - 459.67
			},
		"c":
			{
			"k": lambda t: t + 273.15,
			"f": lambda t: t * 9/5 + 32
			},
		"f":
			{
			"c": lambda t: (t - 32) * 5/9,
			"k": lambda t: (t + 459.67) * 5/9 
			}
	}

	#Everything but the last two characters
	value = float(conversion_string[:-2])
	#Units to convert from and to convert to. Last two chars
	(conversion_from, conversion_to) = conversion_string[-2:] 

	#If we're being asked to conver to the same unit, simply remove the last char
	if conversion_from == conversion_to:
		return conversion_string[:-1]

	else:
		try:
			#Getting the conversion function defined in the dict and returning the result
			conversion_func = conversion_dict[conversion_from][conversion_to]
			return (str(conversion_func(value)) + conversion_to)

		#If there's no conversion_function defined, we'll assume it isn't possible
		except KeyError: 
			return "Conversion not possible"



###############################################################################
#########################    TESTING    #######################################
###############################################################################

testCases = ["212fc", "70cf", "100cr", "315.15kc"]

for line in testCases:
	print(getting_degree(line))
