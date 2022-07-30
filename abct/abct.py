from abct.math import flog2
n   = lambda x: (x + 1) % 2 + 1
s   = lambda x: flog2(x + 1)
r   = lambda x: x // 2 - n(x) + 1 + n(x) * 2**(s(x) - 1)
pn  = lambda p: r(p) + (n(p) == 2) * (r(r(p)) - r(p))
dn  = lambda p, d: (d + (n(p) == n(d) == 2) * (n(r(p)) * 2**s(d)) - (n(p) == 1)) // (3 - n(p))
