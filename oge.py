c=0
while True:
    a=int(input())
    if a>=10 and a <100 and a%8==0:
        c+=a
    if a==0:
        break
print(c)