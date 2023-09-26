# operator bitwise, operasi biner
a = 8
b = 4

# bitwise OR (|)
c = a | b
print("\n=====OR=====")
print('nilai : ',a, 'binary : ',format(a,'08b'))
print('nilai : ',b, 'binary : ',format(b,'08b'))
print("-----------------------(|)")
print('nilai : ',c, 'binary : ',format(c,'08b'))
# bitwise AND(&)
c = a & b
print("\n=====AND=====")
print('nilai : ',a, 'binary : ',format(a,'08b'))
print('nilai : ',b, 'binary : ',format(b,'08b'))
print("-----------------------(&)")
print('nilai : ',c, 'binary : ',format(c,'08b'))
# bitwise XOR(^)
c = a ^ b
print("\n=====XOR=====")
print('nilai : ',a, 'binary : ',format(a,'08b'))
print('nilai : ',b, 'binary : ',format(b,'08b'))
print("-----------------------(^)")
print('nilai : ',c, 'binary : ',format(c,'08b'))
c = ~b
#bitwise NOT(~)
print("\n=====XOR=====")
print('nilai : ',a, 'binary : ',format(a,'08b'))
print('nilai : ',b, 'binary : ',format(b,'08b'))
print("-----------------------(^)")
print('nilai : ',c, 'binary : ',format(c & 0xFF,'08b'))
