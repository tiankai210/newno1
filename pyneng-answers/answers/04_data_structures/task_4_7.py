# -*- coding: utf-8 -*-
"""
Task 4.7

Convert MAC address in mac string to binary string like this:
'101010101010101010111011101110111100110011001100'

Print the resulting new string to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

mac = "AAAA:BBBB:CCCC"

#转化为二进制
bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))
print(bin_mac)
