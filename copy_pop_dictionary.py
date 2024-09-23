mhs= {
    'alp' : 'alip',
    'prh' : 'parhan',
    'why' : 'wahyu',
    'ndn' : 'nando',
    'ilh' : 'ilham'
}

print(f'mhs : {mhs}')

# copy dctionary
new_mhs = mhs
print(f'copy mhs :{new_mhs}\n')
# coba datanya diganti
new_mhs['alp'] = 'aliffian'
print(f'mhs : {mhs}')
print(f'copy mhs :{new_mhs}\n')
# jika dengan cara diatas, maka akan sama perilakunya seperti list, akan merubah kedua list jika dirubah

# menggunakan method copy()
new_mhs_2 = mhs.copy()
new_mhs['alp'] = 'aliffian ilham'
print(f'mhs : {mhs}')
print(f'copy mhs :{new_mhs}')
print(f'copy mhs 2 :{new_mhs_2}\n')


# pop dictionary
dataAlip = mhs.pop('alp')
print(dataAlip)
print(f'mhs : {mhs}')
print(f'copy mhs :{new_mhs}')
print(f'copy mhs 2 :{new_mhs_2}\n')

# popitem dictionary (item terakhir)
item_terakhir = mhs.popitem()
print(item_terakhir)
print(f'mhs : {mhs}')
print(f'copy mhs :{new_mhs}')
print(f'copy mhs 2 :{new_mhs_2}\n')