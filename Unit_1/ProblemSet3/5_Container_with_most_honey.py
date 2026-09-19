'''
Christopher Robin is helping Pooh construct the biggest hunny jar possible.

Help him write a function that accepts an integer array heights of length n. T
he height of each element is given by heights[i].

There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, heights[i]).

Find two lines that, together with the x-axis, form the container that holds the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.
Example Output:

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

49
height = [1, 1]

1

'''

def most_honey(heights):
    left = 0
    right = len(heights)-1
    max_honey = 0
    height = 0

    while left < right:
        width = right - left
        height = min(heights[right], heights[left])

        temp = width * height
        max_honey = max(max_honey, temp)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_honey


# T: O(n), S: O(1)

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))