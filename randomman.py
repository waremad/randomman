import random

def correlation(X,Y):
    xb = sum(X)/len(X)
    yb = sum(Y)/len(Y)

    subx = []
    for i in X:
        subx.append((i-xb)**2)
    suby = []
    for i in Y:
        suby.append((i-yb)**2)
    
    subxy = []
    for i in range(len(X)):
        subxy.append((X[i]-xb)*(Y[i]-yb))
    
    sxy = sum(subxy)/len(X)
    sx = sum(subx)/len(X)
    sy = sum(suby)/len(Y)

    if sxy==0 or sx==0 or sy==0:
        return 1

    return sxy/( (sx*sy)**0.5 )

def manpar(XY):
    n = 10

    xym = []
    for i in range(len(XY)-1):
        xym.append(XY[1:][i] - XY[:-1][i])

    num = [0]
    for i in range(n - 1):
        num.append(i+1)
        num.append(-i-1)
    num = sorted(num)
    #print(num)
    ddnum = {}
    for i in num:
        ddnum[i] = 0
    #print(ddnum)

    for i in xym:
        ddnum[i] += 1

    avedd = sum(ddnum.values())/n

    print(list(ddnum.values()))

    for i in range(n):
        ddnum[i] = avedd*2 - ddnum[i]

    ddkey = ddnum.keys()
    ddval = ddnum.values()

    print(list(ddnum.values()))

    c = correlation(list(ddkey),list(ddval))
    print(c)
    return (c)*1000 //1 /10

ls = []
"""
for i in range(1000):
    ls.append(random.randint(0,9))
print(ls)
"""

#"""
with open("in.txt") as f:
    s= f.read()
    print(type(s))
    print(s)
    ls = list(str(s))
    print(ls)
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    print(ls)
#"""

out =  manpar(ls)
print(out)