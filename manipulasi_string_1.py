# Operasi dan manipulasi string
# 1. concatenation (menggabungkan string)
nama_depan = 'Aliffian'
nama_belakang = 'ilham'
nama_lengkap = nama_depan +" "+ nama_belakang
print(nama_lengkap)

# 2. Menghitung Panjang string
length = len(nama_lengkap)
print(nama_lengkap + ' panjangnya ' + str(length) + ' karakter.')

# 3 Operator pada string
# in -> mengecek apakah ada karakter di suatu string
i = 'i'
status = i in nama_lengkap
print(i + " ada di "+ nama_lengkap + ' = ' + str(status))

L = 'L'
status = L in nama_lengkap
print(L + " ada di "+ nama_lengkap + ' = ' + str(status))

# not in
i = 'i'
status = i not in nama_lengkap
print(i + " tidak ada di "+ nama_lengkap + ' = ' + str(status))

L = 'L'
status = L not in nama_lengkap
print(L + " tidak ada di "+ nama_lengkap + ' = ' + str(status))


# mengulang string
print(10*'wk')
print(15*'=')

# Indexing
print('index ke-0 : ' + nama_lengkap[0])
print('index ke-5 : ' + nama_lengkap[5])
print('index ke-(-1) : ' + nama_lengkap[-1])
print('index ke-(-5) : ' + nama_lengkap[-5])
print('index ke-[0:3] : ' + nama_lengkap[0 : 4])
print('index ke-[0,2,4,6,8,10] : ' + nama_lengkap[0 : 11 : 2])

# item paling kecil (sesuai ascii)
print("item paling kecil di ascii : " + min(nama_lengkap))
# item paling besar
print("item paling besar di ascii : " + max(nama_lengkap))

# ASCII code
ascii_code = ord(" ")
print("ACII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("char untuk kode ASCII 117 adalah : "+ chr(data))

# Operator dalam bentuk method
data = 'aliffian ilham febriyana'
jumlah = data.count('a',1,13)
print('jumlah a dalam ' + data + ' = ' + str(jumlah))
