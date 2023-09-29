data = "ini adalah string"
print(type(data))

# cara membuat string

'''
    1. Menggunakan single quote ''
    2. Menggunakan double quote ""
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo Dunia"')
print("'Halo Dunia'")
print("Hari ini adalah juma'at")


#menggunakan tanda \
#membuat tanda ' menjadi string
print('mari sholat juam\'at')
print('g\'morn, don\'t forget it')

print("C:\\user\\aliffianIlham")

# tab
print("ucup\t\tmenang, lomba lari")

# backslash
print("ucup \brina, jadi ade kakak")

# new line
print("baris pertama.\nbaris kedua")# line feed (LF)
print("baris pertama.\rbaris kedua")# carriage return (CR)
print("baris pertama.\r\nbaris kedua") #  line feed carriage return (CRLF)

# string literal (RAW)
print("C:\\new folder") # akan kebanyakan dengan backslash

#menggunakan raw string
print(r"C:\new folder")

#multiline
print('''
Nama : Ucup
Kelas : 3 sd \new normal
web : https://website.html/page1.html
''')