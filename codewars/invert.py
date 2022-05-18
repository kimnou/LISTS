###invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
###invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
###invert([]) == []

# l=[1,2,3,4,5]
# i=0
# while i<len(l):
#     print("-",l[i],end=" ")
#     i+=1

l=[1,2,3,4,5]
i=0
while i<len(l):
    print(-l[i],end=",")
    i+=1
