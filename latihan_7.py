import datetime as dt
import os
import random
import string
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


while True : 
    print(10*'=' + 'SELAMAT DATANG'+ 10*'=')
    mahasiswa = dict.fromkeys(mhs_template.keys())
    mahasiswa['nama'] = input("Masukkan Nama mhs : ")
    mahasiswa['nim'] = input("Masukkan NIM mhs : ")
    mahasiswa['sks_lulus'] = int(input("Masukkan SKS mhs : "))
    mahasiswa['beasiswa'] = bool(input('Masukkan beasiswa mhs (True / False) : '))
    TAHUN_LAHIR = int(input("Masukkan tahun lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Masukkan bulan lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Masukkan tanggal lahir (1-31) : "))
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mhs.update({KEY : mahasiswa})
    
    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<13} {'SKS':<3} {'BEASISWA':<8} {'LAHIR':<8}")
    print(60*'=')
    for key in data_mhs:
        KEY = key
        NAMA = data_mhs[key]['nama']
        NIM = data_mhs[key]['nim']
        SKS = data_mhs[key]['sks_lulus']
        BEASISWA = data_mhs[key]['beasiswa']
        LAHIR = data_mhs[key]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<13} {SKS:<3} {BEASISWA:^8} {LAHIR:<8}")
    is_lanjut = input("Lanjut (y/n?")
    if is_lanjut == 'n' : 
        break

print("TERIMA KASIH")