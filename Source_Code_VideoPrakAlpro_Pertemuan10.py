'''
Nama : Ivan Reynaldo
NIM  : 71200589
Grup : D
Universitas Kristen Duta Wacana

Ibu Lunox adalah seorang guru di SMA Burung Merpati. Ibu Lunox kewalahan ketika harus memeriksa semua pr 
siswanya, yang adalah menghitung Luas Persegi Panjang. Ibu Lunox meminta anda untuk membuatkan program 
yang dapat menghitung persegi panjang, Bantu lah ibu Lunox!

Referensi UG 10

Input : Membuat dictionary yang berisikan panjang dan lebar, yang nanti akan digunakan untuk perhitungan luas
Proses : Membuat fungsi yang akan menghitung luas persegi panjang dan mengembalikan luas tersebut
Output : Dapat menampilkan Luas Persegi panjang dengan sesuai
'''

def LuasPersegiPanjang(sisi):
    keys = []
    for key in sisi:
        keys += key
    Panjang1 = list(sisi[keys[0]])
    Lebar1 = list(sisi[keys[1]])
    #Mencari Luas
    luas = Panjang1[0] * Lebar1[0]
    print("Luas Persegi Panjang adalah ", end='')
    return luas

sisi = {'P':[20],'L':[15]}
print(LuasPersegiPanjang(sisi))