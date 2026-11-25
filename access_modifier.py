# ===== Contoh dari modul =====
class ProgramStudi:
    def __init__(self, kode, ketua):
        self.kode = kode                # public
        self._ketua = ketua             # protected
        self.__anggaran = 500000000     # private

    # Getter protected
    def get_ketua(self):
        return self._ketua

    # Setter protected
    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    # Getter private (wajib karena __anggaran private)
    def get_anggaran(self):
        return self.__anggaran

    # Setter private
    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran


# ===== Latihan a: class Mahasiswa =====
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk            # private

    # Getter & setter semester (protected)
    def get_semester(self):
        return self._semester

    def set_semester(self, semester_baru):
        if semester_baru < 1:
            raise ValueError("Semester minimal 1.")
        self._semester = semester_baru

    # Getter & setter IPK (private)
    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, ipk_baru):
        if not (0.0 <= ipk_baru <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0.")
        self.__ipk = ipk_baru


def tampilkan(m):
    print("NIM      :", m.nim)
    print("Nama     :", m.nama)
    print("Semester :", m.get_semester())
    print("IPK      :", m.get_ipk())
    print()


# ===== Penggunaan =====
if __name__ == "__main__":
    # --- Contoh modul: ProgramStudi ---
    print("=== Contoh ProgramStudi ===")
    ps = ProgramStudi("TI", "Pak Wayan")

    print("Kode:", ps.kode)
    print("Ketua Prodi:", ps.get_ketua())
    print("Anggaran:", ps.get_anggaran())

    ps.set_ketua("Bu Diah")
    print("Ketua Prodi (baru):", ps.get_ketua())

    ps.kurangi_anggaran(100000000)
    print("Anggaran Tersisa:", ps.get_anggaran())
    print()

    # --- Latihan b: buat 2 objek dan tampilkan ---
    mhs1 = Mahasiswa("23001", "Budi", 3, 3.4)
    mhs2 = Mahasiswa("23002", "Siti", 5, 3.85)

    print("=== Data Awal ===")
    tampilkan(mhs1)
    tampilkan(mhs2)

    # --- Latihan c: ganti semester dan IPK ---
    mhs1.set_semester(4)
    mhs1.set_ipk(3.6)

    mhs2.set_semester(6)
    mhs2.set_ipk(3.9)

    print("=== Setelah Diubah ===")
    tampilkan(mhs1)
    tampilkan(mhs2)

    # --- Bahan analisis: percobaan akses langsung ---
    print("=== Percobaan Akses Langsung ===")
    print("Public    (nim)      :", mhs1.nim)
    print("Protected (_semester):", mhs1._semester)   # bisa, tapi tidak dianjurkan
    try:
        print(mhs1.__ipk)                             # private
    except AttributeError as e:
        print("Private   (__ipk)    : ERROR ->", e)