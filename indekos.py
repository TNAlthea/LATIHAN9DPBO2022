from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, biaya_sewa):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.biaya_sewa = biaya_sewa

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_biaya_sewa(self):
        return self.biaya_sewa

    def get_summary(self):
        return "Hunian Indekos."

    def get_pemilik_penghuni(self):
        return self.nama_pemilik + self.nama_penghuni