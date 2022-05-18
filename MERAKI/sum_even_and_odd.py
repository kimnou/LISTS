elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
while i<len(elements):
    if elements[i]%2==0:
        even_sum=even_sum+elements[i]
    else:
        odd_sum=odd_sum+elements[i]
    i+=1
print("sum of even no's:",even_sum)
print("sum of odd no's:",odd_sum)