# базовые алгоритмы (блоксхемы и тд)

# int float bool str
# list tuple set dict
# условные конструкции
# логические и арифметические опреации
# циклы
# блочные конструкции
# типы данных
# область видимости переменной и приведение типов
# функции обьявление,вызов,как предаются данные,как пихать параметры,как указать переменные
# все структуры данных лист кортеж сет дикшенори словари и тд
# методы структур
# алгоритмы сортировок (пузырек вставками)
# решение задач с помощью стурктур данных
# работа со строками

# def calc_summ(a,b,c):
#     print(a+b+c)

# calc_summ(1,2,3)
# '''vse rabotaet'''
# no esli budet 2 znach, ono ne zarabotaet
# znachenia chto bili pozhe perezatiraut iznach


# vozvrash znach
# def calc_summ(a,b,c):
#     return(a+b+c)
#
# print(calc_summ(1,2,3))

# def even_odd(a):
#     if a%2==0:
#         return 'odd'
#     else:
#         return 'even'
#
# print(even_odd(7))
# budet even

# def fact(n):
#     if n>1:
#         return n*fact(n-1)
#     else:
#         return 1
#
# print(fact(3))
#
# ls=[2, 2, 4, 4, 4, 5, 5, 6]
# print(ls)
# n=6
# min_i=0
# max_i=len(ls)-1
# def binary_search(ls,n,min_i=0,max_i=-1):
#     if max_i==-2:max_i=len(ls)-1
#     if min_i>max_i: return False
#     current_i=(max_i+min_i)//2
#     if n==ls[current_i]: return True
#     elif n<ls[current_i]: return binary_search(ls,n,current_i-1)
#     else: return binary_search (ls,n,current_i+1,max_i)


# strukturi dannih


# def words_ret(st):
#     ls = st.split(' ')
#     a=[]
#     for i in ls:
#         if len(i)<3:
#             a.add(i)
#     return a
#
# st= 'я люблю rr кк'
# print(words_ret(st))

# ls1='yoyo antihype ye'
# ls2='yoyo vagabund ye'
# def same_words(ls1,ls2):
#     ll=ls1.split(' ')
#     lm=ls2.split(' ')
#     words=set()
#     for i in ll:
#         for j in lm:
#             if i==j:
#                 words.add(i)
#     return words
# print(same_words(ls1,ls2))


# ll=ls1.split(' ')
# lm=ls2.split(' ')
# print(set(ll).intersection(set(lm)))


# ls1='   yoyo antihype    ye   '
# def words(ls1):
#     ls=ls1.split(' ')
#     word=0
#     for i in ls:
#         if len(i)!=0:
#             word+=1
#     return word
# print(words(ls1))

