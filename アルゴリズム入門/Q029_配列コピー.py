# コピー元配列の宣言と初期化
a = [10, 20, 30, 40, 50]

# コピー先配列の宣言（0で初期化）
b = [0] * len(a)

# コピー先配列内容の表示（初期状態）
for i in range(len(b)):
    print(b[i])

# 配列データのコピー
for i in range(len(a)):
    b[i] = a[i]

# コピー先配列内容の表示（コピー後）
for i in range(len(b)):
    print(b[i])
