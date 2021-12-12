a=int(input())
base=int(input())
newn=''
while a>0:
    newn=str(a%base)+newn
    a//=base
print(newn)



