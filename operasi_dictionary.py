list_dict = {
    'nama' : 'alip',
    'kelas' : 2,
    'asal' : 'purwodadi'
}

# panjang dictionary
len_dict = len(list_dict)
print(f'Dictionary : {list_dict}')
print(f'len dictionary : {len_dict}')

# Mengecek key exist atau tidak
key = 'nama'
check_key = key in list_dict
print(f'apakah key nama ada pada list dict ? {check_key}')

# mengakses value (read) dg get
## misal kita akses biasa
print(f"akses biasa {list_dict['nama']}")
## jika kita menggunakan get
print(f"akses get {list_dict.get('nama')}")
print(list_dict.get('umur', 'key tidak ditemukan'))

# Update data dictionary
list_dict['nama'] = 'nando'
print(f'data dict setelah di update : {list_dict}')
# jika key tidak ada pada dict
list_dict['umur'] = 21
print(list_dict)

## Menggunakan method update
list_dict.update({'nama': 'alya'})
print(f'data dict setelah di update() : {list_dict}')
list_dict.update({'hobi': 'makan'})
print(f'data dict setelah di update() : {list_dict}')