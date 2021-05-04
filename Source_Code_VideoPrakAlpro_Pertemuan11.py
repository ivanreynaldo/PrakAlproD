'''
Nama : Ivan Reynaldo
NIM  : 71200589
Grup : D
Universitas Kristen Duta Wacana

Pak Dodoy merupakan seorang kuli yang bekerja pada sebuah proyek borongan. Pak Dodoy di gaji setiap hari
sampai proyek tersebut selesai. Gaji tersebut tidak menentu setiap harinya, karena mereka di gaji berdasarkan 
seberapa keras mereka bekerja. Pak dodoy ingin menghitung jumlah penerimaannya selama seminggu dan ingin
menghitung jumlah rata-ratanya, namun karena Pak Dodoy selalu bolos kelas matematika sewaktu sekolah, Ia
tidak bisa menghitung. Pak Dodoy meminta bantuan anda, bantulah Pak Dodoy!

Referensi : Soal UG 11

Input : diberikan tuple yang berisi nama-nama hari, lalu meminta input dari user berupa jumlah uang yang
        diterima setiap harinya
Proses : Membuat perulangan yang dapat menerima input nominal uang setiap harinya, dan nama harinya 
         diambil dari tuple yang ada. lalu semua inputan di jumlahkan dan di cari rata-ratanya
Output : Menampilkan perulangan yang nama hari nya sesuai dgn tuple dan menampilkan total jumlah penerimaan
         selama seminggu dan rata-ratanya.'''

def hitungpenerimaan (hari):
    indeks = 0
    total = 0
    batas = len(hari)
    while indeks < batas :
        print('Masukkan jumlah penerimaan anda pada hari', hari[indeks],end='')
        penerimaan = int(input(': Rp. '))
        total += penerimaan
        indeks += 1
    rata2 = total / batas
    print('Total penerimaan anda selama minggu ini adalah : Rp.', total)
    print('Rata-rata penerimaan anda adalah : Rp.', round(rata2,2))

hari = ('Senin','Selasa','Rabu','Kamis')
hitungpenerimaan(hari)