from abct.abct import s

# convert artihmetic bijective base-2 numeric value to BCT string of 0,1s
bct = lambda i, s='': bct((i - 2 * ((i + 1) % 2)) // 2, '%s%d' % (s, (i + 1) % 2)) if i else s
# convert BCT binary string into bijective base-2 int
bin_to_bb2 = lambda s: sum([int(c) * 2 ** i for i,c in enumerate(s.replace(' ', '').replace('1', '2').replace('0', '1'))])
# Output encoded BCT bytes (with STX=\x02, ETX=\x03, start bit = 1, stop bit = 0 checking):
bct_out = lambda s: b''.join([bytes([(int(s[len(s)%10:][i*10+1:i*10+9], 2)) for i in range(len(s)//10) if s[len(s)%10:][i*10] == '1' and s[len(s)%10:][(i+1)*10-1] == '0'])])[1:-1]
abct_out = lambda i: bct_out(bct(i))
has_out = lambda p, d: p // 2**(s(p) - 2) == 5 and d > 2**10 and d // 2**(s(d) - 10) == 2 * 3**6 - 7**2
