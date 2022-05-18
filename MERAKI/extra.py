# num=list(range(10))
# print(num)

####list comphrension(using for loop)

# num=[i for i in range(0,10)]
# print(num)


####copy list
# a=[[1,2,3],[4,5]]
# b=list(a)
# a[1][1]=25
# print(a)
# print(b)


##for loops on list
a=['cat','dog','duck','parrot']
print(a)
for i in a:
    print(i)
for i in range(0,len(a)):
    print("index:"+str(i)+" value:"+a[i])