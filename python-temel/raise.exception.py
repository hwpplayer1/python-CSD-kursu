def banner(text):
    if not isinstance(text, str):
        raise TypeError
    print('-' * len(text))
    print(text)
    print('-' * len(text))

banner('ankara')
banner(100)
