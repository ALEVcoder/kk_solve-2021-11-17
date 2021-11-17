# n natural son berilgan. Kvadrat n dan kichik bo`lgan barcha natural sonlarni chiqaruvchi dastur
from math import *
n = int(input())

for i in range(1,n):
    if i < sqrt(n):
        print(i)