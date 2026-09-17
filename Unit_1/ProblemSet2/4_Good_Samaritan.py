'''
Superman is doing yet another good deed, 
using his power of flight to distribute meals for the Metropolis Food Bank.
He wants to distribute meals in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. 
There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, 
write a function minimum_boxes() 
that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes.

def minimum_boxes(meals, capacity):
	pass
Example Usage:

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)
Example Output:

2
4
'''

def minimum_boxes(meals, capacity):
    total = sum(meals)
    ans = 0
    capacity.sort(reverse=True)
    for c in capacity:
        if(total<=0):
            break
        total-=c
        ans+=1
    return ans if total<=0 else -1
        




meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))