def foo(a, b, c = 10, d = 20, e = 30, f = 40):
    print("a = {}, b = {}, c = {}, d = {}, e = {}, f = {}".format(a, b, c, d, e, f))

#foo(10)                                          # geçersiz!
foo(10, 20)                                      # geçerli !
foo(100, c = 200, b = 300)                       # geçerli
foo(100, c = 200, b = 300, d = 400)              # geçerli
#foo(100, 200, b = 300)                           # geçersiz!
