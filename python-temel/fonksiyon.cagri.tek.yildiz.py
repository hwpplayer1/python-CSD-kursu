def foo(a, b, c, d, e):
    print("a = {}, b = {}, c ={}, d = {}, e ={}".format(a, b, c, d, e))
t = (30,40)
foo(10, 20, *t, 50)             # a = 10, b = 20, c = 30, d = 40, e = 50
#t = (30, 40)
#foo(10, 20, 30, 40, 50)         # a = 10, b = 20, c = 30, d = 40, e = 50
# İki çağrı da eşdeğerdir.