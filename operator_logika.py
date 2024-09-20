# Operator Logika (untuk melakukan operasi logika)
'''
    1. not 
    2. or
    3. and
    4. xor
'''

# NOT
print('====== NOT')
a = True
b= not a
print('data a : ', a)
print('=========== not')
print('data b : ',b )

# or (Jika salah satu True, maka hasilnya True)
print("====== OR")
a = False
b = False
hasil = a or b
print(a, ' or ', b, ' = ', hasil)
a = False
b = True
hasil = a or b
print(a, ' or ', b, ' = ', hasil)
a = True
b = False
hasil = a or b
print(a, ' or ', b, ' = ', hasil)
a = True
b = True
hasil = a or b
print(a, ' or ', b, ' = ', hasil)

# and (Jika semua True, maka hasilnya True)
print("====== and")
a = False
b = False
hasil = a and b
print(a, ' and ', b, ' = ', hasil)
a = False
b = True
hasil = a and b
print(a, ' and ', b, ' = ', hasil)
a = True
b = False
hasil = a and b
print(a, ' and ', b, ' = ', hasil)
a = True
b = True
hasil = a and b
print(a, ' and ', b, ' = ', hasil)

# xor (Jika keduanya sama true/true, false,false, maka false)
print("====== xor")
a = False
b = False
hasil = a ^ b
print(a, ' xor ', b, ' = ', hasil)
a = False
b = True
hasil = a ^ b
print(a, ' xor ', b, ' = ', hasil)
a = True
b = False
hasil = a ^ b
print(a, ' xor ', b, ' = ', hasil)
a = True
b = True
hasil = a ^ b
print(a, ' xor ', b, ' = ', hasil)