def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(10, 20, c = 10, d = 20)                        #geçerli
foo(10, 20, d = 20, c = 20)                        #geçerli
