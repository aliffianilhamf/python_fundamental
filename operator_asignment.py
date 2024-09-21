a = 10
print('Nilai a = ', a)

# Penjumalahan
# a = a + 2
a += 2
print('Nilai a += 2 = ', a)

# Pengurangan
# a = a - 2
a -= 2
print('Nilai a -= 2 = ', a)

# Pembagian
# a = a / 2
a /= 2
print('Nilai a /= 2 = ', a)

# Perkalian
# a = a * 2
a *= 2
print('Nilai a *= 2 = ', a)

# Eksponen pangkat
# a = a ** 2
a **= 2
print('Nilai a *= 2 = ', a)

# Floor Division
# a = a // 2
a //= 3
print('Nilai a *= 2 = ', a)


# BITWISE OPERATOR
# OR
a = False
a |= True
print('Nilai a |= True = ', a)

# AND
a = False
a &= True
print('Nilai a &= True = ', a)

# XOR
a = False
a ^= True
print('Nilai a ^= True = ', a)

# RIGHT SHIFT
print(10*'=')
a = 0b1010
print('Nilai a :', format(a, '04b'))
a >>= 2
print('Nilai a >>= 2 :', format(a, '04b'))

# LEFT SHIFT
print(10*'=')
a = 0b1010
print('Nilai a :', format(a, '04b'))
a <<= 2
print('Nilai a <<= 2 :', format(a, '04b'))