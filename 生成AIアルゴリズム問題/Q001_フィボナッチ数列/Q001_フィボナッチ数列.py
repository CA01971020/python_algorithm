# フィボナッチ関数
def fibonacci(n: int) -> int:

    fn1:int = 0
    fn2:int = 1

    if n == 0 :
        return 0
    elif n == 1:
        return 1

    for _ in range(2 , n + 1):
        fn1,fn2 = fn2, fn1 + fn2
        i += 1

    return fn2

print(fibonacci(10))

# def fibonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     a, b = 0, 1
    # 2からn+1まで生成
#     for _ in range(2, n + 1):
#         a, b = b, a + b

#     return b

# print(fibonacci(10))
