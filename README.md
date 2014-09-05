Python-PrettyPrintDictionary
============================

Prints Dictionary key-values in a human readable manner.

<h2>What it is?</h2>
Suppose you have the following dictionary:
```
dict_1 = {'a': 0, '1': {1: 'c', 2: 'd'}, '2': [1, 2, 3, 4, 5, 6]}
```
When you print this on the console you will have this:
```
>>> {'a': 0, '1': {1: 'c', 2: 'd'}, '2': [1, 2, 3, 4, 5, 6]}
```
What if you have a very larger dictionary of things that each key has an iterable object, i.e dictionary, list, ...? How does it look like?

Suppose you have the following dictionary:
```
dict_1 = {'a': 0, '1': {1: {'abc': [1, 2, 3, 4, 5, 6], 'efg': [7, 8, 9, 10, 100]},
                        2: {'1': {1: 'abc', 2: 'efg'}, '2': {3: 'abc'}}}, '2': [1, 2, 3, 4, 5, 6]}
```
if you print if normally it will be this:
```
{'a': 0, '1': {1: {'abc': [1, 2, 3, 4, 5, 6], 'efg': [7, 8, 9, 10, 100]}, 2: {'1': {1: 'abc', 2: 'efg'}, '2': {3: 'abc'}}}, '2': [1, 2, 3, 4, 5, 6]}
```
But if you use this lib it would be this:


<h2>Usage</h2>

Simply import the <b>PrettyDict</b> from <b>pretty_print_dictionary</b> 
```
from pretty_print_dictionary import PrettyDict
```

Create your own dictionary.
```
my_dictionary = {0:[1,2,3], 1:['a','b']}
```

Create a class of <b>PrettyDict</b> and set your dictionary as its argument.
```
pd = PrettyDict(my_dictionary)
```

Call the <b>ppd</b>(Pretty Print Dictionary) method to print the dictionary
```
pd.ppd()
```

Output
```
0
  1,2,3 
1   
  a,b 
```

