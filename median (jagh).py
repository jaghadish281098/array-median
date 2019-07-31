n=int(raw_input())
x=[]
for i in range(n):
    a=int(raw_input())
    x.append(a)
print x
x.sort()
print x
if len(x)%2==0:
    print (x[(len(x)/2)]+x[(len(x)/2)-1])/2.0
else:
    print x[int(len(x)/2)]




 
