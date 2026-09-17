'''
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy()
 that accepts a string word and returns a new string that removes 
 any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass
Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir" 
tiggerfy(word)
Example Output:

"r"
"eplan"
"chor"
'''

'''
U: input is a str -> we have to make sure all instances are case insensitive
I: use string functions to substitute the substrings (lower and replace)

word length = O(n)


'''

def tiggerfy(word):
    # another method : Using for loop - S.C. = O(1)
    word = word.lower()
    word = word.replace("i", "")
    word = word.replace("t", "")
    word = word.replace("gg", "")
    word = word.replace("er", "")
    return word


text = "Trigger"
print(tiggerfy(text))

text = "eggplant"
print(tiggerfy(text))

word = "Choir choir"
print(tiggerfy(word))
