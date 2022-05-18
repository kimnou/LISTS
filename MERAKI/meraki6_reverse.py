### write a code that reverse the order of the items in a list.

# places=["delhi","gujarat","rajasthan","punjab","kerela"]
# places.reverse()
# print(places)

# places=["delhi","gujarat","rajasthan","punjab","kerela"]
# i=-1
# while i>=-len(places):
#     print(places[i])
#     i=i-1

places=["delhi","gujarat","rajasthan","punjab","kerela"]
l=len(places)-1
i=l
while i>=0:
    print(places[i])
    i-=1
