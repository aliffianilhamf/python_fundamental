#Operator aritmatika
a = 5
b = 2
# Operasi Penjumlahan
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi Pengurangan
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi Perkalian
hasil = a * b
print(a , '*' , b , '=' , hasil)

# operator Pembagian (Hasilnya bilangan desimal)
hasil = a / b
print(a , '/' , b , '=' , hasil)

# Operator eksponen (pangkat)
hasil = a ** b
print(a , '**' , b , '=' , hasil)

# Operator Floor division (hasil pembagian bilangan bulat)
hasil = a // b
print(a , '//' , b , '=' , hasil)

# prioritas operator
'''
    1 tanda kurung ()
    2 eksponen
    3 perkalian, pembagian, modulus, perkalian, floor division
    4 penjumlahan , pengurangan
'''
x = 2
y = 3
z = 4

hasil = x ** y + z / z % a // y
print(x, '**' ,y, '+', z, '/', z, '%', a, '//', y, '=', hasil)

hasil = (x + y) * z
print('(',x , '+', y,') *',z ,'=',hasil)