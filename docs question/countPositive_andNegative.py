list=[2,-7,5,-64,-14]
positive=0
negative=0
i=0
while i<len(list):
    if list[i]>0:
        positive+=1
    else:
        negative+=1
    i+=1
print("positive_count:",positive)
print("negative_count:",negative)
