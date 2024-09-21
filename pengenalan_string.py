data_string = "semarang panas"
print(data_string, ', Tipe nya : ', type(data_string))

# MEMBUAT STRING
'''
    1. Bisa menggunakan petik satu '....' (single quote)
    2. Bisa menggunakan petik dua "...." (double quote)
'''

contoh_single_quote = 'Menggunakan single quote'
print(contoh_single_quote)
contoh_double_quote = 'Menggunakan double quote'
print(contoh_double_quote)

# misal untuk percakapan yang butuh double quote, berarti kita menggunakan single quote 
data_string = '"halo, selamat pagi"'
print(data_string)
# Misal untuk tanda petik satu, berarti kira menggunakan double quote
data_string = "hari ini jum'at"
print(data_string)

#selain itu kita juga bisa menggunakan tanda backslahs
data_string = 'hari ini jum\'at'
print(data_string)

# MENGGUNAKAN TANDA BACKSLASH (\)
# untuk backslash sendiri
data_string = 'C:\\kuliah\\minggu1'
print(data_string)

# tab
data_string = 'satu, dua, tab, \ttiga, empat'
print(data_string)

# backspace
data_string = 'satu, dua, hapus, \btiga, empat'
print(data_string)

# newline
print('baris pertama.\nbaris kedua') #LF -> LINE FEED -> UNIX
print('baris pertama.\rbaris kedua') # CR -> CARRIAGE RETURN ->
print('baris pertama.\r\nbaris kedua') #CRLF -> LINE FEED CARRIAGE RETURN -> WINDOWS


# string literal atau raw

print('C:\new folder') # akan salah pathnya

# bisa menggunakan raw string
print(r'C:\new folder')

# multiline string literal
print('''
      Nama : edo
      alamat : semarang
      ''')

# multiline string literal + raw string
print(r'''
      nama : eki' kurniawan
      kelas : 3 esde
      web : www.eki.kurni.com/articles
      ''')