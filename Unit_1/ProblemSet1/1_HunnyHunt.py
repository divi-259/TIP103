# Source: https://usaco.guide/general/io

'''
Write a function linear_search() to help Winnie the Pooh locate his lost items. 
The function accepts a list items and a target value as parameters. 
The function should return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

def linear_search(items, target):
	pass
Example Usage:

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
Example Output:

3
-1

'''

def linear_search(items, target):
    for i in range(len(items)):
        if(items[i]==target):
            return i
    return -1
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
ans = linear_search(items, target)
print(ans)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
ans = linear_search(items, target)
print(ans)