Though `generator` are subclasses of `iterators`, they are better and performant in many ways.

`iterators` are implemented as classes using hooks `__iter__` and `__next__` while `generators` are mere functions with `yield` keyword.

When an `iterator` object is created and you loop over, everytime `__next__` hook is called to generate a new value. This makes instance to store the values in `member` variables until next iteration.

When generator function is called, it returns `generator iterator` or `generator object`, it also stores references to args in the function state.

Now, when these generator objects are looped over, function is executed till `yield` keyword, value is returned, state of the function including instruction pointer, locals and other parameters are saved until resumed. When they are iterated over again, state is restored.
This is much more performant as compared to calling a function/callback on every iteration.

Benefits:

- `generators` are easy and compact to implement and use.
- Reduces overhead of multiple function calls ( no `__next__` and `__iter__` hooks ).
- Raises any exception like normal function and get exhausted.
- Can be thrown custom exceptions to exhaust them (`throw` method ), not supported in iterators.
- Can be used a coroutines and consume values from user. (`send` method)
