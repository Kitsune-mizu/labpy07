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
                print(f"- nama: {nama} nilai: {nilai}")

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

daftar = Mahasiswa()
while True:
    print("\n===== Menu =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    menu = input("Pilih menu (1-5): ")
    if menu == "1":
        daftar.tambah(input("Nama: "), int(input("Nilai: ")))
    elif menu == "2":
        daftar.tampilkan()
    elif menu == "3":
        daftar.ubah(input("Nama: "), int(input("Nilai Baru: ")))
    elif menu == "4":
       daftar.hapus(input("Nama: "))
    elif menu == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
