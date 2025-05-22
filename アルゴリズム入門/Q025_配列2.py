numbers = [10, 20, 30, 40, 50]
a =len(numbers)

for i in numbers :
    a -= 1
    b = numbers[a]
    print(b)

print("-----------")
# reversed()を使う方法

numbers = [10, 20, 30, 40, 50]

for num in reversed(numbers):
    print(num)

print("-----------")
# インデックスを逆順で使う

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
