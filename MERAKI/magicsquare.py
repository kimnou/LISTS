# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# print (type(magic_square))
# print (type(magic_square[0]))
# print (type(magic_square[1]))
# print (sum(magic_square[0]))
# print (sum(magic_square[1]))
# print (sum(magic_square[2]))

magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
while i<len(magic_square):
    row=0
    j=0
    row=0
    column=0
    diagonal=0
    while j<len(magic_square[i]):
        row=row+magic_square[i][j]
        column=column+magic_square[j][i]
        diagonal=diagonal+magic_square[j][j]
        j=j+1
    i=i+1
print(row,"=sum of row")
print(column,"=sum of column")
print(diagonal,"=sum of diagonal")
if row==column==diagonal:
    print("magic square")
else:
    print("not magic square")

# =======================

# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# i=0
# r1=0
# r2=0
# r3=0
# while i<len(magic_square):
#     r1=r1+magic_square[i][0]
#     r2=r2+magic_square[i][1]
#     r3=r3+magic_square[i][2]
#     j=0
#     c1=0
#     c2=0
#     c3=0
#     while j<len(magic_square[i]):
#         c1=c1+magic_square[j][0]
#         c2=c2+magic_square[j][1]
#         c3=c3+magic_square[j][2]
#         j+=1
#     i=i+1
# if r1==r2==r3 and c1==c2==c3:
#     print("magic_square")
# else:
#     print("not a magic_square")

