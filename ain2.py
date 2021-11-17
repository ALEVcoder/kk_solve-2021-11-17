import random 
T = 1000000
s= 0
for t in range(T):
    a = random.randint(1,100)
    b = random.randint(1,100)
    if (a*b) % 2 == 0:
        s+=1
print('%.2f' % (s/T))

# Result = 0.75