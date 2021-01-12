def power(x, n):
	if n == 0:
		return 1
	elif n > 0:
		return x*power(x, n-1)
	else:
		return 1/power(x, -n)

def iterLeave(L1, L2):
	return [L1[0], L2[0]] + iterLeave(L1[1:], L2[1:]) if len(L1) > 0 else []

def reverse_rec(L, i=0):
	L[i], L[-1-i] = L[-1-i], L[i]
	if i < len(L)//2+1:
		reverse_rec(L, i+1)

def zigzag(L):
	n = len(L)
	if n == 0:
		print("")
	elif n == 1:
		print(L[0], end = "")
	else:
		print(L[n//2], L[n//2-1], end = " ")
		zigzag(L[:n//2-1]+L[n//2+1:])

def is_balanced(s):
	s = "".join([c for c in s if c in ("(", ")")])
	if len(s) == 0:
		return True
	elif len(s)%2 != 0:
		return False
	else:
		s_new = s.replace("()", "")
		if s == s_new:
			return False
		else:
			return is_balanced(s_new)


# print(power(2, 5))
# print(iterLeave(range(10), range(10, 20)))

L = list(range(10))
print(L)
# reverse_rec(L)
# print(L)

zigzag(L)

print(is_balanced("(()))"))