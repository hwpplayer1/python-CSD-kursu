x = 10

def foo():
    global x
    #print(x)                # exception!

foo()
print(x)
