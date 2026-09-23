'''
Watching a reality TV show, you notice a lot of contestants talk similarly. We want to determine if two contestants have similar speech patterns.

We can represent a sentence as an array of words, for example, the sentence "I've got a text!" can be represented as sentence = ["I've", "got", "a", "text"].

You are given two sentences from different contestants sentence1 and sentence2 each represented as a string array and given an array of string pairs similar_pairs where similar_pairs[i] = [xi, yi] indicates that the two words xi and yi are similar. Write a function is_similar() that returns True if sentence1 and sentence2 are similar, and False if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.

def is_similar(sentence1, sentence2, similar_pairs):
    pass
Example Usage:

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))
Example Output:

True
Example 1 Explanation: "my" and "type" are similar to themselves. The words at 
indices 2 and 3 of sentence1 are similar to words at indices 2 and 3 of 
sentence2 according to the similar_pairs array. 

False
Example 2 Explanation: Sentences are of different length.
'''
from collections import defaultdict

def is_similar(s1, s2, similar_pairs):
    n1 , n2= len(s1), len(s2)
    if n1!=n2:
        return False
    similar = defaultdict(set)
    for a, b in similar_pairs:
        similar[a].add(b)
        similar[b].add(a)

    for w1, w2 in zip(s1, s2):
        if w1==w2:
            continue
        if w2 not in similar[w1]:
            return False
    return True


    

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "an"], ["on","in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))