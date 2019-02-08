# -*- coding: utf-8 -*-
"""
Jacob Ashcraft
Numeric Algorithms 1
Advanced Algorithms
Professor Teichert

"""

# Creating a logical AND
def AND(a, b):
    """
    Returns a single character '0' or '1'
    representing the logical AND of bit a and bit b (which are each '0' or '1')
    
    >>> AND('0', '0')
    '0'
    >>> AND('0', '1')
    '0'
    >>> AND('1', '0')
    '0'
    >>> AND('1', '1')
    '1'
    
    """
    if a == '1' and b == '1':
        return '1';
    
    return '0'

# Creating a logical OR
def OR(a, b):
    """
    Returns a single character '0' or '1'
    representing the logical OR of bit a and bit b (which are each '0' or '1')
    
    >>> OR('0', '0')
    '0'
    >>> OR('0', '1')
    '1'
    >>> OR('1', '0')
    '1'
    >>> OR('1', '1')
    '1'
    
    """
    if a == '0' and b == '0':
        return '0'
    
    return '1'

# Creating a logical XOR
def XOR(a, b):
    """
    Returns a single character '0' or '1'
    representing the logical XOR of bit a and bit b (which are each '0' or '1')
    
    >>> XOR('0', '0')
    '0'
    >>> XOR('0', '1')
    '1'
    >>> XOR('1', '0')
    '1'
    >>> XOR('1', '1')
    '0'
    
    """
    if a == '0' and b == '0' or a == '1' and b == '1':
        return '0'

    return '1'

# Summing two one bit values together
def SUM2(a, b):
    if AND(a, b) == '1':
        return '10'
    if XOR(a, b) == '1':
        return '01'
    return '00'

# Summing three one bit values together
def SUM(a, b, c = 0):
    ab = SUM2(a, b)

    if ab == '00' and c == '1':
        return '01'
    if ab == '01' and c == '1':
        return '10'
    if ab == '10' and c == '1':
        return '11'
    return ab

# Summing two any number of bit values together
def BINARYSUM(a, b):
    sum = bin(int(a, 2) + int(b, 2))[2:]
    return str(sum)

# Multiplying two any number of bit values together
def BINARYMULT(a, b):
    sum = bin(int(a, 2) * int(b, 2))[2:]
    # 
    return sum


###################### TESTS ######################
def test_and():
    assert AND('0','0') == '0'
    assert AND('0','1') == '0'
    assert AND('1','0') == '0'
    assert AND('1','1') == '1'

def test_or():
    assert OR('0','0') == '0'
    assert OR('0','1') == '1'
    assert OR('1','0') == '1'
    assert OR('1','1') == '1'     
    
def test_xor():
    assert XOR('0','0') == '0'
    assert XOR('0','1') == '1'
    assert XOR('1','0') == '1'
    assert XOR('1','1') == '0'

def test_plus2():
    assert PLUS2('0','0') == '00'
    assert PLUS2('0','1') == '01'
    assert PLUS2('1','0') == '01'
    assert PLUS2('1','1') == '11'

def test_plus():
    assert PLUS('0','0') == '00'
    assert PLUS('0','1') == '01'
    assert PLUS('1','0') == '01'
    assert PLUS('1','1') == '10'
    assert PLUS('0','0', '1') == '01'
    assert PLUS('0','1', '1') == '10'
    assert PLUS('1','0', '1') == '10'
    assert PLUS('1','1', '1') == '11'

def test_binarysum():
    assert BINARYSUM('000','0000') == '0'
    assert BINARYSUM('000','0001') == '0'
    assert BINARYSUM('001','0000') == '0'
    assert BINARYSUM('001','0001') == '1'

def test_binarymult():
    assert BINARYMULT('0000','000') == '0'
    assert BINARYMULT('0000','001') == '0'
    assert BINARYMULT('0001','000') == '0'
    assert BINARYMULT('0001','001') == '1'

def main():
    print (XOR('1', '1'))
    print (OR('0', '1'))
    print (AND('1', '1'))
    print (SUM2('1', '1'))
    print (SUM('1', '1', '1'))
    print (BINARYSUM('10110', '0011'))
    print (BINARYMULT('10110', '0011'))

if __name__== "__main__":
    main()