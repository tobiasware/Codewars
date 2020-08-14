def sum_pairs(ints, s):
	for x in ints:
		if s-x in ints:
			y = ints.index(element = s-x, start= 1)
			return [x, ints[y]]


def sum_pairs2(ints, s):
	l = []
	for x in range(len(ints)):
		if s - ints[x] in ints:
			y = ints.index(s - ints[x], x)
			return [ints[x], ints[y]]
	return None


print(sum_pairs2([1, 2, 3, 4, 5, 6], 10))


l5= [10, 5, 2, 3, 7, 5]
print(sum_pairs2(l5, 10))