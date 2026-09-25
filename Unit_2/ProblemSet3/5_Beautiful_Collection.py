'''
Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a string collection where each artist in your gallery is represented by a character. The beauty of a collection is defined as the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its substrings (subcollections), not just of the collection itself.

def beauty_sum(collection):
    pass
Example Usage:

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))
Example Output:

5
Example 1 Explanation: The substrings with non-zero beauty are 
["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

17
'''

def beauty_sum(collection):
    ans = 0
    for i in range(len(collection)):
        freq = {}
        for j in range(i, len(collection)):
            ch = collection[j]
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch] = 1
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            ans += (max_freq-min_freq)
    return ans




print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

