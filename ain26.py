# pythonda 1000gacha bo'lgan tub sonlarni chiqaruvchi dastur

min = 1
max = 100

print( min, "dan", max, "gacha tub sonlar:")

for j in range(min, max + 1):
   # all prime numbers are greater than 1
   if j > 1:
       for i in range(2, j):
           if (j % i) == 0:
               break
       else:
           print(j)