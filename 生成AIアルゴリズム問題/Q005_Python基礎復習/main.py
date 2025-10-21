# 初級問題：偶数カウント

nums = [1 , 2 ,3 , 4 , 5 , 6]
count = 0

for i in nums :
    if i % 2 == 0 :
        count += 1
print(count)

# Pythonic
# def count_even(nums):
#     return sum(1 for n in nums if n % 2 == 0)

# nums = [1, 2, 3, 4, 5, 6]
# print(count_even(nums))

print("----------")

# 中級：文字列反転

a = "python"

def reverse_string(text):
    return text[::-1]

print(reverse_string(a))
