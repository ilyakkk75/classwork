import random
win_pc = 0
win_pl = 0
while True:
    a=int(input('ваш ход: '))  
    if a==1:
       print('камень')
    elif a==2:
       print('ножницы')
    elif a==3:
       print('бумага')
    else:
        print('некорректное значение')
        break
    num=random.randint(1,3)
    if num==1:
        print('камень')
    elif num==2:
        print('ножницы')
    else:
        print('бумага')
    if a==num:
        print('ничья')
    elif a>num:
        win_pl+=1
        print(f'вы выиграли {win_pl}:{win_pc}')
    else:
        win_pc+=1
        print(f'вы проиграли {win_pc}:{win_pl}')
    if win_pc==3 or win_pl==3:
        break
if win_pc==3:
    print(f'компьютер победил со счетом {win_pc}:{win_pl}')
else:
    print(f'пользователь победил со счетом {win_pl}:{win_pc}')




