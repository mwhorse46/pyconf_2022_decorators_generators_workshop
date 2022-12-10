# simple generators
def generate():
    for i in range(10):
        yield i


g = generate()
for i in g:
    print(i)

g_ = (i for i in range(10))
