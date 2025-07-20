sequence = list(map(int, "1 1 0 1 1 1 0 0 1".split()))

count = 0
max_count = 0

for i in sequence:
    if i == 1:
        count += 1
        if count > max_count :
            max_count = count
    else:
        count = 0

print(max_count)