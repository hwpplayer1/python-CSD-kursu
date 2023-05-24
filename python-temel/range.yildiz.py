def foo(a, b, c, *d):
    print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))
foo(100, *range(10))

#Buradaki çağrının eşdeğeri şöyledir: 
 
#foo(100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 