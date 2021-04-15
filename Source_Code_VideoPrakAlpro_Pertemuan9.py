''' 
Nama : Ivan Reynaldo
NIM  : 71200589
Grup : D
Universitas Kristen Duta Wacana

Pak Lancelot adalah guru di SMP Hogwarts, Ia kebingungan mencari persamaan yang ada didalam 2 list.
Dia meminta anda untuk membuat program yang dapat mencari persamaan pada kedua list yang diberikan.
Jika Ada sebuah 1 saja persamaan maka nilai return harus diberitahukan bahwa ada persamaan, 
jika tidak ada sama sekali persamaan baru nilai return berupa tidak ada yang sama. Tampilkan inputan 
user yang sudah urut dan tampilkan juga persamaan yang ada didapat, Bantulah Pak Lancelot!

Referensi Modul Praktikum 9

Input  : Langsung menginputkan list kedalam fungsi yang nanti akan dibuat
Proses : Membuat fungsi yang nanti akan mengurutkan data terlebih dahulu, lalu membuat perbandingan antara kedua list,
         dan menemukan persamaannnya.
Output : Menampilkan nilai "Ada Persamaan!" jika dalam kedua list ada yang sama, 
         dan menampilkan nilai "Tidak Ada Persamaan!" Jika tidak ada yang sama. 
         Juga tampilkan data input yang sudah urut dan data nilai yang sama.
'''

def cariPersamaan (list1,list2):
    list1.sort()
    list2.sort()
    print("Data Masuk Urut :")
    print(list1)
    print(list2,'\n')
    hasil = 'Tidak Ada Persamaan!'
    list_sama = []
    for i in list1:
        for j in list2:
            if i==j:
                hasil = 'Ada Persamaan!'
                list_sama += [i]
    
    if list_sama != []:
        print(hasil)
        print('List Data yang sama :')
        return list_sama
    else:
        return hasil

input1 = input("Masukkan data list1 (Masukkan nilai dengan pemisah spasi): ")
input2 = input("Masukkan data list2 (Masukkan nilai dengan pemisah spasi): ")

list1 = input1.split()
list2 = input2.split()

print(cariPersamaan(list1,list2))