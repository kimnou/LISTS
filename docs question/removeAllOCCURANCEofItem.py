# a=[1,2,3,4,5,1,2]
a=[5,6,7,8,9,10]
i=0
while i<len(a):
    # if a[i]==1:
    if a[i]==7:
        a.remove(a[i])
    i+=1
print(a)