'''
Write a function squash_spaces() that takes in a string s as a parameter and 
returns a new string with each substring with consecutive spaces reduced to a single space.
Assume s can contain leading or trailing spaces, but in the result should be trimmed. 
Do not use any of the built-in trim methods.

def squash_spaces(s):
    pass
Example Usage

s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)
Example Output:

"Up, up, and away!"
"With great power comes great responsibility."
'''

def squash_spaces(s):
    left = 0
    if not s:
        return s
    ans = []
    while left < len(s):
        if s[left]==' ' and ((not ans) or (ans[-1]==' ')):
            left+=1
            continue
        else:
            ans.append(s[left])
            left+=1
    if(ans and ans[-1]==' '):
        ans.pop()
    return ''.join(ans)

s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "    "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))