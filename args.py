# args

## fungsi biasa
def hasil(angka_1, angka_2, angka_3, angka_4):
    value = angka_1 + angka_2 + angka_3 + angka_4
    
    return value

hasil_tambah = hasil(1,2,3,4)
print(hasil_tambah)

## kita bisa atasi menggunakan args untuk parameter yang banyak itu
## args bentuknya tupple
def hasil_args(*args):
    nama = args[0]
    nim = args[1]
    umur = args[2]
    
    print(f'haii {nama} {nim} {umur}')
    
hasil_args('Aliffian', 'A1122222', 21)

def hasil_tambah(*data):
    output = 0
    for angka in data : 
        output+=angka
        
    return output

output = hasil_tambah(12,12,22,22,11,11,22,223,33)

print(f'hasil : {output}')