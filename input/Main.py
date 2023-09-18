#input user

#data yang di masukkan pasti string
data = input("Masukkan data : ")

print("data ", data, "Bertipe data ", type(data))

# jika ingin mengambil angka, harus di casting dulu
data_int = int(input("Masukkan angka : "))
data_float = float(input("Masukkan angka : "))

print("data ", data_int, "Bertipe data ", type(data_int))
print("data ", data_float, "Bertipe data ", type(data_float))

#data boolean
data_bool = bool(input("Masukkan nilai boolean : "))

print("data ", data_bool, "Bertipe data ", type(data_bool))

