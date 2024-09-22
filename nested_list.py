data_1 = [1,2,3]
data_2 = [4,5,6]

data_lengkap =[5,6,7,8,9,10]

print(f'data_1 : {data_1}')
print(f'data_2 : {data_2}')
print(f'data_lengkap : {data_lengkap}')

# nested list
nested_list_1 = [data_1,data_2]
print(f'nested_list_1 : {nested_list_1}')

nested_list_2 = [data_lengkap, data_1, 9,8, 'alip']
print(f'nested_list_2 : {nested_list_2}')

# Contoh Penggunaan 
mhs_1 =['alif', 21, 'cowo']
mhs_2 = ['nando', 20,'cowo']
mhs_3 = ['neneng', 19, 'cewe']

list_mhs = [mhs_1,mhs_2,mhs_3]
print(f'list mahasiswa : \n{list_mhs}')

for mhs in list_mhs : 
    print(f'nama : {mhs[0]}')
    print(f'umur : {mhs[1]}')
    print(f'jenis kelamin : {2}\n')
    

# dengan reference
list_copy = list_mhs.copy()
print(f'mahasiswa copy : {list_copy}')
mhs_1[0] = 'awann'
print(f'mahasiswa copy setelah di ubah mhs_1 : {list_copy}')
print(f'list mahasiswa : \n{list_mhs}')





