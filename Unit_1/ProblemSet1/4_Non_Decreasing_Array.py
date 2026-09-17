'''
Given an array nums with n integers, write a function non_decreasing() that checks if 
nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds 
for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
	pass
Example Usage:

nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)
Example Output:

True
False

[4,5,6,2,6]
[1,1,2,3,2,3]

T: O(n)
S: O(1)

'''

def non_decreasing(nums):
    count = 0
    for i in range(len(nums)-1):
        if(nums[i] > nums[i+1]):
            count+=1
            if count>1:
                return False
            # update whatever number needs change
            if(i==0 or nums[i-1]<nums[i+1]):
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
    return True

nums = [1,1,2,3,2,3,2]
print(non_decreasing(nums))

nums = [4, 2, 4]
print(non_decreasing(nums))