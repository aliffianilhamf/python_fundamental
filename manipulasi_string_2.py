# manipulasi string menggunakan method
# 1. Mengubah karakter case
data = 'nama saya nando'
print('text asli : ' + data)

## capitalize()
print('capitalize() : '+ data.capitalize())
## title()
print('title() : ' + data.title())
## upper()
print('upper() : ' + data.upper())
## lower()
print('lower() : ' + data.lower())
## swapcase()
print('swapcase() : ' + data.swapcase())

# 2. Pengecekan karakter _case_
## islower()
print(data + ' islower() ? : ' + str(data.islower()))
## isupper()
print(data + ' isupper() ? : ' + str(data.isupper()))
## istitle()
print(data + ' istitle() ? : ' + str(data.istitle()))

# 3. Pengecekan karakter _whitespace_
## isspace()
data2 = " "
print(data + ' isspace() ? : ' + str(data.isspace()))
print(data2 + ' isspace() ? : ' + str(data2.isspace()))

# 4.Pengecekan karakter alfabet dan angka
## isalpha()
print("abcdef.isalpha() "+str("abcdef".isalpha()))# output ➜ True, karena abcdef adalah alfabet

print("abc123.isalpha() "+str("abc123".isalpha()))# output ➜ False, karena ada karakter 123 yang bukan merupakan alfabet

## isdigit()
print("123456.isdigit() "+str("123456".isdigit()))# output ➜ True, karena 123456 adalah digit

print("123abc.isdigit() "+str("123abc".isdigit()))# output ➜ False, karena ada karakter abc yang bukan merupakan digit

## isdecimal()
print("123456.isdecimal() "+str("123456".isdecimal()))# output ➜ True, karena 123456 adalah angka desimal

print("123abc.isdecimal() "+str("123abc".isdecimal())) # output ➜ False, karena ada karakter abc yang bukan merupakan angka desimal

## isnumeric()
print("123456.isnumeric() "+str("123456".isnumeric())) # output ➜ True, karena 123456 adalah angka numerik

print("123abc.isnumeric() "+str("123abc".isnumeric()))# output ➜ False, karena ada karakter abc yang bukan merupakan numerik

## isalnum()
print("123abc.isalnum() "+str("123abc".isalnum()))# output ➜ True, karena 123 adalah digit dan abc adalah alfabet 

print("12345⅓.isalnum() "+str("12345⅓".isalnum()))# output ➜ True, karena 12345⅓ adalah digit

print("abcdef.isalnum() "+str("abcdef".isalnum()))# output ➜ True, karena abcdef adalah alfabet

print("abc 12.isalnum() "+str("abc 12".isalnum()))# output ➜ False, karena ada karakter spasi yang bukan merupakan karakter digit ataupun alfabet

# 5. Pengecekan substring
## startswith
data = 'aliffian ilham febriyana'
starts = 'aliffian'
print(data + ' diawali dengan ' + starts + ' ? : '+ str(data.startswith(starts)))

## endswith
ends = 'ilham'
print(data + ' diakkhiri dengan ' + ends + ' ? : '+ str(data.startswith(ends)))

# 6. Join string
pisah =  ['aku', 'sayang', 'kamu']
gabung = '-'.join(pisah)
print(gabung)

# 7. split string
gabung ='aku-sayang-kamu'
pisah = gabung.split('-')
print(pisah)

# 8. Alokasi karakter
## rjust()
kanan = "kanan".rjust(15)
print("'" + kanan + "'")

## ljust()
kiri = "kiri".ljust(15)
print("'" + kiri + "'")

## center()
center = "center".center(15,'=')
print("'" + center + "'")

# 9. Trim / Strip
#lstrip()
data = '''
    hello python
'''
print(f'====={data}=====')
print('hasil lstrip() : \n' + f'====={str(data.lstrip())}=====')

#rstrip()
data = '''
    hello python
'''
print(f'====={data}=====')
print('hasil rstrip() : \n' + f'====={str(data.rstrip())}=====')

#strip()
data =':::::hello python:::::'
print(f'====={data}=====')
print('hasil strip() : \n' + f'''====={data.strip(':')}=====''')