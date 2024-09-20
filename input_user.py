#Mengambil data input dari user

data_input = input("Siapa Nama Anda? : ")

print("Nama Anda Adalah : ", data_input, "tipenya : ", type(data_input))


# Menereima inputan Integer harus di casting dulu ke integer
data_integer = int(input("Berapa Umur Anda? : "))
print("Umur Anda Adalah : ", data_integer, "tipenya : ", type(data_integer))

# Menereima inputan Float harus di casting dulu ke float
data_float = float(input("Berapa Berat Badan Anda? : "))
print("Berat Badan Anda Adalah : ", data_float, "tipenya : ", type(data_float))

# Menereima inputan boolean harus di casting dulu ke boolean
# akan mengembalikan true jika input diisi oleh user, dan akan mengembalikan false jika inputan kosong
data_bool = bool(input("Apakah anda sedang sakit? : "))
print("Anda Menjawab : ", data_bool, "tipenya : ", type(data_bool))

#jika ingin menerima inputan biner 1 = true, dan 0 = false maka kodenya adalah spt brikut
data_biner = bool(int(input("Apakah anda sakit? (1=ya, 0=tidak) : ")))
print("Anda Menjawab : ", data_biner, "tipenya : ", type(data_biner))