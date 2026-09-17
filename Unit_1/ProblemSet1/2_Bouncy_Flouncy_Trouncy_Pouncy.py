
'''

Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
	pass
Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
Example Output:

2
4
'''
# U: 
# output = 1, traverse through our list, increase or decrease output
# return output
# T: O(n), S: O(1)
def final_value_after_operations(operations):
    output = 1

    for item in operations:
        if item == 'bouncy' or item == 'flouncy':
            output += 1
        elif item == 'trouncy' or item == 'pouncy':
            output -= 1

    return output


operations = ["trouncy", "flouncy", "flouncy"]
output = final_value_after_operations(operations)
print(output)

operations = ["bouncy", "bouncy", "flouncy"]
output = final_value_after_operations(operations)
print(output)

