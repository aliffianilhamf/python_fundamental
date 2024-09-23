import datetime as dt
import os


# template dict mahasiswa
mhs_template = {
    'nama' : 'jawil jangkung',
    'nim' : 'A1120221236',
    'sks_lulus' : 142,
    'beasiswa' : True,
    'lahir' : dt.datetime(2001,1,1)
}

os.system("cls")
data_mhs = {}
mahasiswa = dict.fromkeys(mhs_template.keys())
print(10*'=' + 'SELAMAT DATANG'+ 10*'=')
mahasiswa['nama'] = input("Masukkan Nama mhs : ")
mahasiswa['nim'] = input("Masukkan NIM mhs : ")
mahasiswa['sks_lulus'] = int(input("Masukkan SKS mhs : "))
mahasiswa['beasiswa'] = bool(input('Masukkan beasiswa mhs (True / False) : '))
TAHUN_LAHIR = int(input("Masukkan tahun lahir (YYYY) : "))
BULAN_LAHIR = int(input("Masukkan bulan lahir (1-12) : "))
TANGGAL_LAHIR = int(input("Masukkan tanggal lahir (1-31) : "))
mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print(mahasiswa)