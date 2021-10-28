saldo_umum = 0
saldo_tabungan = 0

def Informasi_Saldo():
        print("")
        print("")
        print("Jumlah Saldo Umum Anda Saat ini Rp. {}".format(saldo_umum))
        print("Jumlah Saldo Tabungan Anda Saat ini Rp. {}".format(saldo_tabungan))
        print("")
        print("")

def Ambil_Saldo_Umum(tarik_tunai):
        global saldo_umum
        saldo_umum=saldo_umum-tarik_tunai
        print("")
        print("")
        print("Sisa Saldo Umum anda Rp. {}".format(saldo_umum))
        print("")
        print("")

def Ambil_Saldo_Tabungan(tarik_tabungan):
        global saldo_tabungan
        saldo_tabungan=saldo_tabungan-tarik_tabungan
        print("")
        print("")
        print("Sisa Saldo Tabungan anda Rp. {}".format(saldo_tabungan))
        print("")
        print("")

    
def Saldo_Umum(tambah_umum):
        global saldo_umum
        saldo_umum=saldo_umum+tambah_umum
        print("")
        print("")
        print("Nominal Uang yang Akan Ditambahkan pada Saldo Umum Rp. {}".format(saldo_umum))
        print("")
        print("")

def Saldo_Tabungan(Tambah_Tabungan):
        global saldo_tabungan
        saldo_tabungan=saldo_tabungan+Tambah_Tabungan
        print("")
        print("")
        print("Nominal Uang yang Akan Ditambahkan pada Saldo Tabungan Rp. {}".format(saldo_tabungan))
        print("")
        print("")


opsi = None
jumlah = None
option = None
tambah_umum = None
Tambah_Tabungan = None

while True:
        print("Selamat Datang")
        print("pilih opsi:")
        print("1. Informasi Saldo")
        print("2. Tambah Saldo")
        print("3. Ambil Saldo")
        print("4. Keluar")
        pilih = int(input("Silahkan pilih menu: "))
        if pilih == 1:
           Informasi_Saldo()

        elif pilih == 2:
            print("")
            print("1. Umum \n2. Tabungan")
            opsi = int(input("Silahkan pilih opsi tambah saldo:"))
            if opsi == 1:
               jumlah=int(input("Nominal Uang yang Akan Ditambahkan pada Saldo Umum Rp. "))
               Saldo_Umum(jumlah)

            else:
               jumlah=int(input("Nominal Uang yang Akan Ditambahkan pada Saldo Tabungan Rp. "))
               Saldo_Tabungan(jumlah)

        elif pilih == 3:
            print("")
            print("1. Umum \n2. Tabungan")
            option = int(input("Silahkan pilih opsi untuk tarik tunai:"))
            if option == 1:
                print("")
                jumlah = int(input("1. Nominal Yang Akan Ditarik pada Saldo Umum Rp."))
                Ambil_Saldo_Umum(jumlah)

            else: 
                print("")
                jumlah = int(input("1. Nominal Yang Akan Ditarik pada Saldo Tabungan Rp."))
                Ambil_Saldo_Tabungan(jumlah)

        elif pilih == 4:
                print("")
                print("Terimakasih Telah Menggunakan ATM!")
                print("")
        
        else:
            print("")
            print("Pilihan tidak tersedia!")
            print("")