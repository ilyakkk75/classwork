# def minimum(a):
#     minimum=a[0]
#     for i in a:
#         if i<minimum:
#             minimum=i
#     return (minimum)
#
# a=[3,5,2,1]
# print(minimum(a))


# a=int(input())
# b=int(input())
# if a > b:a,b=b,a
#
# list=[4,2]
# if list[0]>list[1]:
#     list[0],list[1]=list[1],list[0]
# print(list)

# BUBBLESORT
# list=[2,1,4,5,879,98,0,943,4,23,34,222222,22222222,79,3]
# counter=0
# for j in range(len(list)-1):
#     flag=False
#     for i in range(len(list)-1-j):
#         counter+=1
#         if list[i]>list[i+1]:
#             flag=True
#             list[i],list[i+1]=list[i+1],list[i]
#     if not flag:
#         break
# print(list)
# print(counter)
# СОРТИРОВКАВСТАВКА;

# sum=0
# def show_sum():
#     global sum
#     a=int(input())
#     sum += a
#     if a==0:
#         return sum
#     else:
#         return show_sum()
# print(show_sum())
# show_sum()
