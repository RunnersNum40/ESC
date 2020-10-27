l=lambda o,t:len(o)>=len(t)and all(x==y for x,y in zip(o,t))
n=lambda o,t:any(l(o[i:],t)for i in range(len(o)))
r=lambda o:len(o)>1 and(o[0]==o[1]or r(o[1:]))
d=lambda o:print(len(o), "x", len(o[0]))
mul=lambda o,t:[[sum(n*i for n,i in zip(o[x],[b[y] for b in t]))for x in range(len(o))]for y in range(len(o))]