# width and multiline

nama = "paparazi"
umur = 23
tinggi = 165.7
berat = 57.5

# string standard
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, berat = {berat}"
print("\n"+5*"=" + "data string" + 5*"=")
print(data_string)

# string new line (\n)
data_string = f"nama = {nama}, \numur = {umur}, \ntinggi = {tinggi}, \nberat = {berat}"
print("\n"+5*"=" + "data string" + 5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""
nama   = {nama:>5}
umur   = {umur:5}
tinggi = {tinggi:>5}
berat  = {berat:>5}
"""
print("\n"+5*"=" + "data string" + 5*"=")
print(data_string)
