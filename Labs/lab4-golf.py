e=lambda L:[n%2 for n in L].count(0)
l=lambda x:"[%s]"%(",".join(map(str,x)))
s=lambda o,t:len(o)==len(t)and all(x==y for x,y in zip(o, t))

print(repr(l([1, 2, 3, 4])))
