def fungsi(nama,tinggi,berat):
    print(f"{nama} memiliki tinggi badan {tinggi} dan berat badan {berat}")

fungsi("armin",170,50)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} memiliki tinggi badan {tinggi} dan berat badan {berat}")

fungsi(["min",100,120])

#*args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi badan {tinggi} dan berat badan {berat}")

fungsi("ar",170,80)


#kasus
def tambah(*args):
    output = 0
    for angka in args:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(27,22,77)
print(f"hasil = {hasil}")
