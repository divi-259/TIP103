'''
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function can_make_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

def can_make_balanced(code):
    pass
Example Usage:

code1 = "arghh"
code2 = "hahag"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
'''

def can_make_balanced(code):
    freq = {}
    for ch in code:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch]+=1
    freq_count = {}
    for val in freq.values():
        if val in freq_count:
            freq_count[val]+=1
        else:
            freq_count[val] = 1
    # total unique frequencies 
    total_uniq = len(freq_count)
    if(total_uniq > 2):
        return False # can never make it all equal
    if(total_uniq==1):
        # if all chars are same or if the freq is 1 - we can remove 1 char
        if len(freq.keys())==1:
            return True
        # all chars have one occurrence
        if list(freq_count.keys())[0]==1:
            return True
        else:
            return False

    # if there are exactly two uniq frequencies 
    for val, f in freq_count.items():
        if val==1 and f==1:
            return True
    # further checks on two unique frequencies
    values = list(freq_count.keys())

    if values[0]-values[1] == 1 and freq_count[values[0]]==1:
        return True
    if values[1]-values[0]==1 and freq_count[values[1]]==1:
        return True

    return False


        



code1 = "arghh"
code2 = "hahaf"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 