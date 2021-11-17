# Foydalanuvchi tomonidan kriitilgan sonar yig`indisini hisoblash dasturi. 
# Agar manfiy son kirtilsa skil uz ishini tuxtatadi

while True:
    n = int(input())

    for i in range(0,n):
        print(i+i)
        if n <= 0:
            print('Dasturing tugadi.')
            break