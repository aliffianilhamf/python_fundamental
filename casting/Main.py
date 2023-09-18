#casting = konversi tipe data

#integer
data_int = 10
print("data ", data_int, "Bertipe data ", type(data_int))

#konversi ke float
data_float = float(data_int)
#konversi ke string
data_string = str(data_int)
#konversi ke bool
data_bool = bool(data_int) #akan false jika nilai int = 0

print("data ", data_float, "Bertipe data ", type(data_float))
print("data ", data_string, "Bertipe data ", type(data_string))
print("data ", data_bool, "Bertipe data ", type(data_bool))

print("====================Float=====================")
#float
data_float1 = 3.14
print("data ", data_float, "Bertipe data ", type(data_float))

#konversi ke int
data_int1= int(data_float1)
#konversi ke string
data_string1 = str(data_float1)
#konversi ke bool
data_bool1 = bool(data_float1)

print("data ", data_int1, "Bertipe data ", type(data_int1))
print("data ", data_string1, "Bertipe data ", type(data_string1))
print("data ", data_bool1, "Bertipe data ", type(data_bool1))

print("=====================Bool====================")
#boolean
data_bool2 = False
print("data ", data_bool2, "Bertipe data ", type(data_bool2))

#konversi ke int
data_int2= int(data_bool2)
#konversi ke string
data_string2= str(data_bool2)
#konversi ke float
data_float2= float(data_bool2)

print("data ", data_int2, "Bertipe data ", type(data_int2))
print("data ", data_string2, "Bertipe data ", type(data_string2))
print("data ", data_float2, "Bertipe data ", type(data_float2))

print("=====================String====================")
#boolean
data_string3 = "10"
print("data ", data_string3, "Bertipe data ", type(data_string3))

#konversi ke int
data_int3= int(data_string3) #string harus angka
#konversi ke bool
data_bool3= bool(data_string3)#flase jika string kosong
#konversi ke float
data_float3= float(data_string3)#sring harus angka

print("data ", data_int3, "Bertipe data ", type(data_int3))
print("data ", data_bool3, "Bertipe data ", type(data_bool3))
print("data ", data_float3, "Bertipe data ", type(data_float3))