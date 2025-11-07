def square_value(func, x):
    y = x**2
    return func(y)


def f(x) -> int:
    return x * 3


calc = square_value(f, 3)

print(calc)
