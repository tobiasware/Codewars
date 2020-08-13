def iq_test(numbers):
	l = [int(x) % 2 for x in numbers.split(" ")]

	if l.count(0) > 1:
		return l.index(0)+1
	else:
		return l.index(1)+1





iq_test("2 4 7 8 10") #3
iq_test("1 2 2") #1
print("test")