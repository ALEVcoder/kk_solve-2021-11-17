# Ush xonali sonni raqamlarini bir xil yoki bir emasligini topuvchi dastur

n = int(input())
a = n//100
b = (n%100)//10
c = n%10

if a==b and b==c and a==c:
    print('Yes')
else:
    print("No")

