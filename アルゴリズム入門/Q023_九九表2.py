# 計算回数（列）
n = 9
# 対象数字（行）
i = 0

# 作成したコード
for i in range(1 , n + 1):
    # スペース
    s = ""
    for j in range(1 , n + 1):
        a = j * i
        if a <= 9:
            print(s , a , end=" ")
        else:
            print(a , end=" ")
    print()

print("-----code1-----")

# f-string で出力を2桁に揃える方法
for i in range(1, 10):
    for j in range(1, 10):
        # :2 は「2文字分で右詰め表示」という意味。
        print(f"{i * j:2}", end=" ")
    print()

print("-----code2-----")
# str.rjust()を使った方法
for i in range(1, 10):
    for j in range(1, 10):
        print(str(i * j).rjust(2), end=" ")
    print()

print("-----code3-----")
# リスト内包表記＋joinで簡潔にする
for i in range(1, 10):
    print(" ".join(f"{i * j:2}" for j in range(1, 10)))

print("-----code4-----")
# 改善案
n = 9

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a = i * j
        if a < 10:
            print(" ", a, end=" ")
        else:
            print(a, end=" ")
    print()