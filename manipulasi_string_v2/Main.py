# operator dalam bentuk method

## merubah case dari string

# merubah semua huruf ke uppercase
salam = "slur!"
print("normal = " + salam)
salam = salam.upper()
print("Upper = " + salam)

# merubah semua huruf ke lower case
alay = "Kamu kece sekelaieeZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = "+ alay)


#pengecekan dengan isX method

#contoh pengecekan lowercase
gunung = "bromo"
is_lower = gunung.islower()# hasilnya bool
print(gunung + " is lower = "+str(is_lower))
is_upper = gunung.isupper() # hasilnya bool
print(gunung + " is upper = "+str(is_upper))

# isalpha() -> semuanya huruf dan ga kosong
# isalnum() -> huruf dan angka
# isdecimal() -> angka
# isspace() -> spasi,tab,newline
# istitle() -> semua kata dimulai huruf besar

film = "The Imitation Game"
is_alpha = film.isalpha()
print("isalpha ? = "+ str(is_alpha))
is_alnum = film.isalnum()
print("isalpha ? = "+ str(is_alpha))
is_decimal = film.isdecimal()
print("isalpha ? = "+ str(is_decimal))
is_space = film.isspace()
print("isalpha ? = "+ str(is_space))
is_title = film.istitle

## cek komponen startswith(), endswith()
start = "ichiro oda".startswith("ichiro")
print("start = " + str(start))

end = "ichiro oda".endswith("oda")
print("end = " + str(end))

# penggabungan komponen join(), split()
data = ['aku', 'tresno', 'koe']
print(data)
gabung = ','.join(data)
print(gabung)

gabung = ' '.join(data) 
print(gabung)

gabung = ' kiw '.join(data)
print(gabung)

gabung = 'akukiwetresnokiwkoe'
print(gabung.split('kiw'))

#alokasi karakter rjust(), ljust(), center()
kanan = 'kanan'.rjust(10)
print("'" + kanan + "'")

kiri = 'kiri'.ljust(10)
print("'" + kiri + "'")

tengah = 'tengah'.center(10, "=")
print("'" + tengah + "'")

# kebalikannnya strip() 
tengah = tengah.strip("=") #-> menghilangkan tanda =
print(tengah)