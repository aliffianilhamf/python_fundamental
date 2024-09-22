# Kalkulator Sederhana
print(10*'='+'KALKULATOR SEDERHANA'+10*'=')
input_1 = float(input("Masukkan Angka Pertama \t\t: "))
opr = input("Pilih operator (+, -, *, /) \t: ")
input_2 = float(input("Masukkan Angka Kedua \t\t: "))

hasil = 0
if opr == '+' : 
    hasil = input_1 + input_2
elif opr == '-'  : 
    hasil = input_1 - input_2
elif opr == '*' or opr == 'x' : 
    hasil = input_1 * input_2
elif opr == '/' : 
    hasil = input_1 / input_2
else : 
    print('Masukkan input yang benarr lah')
    
print(f'Hasilnya adalah : {hasil}')
hasil = 0
print('Terima kasih.')