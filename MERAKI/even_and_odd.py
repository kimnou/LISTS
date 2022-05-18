elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_count=0
even_sum=0
odd_sum=0
even_avg=0
odd_avg=0
while i<len(elements):
    if elements[i]%2==0:
        even_sum=even_sum+elements[i]
        even_count+=1
        even_avg=even_sum//even_count
    else:
        odd_sum=odd_sum+elements[i]
        odd_count+=1
        odd_avg=odd_sum//odd_count
    i+=1
print("even average:",even_avg)
print("odd average:",odd_avg)
print("total average:",sum(elements)//len(elements))
print("even sum:",even_sum)
print("odd sum:",odd_sum)
print("total sum:",sum(elements))
print("even count:",even_count)
print("odd count:",odd_count)
print("total count:",len(elements))
