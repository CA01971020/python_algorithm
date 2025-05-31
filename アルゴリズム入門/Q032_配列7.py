def initial_sum(initial: list[int]):
    max_value = 100
    min_value = 80
    list = []

    for tmp in initial:
        if min_value <= tmp <= max_value:
            list.append(tmp)

    a = sum(list)
    print(a)

initial_sum([68, 55, 72, 93, 87])
