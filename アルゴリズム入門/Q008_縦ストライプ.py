r = 5
c = 7
i = 0

for _ in range(r) :
    for _ in range(c):
        if i % 2 == 0 :
            print("A" ,end="")
        else:
            print("b",end="")
        i += 1
    i = 0
    print()
