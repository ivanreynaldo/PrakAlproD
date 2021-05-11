'''
Nama : Ivan Reynaldo
NIM  : 71200589
Grup : D
Universitas Kristen Duta Wacana

Bill Gerbang sangat suka mengecek dalam sebuah kalimat apakah ada semua huruf vokal atau tidak.
Namun ia tidak bisa membuat program seperti itu, sebagai teman sejati sehati dari Bill, bantu
Bill Gerbang dalam membuat program yang dapat mengecek dalam sebuah kalimat, apakah ada huruf 
atau tidak!

Referensi : Soal UG 12

Input : Meminta inputan berupa kalimat yang akan dicek, apakah ada huruf vokal atau tidak.

Proses : Membuat fungsi yang dapat mengecek apakah dalam kalimat yang di Inputkan user, berisi
         semua huruf vokal atau tidak.

Output : Menampilkan Output berupa penegasan, apakah kalimat yang di Inputkan berisi semua huruf
         vokal atau tidak. '''

def cekhurufvokal(data):
    huruf_vokal = set('aiueo')
    salah = 0
    for huruf in huruf_vokal:
        if huruf in data:
            benar = 'Kalimat ini mempunyai semua huruf vokal'
        else:
            salah += 1
            salahh = 'Kalimat ini tidak mempunyai semua huruf vokal'
            break
    if salah > 0:
        return salahh
    else:
        return benar

kalimat = input('Masukkan Kalimat : ')
kalimat.lower()
print(cekhurufvokal(kalimat))