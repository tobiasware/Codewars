# 2 : interesting number
# 1 : interesting number within next two miles
# 0 : not interesting


def zero(num):
	for x in str(num)[1:]:
		if x != "0":
			return False
	return True



		


def is_interesting(num):
	# interesting = 2
	# if x < 98:
	# 	return 0
	interestingNumber = False

	interestingNumber = zero(num)


print(zero(100))
	
	