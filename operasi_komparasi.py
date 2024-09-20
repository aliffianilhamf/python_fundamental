# Operasi komparasi adalah membandingkan dua buah nilai dimana hanya mengembalikan nilai boolean

'''
    1. Lebih dari (>)
    2. Kurang dari (<)
    3. sama dengan (==)
    4. Lebih dari sama dengan (>=)
    5. Kurang dari sama dengan (<=)
    6. Tidak sama dengan (!=)
'''

a = 5
b = 3

# Lebih dari (>)
print('========lebih dari (>)')
lebih_dari = a > b
print(a ,' > ', b,' = ', lebih_dari)
lebih_dari = a > 6
print(a ,' > ', 6,' = ', lebih_dari)
lebih_dari = a > 5
print(a ,' > ', 5,' = ', lebih_dari)

# kurang dari (<)
print('========kurang dari (<)')
kurang_dari = a < b
print(a ,' < ', b,' = ', kurang_dari)
kurang_dari = a < 6
print(a ,' < ', 6,' = ', kurang_dari)
kurang_dari = a < 5
print(a ,' < ', 5,' = ', kurang_dari)

# sama dengan (==)
print('========sama dengan (==)')
sama_dengan = a == b
print(a ,' == ', b,' = ', sama_dengan)
sama_dengan = a == 6
print(a ,' == ', 6,' = ', sama_dengan)
sama_dengan = a == 5
print(a ,' == ', 5,' = ', sama_dengan)

# lebih dari sama dengan (>=)
print('========lebih dari sama dengan (>=)')
lebih_dari_sama_dengan = a >= b
print(a ,' >= ', b,' = ', lebih_dari_sama_dengan)
lebih_dari_sama_dengan = a >= 6
print(a ,' >= ', 6,' = ', lebih_dari_sama_dengan)
lebih_dari_sama_dengan = a >= 5
print(a ,' >= ', 5,' = ', lebih_dari_sama_dengan)

# kurang dari sama dengan (<=)
print('========kurang dari sama dengan (<=)')
kurang_dari_sama_dengan = a <= b
print(a ,' <= ', b,' = ', kurang_dari_sama_dengan)
kurang_dari_sama_dengan = a <= 6
print(a ,' <= ', 6,' = ', kurang_dari_sama_dengan)
kurang_dari_sama_dengan = a <= 5
print(a ,' <= ', 5,' = ', kurang_dari_sama_dengan)


# object identity (is)
print('========object identity (is)')
#hanya untuk komparasi object, tidak bisa literal
x = 7
y = 7
hasil = x is y
print(x, ' is ', y, ' = ',hasil)
#sebenarnya yang dibandingkan adalah kode dalam memorinya
print("nilai x : ", x , 'id : ',hex(id(x)) )
print("nilai y : ", y , 'id : ',hex(id(y)) )
z = 10
hasil = x is z
print(x, ' is ', z, ' = ',hasil)
# hasil = x is 7 #SyntaxWarning: "is" with a literal. Did you mean "=="?
# print(x, ' is ', 7, ' = ',hasil)

# object identity ( is not)
print('========object identity (is not)')
#hanya untuk komparasi object, tidak bisa literal
x = 7
y = 7
hasil = x is not y
print(x, ' is not ', y, ' = ',hasil)
#sebenarnya yang dibandingkan adalah kode dalam memorinya
print("nilai x : ", x , 'id : ',hex(id(x)) )
print("nilai y : ", y , 'id : ',hex(id(y)) )
z = 10
hasil = x is not z
print(x, ' is not ', z, ' = ',hasil)
# hasil = x is not 7 #SyntaxWarning: "is not" with a literal. Did you mean "=="?
# print(x, ' is not ', 7, ' = ',hasil)

