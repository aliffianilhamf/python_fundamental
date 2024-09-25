# Program menghitung luas dan keliling lingkaran

# print(f"{'PROGRAM MENGHITUNG':^40}")
# print(f"{'LUAS DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{40*'=':^40}")

# panjang = int(input("Masukkan Panjang = "))
# lebar = int(input("Masukkan Lebar = "))

# LUAS = panjang * lebar
# KELILING = 2 * (panjang + lebar)

# print(f"Hasil Luasnya = {LUAS}")
# print(f"Hasil Kelilingnya = {KELILING}")

## coba dengan fungsi 
def header():
    '''Fungsi Header Program'''
    print(f"{'PROGRAM MENGHITUNG':^40}")
    print(f"{'LUAS DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{40*'=':^40}")

def input_user() : 
    '''Fungsi Input dari User'''
    panjang = int(input("Masukkan Panjang = "))
    lebar = int(input("Masukkan Lebar = "))
    
    return panjang, lebar
    
def hitung_luas(panjang, lebar):
    '''Fungsi hitung luas persegi panjang'''
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    '''Fungsi hitung keliling persegi panjang'''
    return 2 * (panjang + lebar)

def display(message, value) :
    print(f"Hasil hitung {message} = {value}")

while True : 
    
    header()
    PANJANG,LEBAR =input_user()
    
    LUAS = hitung_luas(PANJANG, LEBAR)
    KELILING = hitung_keliling(PANJANG, LEBAR)
    
    display("Luas", LUAS)
    display("Keliling", KELILING)
    
    is_lanjut = input("Apakah anda ingin lanjut (y/n)?")
    if is_lanjut == 'n' : 
        break