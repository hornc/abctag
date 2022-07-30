def flog2(x):
    """
    Floor of log2.
    Equivalent to math.floor(math.log(x, 2))
    but does not give rounding errors on
    x >= 2**48 - 1
    """
    if x <= 0:
        raise ValueError("math domain error")
    return x.bit_length() - 1
