def F(n):
    print(n)
    if n<3:
        F(n+1)
    print(f'end {n}')
F(1)