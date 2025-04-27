r = 5
c = 7
i = 0

while i < r:
    if i % 2 == 0:
        for _ in range(c):
            print("S" , end="")
    print()
    i += 1

# whileの例
# r = 5
# c = 7
# i = 0

# while i < r:
#     if i % 2 == 0:
#         for _ in range(c):
#             print("■", end="")
#     print()  # ここは必ず実行する
#     i += 1



# forの例
# r = 5
# c = 7

# for i in range(r):
#     if i % 2 == 0:
#         for _ in range(c):
#             print("■", end="")
#     print()  # 毎回必ず改行


# 違う
# r = 5
# c = 7
# i = 0
# t = 0

# while i <= r - 1:
#     if i % 2 == 0:
#         for t in range(c):
#             print("S" , end="")
#     else:
#         print("")
#     i += 1