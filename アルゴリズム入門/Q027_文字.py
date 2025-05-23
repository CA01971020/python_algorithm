s = ["abc" , "abcd" ,"abcde" , "xx" , "yyy"]
n = 0
nl = 3
for i in s :
    a = len(s[n])
    if a <= nl :
        print(s[n])
    n += 1

print("----------")
# 修正例

s = ["abc", "abcd", "abcde", "xx", "yyy"]
n = 3

for item in s:
    if len(item) <= n:
        print(item)
