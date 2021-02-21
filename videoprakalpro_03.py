#Nama : Ivan Reynaldo
#NIM  : 71200589
#Grup : D
#Universitas Kristen Duta Wacana

'''Pak Jerami adalah seorang dosen Sastra Pulu Pulu, di Universitas Jangan Maen-Maen. Pak Jerami sudah lelah menuliskan 
nilai mahasiswanya satu-satu. Pak Jerami meminta bantuan Ivan untuk membuatkan program yang dapat menginput nama dan nilai
lalu dapat memberikan output berupa grade A jika >= 85, B jika >= 75, C jika >= 60, D jika >= 50, dan E jika dibawah 50.
Pak Jerami menyampaikan agar memberi pesan yg muncul jika mahasiswa mencoba menginputkan nilai dengan hal yang macam-macam. 
Bantu Pak Jerami agar dia bisa lebih santai dalam melakukan tugasnya! #https://www.petanikode.com/python-percabangan/

input : nama dan nilai

proses : Membuat percabangan nilai dengan if, elif, else dan juga menampilkan pesan jika ada kesalahan yang dilakukan
         pengguna dengan menggunakan try dan except.

Output : Menampilkan grade yang didapat mahasiswa, yang sesuai dengan nilai yang didapatnya. 
         Menampilkan saran dari Pak Jerami. 
         Menampilkan pesan error jika user melakukan kesalahan pada pengisian nilai.


'''

try :
    nama = str(input("Masukkan Nama Anda : "))
    nilai = float(input("Masukkan Nilai Anda : "))

    if nilai >= 85 :
        print("Grade kamu adalah A")
        print("Grade kamu sangat baik", nama, ". Pertahankan dan terus tingkatkan kemampuanmu!")
    elif nilai >= 75 :
        print("Grade kamu adalah B")
        print("Grade kamu baik", nama, ". Terus tingkatkan sehingga bisa menjadi A!")
    elif nilai >= 60 :
        print("Grade kamu adalah C")
        print("Grade kamu cukup", nama, ". Harus lebih banyak belajar, jangan asal lulus!")
    elif nilai >= 50:
        print("Grade kamu adalah D")
        print("Grade kamu buruk", nama, ". Harus lebih serius dan berhenti bermain-main!")
    else :
        print("Grade kamu adalah E")
        print("Grade kamu sangat buruk", nama, ". Harus mengulang matakuliah!")
except :
    print("Jangan Maen-Maen!!!")

    