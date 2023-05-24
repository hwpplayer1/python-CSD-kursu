def foo(a, b, c, d, e, **f): 
    print("a = {}, b = {}, c = {}, d = {}, e = {}, f = {}".format(a, b, c, d, e, f)) 
 
d = {'c': 30, 'd': 40, 'e': 50, 'x': 100, 'y': 200} 
foo(10, 20, **d)   # a = 10, b = 20, c = 30, d = 40, e = 50, x = 100, y = 200