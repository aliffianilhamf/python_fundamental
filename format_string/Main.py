# format string

#string
str = "nenenk"
format_str = f"ini adalah {str}"
print(format_str)
#booelan 
boolean = False
format_str = f"ini adalah {boolean}"
print(format_str)

#angka
angka = 3.14
format_str = f"angka : {angka}"
print(format_str)

#decimal 
angka = 55
format_str = f"desimal {angka:d}"
print(format_str)

#ribuan
ribuan = 5000
format_str = f"ribuan : {ribuan:,}"
print(format_str)

# bilangan decimal
angka = 50.5004
format_str = f"desimal = {angka:.2f}"
print(format_str)

# leading zero
angka = 2003.0502
format_str = f"desimal {angka:09.2f}" # menambahkan o di depan, menambahkan menjadi 9 karakter, dan 2 angka di blkng koma
print(format_str)

# menampilkan tanda + dn -
minus = -6
plus = 8.12345
format_minus = f"minus {minus:+d}"
format_plus = f"plus {plus:+.2f}"
print(format_plus)
print(format_minus)

# persen
persen = 0.045
format_persen = f"persen : {persen:.2%}"
print(format_persen)

# operasi aritmatika
angka1 = 10000
angka2 = 10

format_hasil = f"hasilnya : {angka1 * angka2}"


# fromat biner, oktal, hexsa
angka = 50
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)