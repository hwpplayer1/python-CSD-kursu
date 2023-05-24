def foo(a, b, **kwargs):
    legal_args = ['width', 'height', 'color', 'spec']
    for key in kwargs:
        if key not in legal_args:
            print('{} is invalid arguments'.format(key))
            return
    
    width = kwargs.get('width', 1)
    height = kwargs.get('width', 1)
    color = kwargs.get('color', 'red')
    spec = kwargs.get('spec', 'default')

    print(f'a = {a}, b = {b}, width = {width}, height =  {height}, color = {color}, spec = {spec}')

foo(10, 20)
foo(10, 20, color = 'blue', spec = 'x12')
foo(10, 20, height = 10, color = 'red')