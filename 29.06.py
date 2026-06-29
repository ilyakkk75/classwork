# marks = [2,8,6,-3,-2,5,6]
# # for i in range(len(marks)):
# #     if marks[i]<0:
# #         marks[i]*=-1
# # print(marks)
# marks[0],marks[len(marks)-1]=marks[len(marks)-1],marks[0]
# marks[1],marks[len(marks)-2]=marks[len(marks)-2],marks[1]
# marks[2],marks[len(marks)-3]=marks[len(marks)-3],marks[2]
# print(marks)
a=[[2,3,4],[1,8,6]]
for i in range(len(a)):
    summa=0
    for j in a[i]:
        summa+=j
        print(j,end='\t')
    print('|',summa)
print('----------------')
result=0
for i in range(len(a[0])):
    summa=0
    for j in range(len(a)):
        summa+=a
    print(summa,end='\t')
    result+=summa
print('|',result)















































