# Casting adalah mengubah bentuk tipe data

# misal di python ada tipe data int, float,str, bool

#Integer
print("===== INTEGER =====")
contoh_int = 10
print("data : ", contoh_int, " tipenya : ", type(contoh_int))

contoh_float = float(contoh_int)
contoh_str = str(contoh_int)
contoh_bool = bool(contoh_int)
print("data : ", contoh_float, " tipenya : ", type(contoh_float))
print("data : ", contoh_str, " tipenya : ", type(contoh_str))
print("data : ", contoh_bool, " tipenya : ", type(contoh_bool))

#Float
print("===== FLOAT =====")
contoh_float = 10.9
print("data : ", contoh_float, " tipenya : ", type(contoh_float))

contoh_int = int(contoh_float)
contoh_str = str(contoh_float)
contoh_bool = bool(contoh_float)
print("data : ", contoh_int, " tipenya : ", type(contoh_int))
print("data : ", contoh_str, " tipenya : ", type(contoh_str))
print("data : ", contoh_bool, " tipenya : ", type(contoh_float))


#Bool
print("===== BOOLEAN =====")
contoh_bool = False
print("data : ", contoh_bool, " tipenya : ", type(contoh_bool))

contoh_int = int(contoh_bool)
contoh_str = str(contoh_bool)
contoh_float = bool(contoh_bool)
print("data : ", contoh_int, " tipenya : ", type(contoh_int))
print("data : ", contoh_str, " tipenya : ", type(contoh_str))
print("data : ", contoh_bool, " tipenya : ", type(contoh_float))


#String
print("===== String =====")
contoh_string = "False"
print("data : ", contoh_string, " tipenya : ", type(contoh_string))

contoh_int = int(contoh_string)# Harus Angka
contoh_bool = bool(contoh_string)
contoh_float = bool(contoh_string)# Harus Angka
print("data : ", contoh_int, " tipenya : ", type(contoh_int))
print("data : ", contoh_str, " tipenya : ", type(contoh_str))
print("data : ", contoh_string, " tipenya : ", type(contoh_float))
