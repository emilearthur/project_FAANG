# Notes:

## Comprehension
Python supports similar comprehension syntaxes that respectively produce a set, generator, or dictionary.
* list comprehension => ```[k for k in range(1, n+1)]```
* set comprehension => ```{k*k for k in range(1, n+1)}```
* generator comprehension => ```(k*k for k in range(1, n+1))```
* dictionary comprehension => ```{k: k*k for k in range(1, n+1)}```

The generator syntax is particularly attractive when results do not need to be stored in memory.
Eg. compute sum of the first n squares, the generator syntax will be
`total = sum(k*k for k in range(1, n+1))`, this is preferred to used of instantiated list comprehension as the parameter.


## OOP
Each object is an instance of a class. The class definition typically specifies instance variables, also known as data members, that the object contains, as well as the methods also known as member functions, that the object can execute.

### Software Development
* Design
Rules when determining how to design classes;
  * Responsibilities: Divide the work into different actors, each with different responsibility.  Try to describe responsibilities using action verbs. These actors will form the classes for the program.
  * Independence: Define the work for each class to be independent from other classes as possible. Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program. Give data (as instance variables) to the class that has jurisdiction over the actions that requires access to the data.
  * Behaviors: Define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be well understood by other classes they interact with it.
* implementation
  * CRC cards
  * UML
  * Pseudo-Code
  * Coding Style and Documentation
  * Documentation
* Testing and Debugging: Testing is the process of experimentally checking the correctness of a program, while debugging is the process of tracking the execution of a program and discovering the errors in it.<br />
Two types of testing strategies:
  * top-down: testing proceeds from the top to the bottom of the program hierarchy.
  * bottom-up: testing proceeds from lower-level components to higher-level components. Also known as **unit testing**.

### Operator Overloading and Python’s Special Methods
Python’s  built-in  classes  provide  natural  semantics  for  many  operators.

In addition to traditional  operator overloading,  Python relies on specially  named methods  to  control  the  behavior  of  various  other  functionality,  when  applied touser-defined  classes
check [Vector.py](/Vector.py)


### Iterators
Iteration is an important concept in the design of data structure.
Iterator support a special method named __next__ that returns the next element of the collections, if any or raises a StopIteration exception to indicate that there are no further elements.
