---
marp: true
author: satyam soni
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# About me

A `Python Enthusiast` with _*6.5 years*_ of experience working across multiple domains, verticals, and Frameworks. I am an active Open-Source contributor, with multiple libraries published over PyPI (`lazy-alchemy`, `py-lambda-warmer`, `flask-dantic` etc.), and currently working as Technology Lead with SenecaGlobal, delivering Python Based Full Stack Solutions to clients.

---

# What are we gonna cover?

- `decorators`
- `generators`

Their `importance` and `applications`. ...

---

# What is a `Decorator`?

`A decorator is a design pattern in Python` that allows a user to `add new functionality` to `an existing object` without `modifying its structure`.

---

# Why `Decorator`?

Let us understand with an example.

Say you have a function `ABC` that is working fine. You now want to add additional functionality to `log time`. You went ahead and modified the code. Now say you have a hundred similar kinds of functions and you now want to modify each one of them.

This is where the `decorator` pattern helps!

![w:200 bg right:20% blur:1px](download.png)

---

# Applications of `Decorator`

- Adding validation layer.
- Wrapping up objects/ Proxying.
- Registering plugins.
- Extending functionality.
- Dependency injection.

... _many more_.

---

# let us talk more about `decorators`

We may code along as we discuss this in detail. The below link would include all the source codes.

[Pyconf 2022 Workshop - Decorators](https://github.com/satyamsoni2211/pyconf_2022_decorators_generators_workshop/tree/main/decorators)

---

# What is a `Generator`?

`generator functions` are a special kind of function that returns a lazy iterator.

---

# Why `Generator`?

Let us consider this code segment

```python
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

This reads a `CSV` file and returns the list of the lines. This may be okay for a small file but consider the file to be `GB` in size. Is it okay to load everything at once or read it lazily as and when required?

This is where the generator helps you with, iterating over the object lazily.

---

# `Generators` Over `Iterators`?

Though `Generators` are a subclass of `Iterators`, they are more handy and compact. Unlike `Iterators`, which require `__iter__` and `__next__` methods, generators are simple functions with a `yield` statement.

```python
>>> import collections, types
>>> issubclass(types.Generator,collections.Iterator)
>>> True
```

`Generators` also save the local state of the function (variable binding, instruction sets ...) when execution pauses.

---

# Magical `yield` keyword

`yield` is a special keyword in python which turns a normal function into a `generator`. `yield` is also responsible for generating new value, returning the generated value, and suspending the execution until the next iteration.

`yield` is like `return` in Python, except that it also saves the state of the function, suspends its execution, and resumes it when called upon.

`yield` can also consume values using `send()` method on `generator object`.

---

# Initializing a `generator`

When we call a generator function, it returns a `generator object` that can be stored in a variable.

When we call `next()` on this generator object, **it initializes generator object**, execution starts and suspends till it reaches the `yield` keyword.

**Note**: _We will need to initialize the generator object by calling the `next` method before we can use the `send()`, `throw()` and `close()` methods_.

---

# Facts about `generators`

- `generators` also get exhausted like an `iterator` object and raise the `StopIteration` Exception. When looped over, this exception is automatically handled by construct.

- `generator objects` can only be used once i.e. they cannot be reused once exhausted.

_Note: `StopIteration` is a natural exception that’s raised to signal the end of an iterator._

---

# Let's code generators

The below link would include all the source codes for `generators`.

[Pyconf 2022 Workshop - Generators](https://github.com/satyamsoni2211/pyconf_2022_decorators_generators_workshop/tree/main/generators)

---

# Q&A

---

# Thank You.
