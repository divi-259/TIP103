'''
In the mystical market, chains of magical items are represented by a balanced parentheses string. Let A and B denote any balanced chains (including the simplest chain "()"). The score is defined recursively:

Base: "()" has a power score of 1. (Note: "()" itself is a valid A.)

Concatenation: If A and B are balanced chains, then AB has score score(A) + score(B).

Enclosure: If A is a balanced chain, then (A) has score 2 × score(A).

Given a balanced string chain, return its total power score.

def score_of_mystical_market_chains(chain):
  pass
Example Usage:

print(score_of_mystical_market_chains("()"))  
print(score_of_mystical_market_chains("(())"))
print(score_of_mystical_market_chains("()()")) 
Example Output:

1
2
2
'''

def score_of_mystical_market_chains(chain):
    

print(score_of_mystical_market_chains("()"))  
print(score_of_mystical_market_chains("(())"))
print(score_of_mystical_market_chains("()()")) 