'''
In your time travel adventures, you are given an array of digit strings portals and a digit string destination. Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

def num_of_time_portals(portals, destination):
    pass
Example Usage:

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
Example Output:

4
2
6
'''

def num_of_time_portals(portals, destination):
    ans = 0
    for i in range(len(portals)):
        for j in range(i+1, len(portals)):
            str = portals[i] + portals[j]
            rev = str[::-1]
            if str==destination:
                ans+=1
            if rev==destination:
                ans+=1
    return ans


portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))