initial:int = [68, 55, 72, 93, 87]
tmp:int = 0

# initialの(要素数-1)回処理を実行
for i in range(len(initial) - 1):
    # 初回の計算処理
    if i == 0 :
        tmp = initial[0] + initial[i + 1]
        print(tmp)
    # 2回目移行の計算処理
    else :
        tmp = tmp + initial[i + 1]
        print(tmp)

print("----------")
# 改善コード例

initial = [68, 55, 72, 93, 87]
tmp = 0

for num in initial:
    tmp += num
    # 累積値を表示
    print(tmp)


print("----------")
# Python記法

print(sum(initial))