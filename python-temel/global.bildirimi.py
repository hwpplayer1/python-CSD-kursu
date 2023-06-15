x = 10

def foo():
    global x
    x = 20                    # global olan x
    print(x)                  # 20

foo()
print(x)                      # 20
    
