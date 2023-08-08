# row = 4
# col = 7
# k = 1
# for i in range(row):
#     if i % 2 == 1:
#         k += row
#         for j in range(col):
#             print(k,end = ' ')
#             k -= 1
#         k += row + 2
        
#     else:
#         for j in range(col):
#             print(k, end=' ')
#             k += 1
#     print()
row = 5
col = 6
for i in range(1,row+1):
    k = i
    for j in range(col):
        print(k, end=' ')
        k += row
    print()
ls = []
count = 1
# for i in range(row):
#     temp = []
#     if  i % 2 == 0:
#         for j in range(col):
#             temp.append(count)
#             count += 1
#     else:
#         for j in range(col):
#             temp.insert(0, count)
#             count += 1
#     ls.append(temp)

# print(*ls, sep="\n")