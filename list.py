 # LIST
 
 # list of numbers
list_num = [1,2,3,4,5,6]
print(list_num)

# list of string
list_str = ['alip', 'ilham', 'nando']
print(list_str)

# List of boolearn
list_bool = [False, True, False, True]
print(list_bool)

# List campuran
list_campur = ['alip', 21, True]
print(list_campur)

## Cara alternatif membuat list
### range
data_range = range(0, 10, 2) # (start, stop, step)
print(data_range)

list_dengan_range = list(data_range)
print(list_dengan_range)

### for i
list_dengan_for = [i for i in range(0,10)]
print(list_dengan_for)

### for if
list_dengan_for = [i for i in range(0,10) if i != 5]
print(list_dengan_for)

list_dengan_for = [i for i in range(0,10) if i % 2 == 0]
print(list_dengan_for)
list_dengan_for = [i for i in range(0,10) if i % 2 != 0]
print(list_dengan_for)