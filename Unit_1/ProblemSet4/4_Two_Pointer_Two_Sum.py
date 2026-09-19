'''
Use the two pointer approach to implement a function two_sum() 
that takes in a sorted list of integers nums and an integer target as parameters and 
returns the indices of the two numbers that add up to target. 
You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the indices in any order.

def two_sum(nums, target):
    pass
Example Usage

nums = [2, 7, 11, 15]
target = 9
two_sum(nums, target)

nums = [2, 7, 11, 15]
target = 18
two_sum(nums, target)
Example Output:

[0, 1]
[1, 2]
'''

def two_sum(nums, target):
    n = len(nums)
    i, j = 0, n-1
    while(i<j):
        sum = nums[i] + nums[j]
        if sum==target:
            return [i,j]
        elif sum>target:
            j-=1
        else:
            i+=1
    return [-1,-1]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))