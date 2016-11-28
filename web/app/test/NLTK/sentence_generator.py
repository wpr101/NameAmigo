from nltk.parse.generate import generate
from nltk import CFG


my_grammar = """
  S -> NP VP
  NP -> Det N
  PP -> P NP
  VP -> 'slept' | 'saw' NP | 'walked' PP | 'jumped' PP
  Det -> 'the' | 'a'
  N -> 'man' | 'park' | 'dog' | 'cat' | 'lion' | 'bird' | 'whale'\
  | 'fish' | 'snake' | 'elephant' | 'rat'
  P -> 'in' | 'with' | 'on'
"""

grammar1 = """
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
"""

grammar2 = """
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
"""

grammar = CFG.fromstring(grammar2)

for sentence in generate(grammar, n=2000, depth=7):
    print(' '.join(sentence))
