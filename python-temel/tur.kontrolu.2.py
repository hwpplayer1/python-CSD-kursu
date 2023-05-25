def disp_banner(s, ch = '-'):
    if isinstance(s, int):
        s = str(s)
    print(ch * len(s))
    print(s)
    print(ch * len(s))

disp_banner('ankara')
disp_banner(120)
