def sum_pairs(ints, s):
	for x in ints:
		if s-x in ints:
			y = ints.index(element = s-x, start= 1)
			return [x, ints[y]]


def sum_pairs2(ints, s):
	k = 999999999
	l = []
	for x in range(len(ints)):
		if s - ints[x] in ints[x+1:]:# and s -ints[x] != 0:
			y = ints.index(s - ints[x], x+1)
			l.append([x, y])
			if y < k:
				k = y
				print("k:", k, "    ", ints[k])
			if x >= k:
				break
	print(l)
	if not l:
		return None

	minimum = l[0][1]
	temp = l[0]
	for x in l[1:]:
		if x[1] < minimum:
			temp = x

	return [ints[temp[0]], ints[temp[1]]]



# print(sum_pairs2([1, 2, 3, 4, 5, 6,5 ,5, 1 ,9, 0, 10], 10))


# l5= [10, 5, 2, 3, 7, 5, 0, 1,9, 12, -2, 6,4]
# print(sum_pairs2(l5, 10))

def sum_pairs3(ints, s):
	l = {ints[0]}
	for x in ints[1:]:
		tmp = s - x
		if (tmp != s or tmp == 0) and tmp in l:
			return [tmp, x]
		l.add(x)
	return None



l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs3(l1, 8))
print(sum_pairs3(l7, 0))

l1 = [0]
print(l1)