import datetime as dt

mhs_1 = {
    'nama' : 'alip ganteng',
    'nim' : 'A1120221234',
    'sks_lulus' : 144,
    'beasiswa' : True,
    'lahir' : dt.datetime(2003,2,1)
}
mhs_2 = {
    'nama' : 'Parhan GG',
    'nim' : 'A1120221235',
    'sks_lulus' : 140,
    'beasiswa' : False,
    'lahir' : dt.datetime(2003,5,2)
}
mhs_3 = {
    'nama' : 'jawil jangkung',
    'nim' : 'A1120221236',
    'sks_lulus' : 142,
    'beasiswa' : True,
    'lahir' : dt.datetime(2001,1,1)
}

daftar_mhs = {
    'MHS001' : mhs_1,
    'MHS002' : mhs_2,
    'MHS003' : mhs_3
}

# print(f'Daftar MHS : {daftar_mhs}')
print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<13} {'SKS':<3} {'BEASISWA':<8} {'LAHIR':<8}")
print(60*'=')

for mhs in daftar_mhs : 
    # print(daftar_mhs[mhs]['nama'])
    # Huruf kapital untuk konstanta
    KEY = mhs
    NAMA = daftar_mhs[mhs]['nama']
    NIM = daftar_mhs[mhs]['nim']
    SKS = daftar_mhs[mhs]['sks_lulus']
    BEASISWA = daftar_mhs[mhs]['beasiswa']
    LAHIR = daftar_mhs[mhs]['lahir'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17} {NIM:<13} {SKS:<3} {BEASISWA:^8} {LAHIR:<8}")