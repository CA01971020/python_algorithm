def initial_avg (initial:int):
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

    avg = tmp / len(initial)

    print(avg)

initial_avg([68, 55, 72, 93, 87])

print("----------")
# 改善コード

def initial_avg(initial: list[int]):
    total = sum(initial)
    avg = total / len(initial)
    print(avg)

initial_avg([68, 55, 72, 93, 87])
