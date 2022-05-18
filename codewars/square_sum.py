numbers=[1,2,2]
i=0
square=0
a=[]
while i<len(numbers):
    square=numbers[i]*numbers[i]
    a.append(square)
    j=0
    sum=0
    while j<len(a):
        sum=sum+a[j]
        j+=1
    i+=1
print(sum)