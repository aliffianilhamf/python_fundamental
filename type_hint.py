## Type hint

def contoh_type_hint( angka : int) ->int : 
    '''CONTOH FUNGSI TYPE HINT'''
    hasil = angka + angka
    
    return hasil

hasil = contoh_type_hint(10)
print(hasil)
# hasil = contoh_type_hint(False)
# print(hasil) -> Akan Ambigu

## contoh lain

def say_hello(message:str):
    print(message)
    
say_hello("Haloo guys")
