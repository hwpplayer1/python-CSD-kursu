def foo(*a):
    print(a)

foo()                       # ()
foo(10)                     # (10,)
foo(10, 20)                 # (10, 20)    
foo(10, 20, 30)             # (10, 20, 30)