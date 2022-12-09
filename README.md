# `Decorators` and `Generators`: Control your code with ease

`Decorators` are very powerful and handy constructs in Python. They shine when it comes to writing reusable code and controlled flows. `Generators` come in handy when you want to iterate over an object, save memory or preserve the state.

Both of these constructs are easy to implement. Using them can reduce the number of lines of code, make it more readable and optimise performance.

Most Python developers know or would have heard of them. However, only a handful know how to use them well. While working with libraries and frameworks, this can become a `bottleneck` as developers lose out on the functionality they offer.

This workshop aims to help people to implement and use `decorators` and `generators` like a pro.

### Decorators

---

Decorators can help ease code development by making code reusable, implementing single entry points for the workflow, caching, registering plugins, etc. Below is the list of topics covered in the workshop:

- Functional Decorators
  - Simple Decorators ( Basic )
  - Decorator with Arguments
- Class-based Decorators
  - Simple Decorators ( Basic )
  - Decorator with Arguments
  - Descriptors as Decorators
- Decorator Chaining
- Applications
  - Extending existing functionality using decorators.
  - Access Control using decorators (Security).
  - Wrapping Functions into Classes using Decorators.
  - Registering plugins using Decorators.
  - Dependency Injection using Decorators.
  - Working of Route Decorator ( FastAPI & Flask ).
  - Creating @property decorator.
  - Converting generators to context managers.

### Generators

---

Generators can help optimize code when you need to iterate over a large object and save some memory. They are very easy to implement and iterate over. Below is the list of topics that would be covered:

- `yield` keyword.
- Basic Generator Implementation.
- `yield from` expressions in `generators`.
- `generator` expressions.
- Reading files using generators.
- Generator's advanced methods:
  - `send` method ( coroutines )
  - `throw` method ( Custom Exceptions )
  - `close` method ( Closing Generator )
- Using generators with `context managers`.

---

### Instructions to setup up the environment to run code

Pre-Requisites:

- `python >= 3.9` installed. Please run the below set of commands.
- Code editor of your choice. Recommended `VSCode`, `PyCharm`.

Please run the below commands to set up the virtual environment to start with:

```bash
pip install poetry # must have for virtualenv
poetry install # will install all the required dependencies
poetry shell # will activate the environment
```

Recommended VSCode Plugins:

- https://marketplace.visualstudio.com/items?itemName=ms-python.python
- https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager
- https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode

---

The above-mentioned topics would cover constructs completely and would help attendees gain confidence to use them in their source code.

> **Note**:
> _Link to code repository that will be used during the workshop: [https://github.com/satyamsoni2211/pyconf_2022_decorators_generators_workshop](https://github.com/satyamsoni2211/pyconf_2022_decorators_generators_workshop)._ > _`README.md` file would contain a link to PPT and other details regarding the constructs and important articles for future reference. The repository will contain the hands-on source code._
> Candidate should hold basic knowledge for **`Python`**.

PPT: [ Presentation - Decorators and Generators: Control your code with ease ](slideshow.pptx)
