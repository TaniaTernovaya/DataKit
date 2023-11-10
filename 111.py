def is_triangle(a, b, c):
    if a >= b + c:
        return False
    if b >= a + c:
        return False
    if c >= a + b:
        return False
    return True


print(is_triangle(1, 1, 1))
