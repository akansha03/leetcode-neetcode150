'''
5️⃣ Rearrange Array:
Given [2, 0, 4, 0, 3, 0, 5, 0], rearrange it so all even numbers come first
and odd numbers last, like [2,0,4,0,0,0,3,5]. [Use two pointer approach]
'''

def rearrange_array(nums):
    size = len(nums)
    if size == 0:
        return []
    left, right = 0, size-1
    while left<=right:
        if nums[left]%2 == 0:
           left += 1
        elif nums[right]%2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

print(rearrange_array([2,1,4,1,3,0,5,0]))
