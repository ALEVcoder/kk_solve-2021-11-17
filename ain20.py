# Kichik kalkulyator

a = int(input('birinchi son'))
amal = input('Amalni kiriting')
b = int(input('ikkinchi son'))

if amal == '+':
    print(a+b)
elif amal == '-':
    print(a-b)
elif amal == '*':
    print(a*b)
elif amal == '/':
    if b > 0:
        print(a/b)
    else:
        print('Nolga bo`lish mumkin emas')