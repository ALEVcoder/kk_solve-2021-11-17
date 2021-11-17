n = int(input())
a = input().split(" ")

ygindi = int(a[0])+int(a[1])+int(a[2])

if ygindi > n:
    print('Yes')
elif ygindi < n:
    print('No')