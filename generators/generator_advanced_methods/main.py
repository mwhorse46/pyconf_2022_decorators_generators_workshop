# send, throw, close methods in generators
def generate():
    try:
        yield 1
    except:
        pass


g = generate()
next(g)
# g.close()
try:
    g.throw(Exception("fake exception"))
except:
    next(g)
