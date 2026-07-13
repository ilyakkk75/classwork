import random
# a='мяу замай реп йоу'
# ls=a.split(' ')
# words=0
# for i in range(len(ls)):
#     words+=1
# print(words)   многозатратный способ

# st=input()
# print(st.count(' ')+1) доступный способ

# ls=[]
# ls.append(5)
# ls.append(12)
# print(ls)

# ls=[]
# mls=int(input())
# for i in range(mls):
#     ls.append(random.randint(1,100))
# print(ls)


# list=[2,2,3,1,23]
# a=2
# def rem(list,a):
#     for i in list:
#         if i==a:
#             list.remove(a)
# rem(list, a)
# print(list)
#
# def remove_all(list,a):
#     i=0
#     size=len(list)
#     while i < size:
#         if list[i]==a:
#             list.remove(a)
#             size-=1
#             i-=1
#         i+=1list=[2,2,3,1,23]
# list=[2,2,3,1,23]
# a=2
# remove_all(list,a)
# print(list)



# воможность добавлять и удалять студентов
# students=[]
# students_marks=[]
# students_marks.append([])
#
#
# while True:
#     var=int(input('1,2,3'))
#     if var==1:
#         name=input()
#         students.append(name)
#         students_marks.append([])
#     elif var==2:
#         index=int()
#         if 1<=index<=len(students):
#             students.pop(index-1)
#         else:
#             print('такого студента нет')
#     elif var==3:
#        for i in range (len(students)):
#            print(f'{i+1},{students[i]}:{students_marks[i]}')
#     elif var==4:
#         index=int(input('введите номер студента'))
#         if index<1 or index>len(students):
#             print('некорректно')
#         else:
#             index_marks=int(input('какую оценку поменять'))
#             if len(students_marks[index-1])<index_marks:
#                 print('такой нет')
#             else:
#                 marks = int(input())
#                 students_marks[index-1][index_marks]=marks
#
#
#     else:
#         break
