list_buku = []
while True : 
    judul = input('Masukkan Judul Buku : ')
    penulis = input('Masukkan Penulis Buku : ')
    
    buku = [judul, penulis]
    list_buku.append(buku)
    print(f'no. | judul buku | penulis')
    for idx, book in enumerate(list_buku) :
        print(f'{idx+1} | {book[0]} | {book[1]}')
        
    isLanjut = input('apakah anda ingin lanjut (y/n)? ')
    if isLanjut == 'n' : 
        break
    
print(f'PROGRAM SELESAI')
    