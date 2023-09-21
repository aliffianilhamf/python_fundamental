# latihan 3
# ++++++ 3 -------- 10 ++++++++
inputUser = float(input("Masukkan angka kurang dari 3 atau\nlebih dari 10 : "))

# +++++++3---------
isKurangDari = inputUser < 3
print("Angka kurang dari 3 : ", isKurangDari)

# ----------- 10 ++++++++
isLebihDari = inputUser > 10
print("Angka lebih dari 10 : ",isLebihDari)

# ++++++ 3 -------- 10 ++++++++
isHasil = isLebihDari or isKurangDari
print("Angka yang anda masukkan :", isHasil)


# -------- 3 +++++++++ 10 ----------
inputUser = float(input("Masukkan angka lebih dari 3 dan\nkurang dari 10 : "))

# +++++++3---------
isLebihDari = inputUser > 3
print("Angka kurang dari 3 : ", isKurangDari)

# ----------- 10 ++++++++
isKurangDari = inputUser < 10
print("Angka lebih dari 10 : ",isLebihDari)

# ------ 3 ++++++ 10 -------
isHasil = isLebihDari and isKurangDari
print("Angka yang anda masukkan :", isHasil)


#-----0+++++5-------8++++++11-----
inputUser = float(input("Masukkan angka lebih dari 0 dan\nkurang dari 5\natau lebih dari 8 dan\nkurang dari 11 : "))

#-----0+++++
isLebihDari0 = inputUser > 0
print("Angka kurang dari 3 : ", isKurangDari)

# +++++5-----
isKurangDari5 = inputUser < 5
print("Angka lebih dari 10 : ",isLebihDari)

# -----8+++++
isLebihDari8 = inputUser > 8
print("Angka kurang dari 3 : ", isKurangDari)

# +++++11-----
isKurangDari11 = inputUser < 11
print("Angka lebih dari 10 : ",isLebihDari)

#-----0+++++5-------8++++++11-----
isHasil = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print("Angka yang anda masukkan : ", isHasil)