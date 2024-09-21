import datetime as dt

print('Silahkan masukkan tanggl, \nbulan, dan tahun lahir anda\n')

tanggal = int(input("Tanggal \t: "))
bulan= int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("Tanggal lahir anda : ", tanggal_lahir)

# mencari tanggal hari ini untuk di hitung agar bisa menentukan umur
hari_ini = dt.date.today()
print(f'Hari ini tanggal : {hari_ini}')
umur_dalam_hari = hari_ini - tanggal_lahir
umur_dalam_tahun = umur_dalam_hari.days// 365
umur_dalam_bulan = (umur_dalam_hari.days % 365) // 30
print(f'Umur anda adalah : {umur_dalam_tahun} Tahun, {umur_dalam_bulan} Bulan')