### write a code that prints the maximum in this list.

# numbers=[50,40,23,70,56,12,5,10,7]
# numbers.sort()
# print("maximum number is:",numbers[-1])

# numbers=[50,40,23,70,56,12,5,10,7]
# maximum=max(numbers)
# print(maximum)

# numbers=[50,40,23,70,56,12,5,10,7]
# print(max(numbers))

# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# while i<len(numbers):
#     i+=1
# print(max(numbers))

a=[50,40,23,70,56,12,5,100,7]
maximum=a[0]
i=0
while i<len(a):
    if a[i]>maximum:
        maximum=a[i]
    i+=1
print(maximum)