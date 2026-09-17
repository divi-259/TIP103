'''
Write a function local_maximums() that accepts an n x n integer matrix grid and r
eturns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered 
around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

def local_maximums(grid):
	pass
4x4 matrix with cells numbered according to Example 1 input next to 2x2 matrix numbered according Example 1 output

Example Usage:

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
local_maximums(grid)
Example Output:

[[9, 9], [8, 6]]
[[2, 2, 2], [2, 2, 2], [2, 2, 2]]
'''

def getMax(grid, r, c):
	best = float('-inf')
	for i in range(r,r+3):
		for j in range(c, c+3):
			best = max(grid[i][j],best)
	return best

def local_maximums(grid):
	n = len(grid)
	r = n-2
	ans = [[0] * r for _ in range(r)]
	for i in range(n-2):
		for j in range(n-2):
			ans[i][j] = getMax(grid,i,j)
	return ans

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))