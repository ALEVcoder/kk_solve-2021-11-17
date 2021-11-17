# S=1*5+2*6+3*7+...+n*(n+4) ifodani hisoblash dasturini pradsedura yordamida tuzing
n = int(input())

s = 0
for i in range(1, n + 1):
    s = s + i * (i + 4)

print('Yigindi :',s)

