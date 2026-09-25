'''
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

def find_balanced_subsequence(art_pieces):
    pass
Example Usage:

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
Example Output:

5
Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

2
0
'''

def find_balanced_subsequence(art_pieces):
    frequency={}
    maxlen = 0

    for piece in art_pieces:
        frequency[piece] = frequency.get(piece,0)+1

    for key in sorted(frequency):
        if key+1 in frequency:
            maxlen=max(maxlen,frequency[key]+frequency[key+1])
    return maxlen

art_pieces1 = [1,3,2,2,5,2,3,7] 
# for key in sorted(frequency)
# if key+1 in frequency:
# maxlen = max(maxlen, frequency[key] + frequency[key+1])
art_pieces2 = [1,2,3,4]
# [1:1] [2:1] [3:1] [4:1]
# max_len = max(f1 + f2, max_len)

art_pieces3 = [1,1,1,1]
# [1:4]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))