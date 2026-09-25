'''
You have a list of integers collection_sizes representing the sizes of different art collections in your gallery and are trying to determine how to group them to best fit in your space. Given an integer k write a function count_divisible_collections() that returns the number of non-empty subarrays (contiguous parts of the array) where the sum of the sizes is divisible by k.

def count_divisible_collections(collection_sizes, k):
    pass
Example Usage:

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  
Example Output:

7
Example 1 Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

0
'''

def count_divisible_collections(nums, k):
    ans = 0
    prefix_sum = 0
    prefix_count = {0:1} # 0 sum is occurring in empty array
    for i in range(len(nums)):
        prefix_sum += nums[i]
        mod = prefix_sum%k
        if mod in prefix_count:
            ans += prefix_count[mod]
            prefix_count[mod] +=1
        else:
            prefix_count[mod] = 1
    return ans

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2)) 