# +++++++3-------10+++++++

angka = float(input("Masukkan angka \nkurang dari tiga \natau lebih dari 10 : "))
print("angka yang anda masukkan : ", angka)

# +++++++++3-----------
is_kurang_dari_3 = angka < 3
print(angka," kurang dari 3 ? = ", is_kurang_dari_3)

#---------10++++++++++
is_lebih_dari_10 = angka > 10
print(angka," Lebih dari 10 ? = ", is_lebih_dari_10)

#++++++3-----10+++++
hasil =is_kurang_dari_3 or is_lebih_dari_10
print("Jawaban anda : ", hasil)

print('\n',10*'=','\n')
#-------3++++++10------
angka = float(input("Masukkan angka \nlebih dari tiga \ndan kurang dari 10 : "))
print("angka yang anda masukkan : ", angka)

# -------3+++++++
is_lebih_dari_3 = angka > 3
print(angka, " Lebih dari 3 ? = ", is_lebih_dari_3)

#++++++10-------
is_kurang_dari_10 = angka < 10
print(angka, " kurang dari 10 ? = ", is_kurang_dari_10)

# ------3++++++++10-------
hasil = is_lebih_dari_3 and is_kurang_dari_10
print("jawaban anda : ", hasil)



print('\n', 10*'=','LATIHAN SOAL 1',10*'=','\n')
# Latihan soal
# -----0+++++5-----8+++++11-----
angka = float(input("Masukkan angka \nlebih dari 0 \ndan kurang dari 5 \natau lebih dari 8 \ndan kurang dari 11 : "))
print("angka yang anda masukkan : ", angka)

#--------0++++++
is_lebih_dari_0 = angka > 0
print(angka, " lebih dari 0 ? = ", is_lebih_dari_0)

# +++++5-----
is_kurang_dari_5 = angka < 5
print(angka, " kurang dari 5 ? = ", is_kurang_dari_5)

# ------8+++++
is_lebih_dari_8 = angka > 8
print(angka, " lebih dari 8 ? = ", is_lebih_dari_8)

# +++++11------
is_kurang_dari_11 = angka < 11
print(angka, ' Kurang dari 11 ? = ', is_kurang_dari_11)

# -----0+++++5-----8+++++11-----
hasil = (is_lebih_dari_0 and is_kurang_dari_5) or (is_lebih_dari_8 and is_kurang_dari_11)
print("Jawaban anda adalah : ", hasil)

print('\n', 10*'=','LATIHAN SOAL 2',10*'=','\n')
#+++++0-----5+++++8-----11+++++
angka = float(input("Masukkan angka \nkurang dari 0 \natau lebih dari 5 dan kurang dari 8 \natau lebih dari 11 : "))
print("angka yang anda masukkan : ", angka)
# +++++0-----
is_kurang_dari_0 = angka < 0
print(angka, ' kurang dari 0 ? = ', is_kurang_dari_0)

# -----5+++++
is_lebih_dari_5 = angka > 5
print(angka, ' lebih dari 5 ? = ', is_lebih_dari_5)

# +++++8-----
is_kurang_dari_8 = angka < 8
print(angka, ' kurang dari 8 ? = ', is_kurang_dari_8)

# -----11++++
is_lebih_dari_11 = angka > 11
print(angka, ' lebih dari 11 ? = ', is_lebih_dari_11)

# +++++0-----5+++++8-----11+++++
hasil = is_kurang_dari_0 or (is_lebih_dari_5 and is_kurang_dari_8) or is_lebih_dari_11
print('Jawaban anda adalah : ', hasil)