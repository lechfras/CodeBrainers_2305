def quadratic(a, b, c):
    """
        x1 = (-b - sqrt(delta)) / 2a
        x2 = (-b + sqrt(delta)) / 2a
    when delta > 0,
        x0 = -b / 2a
    when delta = 0,
    and None otherwise.
    delta = b^2 - 4ac


    """

    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return (-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)
    elif delta == 0:
        return -b / (2 * a)
    else:
        return None
