x = input()

for i in range(3, len(x)):
    l = i - 3
    if len(set(x[l:i+1])) == 4:
        print(i+1)
        break

for i in range(13, len(x)):
    l = i - 13
    if len(set(x[l:i+1])) == 14:
        print(i+1)
        break
