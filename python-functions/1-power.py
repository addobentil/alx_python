
def pow(a, b):
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:
        return 1 / pow(a, -b)
