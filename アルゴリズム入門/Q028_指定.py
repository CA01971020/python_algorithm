n = [40 , 10 , 30 , 50 , 20 , 39]
min:int = 20
max:int = 39

for tmp in n:
    if tmp > max:
        continue
    elif tmp >= min:
        print(tmp)

print("----------")
#例

for tmp in n:
    if min <= tmp <= max:
        print(tmp)