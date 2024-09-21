# Operator bitwise (masing - masing biner) operator untuk menangani kode binary

'''
    1. or (|)
    2. and (&)
    3. xor (^)
    4. not (~)
'''
a = 10
b = 5

# OR (|)
c = a | b
print(10*'=','OR',10*'=')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai : ', b, ', binary : ', format(b, '08b'))
print(20*'=','|')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# AND (&)
c = a & b
print(10*'=','AND',10*'=')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai : ', b, ', binary : ', format(b, '08b'))
print(20*'=','&')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# XOR (^)
c = a ^ b
print(10*'=','XOR',10*'=')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai : ', b, ', binary : ', format(b, '08b'))
print(20*'=','&')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# NOT (~)
c = ~a
print(10*'=','NOT',10*'=')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print(20*'=','~')
print('nilai : ', c, ', binary : ', format(c & 0xFF, '08b'))


# SHIFT RIGHT (>>)
c = a >> 2
print(10*'=','SHIFT RIGHT',10*'=')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print(20*'=','>>')
print('nilai : ', c, ', binary : ', format(c , '08b'))

# SHIFT LEFT (<<)
c = a << 2 
print(10*'=','SHIFT LEFT',10*'=')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print(20*'=','<<')
print('nilai : ', c, ', binary : ', format(c , '08b'))


