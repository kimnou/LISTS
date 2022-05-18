###For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
###you should return [10, -65].

a=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
i=0
p_count=0
n_sum=0
while i<len(a):
    if a[i]>=1:
        p_count+=1
    else:
        n_sum=n_sum+a[i]
    i+=1
print(p_count,n_sum)