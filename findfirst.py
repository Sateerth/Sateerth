def is_disarium(num):
    return num == sum(int(digit) ** (i+1) for i, digit in enumerate(str(num)))


def first_n_disarium(n):
    res, num = []
    while len(res) < n:
        
        num += 1
    return res


def disarium_between(start, end):
    return [num for num in range(start, end+1) if is_disarium(num)]


print("First 5 Disarium numbers:", first_n_disarium(5))
print("Disarium numbers between 1 and 200:", disarium_between(1, 200))
