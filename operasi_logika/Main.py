# Operator logika atau boolean
'''
    NOT
    AND
    OR
    XOR
'''
# Not (kebalikan)
print("===== NOT =====")
a = False
b = not a
print('data a = ', a)
print('data b = ', b)

# AND (akan true bila keduanya true)
print("===== AND =====")
a = False
b = False
hasil = a and b
print(a,'AND',b,'=', hasil)
a = False
b = True
hasil = a and b
print(a,'AND',b,'=', hasil)
a = True
b = False
hasil = a and b
print(a,'AND',b,'=', hasil)
a = True
b = True
hasil = a and b
print(a,'AND',b,'=', hasil)

# OR ( akan false jika keduanya false)
print("===== or =====")
a = False
b = False
hasil = a or b
print(a,'or',b,'=', hasil)
a = False
b = True
hasil = a or b
print(a,'or',b,'=', hasil)
a = True
b = False
hasil = a or b
print(a,'or',b,'=', hasil)
a = True
b = True
hasil = a or b
print(a,'or',b,'=', hasil)

# xor (akan false jika keduanya true, false)
print("===== xor =====")
a = False
b = False
hasil = a ^ b
print(a,'xor',b,'=', hasil)
a = False
b = True
hasil = a ^ b
print(a,'xor',b,'=', hasil)
a = True
b = False
hasil = a ^ b
print(a,'xor',b,'=', hasil)
a = True
b = True
hasil = a ^ b
print(a,'xor',b,'=', hasil)