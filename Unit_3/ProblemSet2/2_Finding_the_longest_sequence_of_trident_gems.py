'''
The people of Atlantis are collecting rare Trident Gems as they explore the ocean. The gems are arranged in a sequence of integers representing their value. Write a recursive function that returns the length of the consecutive sequence of gems where each subsequent value increases by exactly 1.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def longest_trident_sequence(gems):
    pass
Example Usage:

print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))
Example Output:

5
Example 1 Explanation: longest sequence is 2, 3, 4, 5, 6

2
Example 2 Explanation: longest sequence is 7, 8 or 1, 2
'''

def helper(gems, index, currlen, maxlen):
    if index==len(gems)-1:
        return max(currlen, maxlen)
    if(gems[index]+1==gems[index+1]):
        return helper(gems, index+1, currlen+1, max(currlen, maxlen))
    else:
        return helper(gems, index+1, 1, maxlen)

def longest_trident_sequence(gems):
    if not gems:
        return 0
    return helper(gems, 0, 1, 1)



print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))