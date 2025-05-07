n = 8

for i in range(n):
    for j in range(n):
        if j == (n - i - 1) :
            print("a", end="")
        else :
            print(" ", end="")
    print()

# その他の方法
print("----------")
#文字列連結で1行ずつ作って出力
print("other 1")

for i in range(n):
    line = " " * (n - i - 1) + "a"
    print(line)

print("----------")
#リストを使って行を作成
print("other 2")

for i in range(n):
    row = [' '] * n
    row[n - i - 1] = 'a'
    print(''.join(row))

print("----------")
#文字列フォーマット
print("other 3")

for i in range(n):
    print(f"{' ' * (n - i - 1)}a")