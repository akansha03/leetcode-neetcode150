'''
8️⃣ Search insert position. int [] numbers = {1,3,5,6};
int target = 5;
int target2 = 2;
int target3 = 7;

Output: 2, 1, 4
'''

def search_insert_position(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if nums[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return left
print(search_insert_position([1,3,5,6], 5))
print(search_insert_position([1,3,5,6], 2))
print(search_insert_position([1,3,5,6], 7))
