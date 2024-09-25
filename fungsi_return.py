## fungsi dengan return 
def kuadrat(angka, kuadrat): 
    hasil = angka ** kuadrat

    return hasil

hasil_kuadrat = kuadrat(2,6)
print(hasil_kuadrat)

## fungsi jika memiliki return banyak

def operasi_aritmatika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    bagi  = angka_1 / angka_2
    kali = angka_1 * angka_2
    kurang = angka_1 - angka_2
    
    return tambah, bagi, kali, kurang
    
ta,ba,ka,ku = operasi_aritmatika(10 , 5)
print(f'Hasil tambah = {ta}')
print(f'Hasil bagi = {ba}')
print(f'Hasil kali = {ka}')
print(f'Hasil kurang = {ku}')