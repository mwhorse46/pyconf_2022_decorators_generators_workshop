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

A `Python Enthusiast` with _*6.5 years*_ of experience working across multiple domains, verticals and Frameworks. He is also an active Open-Source contributor, with multiple libraries published over PYPI (`flask-dantic`, `lazy-alchemy`, `py-lambda-warmer` etc.), and currently working as `Technology Lead` with `SenecaGlobal`, delivering Python Based Full Stack Solutions to the clients.

---

# What are we gonna cover ?

- `decorators`
- `generators`

There `importance` and `applications`. ...

---

# What is a `Decorator` ?

As per docs, `A decorator is a design pattern in Python` that allows a user to `add new functionality` to `an existing object` without `modifying its structure`.

---

# Why `Decorator` ?

Let us understand with an example.

Say you have a function `abc` which is working absolutely fine. You now want to add an additional functionality to `log time`. You went ahead and modified code. Now say you have a hundred functions and you want to modify each one of them ?

This is where `decorator` helps !

![w:200 bg right:20% blur:1px](download.png)

---

# Applications of `Decorator`

- Adding validation layer.
- Wrapping up objects/ Proxying.
- Registering plugins.
- Extending functionality.
- Dependancy injection.

... _many more_.

---

# Lets talk more on `decorators`

We may code along as we discuss this in detail. Below link would include all the source code.

> [https://github.com/satyamsoni2211/pyconf_2022_decorators_generators_workshop/tree/main/decorators](https://github.com/satyamsoni2211/pyconf_2022_decorators_generators_workshop/tree/main/decorators)

---

# What is a `Generator` ?

`generator functions` are a special kind of function that return a lazy iterator.

---

# Why `Generator` ?

Lets consider this code segment

```python
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

This reads a `csv` file and returns list of the lines. This may be okay for small file but consider file to be `gb's` in size. Is it okay to load everything at once or read it lazily as and when required ?

This is where generator helps you with, iterating over the object lazily.
