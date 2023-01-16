# Functions as First-Class Objects

__doc__ is one of several attributes of function objects.

use __doc__ can we get some imformation of the function


## Higher-Order Functions

A function that takes a function as an argument or returns a function as the result is a higher-order function

call a function with a dynamic set of arguments, you can write fn(*args, **kwargs)

## Modern Replacements for map, filter, and reduce

listcomp

for example 

```python
list(map(factorial, range(6)))
[factorial(n) for n in range(6)]
```

```python
list(map(factorial, filter(lambda n: n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]
```

```python
all(iterable)
```
Returns True if there are no falsy elements in the iterable; **all([])** returns True. 

```python
any(iterable)
```
Returns True if any element of the iterable is truthy; **any([])** returns False.

## Anonymous Functions

The lambda keyword creates an anonymous function within a Python expression.
 
 the body cannot contain other Python statements such as while, try, etc. 
 Assignment with = is also a statement, so it cannot occur in a lambda

```python
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])
```

['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

## The Nine Flavors of Callable Objects


## User-Defined Callable Types

```python
import random

class BingoCage:
    def __init__(self, items): 
        self._items = list(items) 
        random.shuffle(self._items)
    
    def pick(self): 
        try:
            return self._items.pop() 
        
        except IndexError:
            raise LookupError('pick from empty BingoCage') 
    
    def __call__(self):
        
        return self.pick()
```

## From Positional to Keyword-Only Parameters
To specify keyword-only arguments when defining a function, name them after the argument prefixed with *

```python
def f(a, *, b):
    return a, b

f(1, b=2)
>>> (1, 2)

f(1, 2)
Traceback (most recent call last):
```

## Positional-Only Parameters

To define a function requiring positional-only parameters, use / in the parameter list.

```python
def divmod(a, b, /): 

    return(a//b,a%b)
```
All arguments to the left of the / are positional-only. 
After the /, you may specify other arguments, which work as usual.

## The operator Module
```python

from functools import reduce
def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
```