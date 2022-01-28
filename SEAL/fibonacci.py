def fibonacci(n1, n2, n):
    (print(f"{n1}\n{n2}"), fibonacci(n2, n1+n2, n))if n1<1 else (print(f"{n2}"), fibonacci(n2, n1+n2, n))if n2<=n else 0


fibonacci(0, 1, n=int(input('Enter the maximum limit of the fibonacci series: ')))
