# Operator Komparasi menghasilkan true dan false
a = 4
b = 2
# lebih dari (>)
print("=====lebih dari (>)======")
hasil = a > b
print(a , '>', b , '=', hasil)
hasil = b > a
print(b , '>', a , '=', hasil)
hasil = b > 2
print(b , '>', 2 , '=', hasil)

# kurang dari (>)
print("=====kurang dari (<)======")
hasil = a < b
print(a , '<', b , '=', hasil)
hasil = b < a
print(b , '<', a , '=', hasil)
hasil = b < 2
print(b , '<', 2 , '=', hasil)

# lebih dari sama dengan (>.)
print("=====lebih dari sama dengan(>=)======")
hasil = a >= b
print(a , '>=', b , '=', hasil)
hasil = b >= a
print(b , '>=', a , '=', hasil)
hasil = b >= 2
print(b , '>=', 2 , '=', hasil)

# kurang dari sama dengan (>.)
print("=====kurang dari sama dengan(<=)======")
hasil = a <= b
print(a , '<=', b , '=', hasil)
hasil = b <= a
print(b , '<=', a , '=', hasil)
hasil = b <= 2
print(b , '<=', 2 , '=', hasil)

# sama dengan (==)
print("===== sama dengan(==)======")
hasil = a == b
print(a , '==', b , '=', hasil)
hasil = b == 2
print(b , '==', 2 , '=', hasil)

# tidak sama dengan (!=)
print("===== tidak sama dengan(!=)======")
hasil = a != b
print(a , '!=', b , '=', hasil)
hasil = b != 2
print(b , '!=', 2 , '=', hasil)

# operator "is" untuk komparasi object identity
print("===== object identity(is)======")
x = 5
y = 5

hasil = x is y
print(x , 'is', y, '=', hasil)

x = 5
y = 7
hasil = x is y
print(x , 'is', y, '=', hasil)

print("===== object identity(is not)======")
x = 5
y = 5

hasil = x is not y
print(x , 'is', y, '=', hasil)

x = 5
y = 7
hasil = x is not y
print(x , 'is', y, '=', hasil)