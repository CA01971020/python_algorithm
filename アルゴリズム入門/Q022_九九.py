# 計算回数（列）
n = 9
# 対象数字（行）
i = 0

for i in range(1 , n + 1):
    for j in range(1 , n + 1):
        a = j * i
        print(a , end=" ")
    print()