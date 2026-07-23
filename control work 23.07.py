# nun1:
# max=0
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# nums=[a,b,c,d]
# for i in nums:
#     if max<i:
#         max=i
# print(max)
# num2
# a=int(input())
# b=int(input())
# if a>b:
#     a,b=b,a
# for i in range(b,a-1,-1):
#     print(i)
# num3

# size = int(input())
# peremen = 5
# square = []
# for i in range(size):
#     row = []
#     for j in range(size):
#         row.append(peremen)
#         peremen += 1
#     square.append(row)
# for row in square:
#     print(row)

# num4
# a=str(input())
# if a.isalpha() and a.isupper():
#     print('yes')
# else:
#     print('no')
# # num5
# list=[]
# for i in range(0,24,3):
#     list.append(i)
# print(list)
# num6
# from random import randint
#
# a = int(input())
# b = int(input())
# n = int(input())
# ls = [[], []]
# min=0
# max=0
# for i in range(n):
#     ls[0].append(randint(a, b))
#     ls[1].append(randint(a, b))
# print(ls)
# sum = sum(ls[0]) + sum(ls[1])
# count = len(ls[0]) + len(ls[1])
# sredarif = sum / count
# print(sredarif)
# # num7
# list=ls[0]+ls[1]
# min=list[0]
# max=list[0]
# for i in list:
#     if i<min:
#         min=i
#     if i>max:
#         max=i
# print(min)
# print(max)
# num8
# def num(nums, a):
#     for i in nums:
#         if i == a:
#             return "число найдено"
#     return "число не найдено"
#
# nums = [4, 4, 5, 32, 4]
# a = 4
# print(num(nums, a))
# num9
# def nechet(nums):
#     n=[]
#     for i in nums:
#         if i%2!=0:
#             n.append(i)
#     return n
# nums=[8,3,56,7,4]
# print(nechet(nums))
# num10
# list=[[3,4,23,3],[3,4,2,3],[3,4,1,3]]
# n=int(input())
#
# def elem (list,n):
#     a=[]
#     for i in range(len(list)):
#         a.append(list[i][n-1])
#     return a
# print(elem(list,n))
# num12
# students=[]
# def add_students():
#     name=input('имя: ')
#     school_class=input('класс: ')
#     students.append({
#         'имя': name,
#         'класс':school_class,
#         'оценки': []
#     })
#
# def add_grades():
#     name=input('имя студента ')
#     for i in students:
#         if students['name']==name:
#             grade=int(input('оценка: '))
#             students['grades'].append(grade)