
def merge_two_arrays(array_1, array_2):

    for num in array_2:
        array_1.append(num)
    return array_1

num_1 = [5,3,2]
num_2 = [9,0,1]
result = merge_two_arrays(num_1, num_2)
print(result)
