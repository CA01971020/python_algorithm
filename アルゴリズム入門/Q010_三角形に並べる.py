randc = 8

i = 0
j = 0

for i in range(randc):
    for _ in range(randc) :
        if j <= 0 :
            print("a" , end="")
            j += 1
    i += 1
    print()

print("------")

n = 8  # 繰り返しの数

for i in range(n):  # 行ループ
    for j in range(i + 1):  # 列ループ
        print("a", end="")  # 改行なしで■を出力
    print()  # 行の終わりで改行
