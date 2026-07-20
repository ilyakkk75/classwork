# # import random
# #
# # def crs(size):
# #     ls=[]
# #     while size>0:
# #         num=random.randint(1,9)
# #         if num not in ls:
# #             ls.append(num)
# #             size-=1
# #     return ls
# # a=int(input())
# # n1 =set(crs(a))
# # print(n1)
# # b=int(input())
# # n2=set(crs(b))
# # print(n2)
# # print(len(n1.intersection(n2)))
# # print((len(n1)+len(n2)-len(n1.intersection(n2))*2)>len(n1.intersection(n2)) and 'уникальных больше' or 'общих больше')
# import random
#
# # product={
# #     'name': 'мышка',
# #     'price':1200.50,
# #     'count':120,
# #     'colors':['красный','синий']
# # }
# # product['category']='акссесуары'
# # # mozhno dobavlyat i izmenyat keys
# # for i in product.keys():
# #     print(f'{i} - {product[i]}')
#
# disciplines={'eng','math','rus','lit'}
# def show_dict(product):
#     for i in product.keys():
#         print(f'{i} - {product[i]}')
# def marks():
#     st1={}
#     for i in disciplines:
#         st1[i] = []
#         for j in range(random.randint(3,9)):
#             st1[i].append(random.randint(2,5))
#     return st1
#
# st1=marks()
# show_dict(st1)
# def avg(list):
#     sum=0
#     for i in list:
#         sum+=i
#     return sum/len(list)
# def sred (st):
#     max=0
#     disc_name='unnamed'
#     for i in st.keys():
#         avg_mark=avg(st[i])
#         if max<avg_mark:
#             max=avg_mark
#             disc_name=i
#     return disc_name
#
# st1=avg()
#
# def more_then_3(dict):
#     dict_name=[]
#     for i in dict.keys:
#         mark=avg(avg(dict[i]))
#         if mark>=3:
#             dict_name+=i
#     return dict_name
#
#
#