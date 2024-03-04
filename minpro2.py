import os
import time


def cls():
    os.system('cls')
    return

class Node:
    def __init__(self,  id, nama, kategori, harga, stok):
        self.id = id
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambahDepan(self, id, nama, kategori, harga, stok):
        new_node = Node(id, nama, kategori, harga, stok)
        if self.head is None:
            self.head = new_node
        else:
            if self.cek_id(id):
                print(f"Barang dengan ID {id} sudah ada dalam daftar")
                time.sleep(2)
                cls()
                return
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    
    def tambahBelakang(self, id, nama, kategori, harga, stok):
        new_node = Node(id, nama, kategori, harga, stok)
        if self.head is None:
            self.head = new_node
        else:
            if self.cek_id(id):
                print(f"Barang dengan ID {id} sudah ada dalam daftar")
                time.sleep(2)
                cls()
                return
            tambah = self.head
            while tambah.next is not None:
                tambah = tambah.next
            tambah.next = new_node
            new_node.prev = tambah

    def tambahTengah(self, tn, id, nama, kategori, harga, stok):
        new_node = Node(id, nama, kategori, harga, stok)
        if self.head is None:
            print("Belum ada barang yang tersedia, tidak bisa menambahkan barang")
            return
        else:
            tambah = self.head
            while tambah is not None:
                if tambah.id == tn:
                    break
                tambah = tambah.next
            if tambah is None:
                print(f"id barang : {tn} tidak ada dalam list")
            else:
                if self.cek_id(id):
                    print(f"Barang dengan ID {id} sudah ada dalam daftar")
                    time.sleep(2)
                    cls()
                    return
                new_node.prev = tambah
                new_node.next = tambah.next
                if tambah.next is not None:
                    tambah.next.prev = new_node
                tambah.next = new_node

    def cek_id(self, id):
        current = self.head
        while current is not None:
            if current.id == id:
                return True
            current = current.next
        return False

    def update_barang(self, id_barang, nama_baru, kategori_baru, harga_baru, stok_baru):
        if self.head is None:
            print("Tidak ada barang dalam daftar")
            return
        current = self.head
        while current:
            if current.id == id_barang:
                current.nama = nama_baru
                current.kategori = kategori_baru
                current.harga = harga_baru
                current.stok = stok_baru
                print(f"Barang dengan ID {id_barang} telah diperbarui")
                return
            current = current.next
        print(f"Barang dengan ID {id_barang} tidak ditemukan dalam daftar")

    def delawal (self):
        if self.head is None:
            print("Tidak ada barang dilist")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head_prev = None

    def delakhir (self):
        if self.head is None:
            print(f"Tidak ada barang dilist")
            return
        if self.head.next is None:
            self.head = None
            return
        hapus = self.head
        while hapus.next is not None:
            hapus = hapus.next
        hapus.prev.next = None

    def deltengah(self, id_barang):
        if self.head is None:
            print("Tidak ada barang dilist")
            return
        if self.head.next is None:
            if self.head.id == id_barang:
                self.head = None
                return
            else:
                print(f"Barang dengan id {id_barang} tidak ditemukan")
                return
        current = self.head
        while current.next is not None:
            if current.id == id_barang:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
        if current.id == id_barang:
            current.prev.next = None
        else:
            print(f"Barang dengan id {id_barang} tidak ditemukan")

    def display(self):
        if self.head == None:
            print("Tidak ada barang")
        else:
            current = self.head
            while current:
                print(f"id = {current.id}")
                print(f"Nama barang = {current.nama}")
                print(f"kategori = {current.kategori}")
                print(f"Harga = {current.harga}")
                print(f"Stok = {current.stok}\n")
                current = current.next

doublelinked = DoubleLinkedList()
doublelinked.tambahDepan("1a", "Cat merah", "Cat", 40000, 23)
doublelinked.tambahTengah("1a" , "1c", "paku", "bangunan", 2000, 200)
doublelinked.tambahBelakang("1b", "Cat biru", "Cat", 40000, 23)
doublelinked.tambahBelakang("1d", "Semen", "Bangunan", 25000, 15)


def main():
    while True:
        cls()
        print("======================================")
        print("[+] 1. Tampilkan barang            [+]")
        print("[+] 2. Tambahkan barang di awal    [+]")
        print("[+] 3. Tambahkan barang di akhir   [+]")
        print("[+] 4. Tambahkan barang di tengah  [+]")
        print("[+] 5. Update barang               [+]")
        print("[+] 6. Hapus barang di awal        [+]")
        print("[+] 7. Hapus barang di akhir       [+]")
        print("[+] 8. Hapus barang di tengah      [+]")
        print("[+] 9. Keluar                      [+]")
        print("======================================")
        pilihmenu = input("Masukkan pilihan anda : ")
        if pilihmenu == "1":
            cls()
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "2":
            cls()
            inid = input("Masukkan id barang : ")
            nama = input("Masukkan nama barang : ")
            kategori = input("Masukkan kategori barang : ")
            harga = int(input("Masukkan harga barang : "))
            stok = int(input("Masukkan stok barang : "))
            doublelinked.tambahDepan(inid, nama, kategori, harga, stok,)
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "3":
            cls()
            inid = input("Masukkan id barang : ")
            nama = input("Masukkan nama barang : ")
            kategori = input("Masukkan kategori barang : ")
            harga = int(input("Masukkan harga barang : "))
            stok = int(input("Masukkan stok barang : "))
            doublelinked.tambahBelakang(inid, nama, kategori, harga, stok,)
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "4":
            cls()
            idsebelum = input("Masukkan id barang yang digunakan untuk menambah barang setelah id ini : ")
            inid = input("Masukkan id barang : ")
            nama = input("Masukkan nama barang : ")
            kategori = input("Masukkan kategori barang : ")
            harga = int(input("Masukkan harga barang : "))
            stok = int(input("Masukkan stok barang : "))
            doublelinked.tambahTengah(idsebelum, inid, nama, kategori, harga, stok,)
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "5":
            cls()
            id_barang = input("Masukkan ID barang yang ingin diperbarui: ")
            nama_baru = input("Masukkan nama baru barang: ")
            kategori_baru = input("Masukkan kategori baru barang: ")
            harga_baru = int(input("Masukkan harga baru barang: "))
            stok_baru = int(input("Masukkan stok baru barang: "))
            doublelinked.update_barang(id_barang, nama_baru, kategori_baru, harga_baru, stok_baru)
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "6":
            cls()
            doublelinked.display()
            doublelinked.delawal()
            doublelinked.display()
            keluar = input()
        elif pilihmenu == "7":
            cls()
            doublelinked.display()
            doublelinked.delakhir()
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "8":
            cls()
            doublelinked.display()
            id_barang = input("Masukkan id barang yang ingin dihapus (barang harus berada di antara barang lain) : ")
            doublelinked.deltengah(id_barang)
            doublelinked.display()
            keluar = input("")
        elif pilihmenu == "9":
            break

main()