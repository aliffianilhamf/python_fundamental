data_angka = [1,24,3,53,54,3,32,1,45,4,2,3,2,5,656,7,23,23,3]
print(f'data angka : \n{data_angka}')
## count
data_3 = data_angka.count(3)
data_4 = data_angka.count(4)
print(f'data 3 jumlahnya : {data_3}')
print(f'data 4 jumlahnya : {data_4}')

## index() -. mengetahui data di index berapa
data_str = ['febri','alip', 'ilham',  'nando']
print(f'data str : \n{data_str}')
index_ilham = data_str.index('ilham')
print(f'ilham berada pada index : {index_ilham}')

## Mengurutkan list dengan sort()
data_angka.sort()
print(f'data angka setelah di sort() : \n {data_angka}')
data_str.sort()
print(f'data str setelah di sort() : \n {data_str}')

### membalikkan nilai list dari yang terbesar ke terkecil
## setelah di sort, terus di reverse()
data_angka.reverse()
data_str.reverse()
print(f'data angka setelah di sort() + reverse() : \n {data_angka}')
print(f'data str setelah di sort() + reverse() : \n {data_str}')