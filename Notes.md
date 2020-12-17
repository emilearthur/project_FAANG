# Notes:

## Comprehension
Python supports similar comprehension syntaxes that respectively produce a set,
generator, or dictionary.
* list comprehension => ```[k for k in range(1, n+1)]```
* set comprehension => ```{k*k for k in range(1, n+1)}```
* generator comprehension => ```(k*k for k in range(1, n+1))```
* dictionary comprehension => ```{k: k*k for k in range(1, n+1)}```

The generator syntax is particularly attractive when results do not need to be stored in memory.
Eg. compute sum of the first n squares, the generator syntax will be
`total = sum(k*k for k in range(1, n+1))`, this is preferred to used of instantiated list comprehension as the parameter. 
