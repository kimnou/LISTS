from xxlimited import Str


list=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
a=[]
while i<len(list):
    if type(list[i])==int:
        a.append(list[i])
    i+=1
print(a)
