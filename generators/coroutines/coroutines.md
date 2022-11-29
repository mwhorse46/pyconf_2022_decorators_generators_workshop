`Coroutines` are special user case of `generators` which can consume values.

`generators` exposed a special method `send` which can be used to consume values. This method can only be used once `generator` object is initialized.

benefits:

- reduces overhead of reinitialization.
- can store previous states of the locals.
