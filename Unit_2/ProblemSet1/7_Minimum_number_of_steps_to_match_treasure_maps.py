'''
Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, you can choose any character of map2 and replace it with another character.

Return the minimum number of steps to make map2 an anagram of map1.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

def min_steps_to_match_maps(map1, map2):
    pass
Example Usage:

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
Example Output:

1
6
0
'''

def min_steps_to_match_maps(map1, map2):
    count1 = {}
    count2 = {}
    
    for char in map1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    
    for char in map2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    
    # Step 2: Calculate the number of changes needed
    steps = 0
    for char in count2:
        if char in count1:
            if(count2[char] > count1[char]):
                steps += count2[char]-count1[char]
        else:
            steps+=count2[char]
    return steps


map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))