
def increment_number(nums):
    size = len(nums)
    if size == 0:
        return []
    carry = 1
    for i in range(size-1, -1, -1):
        temp = nums[i] + carry
        nums[i] = temp%10
        carry = temp//10
    if carry == 0:
        return nums
    return [1] + nums

result = increment_number([9,9,9,9,9])
print(result)
