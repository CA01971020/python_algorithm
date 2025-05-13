# 最大値
n:int = 20
# 対象倍数
bai:int = 4

for i in range(1, n + 1):
    if i % bai == 0:
        print(i)