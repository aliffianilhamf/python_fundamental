daftar_angka = [1,2,3,4,5,4,3,2,1]

# for biasa
print(f'Menggunakan for biasa')
for i in daftar_angka:
    print(f'daftar angka : {i}')
    
# for loop & range
print(f'\nMenggunakan for range')
len_list = len(daftar_angka)
for i in range(len_list):
    print(f'daftar angka (range loop) : {i}')
    
# while loop
print(f'\nMenggunakan while loop')
i = 0
while i < len_list : 
    print(f'daftar angka (while) : {daftar_angka[i]}')
    i+=1
    
# list comprehension
print(f'\nMenggunakan list comprehension')
data = ['alip', 1,2,3, 'adiet', False]
[print(f'daftar angka (comprehension) : {i}') for i in data]

data_kuadarat = [i**2 for i in daftar_angka]
print(f'daftar kuadrat : {data_kuadarat}')

# list enumerate
print(f'\nMenggunakan enumerate')
for idx,data in enumerate(data):
    print(f'index : {idx}, data : {data}')

