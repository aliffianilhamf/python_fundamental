# Pass by reference
a = ['alip', 'ilham', 'febri']
print(f'a : {a}')

b = a
print(f'b : {b}')

# misal datanya kita ubah
print(30*'=')
a[0] = 'jawil'
b.sort()
print(f'a : {a}')
print(f'b : {b}')

# Operasi ini tidak akan berubah, karena ini pass by reference
# yang di copy adalah addressnya, jadi kedua list memiliki address yang sama
print(f'Address dari a : {hex(id(a))}')
print(f'Address dari b : {hex(id(b))}')

# Jika kita benar ingin membuat copy list namun addressnya beda

print('c adalah list dari copy() a ')
c = a.copy()
print(f'c : {c}')

print(f'Address dari a : {hex(id(a))}')
print(f'Address dari b : {hex(id(b))}')
print(f'Address dari c : {hex(id(c))}')



# jadi misal kita ubah data C, data A tidak akan berubah
c[1] = 'parhan'
print(f'data c index 1 diubah')
print(f'a : {a}')
print(f'b : {b}')
print(f'c : {c}')

b[0] = 'surya'
print(f'data b index 0 dirubah')
print(f'a : {a}')
print(f'b : {b}')
print(f'c : {c}')

