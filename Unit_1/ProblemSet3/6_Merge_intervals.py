'''
You are given an array of intervals, where each interval is represented as [start, end].

Write a function merge_intervals(intervals) 
that merges all overlapping intervals and returns a new array of the merged, non-overlapping intervals.

def merge_intervals(intervals):
	pass
Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
Example Output:

[[1, 6], [8, 10], [15, 18]]
[[1, 5]]

'''

def merge_intervals(intervals):
	if not intervals:
		return intervals
	n = len(intervals)
	if n==1:
		return intervals
	intervals.sort()
	ans = []
	for low,high in intervals:
		if not ans:
			ans.append([low, high])
		prev_high = ans[-1][1]
		if prev_high>=low:
			ans[-1][1] = max(prev_high, high)
		else:
			ans.append([low, high])
	return ans
		



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))