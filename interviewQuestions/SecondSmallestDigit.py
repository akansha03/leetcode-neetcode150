def smallest_digit(s):
    min_1 = float('inf')
    min_2 = float('inf')
    for c in s:
        if c.isnumeric():
            num = int(c)
            if num<min_1:
                min_2 = min_1
                min_1 = num
            elif min_1<num<min_2:
                min_2 = num
    return min_2

result = smallest_digit("claude2403edualc")
print(result)
