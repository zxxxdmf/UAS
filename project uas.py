# MODULARISASI
from datetime import datetime  # Mengimpor modul datetime untuk pengelolaan waktu

# OPB
class TokoSepatu:
    def __init__(self):
        # Inisialisasi atribut-atribut untuk menyimpan informasi sepatu, harga, dan keranjang belanja
        self.sepatu = ["Converse", "Vans", "Ventela", "Patrobas"]
        self.harga = [700000, 750000, 300000, 350000]
        self.keranjang = []

    def tampilan_menu(self):
        # Menampilkan menu utama toko sepatu
        print("\n =====TOKO SEPATU JAYA SELALU=====\n")
        print("\nMenu:")
        print("1. Masukkan sepatu ke dalam keranjang")
        print("2. Lihat keranjang")
        print("3. Hitung total pembayaran")
        print("4. Pembayaran")
        print("5. Keluar")

    def input_sepatu(self):
        # Menggunakan menu ini, pengguna dapat memilih sepatu, menentukan jumlah yang ingin dibeli, dan menambahkannya ke dalam keranjang
        print("Daftar sepatu: ")
        for i in range(len(self.sepatu)):
            print(f"{i+1}. {self.sepatu[i]}: Rp. {self.harga[i]:,.2f}")

        pilihan = int(input("Pilih nomor sepatu yang kamu inginkan: "))
        if 1 <= pilihan <= len(self.sepatu):
            qty = int(input(f"Masukkan Jumlah {self.sepatu[pilihan-1]} yang ingin kamu beli: "))
            self.keranjang.append((self.sepatu[pilihan-1], self.harga[pilihan-1], qty))
            print(f"{qty} {self.sepatu[pilihan-1]} telah ditambahkan ke dalam keranjang!")
        else:
            print("Pilihan Salah")

    def isi_keranjang(self):
        # Menampilkan isi keranjang dan total pembelian sementara
        if self.keranjang:
            print("\n Isi Keranjang: ")
            total = 0
            for sepatu in self.keranjang:
                item_total = sepatu[1] * sepatu[2]
                total += item_total
                print(f"{sepatu[2]} {sepatu[0]} (Rp. {sepatu[1]:,.2f})")
            print(f"Total Pembelian: Rp. {total:,.2f}")
            # Menyimpan data transaksi dalam file
            self.simpan_data(total)
        else:
            print("Keranjang Kosong :(")

    def hitung_total(self):
        # Menghitung total pembelian sementara tanpa menyimpan data transaksi
        total = sum(item[1] * item[2] for item in self.keranjang)
        print(f"Total Pembelian Sementara: Rp. {total:,.2f}")

    def pembayaran(self):
        # Melakukan proses pembayaran, mencetak struk pembelian, dan membersihkan keranjang
        total = sum(item[1] * item[2] for item in self.keranjang)
        print(f"Total Pembelian Sementara: Rp. {total:,.2f}")
        pembayaran = float(input("Masukkan Jumlah Uang Kamu: "))

        if pembayaran >= total:
            kembalian = pembayaran - total
            print(f"Kembalian: Rp. {kembalian:,.2f}")
            print("Terima Kasih")
            # Menyimpan data transaksi dalam file
            self.simpan_data(total)
            self.keranjang.clear()
        else:
            print("Mohon Maaf Uang Kamu Kurang :(")

    def simpan_data(self, total):
        # Membuat timestamp untuk digunakan sebagai bagian dari nama file
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        nama_file = f"struk_pembelian_{timestamp}.txt"

        with open(nama_file, "w") as file:  # Menggunakan mode "w" agar membuat file baru
            file.write("==== STRUK PEMBELIAN ====\n")
            file.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("\nDaftar Pembelian:\n")
            for sepatu in self.keranjang:
                item_total = sepatu[1] * sepatu[2]
                file.write(f"{sepatu[2]} {sepatu[0]} (Rp. {sepatu[1]:,.2f}) - Total: Rp. {item_total:,.2f}\n")
            file.write(f"\nTotal Pembelian: Rp. {total:,.2f}\n")
            file.write("TERIMA KASIH SUDAH BELANJA DI TOKO KAMI :)")

if __name__ == "__main__":
    # Inisialisasi objek TokoSepatu
    toko = TokoSepatu()

    # ITERASI
    # Loop utama untuk menampilkan menu dan memproses pilihan pengguna
    while True:
        toko.tampilan_menu()
        pilihan = input("Pilih: ")

        if pilihan == "1":
            toko.input_sepatu()
        elif pilihan == "2":
            toko.isi_keranjang()
        elif pilihan == "3":
            toko.hitung_total()
        elif pilihan == "4":
            toko.pembayaran()
        elif pilihan == "5":
            break
        else:
            print("Tidak Valid")
