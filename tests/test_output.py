from abct.output import abct_out, bct_out, has_out

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

class Test_ABCT_output:
    hw = 3928440351693569184044057579967756650479167746
    def test_abct_out(self):
        assert has_out(5, self.hw)
        assert abct_out(self.hw).decode() == 'Hello, World!'

    def test_abct_incorrect_stop_bit(self):
        # incorrect stop bits prevent an indidual 8bit character from being output
        output = self.hw | (1 << 20)  # set 0 stop bit of first char 'H' to 1
        assert output != self.hw
        assert has_out(5, output)  # has_out() simply tests there is an ETX in the data string
        assert abct_out(output).decode() == 'ello, World!'

    def test_abct_incorrect_mid_stop_bit(self):
        output = self.hw | (1 << 90)  # overwrite a 0 stop bit with 1
        assert output != self.hw
        assert has_out(5, output)  # has_out() simply tests there is an ETX in the data string
        # char with invalid stop bit is no longer output:
        assert abct_out(output).decode() == 'Hello, orld!'

    def test_missing_ETX(self):
        output = self.hw | (0xff << 142)  # overwrite ETX with 0xff
        assert not has_out(5, output)  # No ETX := no output trigger
        # but abct_out() will attempt to extract output from any input, regardless of STX / ETX:
        assert abct_out(output).decode() == 'Hello, World!'

    def test_missing_STX(self):
        output = self.hw | (0xff << 2)  # overwrite STX with 0xff
        assert has_out(5, output)  # Missing STX does not currently prevent the output trigger
        # abct_out() will attempt to extract output from any input, regardless of STX / ETX:
        assert abct_out(output).decode() == 'Hello, World!'

    def test_alter_output(self):
        output = self.hw | (1 << 19)  # increment first char by one: "H" → "I"
        assert has_out(5, output)
        assert abct_out(output).decode() == 'Iello, World!'


class Test_BCT_out:
    def test_bct_out(self):
        output = ''.join(hw).replace(' ', '')
        assert bct_out(output).decode() == 'Hello, World!'

    def test_missing_STX(self):
        # This documents current behaviour, not necessarily intended:
        # STX is not required for output to occur
        # However, one valid frame is used as the string marker and not output
        output = ''.join(hw[1:]).replace(' ', '')
        assert bct_out(output).decode() == 'ello, World!'

    def test_bct_out_utf8(self):
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
