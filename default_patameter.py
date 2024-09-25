## contoh 1
def say_hai(nama='bayu'):
    print(f'haii {nama}')
    
say_hai('alip')
say_hai()

## contoh 2
def say_hello(nama, pesan='apa kabar ?') : 
    print(f'hello {nama} {pesan}')
    
say_hello('alip', 'lagi apa ?')
say_hello('bayu')
say_hello(pesan='kamu ngapain', nama='nando')
say_hello(nama='nando')

## contoh 3
# def tambah(angka_1 = 10, angka_2): -> tidak di rekomendasikan python ketika argument non default didahului argument default
#     return angka_1 + angka_2


## contoh 4

def sum_all(angka_1 = 4, angka_2 = 2, angka_3 = 4, angka_4 = 5):
    return angka_1 + angka_2 + angka_3 + angka_4


hasil = sum_all(angka_2=10)
print(hasil)
hasil = sum_all()