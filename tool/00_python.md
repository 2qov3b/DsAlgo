# Properties
Python is *strongly typed* (i.e. types are enforced), *dynamically*, *implicitly typed* (i.e. you don’t have to declare variables), *case sensitive* (i.e. var and VAR are two different variables) and *object-oriented* (i.e. everything is an object).

# Getting help
Help in Python is always available right in the interpreter. If you want to know how an object works, all you have to do is call `help(<object>)`! Also useful are `dir()`, which shows you all the object’s methods, and `<object>.__doc__`, which shows you its documentation string:
```python
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> dir(abs)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

>>> abs.__doc__
'Return the absolute value of the argument.'
```

# Syntax

