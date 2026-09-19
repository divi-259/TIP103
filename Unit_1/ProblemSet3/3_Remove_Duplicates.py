'''
Write a function remove_dupes() that accepts a sorted array items, 
and removes the duplicates in-place such that each element appears only once. 
Return the length of the modified array. You may not create another array; 
your implementation must modify the original input array items.

def remove_dupes(items):
    pass
Example Usage

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)
Example Output:

4
4

'''

# Remove the duplicates
# Modify the original list
# Not create another array
# Return the new length 

# Plan: two pointers: left -> positions of the last unique item. 
# right -> searches through the list 

# O(n) - Time and O(1) - Space

def remove_dupes(items):
    if not items: 
        return 0
    
    left = 0

    for right in range(1, len(items)):
        if items[right] != items[left]:
            left += 1
            items[left] = items[right]
    
    del items[left + 1:]

    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
result = remove_dupes(items)
print(result)
print(items)