# date and time
import datetime as dt

print("silahkan masukkan tanggal, \nbulan dan tahun lahir anda")

tanggal = int(input("Tanggal : "))
bulan = int(input("bulan : "))
tahun = int(input("tahun : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Bertepatan pada hari {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")

umur_hari = hari_ini-tanggal_lahir
print(f"Umur anda adalah {umur_hari} tahun")

umur_tahun = umur_hari.days // 365
sisa_bulan = (umur_hari.days % 365) // 30
print(umur_hari.days % 365)
sisa_hari = (umur_hari.days % 365) % 30
print(f"Umur anda adalah {umur_tahun} tahun {sisa_bulan} bulan {sisa_hari} hari")