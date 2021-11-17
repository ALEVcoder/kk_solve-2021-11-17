# a va b sonlar berilgan. Agar a < b bo`lsa a dan b gacha bo`lgan sonlarni o`shish tartibida aks holdakamayish tartibida chiqaring

a = int(input())
b = int(input())

if a < b:
    for i in range(a,b, 1):
        print(i , end='\n')

else:
    for i in range(a,b, -1):
        print(i , end='\n')