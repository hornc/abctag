def flog2(x):
    """Floor of log2"""
    if x <= 0:
        raise ValueError("math domain error")
    return x.bit_length() - 1
