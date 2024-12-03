class Mahasiswa():
    def __init__(self):
        self.data = {}
         
    def tambah(self, nama, nilai):
        self.data[nama] = nilai
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data:
            print("Belum ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.data.items():
                print(f"- Nama: {nama}, Nilai: {nilai}")

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data {nama} berhasil dihapus.")
        else:
            print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.data:
            self.data[nama] = nilai_baru
            print(f"Data {nama} berhasil diubah.")
        else:
            print(f"Data {nama} tidak ditemukan.")

class Menu():
    def __init__(self):
        self.daftar = Mahasiswa()   

    def tampilkan_menu(self):
        print("\n===== Menu =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

    def proses_input(self, menu):
        if menu == "1":
            nama = input("Nama: ")
            nilai = int(input("Nilai: "))
            self.daftar.tambah(nama, nilai)
        elif menu == "2":
            self.daftar.tampilkan()
        elif menu == "3":
            nama = input("Nama: ")
            self.daftar.hapus(nama)
        elif menu == "4":
            nama = input("Nama: ")
            nilai_baru = int(input("Nilai Baru: "))
            self.daftar.ubah(nama, nilai_baru)
        elif menu == "5":
            print("Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid.")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            menu = input("Pilih menu (1-5): ")
            self.proses_input(menu)

app = Menu()
app.jalankan()
