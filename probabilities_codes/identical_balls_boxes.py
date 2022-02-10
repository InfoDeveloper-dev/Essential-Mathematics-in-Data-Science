"""
In how many different ways one can arrange 6 identical balls in 3 identical boxes
"""

one_way = "[6][0][0]"
second_way = "[5][1][1]"
third_way = "[4][0][2]"
fourth_way = "[3][2][1]"
fifth_way = "[4][1][1]"
sixth_way = "[1][2][3]"
seventh_way = "[2][2][2]"

total_ways = len([
	one_way, second_way, third_way, fourth_way, fifth_way, sixth_way, seventh_way]
	)
print("Total number of ways are....{}".format(total_ways))