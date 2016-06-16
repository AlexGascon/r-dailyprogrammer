"""
DESCRIPTION
Critical hits work a bit differently in this RPG. If you roll the maximum value on a die, you get to roll the die again and add both dice rolls to get your final score. Critical hits can stack indefinitely -- a second max value means you get a third roll, and so on. With enough luck, any number of points is possible.

INPUT
    d -- The number of sides on your die.
    h -- The amount of health left on the enemy.

OUTPUT
The probability of you getting h or more points with your die.
"""

def isdead(d, h):
	total_cases = 1

	#Each iteration of the loop represents that a critical hit has been dealt
	#We have to substract the damage to the total HP and increment the possible
	#cases. As each hit represents a dice roll, the amount of cases grows exponentially
	while d < h:
		total_cases *= d
		h -= d


	# d - h = rolls higher than h
	# + 1 = roll exactly h (lefs with hp = 0 --> kills)
	favorable_cases = d - h + 1
	total_cases *= d

	#We need to cast one of the terms to float in order to avoid getting an
	#integer division
	return favorable_cases/float(total_cases)

