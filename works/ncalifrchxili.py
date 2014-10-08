def a():
    print(b())
    return a
def b():
    return 'hello world'

a()()()
