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
check [SequenceIterator.py](/SequenceIterator.py) and [Range.py](/Range.py)

### Inheritance
A hierarchical design is useful in software development, as common functionality can be grouped at the most general level, thereby promoting reuse of code, while differentiated behaviors can be viewed as extensions of the general case, In object-oriented programming, the mechanism for a modular and hierarchical organization is a technique known as in heritance. This allows a new class to be defined upon an existing class as the starting point. Existing class = base class, parent class or super class and newly defined class is known as sub or child class.
Two ways to differentiate a subclass to superclass are:
* Overriding an existing method by providing a new implementation.
* Extend an exiting method by providing brand new methods.


### Abstract Base Classes
When defining a group of classes as part of an Inheritance hierarchy, one technique for avoiding repetition of code is to design a base class with common functionality that can be inherited by other classes.
Abstract base class is a class whose sole purpose is to serve as a base class through Inheritance. Abstract class cannot directly instantiated while a concrete class is the one that can be instantiated.
The template method pattern is when an abstract base class provides concrete behaviors that rely upon calls to other abstract behaviors. In that way, as soon as a subclass provides definitions for the missing abstract behaviors, the inherited concrete behaviors are well defined.

In [Sequence.py](/Sequence.py) we implemented the following techniques:
* We declare the ABCMeta class of the abc module as metaclass of our Sequence class. A metaclas is different from a superclass as it provides a template for the class definition itself. The ABCMeta declaration assures that the constructor for the class raises an error.
* The use of `@abstractmethod` decorator before the `__len__` and `__getitem__` methods are declared. That decalares two particular methods to be abstract, i.e. we do not provide an implementation within our Sequence base class but we expect any concrete subclasses to suppport those two methods.
Note: Python enforces this expectation by disallowing instantiation for any subclass that does not override the abstract methods with concrete implementations.

The implementations of methods __contains__, index and count do not rely on any assumption about the self instances, other than that syntax len(self) and self[j] are supported (by special methods __len__ and __getitem__, respectively).

### Namespaces and Object-Orientation
A namespace is an abstraction that manages all of the identifiers that are defined in a particular scope, mapping each name to its associated value.
In python, functions, classes and modules are first-class objects and so the value associated with it as an identifier in a namespace may in fact be a function, class or module.

#### Instance and Class Namespaces
We could delcare class CreditCard with slots as

```
class CreditCard:
    __slots__ = '_customer', '_bank', '_account', '_balance', '_limit'
```
  and also for class PredatoryCreditCard as
```
class PredatoryCreditCard(CreditCard):
    __slots__ = '_apr'
```

#### Name Resolution and Dynamic Dispatch
Here we discuss the process used in retrieving a name in Python's OO framework. When object.foo is mentioned, the python interpreter begins a name resolution process as follow:

* The instance namespace is searched; if the desired name is found, its associated value is used.
* Otherwise the class namespace, for the class to which the instance belongs is searched; if name is found its associated value is used.
* If name was not found in the immediate class namespace, the search continues upward through the inheritance hierarchy, checking the class namespace for each ancestor (commonly by checking the superclass class, then it superclass class and so on). The first time the name is found , it associate value is used.
* If the name has still not been found an AttributeError is raised.  

Python uses dynamic dispatch to determine at run-time which implementation of a function to call based upon the type of the object upon which it is invoked.

#### Shallow and Deep Copying
Python provides a module copy which that produces both shallow and deep copies of arbitrary objects.
For shallow copy we can do `palette = copy(warmtones)` and for deep copy we can do `paletter = copy.deepcopy(warmtones)`.

#### Algorithm Analysis
`timeit` helps tp automate evaluations with repetition to account for variance among trails.

**Challenges of Experimental Analysis**
Three major limitation to use for algo. analysis include:
* Experimental running times of two algos are difficult to directly compare unless the experiments are performed in the same hardware and software environments.
* Experiments can be done only on a limited set of test inputs; hence, they leave out the running times of inputs not included in the experiment (and these inputs may be important).
* An algo must be fully implemented in order to execute it to study its running time experimentally.


** Moving Beyond Experimental Analysis.
Goal is to develop an approach to analyze the efficiency of algo. that:
* Allows us to evaluate the relative efficiency of any two algo in a way that is independent of the hardware and software environment.
* Is performed by studying a high-level description of the algo. without need for implementation.
* Takes into account all possible inputs.

** Counting Primitive Operations **
To analyze the running time of an algo without performing experiments, we perform an analysis directly on a high-level description of the algo. We define a set of primitives operations such as the follows:
* Assigning an identifier to an object
* Determining the object associated with an identifier
* Performing an arithmetic operation
* Accessing a single element of a python list by index
* Calling a function (excluding operations executed within the function)
* Returning from a function

Formally, a primitive operation corresponds to a low-level instruction with an execution time that is constant. Ideally, this might be the type of basic operation that is executed by the hardware, although many of our primitive operation may be translated to a small number of instructions. Instead of trying to determine the specific execution time of each primitive operation, we will simply count how many primitive operations are executed, and use this number `t` as a measure of the running time of the algo.
