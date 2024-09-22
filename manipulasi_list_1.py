data_1 =['alip', 'ilham', 'febri']

## Memanggil item pada list
item_0 = data_1[0]
print(f'item pada indek ke 0 adalah : {item_0}')
item_terakhir = data_1[-1]
print(f'item pada indek ke -1 adalah : {item_terakhir}')

##  Mengambil info panjang suatu list
panjang_list = len(data_1)
print(f'Banyaknya data pada list {data_1}, adalah {panjang_list}')

## Menambah item pada posisi tertentu
data_1.insert(1, 'parhan')
print(f'Data list setelah method insert() {data_1}')

## Menambah item pada akhir item list
data_1.append('jawil')
print(f'Data list setelah method append() {data_1}')

## Menambah list dengan list (menggabungkan list)
data_2 = ['deta', 'maryo', 'awann']
data_1.extend(data_2)
print(f'Data list setelah data_1 dan data_2 digabung {data_1}')

## Merubah item list
data_1[2] = 'luki'
print(f'Data list setelah index 2 dirubah {data_1}')


## Menghapus item pada list
# nama harus sesuai
# jika tidak ada, akan error
data_1.remove('parhan')
print(f'Data list setelah parhan di remove() {data_1}')


## Menghapus item list yang paling akhir
data_1.pop()
print(f'Data list setelah di pop() {data_1}')