n = 20

for i in range(1 , n + 1):
    if i % 3 == 0 :
        if i == n :
            print("?" , end="")
        else:
            print("?",end=",")
    elif i == n :
        print(i , end="")
    else :
        print(i , end=",")