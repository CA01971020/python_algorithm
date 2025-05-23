numbers = [10, 20, 30, 40, 50]
i = 0
for a in numbers :
    if i == len(numbers)-1:
        print(a , end=" ")
    else :
        print(a , end=",")
    i += 1

print()
print("----------")

# join()を使った方法
numbers = [10, 20, 30, 40, 50]
# map(str, numbers) でリストの各要素を文字列に変換。
# ",".join(...) で要素間にカンマを入れて結合。
print(",".join(map(str, numbers)))