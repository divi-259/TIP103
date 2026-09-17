'''
Write a function words_with_char() that 
accepts a list of strings words and a character x. 
Return a list of indices representing the words that contain the character x. 
The returned list may be in any order.

def words_with_char(words, x):
	pass
Example Usage:

words = ["batman", "superman"]
x = "a"
words_with_char(words, x)

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
words_with_char(words, x)

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
words_with_char(words, x)
Example Output:

[0, 1]
[0, 2]
[]
'''

def words_with_char(words, x):
	ans = []
	for i in range(len(words)):
		if(words[i].find(x)!=-1):
			ans.append(i)
	return ans

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))