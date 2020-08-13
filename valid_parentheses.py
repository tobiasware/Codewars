def valid_parentheses(string):
	l = []
	for x in string:
		if x == "(":
			l.append("(")
		elif x == ")":
			if len(l) < 1:
				return False
			else:
				l.pop()
	return len(l) == 0


print(valid_parentheses("hi())(")) #F
print(valid_parentheses("hi(hi)()")) #T