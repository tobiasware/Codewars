# 2 : interesting number
# 1 : interesting number within next two miles
# 0 : not interesting


def zero(num):
	for x in str(num)[1:]:
		if x != "0":
			return False
	return True

def same(num):
	return len(str(num)) == str(num).count(str(num)[0])


def seq_inc(num):
	l = list("1234567890")
	index = l.index(str(num)[0])

	for x in range(len(str(num))):
		if index+x > 9:
			return False
		if str(num)[x] != l[index+x]:
			return False
	return True

def seq_dec(num):
	l = list("9876543210")
	index = l.index(str(num)[0])

	for x in range(len(str(num))):
		if index+x > 9:
			return False
		if str(num)[x] != l[index+x]:
			return False
	return True


def palindrom(num):
	for x in range(len(str(num))):
		if str(num)[x] != str(num)[len(str(num))-(x+1)]:
			return False
	return True


def awesome_phrase(num, array):
	return True if num in array else False
 

def is_interesting(num, phrase):
	interesting = 2

	if num < 98:
		return 0

	if num < 100:
		interesting = 1

	for x in range(num, num+3):
		if zero(num) or same(num) or seq_inc(num) or seq_dec(num) or palindrom(num) or awesome_phrase(n, phrase):
			return interesting

print(is_interesting(1000, []))