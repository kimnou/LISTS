### find the second largest number in the given list.

# numbers=[50,40,23,70,56,12,5,10,7]
# maximum=max(numbers)
# numbers.remove(maximum)
# maximum=max(numbers)
# print(maximum)

# numbers=[50,40,23,70,56,12,5,10,7]
# numbers.sort()
# print(numbers[-2])

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# while i<len(numbers):
#     numbers.sort()
#     i+=1
# print(numbers[-2])


numbers = [50, 40, 23, 70, 57, 56, 12, 5, 10, 7]
i=0
while i<len(numbers):
    j=0
    while j<len(numbers):
        if numbers[i]<numbers[j]:
            b=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=b
        j+=1
    i+=1
print(b)
