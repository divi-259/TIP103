'''
A group of time travelers are competing in a series of races to see who can hop through time portals the fastest, from the medieval era to the year 4050.

You're given a list of race outcomes in the form of an integer array races, where each element races[i] = [winner, loser] indicates that the traveler winner defeated the traveler loser in a race.

Write a function find_travelers() that accepts the integer array races as a parameter and returns a list answer of length 2 where:

answer[0] is a list of all travelers who have not lost any races.

answer[1] is a list of all travelers who have lost exactly one race.

Both the input list races and your output list answer should be sorted in increasing order.

Note: Only include travelers who have competed in at least one race — that is, those who appear as either a winner or a loser in the input list races. For example, if races = [[1,2], [5, 6], that may imply the existence of racers 3 and 4. However, since neither racer 3 nor 4 is included in the input list, 3 and 4 should also not appear in the output list answer.

def find_travelers(races):
    pass
Example Usage:

races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))  
print(find_travelers(races2)) 
Example Output

[[1, 2, 10], [4, 5, 7, 8]]
[[1, 2, 5, 6], []]
'''

def find_travelers(races):
    win = set()
    lose = set()
    lose_mul = set()
    n = len(races)
    for i in range(n):
        winner = races[i][0]
        loser = races[i][1]
        if loser in lose:
            lose_mul.add(loser)
        win.add(winner)
        lose.add(loser)
    not_lost = sorted(list(win - lose))
    only_lost_one = sorted(list(lose - lose_mul))
    return [not_lost, only_lost_one]
        

    

races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))  
print(find_travelers(races2)) 