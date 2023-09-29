# Operasi dan manipulasi string

# menggabungkan string (concatenate)
firstName = "monkey"
midleName = "D"
lastName  = "luffy"

fullName = firstName + " "+ midleName +"'"+ lastName
print(fullName)

# menghitung panjang string
panjangString = len(fullName)
print("Panjang dari "+fullName +" = " + str(panjangString))

# cek apakah ada char dalam string
d = 'd'
status = d in fullName
print("karakter " + d +" ada di " + fullName +" "+ str(status))

D = 'D'
status = D in fullName
print("karakter " + D +" ada di " + fullName +" "+ str(status))

d = 'd'
status = d not in fullName
print("karakter " + d +" ada di " + fullName +" "+ str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

#indexing
print("index ke-0"+" "+fullName[0])
print("index ke-6"+" "+fullName[6])
print("index ke-(-1)"+" "+fullName[-1])
print("index ke-(-4)"+" "+fullName[-4])
print("index ke-[0,6]"+" "+fullName[0:7]) # : artinya sampai
print("index ke-[5,9]"+" "+fullName[5:10]) # : artinya sampai
print("index ke-[0,2,4,6,8,10]"+" "+fullName[0:11:2]) # : artinya sampai

#item paling kecil
print("Paling kecil :" + min(fullName))
#item paling besar
print("paling Besar : " + max(fullName))

asciiCode = ord(" ")
print("ASCII code untuk spasi adalah : " + str(asciiCode))
karakter = 120
print("char 120 pada ASCII adalah : " + chr(karakter))


#operator dalam bentuk method
data = "bernard subandi"
jumlah = data.count("a")
print("jumlah a pada "+ data + " adalah " + str(jumlah))
