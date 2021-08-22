from abct.output import abct_out, bct_out

hw = [
        '1 00000010 0',  # 0x02 STX
        '1 01001000 0',  # 0x48 'H'
        '1 01100101 0',
        '1 01101100 0',
        '1 01101100 0',
        '1 01101111 0',
        '1 00101100 0',
        '1 00100000 0',  # 0x32 SPACE
        '1 01010111 0',  # 0x87 'W'
        '1 01101111 0',
        '1 01110010 0',
        '1 01101100 0',
        '1 01100100 0',
        '1 00100001 0',  # 0x33 '!'
        '1 00000011 0'   # 0x03 ETX
        ]


def test_abct_out():
    assert abct_out(3928440351693569184044057579967756650479167746).decode() == 'Hello, World!'


def test_bct_out():
    output = ''.join(hw).replace(' ', '')
    assert bct_out(output).decode() == 'Hello, World!'


def test_bct_out_utf8():
    u = """
        1 00000010 0
        1 11100010 0
        1 10000100 0
        1 10010101 0
        1 11100010 0
        1 10100101 0
        1 10000001 0
        1 11110000 0
        1 10011111 0
        1 10001111 0
        1 10110111 0 
        1 00000011 0
        """.replace(' ', '').replace('\n', '')
    assert bct_out(u).decode() == 'ℕ⥁🏷'
