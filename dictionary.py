# DICTIONARY
## misal kita menggunakan list biasa 
angka = [1,2,3,4]
print(f'angka {angka}')

## jika kita menggunakan dictionarry
contoh_dict = {
    'val_1' : 'alipp',
    'val_2' : 'nando',
    "val_3" :  False,
    'list' : angka,
    'dict_new' : {
        '1' : 'satu',
        '2' : 'dua'
    }
}

# untuk mengakses value nya kita perlu menggunakan key nya
print(f'Data dictionary {contoh_dict}')
print(f'memanggil data dalam dictionary {contoh_dict["val_1"]}')
print(f'memanggil data dalam dictionary {contoh_dict["list"]}')

