s=0
for i in range(1000):
    if (i & (i-1)) == 0:
        s += 1
print(s)

# Result = 11