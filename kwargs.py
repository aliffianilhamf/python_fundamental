# **kwargs

# fungsi biasa
def data(nama, tinggi, berat):
    print(f'Halo {nama} dengan tinggi {tinggi} dan berat {berat}')
    
data('alip', 165, 56)

# # jika menggunakan kwargs
## error
# def data(**kwargs) : 
#     print(kwargs)

# data('alip', 165, 56)

# # jika menggunakan kwargs
## kwargs menghasilkan dictionary
def data(**kwargs) : 
    print(kwargs)

data(nama='alip', tinggi=165, berat=56)

## jadi misal kita gunakan 
def data(**data):
    nama = data['nama']
    tinggi = data['tinggi']
    berat = data['berat']
    
    print(f'Halo {nama} dengan tinggi {tinggi} dan berat {berat}')
    
data(nama='awann', tinggi=185, berat=76)
    










