class Item:
    def __init__(self, id_barang, nama): 
        self.id_barang = id_barang
        self.nama = nama
        self.tersedia = True

    def __str__(self): 
        status = "Tersedia" if self.tersedia else "Tidak Tersedia"
        return f"ID: {self.id_barang}, Nama: {self.nama}, Status: {status}"


class Borrower:
    def __init__(self, id_peminjam, nama): 
        self.id_peminjam = id_peminjam
        self.nama = nama

    def __str__(self): 
        return f"ID: {self.id_peminjam}, Nama: {self.nama}"


class LoanManager:
    def __init__(self): 
        self.daftar_barang = []
        self.daftar_peminjam = []
        self.peminjaman = {}

    def tambah_barang(self, id_barang, nama):
        barang = Item(id_barang, nama)
        self.daftar_barang.append(barang)
        print(f"Barang '{nama}' berhasil ditambahkan.")

    def tambah_peminjam(self, id_peminjam, nama):
        peminjam = Borrower(id_peminjam, nama)
        self.daftar_peminjam.append(peminjam)
        print(f"Peminjam '{nama}' berhasil ditambahkan.")

    def pinjam_barang(self, id_barang, id_peminjam):
        barang = next((b for b in self.daftar_barang if b.id_barang == id_barang), None)
        peminjam = next((p for p in self.daftar_peminjam if p.id_peminjam == id_peminjam), None)

        if barang and peminjam:
            if barang.tersedia:
                barang.tersedia = False
                self.peminjaman[id_barang] = id_peminjam
                print(f"Barang '{barang.nama}' berhasil dipinjam oleh '{peminjam.nama}'.")
            else:
                print(f"Barang '{barang.nama}' sedang tidak tersedia.")
        else:
            print("ID barang atau ID peminjam tidak valid.")

    def kembalikan_barang(self, id_barang):
        if id_barang in self.peminjaman:
            barang = next((b for b in self.daftar_barang if b.id_barang == id_barang), None)
            if barang:
                barang.tersedia = True
                id_peminjam = self.peminjaman.pop(id_barang)
                peminjam = next((p for p in self.daftar_peminjam if p.id_peminjam == id_peminjam), None)
                print(f"Barang '{barang.nama}' telah dikembalikan oleh '{peminjam.nama}'.")
        else:
            print("ID barang tidak valid atau barang belum dipinjam.")

    def tampilkan_daftar_barang(self):
        print("Daftar Barang:")
        for barang in self.daftar_barang:
            print(barang)

    def tampilkan_daftar_peminjam(self):
        print("Daftar Peminjam:")
        for peminjam in self.daftar_peminjam:
            print(peminjam)

    def tampilkan_daftar_peminjaman(self):
        print("Daftar Peminjaman Saat Ini:")
        if self.peminjaman:
            for id_barang, id_peminjam in self.peminjaman.items():
                barang = next((b for b in self.daftar_barang if b.id_barang == id_barang), None)
                peminjam = next((p for p in self.daftar_peminjam if p.id_peminjam == id_peminjam), None)
                if barang and peminjam:
                    print(f"Barang '{barang.nama}' dipinjam oleh '{peminjam.nama}'.")
        else:
            print("Tidak ada peminjaman saat ini.")


# Tampilan
if __name__ == "__main__": 
    pengelola = LoanManager()

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tambah Peminjam")
        print("3. Pinjam Barang")
        print("4. Kembalikan Barang")
        print("5. Tampilkan Daftar Barang")
        print("6. Tampilkan Daftar Peminjam")
        print("7. Tampilkan Daftar Peminjaman")
        print("8. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            id_barang = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            pengelola.tambah_barang(id_barang, nama)
        
        elif pilihan == '2':
            id_peminjam = input("Masukkan ID Peminjam: ")
            nama = input("Masukkan Nama Peminjam: ")
            pengelola.tambah_peminjam(id_peminjam, nama)
        
        elif pilihan == '3':
            id_barang = input("Masukkan ID Barang yang ingin dipinjam: ")
            id_peminjam = input("Masukkan ID Peminjam: ")
            pengelola.pinjam_barang(id_barang, id_peminjam)
        
        elif pilihan == '4':
            id_barang = input("Masukkan ID Barang yang ingin dikembalikan: ")
            pengelola.kembalikan_barang(id_barang)
        
        elif pilihan == '5':
            pengelola.tampilkan_daftar_barang()
        
        elif pilihan == '6':
            pengelola.tampilkan_daftar_peminjam()
        
        elif pilihan == '7':
            pengelola.tampilkan_daftar_peminjaman()
        
        elif pilihan == '8':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
