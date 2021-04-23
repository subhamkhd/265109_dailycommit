n = int(input())

for x in range(1, n):
    if x % 2 != 0:
        if x % 3 == 0 and x % 5 == 0:
            print("SoloLearn")
            continue
        elif x % 3 == 0:
            print("Solo")
            continue
        elif x % 5 == 0:
            print("Learn")
            continue
        else:
            print(x)