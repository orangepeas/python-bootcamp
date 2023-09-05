def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum
print(count([0,0,0,3],3))