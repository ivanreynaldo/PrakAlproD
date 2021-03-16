#Nama : Ivan Reynaldo
#NIM  : 71200589
#Kelas: D
#Universitas Kristen Duta Wacana


''' Pak Dino, seorang guru sekolah dasar SD Pochinki kebingungan untuk memberikan jadwal kepada siswanya,
dikarenakan ia tidak bisa mengantarkan jadwal secara langsung lantaran adanya lockdown dikota pak Dino,
naasnya kamera hp yang hendak digunakannya untuk memoto jadwal pun rusak digigit piranha. Karena 
kebingungan, pak Dino meminta bantuan anda untuk membuatkan program yang menampilkan jadwal untuk anak
muridnya. Pada jadwal tersebut, hari senin di isi oleh mata pelajaran Penjaskes, Bahasa Indonesia, dan
Seni Budaya. Pada hari selasa di isi oleh Matematika, PKN, dan IPA. Hari Rabu, Matematika, IPA, dan
IPS. Hari kamis, Agama, IPS, dan Bahasa Indonesia. Hari Jumat hanya di isi oleh kegiatan ekstrakulikuler.
Lalu hari sabtu adalah pramuka wajib. Pada kegiatan ekstrakulikuler terdapat 3 macam tampilan ekstrakulikuler,
yaitu Drumband, Karate, dan Sepak Bola. Bantulah Pak Dino!!! 

referensi : Soal Unguided 5 nomor 4

input : meminta user untuk apakah ingin membuka jadwal atau tidak, jika ya maka user akan diminta untuk
        memasukkan input berupa hari apa yang ingin dilihat.

proses : membuat perulangan yang berisi percabangan mengenai jadwal pada hari senin-sabtu, memberikan
        menghentikan perulangan jika pengguna menginputkan "tidak" dan memberi pesan peringatan jika
        pengguna menginput selain 'ya' atau 'tidak'

output : menampilkan jadwal yang sesuai dengan kehendak pak Dino, menampilkan salam perpisahan jika user
        menjawab 'tidak' dan menampilkan pesan peringatan jika user menginput selain 'ya' atau 'tidak'

'''

while True :
    print("=====Jadwal SD Pochinki=====")
    user = input("Halloo, Apakah anda ingin melihat jadwal? (Ya/Tidak) : ")
    user = user.lower()
    if user == "ya" :
        hari = input("Jadwal hari apa yang ingin anda lihat? (Senin-Sabtu) : ")
        hari = hari.lower()
        if hari == "senin" :
            print("Penjaskes        | 07.00-08.30 WIB")
            print("*Istirahat*      | 30 menit")
            print("Bahasa Indonesia | 09.00-11.00 WIB")
            print("Seni Budaya      | 11.00-12.30 WIB")
            print("\n")    
        if hari == "selasa" :
            print("Matematika  | 07.00-08.30 WIB")
            print("*Istirahat* | 30 menit")
            print("PKN         | 09.00-11.00 WIB")
            print("IPA         | 11.00-12.30 WIB")
            print("\n")
        if hari == "rabu" :
            print("Matematika  | 07.00-08.30 WIB")
            print("*Istirahat* | 30 menit")
            print("IPA         | 09.00-11.00 WIB")
            print("IPS         | 11.00-12.30 WIB")
            print("\n")
        if hari == "kamis" :
            print("Agama            | 07.30-08.30 WIB")
            print("*Istirahat*      | 30 menit")
            print("IPS              | 09.00-11.00 WIB")
            print("Bahasa Indonesia | 11.00-12.30 WIB")
            print("\n")
        if hari == "jumat" :
            print("Ekskul Drumband   | 15.00-17.00 WIB")
            print("Ekskul Karate     | 15.00-17.00 WIB")
            print("Ekskul Sepak Bola | 15.00-17.00 WIB")
        if hari == "sabtu":
            print("PRAMUKA WAJIB  | 15.00-17.00 WIB")

    if user == "tidak":
        print("Goodbye! :)")
        break
    if user != "ya" and user != "tidak":
        print("Jangan menginputkan yang lain-lain!")
        break

