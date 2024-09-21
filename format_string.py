# format string

#string
data = 'aliffian'
format_str = f'hello {data}'
print(format_str)

# boolean
data = False
format_str = f'boolean = {data}'
print(format_str)

# angka
data = 2003.5
format_str = f'angka = {data}'
print(format_str)

# bilangan bulat 
data = 1234
format_str = f'bilangan bulat = {data}'
print(format_str)

# bilangan dengan ordo ribuan
data = 20000000
format_str = f'jutaan = {data:,}'
print(format_str)

# bilangan desimal
data = 2003.5678
format_str = f'desimal = {data:.2f}'
print(format_str)

# Menampilkan leading zero
data = 2003.5678
format_str = f'leading zero = {data:09.2f}'
print(format_str)

# menampilkan tanda - dan +
angka_minus = -5
angka_plus = 5.0090
format_minus = f'minus = {angka_minus:+d}'
print(format_minus)
format_plus = f'plus = {angka_plus:+.2f}'
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f'persen : {persentase : .2%}'
print(format_persen)

# melakukan operasi aritmatika dalam kurung kurawal
harga = 5000
qty = 5
jumlah = f'jumlah = {harga*qty : ,}'
print(jumlah)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_biner = f'bin = {bin(angka)}'
format_octal = f'oct = {oct(angka)}'
format_hexsa = f'hex = {hex(angka)}'

print(format_biner)
print(format_octal)
print(format_hexsa)