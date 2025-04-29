# 自分のコード

# r = 6
# c = 10
# i = 0

# for _ in range(r):
#     if i % 2 == 0 :
#         for _ in range(10):
#             if i % 2 == 0 :
#                 print("a",end="")
#             else :
#                 print("b",end="")
#             i += 1
#         print()
#         i += 1
#     else :
#         for _ in range(10):
#             if i % 2 == 0 :
#                 print("a",end="")
#             else :
#                 print("b",end="")
#             i += 1
#         print()
#         i += 1

print("----------")
# よりシンプルなコード

rows = 6
cols = 10

for i in range(rows):
    x = i % 2
    for j in range(cols):
        if j % 2 == x:
            print("a", end="")
        else:
            print("b", end="")
    print()
