#This code was created for operational research for optimization code

from itertools import permutations
from sys import maxsize

# ini class
class Kota:
    def __init__(self, kota):
        self.kota = kota
        self.waktu_perjalanan = []

    def findNearestPath(self):  
        graf = []
        waktu1 = [t["waktu yang dibutuhkan"] for t in self.waktu_perjalanan]
        waktu1.insert(0, 0)
        Waktu2_waktu_perjalanan = [t["nama kota"] for t in self.waktu_perjalanan]
        graf.append(waktu1)

        s = 0

        for t in Waktu2_waktu_perjalanan:
            Waktu2 = [t["waktu yang dibutuhkan"] for t in t.waktu_perjalanan]
            Waktu2.insert(Waktu2_waktu_perjalanan.index(t) + 1, 0)
            graf.append(Waktu2)

        Waktu_jalan = []
        for i in range(banyak_kota):
            if i != s:
                  Waktu_jalan.append(i)

        waktu_tempuh = maxsize
        permutasi = list(permutations(  Waktu_jalan))
        for i in permutasi:
            jarak_sekarang = 0
            k = s
            for j in list(i):
                jarak_sekarang += graf[k][j]
                k = j
            if waktu_tempuh > jarak_sekarang:
                waktu_tempuh = jarak_sekarang
                kota_lewat = self.kota + " - " + " - ".join([Waktu2_waktu_perjalanan[a - 1].kota for a in i])

        return kota_lewat, waktu_tempuh
rute1 = Kota("Tokyo")
rute2 = Kota("Saitama")
rute3 = Kota("Kyoto")
rute4 = Kota("Nagoya")
rute5 = Kota("Yokohama")
rute6 = Kota("Osaka")
rute7 = Kota("Kawaguchi")
rute8 = Kota("Tateyama")
banyak_kota = 8

rute1.waktu_perjalanan.extend([{"nama kota": rute2, "waktu yang dibutuhkan": 59}, 
                            {"nama kota": rute3, "waktu yang dibutuhkan": 128},
                            {"nama kota": rute4, "waktu yang dibutuhkan": 94}, 
                            {"nama kota": rute5, "waktu yang dibutuhkan": 18},
                            {"nama kota": rute6, "waktu yang dibutuhkan": 142}, 
                            {"nama kota": rute7, "waktu yang dibutuhkan": 57},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 154}])

rute2.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 59}, 
                            {"nama kota": rute3, "waktu yang dibutuhkan": 203},
                            {"nama kota": rute4, "waktu yang dibutuhkan": 168}, 
                            {"nama kota": rute5, "waktu yang dibutuhkan": 89},
                            {"nama kota": rute6, "waktu yang dibutuhkan": 217}, 
                            {"nama kota": rute7, "waktu yang dibutuhkan": 46},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 219}])

rute3.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 128}, 
                            {"nama kota": rute2, "waktu yang dibutuhkan": 203},
                            {"nama kota": rute4, "waktu yang dibutuhkan": 34}, 
                            {"nama kota": rute5, "waktu yang dibutuhkan": 111},
                            {"nama kota": rute6, "waktu yang dibutuhkan": 43}, 
                            {"nama kota": rute7, "waktu yang dibutuhkan": 181},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 261}])

rute4.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 94}, 
                            {"nama kota": rute2, "waktu yang dibutuhkan": 168},
                            {"nama kota": rute3, "waktu yang dibutuhkan": 34}, 
                            {"nama kota": rute5, "waktu yang dibutuhkan": 94},
                            {"nama kota": rute6, "waktu yang dibutuhkan": 49}, 
                            {"nama kota": rute7, "waktu yang dibutuhkan": 167},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 238}])

rute5.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 18}, 
                            {"nama kota": rute2, "waktu yang dibutuhkan": 89},
                            {"nama kota": rute3, "waktu yang dibutuhkan": 111}, 
                            {"nama kota": rute4, "waktu yang dibutuhkan": 94},
                            {"nama kota": rute6, "waktu yang dibutuhkan": 132}, 
                            {"nama kota": rute7, "waktu yang dibutuhkan": 85},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 173}])

rute6.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 142}, 
                            {"nama kota": rute2, "waktu yang dibutuhkan": 217},
                            {"nama kota": rute3, "waktu yang dibutuhkan": 43}, 
                            {"nama kota": rute4, "waktu yang dibutuhkan": 49},
                            {"nama kota": rute5, "waktu yang dibutuhkan": 132}, 
                            {"nama kota": rute7, "waktu yang dibutuhkan": 195},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 276}])

rute7.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 57}, 
                            {"nama kota": rute2, "waktu yang dibutuhkan": 46},
                            {"nama kota": rute3, "waktu yang dibutuhkan": 181}, 
                            {"nama kota": rute4, "waktu yang dibutuhkan": 167},
                            {"nama kota": rute5, "waktu yang dibutuhkan": 85}, 
                            {"nama kota": rute6, "waktu yang dibutuhkan": 195},
                            {"nama kota": rute8, "waktu yang dibutuhkan": 194}])

rute8.waktu_perjalanan.extend([{"nama kota": rute1, "waktu yang dibutuhkan": 154}, 
                            {"nama kota": rute2, "waktu yang dibutuhkan": 219},
                            {"nama kota": rute3, "waktu yang dibutuhkan": 261}, 
                            {"nama kota": rute4, "waktu yang dibutuhkan": 238},
                            {"nama kota": rute5, "waktu yang dibutuhkan": 173}, 
                            {"nama kota": rute6, "waktu yang dibutuhkan": 276},
                            {"nama kota": rute7, "waktu yang dibutuhkan": 194}])



kota_lewat, waktu_tempuh = rute1.findNearestPath()
print("Kota yang dilewati:", kota_lewat)
print("waktu tempuh terpendek:", waktu_tempuh, "menit")

input()
