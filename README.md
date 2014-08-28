Python-PrettyPrintDictionary
============================

Prints Dictionary key-values in a human readable manner.

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

