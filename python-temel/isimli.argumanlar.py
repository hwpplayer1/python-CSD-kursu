def foo(a, b, c = 10, d = 20, e = 30, f = 40):
    print("a = {}, b = {}, c = {}, d = {}, e = {}, f = {}".format(a, b, c, d, e, f))
foo(1, 2, 3, f = 100)                       # Burada boşuna d ve e için argüman girişi yapmadık
