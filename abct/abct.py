from math import ceil, floor, log
from abct.output import bct
n   = lambda x: (x + 1) % 2 + 1
#s   = lambda x: ceil(log(x, 2)) - 1
s   = lambda x: len(bct(x))
r   = lambda x: x // 2 - n(x) + 1 + n(x) * 2**(s(x) - 1)
pn  = lambda p: r(p) + (n(p) == 2) * (r(r(p)) - r(p))
dn  = lambda p, d: (d + (n(p) == n(d) == 2) * (n(r(p)) * 2**s(d)) - (n(p) == 1)) // (3 - n(p))
