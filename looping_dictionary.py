dict_mhs = {
    'alp' : 'alip',
    'ndn' : 'nando',
    'adt' : 'adit',
    'phn' : 'parhann'
}

# looping biasa (yang keluar adalah key nya)
for mhs in dict_mhs : 
    print(mhs)
    
    
# operator untuk mengambil item / iterables
keys = dict_mhs.keys()
print(f'keys : {keys}')

for key in dict_mhs.keys():
    print(dict_mhs.get(key))
    
values = dict_mhs.values()
print(values)

for value in dict_mhs.values():
    print(value)
    

items = dict_mhs.items()
print(items)

for item in dict_mhs.items():
    print(item)
    
for key, value in dict_mhs.items():
    print(f'key {key}, value {value}')