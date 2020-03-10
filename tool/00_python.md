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
Python has `no mandatory statement termination characters` and `blocks are specified by indentation`. Indent to begin a block, dedent to end one. Statements that expect an indentation level end in a colon `:`. Comments start with the pound `#` sign and are single-line, multi-line strings are used for *multi-line comments*. Values are assigned (in fact, *objects are bound to names*) with the equals sign `=`, and *equality testing* is done using two equals signs `==`. You can increment/decrement values using the `+=` and `-=` operators respectively by the right-hand amount. This works on many datatypes, strings included. You can also use multiple variables on one line. For example:
```python
>>> var = 3
>>> var += 2
>>> var
5

>>> var -= 1
>>> var
4

>>> """This is a multiline comment.
... The following lines concatenate the two strings."""
'This is a multiline comment.\nThe following lines concatenate the two strings.'

>>> str = "Hello"
>>> str += " World!"
>>> str
'Hello World!'
>>> print(str)
Hello World!

# This swaps the variables in one line.
# It doesn't violate strong typing because values aren't
# actually being assigned, but new objects are bound to
# the old names.
>>> var, str
(4, 'Hello World!')
>>> var, str = str, var
>>> var, str
('Hello World!', 4)
```

# Data types
