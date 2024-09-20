# Operator Aritmatika
'''
    1. Penjumlahan
    2. Pengurangan
    3. perkalian
    4. pembagian
    5. modulus
    6. eksponen / pangkat
    7. floor division
'''

a = 12
b = 5
# Penjumlahan 
hasil_penjumlahan = a + b
print(a, " + ", b, " = ", hasil_penjumlahan)

# Pengurangan
hasil_pengurangan = a - b
print(a, " - ", b, " = ", hasil_penjumlahan)

# perkalian
hasil_perkalian = a * b
print(a, " * ", b, " = ", hasil_perkalian)

# pembagian
hasil_pembagian = a / b
print(a, " / ", b, " = ", hasil_pembagian)

# Modulus
hasil_modulus = a % b
print(a, " % ", b, " = ", hasil_modulus)

# eksponen / pangkat
hasil_eksponen= a ** b
print(a, " ** ", b, " = ", hasil_eksponen)

# floor division 
hasil_floor_division= a // b
print(a, " // ", b, " = ", hasil_floor_division)


# Prioritas operasi
'''
    Urutan Prioritas
    1. () Tanda kurung
    2. Eksponen (**)
    3. Perkalian, pembagian, modulus, floor division (*,/,%,//)
'''
x = 1
y = 2
z = 3
hasil = x + y * z - y % x ** y
print(x,'+',y,'*',z,'-',y,'%',x,'**',y, ' = ', hasil) 

hasil_2 = (x + y) * z
print('(',x, '+', y,')', '*', z, ' = ', hasil_2)