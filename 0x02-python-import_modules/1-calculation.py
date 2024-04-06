#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    add = calculator_1.add(a, b)
    sub = calculator_1.sub(a, b)
    mul = calculator_1.mul(a, b)
    div = calculator_1.div(a, b)
    s = [add, sub, mul, div]
    for c in s:
        print("{} + {} = {}".format(a, b, c))
