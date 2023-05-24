def foo(a, b, c):
    print("a = {}, b = {}, c = {}".format(a, b, c))

foo(10, 20 , 30)                           #geçerli
foo(10, c = 30, b = 20)                    #geçerli
foo(c = 30, a = 10, b = 20)                #geçerli
