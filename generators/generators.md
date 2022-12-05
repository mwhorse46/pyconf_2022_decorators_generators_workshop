**Introduced**: PEP 255 – Simple Generators (2001)

**Link**: [https://peps.python.org/pep-0255/](https://peps.python.org/pep-0255/)

Rules about generators:

- Generator functions use `yield` keyword instead of `return`.
- `return` is allowed in `generators`, but would raise `StopIteration` error.

```python
def a(b_=None):
    b = b_
    if not b:
        return
    else:
        yield b


a_ = a()
print(next(a_))
```

- Any exceptions raised inside generator are forwarded to the caller as is like a normal function. This will also exhaust generator function.
- try/ except is not recommended while `yielding` a value in generator function.
- Generator functions if called after exhausted, would raise `StopIteration` error.
- if exceptions are handled and generator returns, it raises `StopIteration` error.
- Like iterators, Generator functions can be iterated over once and can not be reused.
