#Nama : Ivan Reynaldo
#NIM  : 71200589
#Grup : D
#Universitas Kristen Duta Wacana

'''Jess Limited Edition meminta bantuan saya(Ivan) untuk membuat program yang dapat
membantunya untuk mengatur pengeluaran bulanan berdasarkan penghasilannya dari adsense 
yutub. Setiap minggunya, Jess Limited Edition mendapat adsense yutub. Jess menghabiskan
40% dari uang adsensenya untuk membeli makanan, 10% untuk beli kaos, 30% untuk
membeli diamon mobel lejen, dan 20% sisanya disimpannya untuk ditabung biar bisa rakit pc.
Bantu Jess Limited Edition membuat program yang dapat menginput uang adsense setiap minggu,
bulan pertama menabung, dan bulan terakhir menabung serta output berupa total uang makan,
total uang beli kaos, total uang beli diamon mobel lejen dan total tabungannya! 

input : Uang adsense setiap minggu, bulan pertama menabung dan bulan terakhir menabung

Prosesnya : membuat variabel-variabel yang sesuai dengan soal

Output : Total uang makan, total uang membeli kaos, total uang beli diamon mobel lejen
dan total uang tabungannya

'''
print("==========PROGRAM PENGATUR PENGHASILAN BULANAN JESS LIMITID EDITION==========")

#Nilai adsense yutub selama seminggu 
adsense = int(input("Masukkan penghasilan adsense selama seminggu : "))

#Bulan awal menabung
awalnabung = int(input("Awal bulan menabung pada bulan ke "))

#Bulan akhir menabung
akhirnabung = int(input("Akhir bulan menabung pada bulan ke "))

#Lama Menabung
lamamenabung = akhirnabung - awalnabung + 1

#Jumlah Minggu selama bulan menabung 
jumlahminggu = (akhirnabung - awalnabung + 1) * 4

#Total penghasilan dari adsense yutub
totaluangadsense = adsense * jumlahminggu

#Jumlah uang makan selama bulan menabung
uangmakan = adsense * 0.4
totaluangmakan = uangmakan * jumlahminggu

#Jumlah uang membeli kaos selama bulan menabung 
uangkaos = adsense * 0.1
totaluangkaos = uangkaos * jumlahminggu

#Jumlah uang membeli diamond mobel lejen
uangdiamon = adsense * 0.3
totaluangdiamon = uangdiamon * jumlahminggu

#Jumlah uang tabungan buat rakit pc
uangtabungan = adsense * 0.2
totaluangtabungan = uangtabungan * jumlahminggu

#Output

#Total uang adsense
print("Total uang adsense selama", lamamenabung, "bulan adalah", totaluangadsense)

#Total Uang makan
print("Total uang makan selama", lamamenabung, "bulan adalah", totaluangmakan)

#Total Uang beli kaos
print("Total uang beli kaos selama", lamamenabung, "bulan adalah", totaluangkaos)

#Total uang beli diamon mobel lejen
print("Total uang beli diamon selama", lamamenabung, "bulan adalah", totaluangdiamon)

#Total tabungan
print("Total tabungan selama", lamamenabung, "bulan adalah", totaluangtabungan)
