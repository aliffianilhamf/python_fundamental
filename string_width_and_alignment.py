# string alignment & multiline
nama = 'alifian'
kelas = 10
tinggi = 165
berat = 55.6
# menggunakan \n atau newline
print('Nama : ' , nama ,' kelas : ', kelas, ' tinggi : ', tinggi,' berat : ', berat)
print(10*'='+'FORMAT STRING'+10*'=')
print('Nama : ' , nama ,'\nkelas : ', kelas, '\ntinggi : ', tinggi,'\nberat : ', berat)

# Menggunakan tanda kutip 3
print('\n'+10*'='+'FORMAT STRING'+10*'=')
print(f'''
nama : {nama}
kelas : {kelas}
tinggi : {tinggi}
berat : {berat}
      ''')

# Mengatur lebar
print('\n'+10*'='+'FORMAT STRING'+10*'=')
print(f'''
nama   : {nama:>10}
kelas  : {kelas:>10}
tinggi : {tinggi:>10}
berat  : {berat:>10}
      ''')