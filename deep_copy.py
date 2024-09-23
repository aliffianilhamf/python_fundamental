list_1 = [[1,2,3],[4,5,6],1]
print(f'list 1 : {list_1}')

# jika kita menggunaan copy()
list_1_copy = list_1.copy()
print(f'list 1 copy : {list_1_copy}')

## coba kita cek alamat memory
print(f'address dari list 1 : {hex(id(list_1))}')
print(f'address dari list 1 copy : {hex(id(list_1_copy))}')

## coba kita ganti datanya
# maka kedua list akan ikut berubah
list_1[0][0] = 5
print(f'list 1 setelah diubah: {list_1}')
print(f'list 1 copy : {list_1_copy}')

## misal kita tambah 1 data pada list berupa number
## dan kita ubah valuenya

list_1[2] = 88
print(f'list 1 setelah ditambah datanya : {list_1}')
print(f'list 1 copy : {list_1_copy}')
## terbukti jika data list menggunakan method copy, address nya akan sama dan data tidak dapat dirubah di salah satu list
## namun jika datanya bukan list, bisa menggunakan method copy()

# untuk menangani hal tsb, bisa menggunakan package deepcopy
from copy import deepcopy

list_1_deep_copy = deepcopy(list_1)
print(f'list 1 : {list_1}')
print(f'list 1 copy : {list_1_copy}')
print(f'list 1 deep copy : {list_1_deep_copy}')

# jika kita ubah datanya 
# data dari list_1 dan list_1_copy akan berubah, namun list_1_deep_copy tidak akan berubah
list_1[0][0] = 10
print(f'list 1 setelah diubah  : {list_1}')
print(f'list 1 copy : {list_1_copy}')
print(f'list 1 deep copy : {list_1_deep_copy}')

# kita lihat addressnya
print(f'address list_1 : {hex(id(list_1))}')
print(f'address list_1_copy : {hex(id(list_1_copy))}')
print(f'address list_1_deep_copy : {hex(id(list_1_deep_copy))}')















