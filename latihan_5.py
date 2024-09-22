# Latihan Looping

# Pola 1
'''
    *
    **
    ***
    ****
    *****
'''

# # Menggunakan for
# for i in range(5) : 
#     print((i+1)*'*')
    
    
    
# # Menggunakan while
# baris = 10
# count = 1
# while True : 
#     if count % 2 : 
#         print(count*'*')
#         count += 1
#     else : 
#         count +=1
#         continue
    
#     if count == baris : 
#         break
    
'''
     *
     **
    ***
    ****
   *****
'''
baris = 13
kolom = int(baris/2)
count = 1
print(kolom)
while True : 
    if count % 2 :
        print((kolom)*' ',count*'+')
        kolom -= 1
        count +=1
    else : 
       
        count += 1
        continue

    if count > baris : 
        break
    
    
    
    
    
    