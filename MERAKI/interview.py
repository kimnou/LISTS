###print the sum of all the even numbers in a given list.
marks = [4,9,11,12,6,4,3,1]
i=0
sum=0
while i<len(marks):
    if marks[i]%2==0:
        sum=sum+marks[i]
    i+=1
print(sum)
