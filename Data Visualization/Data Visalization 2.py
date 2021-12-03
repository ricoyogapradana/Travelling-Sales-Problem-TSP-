import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("datasetProject1\KedatanganPenduduk.xlsx",sheet_name="April 2021")
kelurahan = (data["Kelurahan"]).tolist()
kelamin = (data["Jenis Kelamin"]).tolist()
jumlah = (data["Jumlah"]).tolist()

hanbaru =[]
minbaru = []
lahbaru = []

tarrah1 = []
tarrah2 = []
tarrah3 = []

lahrah1 = []
lahrah2 =[]
lahrah3 =[]
lahrah4 =[]
lahrah5 =[]
for z in range(len(kelurahan)):
    if kelurahan[z] == "SENEN":
        hanbaru.append(kelurahan[z])
        minbaru.append(kelamin[z])
        lahbaru.append(jumlah[z])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok = (lahbaru[c])
                jarak = lanang + wedok
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita = (minbaru[k])
                if pria != wanita:
                    lurah1 = "Senen"
tarrah1.append(lurah1)
lahrah1.append(jarak)

for z in range(len(kelurahan)):
    if kelurahan[z] == "KENARI":
        hanbaru.append(kelurahan[z])
        minbaru.append(kelamin[z])
        lahbaru.append(jumlah[z])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang1 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok1 = (lahbaru[c])
                jarak1 = lanang1 + wedok1
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria1 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita1 = (minbaru[k])
                if pria1 != wanita1:
                    lurah2 = "Kenari"
tarrah1.append(lurah2)
lahrah1.append(jarak1)

for z in range(len(kelurahan)):
    if kelurahan[z] == "PASEBAN":
        hanbaru.append(kelurahan[z])
        minbaru.append(kelamin[z])
        lahbaru.append(jumlah[z])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang2 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok2 = (lahbaru[c])
                jarak2 = lanang2 + wedok2
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria2 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita2 = (minbaru[k])
                if pria2 != wanita2:
                    lurah3 = "Paseban"
tarrah2.append(lurah3)
lahrah2.append(jarak2)

for z in range(len(kelurahan)):
    if kelurahan[z] == "KRAMAT":
        hanbaru.append(kelurahan[z])
        minbaru.append(kelamin[z])
        lahbaru.append(jumlah[z])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang3 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok3 = (lahbaru[c])
                jarak3= lanang3 + wedok3
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria3 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita3 = (minbaru[k])
                if pria3 != wanita3:
                    lurah4 = "Kramat"
tarrah2.append(lurah4)
lahrah2.append(jarak3)

for x in range(0,len(kelurahan)):
    if kelurahan[x] == "KWITANG":
        hanbaru.append(kelurahan[x])
        minbaru.append(kelamin[x])
        lahbaru.append(jumlah[x])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang4 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok4 = (lahbaru[c])
                jarak4= lanang4 + wedok4
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria4 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita4 = (minbaru[k])
                if pria4 != wanita4:
                    lurah5 = "Kwitang"
tarrah3.append(lurah5)
lahrah3.append(jarak4)

for x in range(0,len(kelurahan)):
    if kelurahan[x] == "BUNGUR":
        hanbaru.append(kelurahan[x])
        minbaru.append(kelamin[x])
        lahbaru.append(jumlah[x])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang5 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok5 = (lahbaru[c])
                jarak5= lanang5 + wedok5
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria5 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita5 = (minbaru[k])
                if pria5 != wanita5:
                    lurah6 = "Kwitang"
tarrah3.append(lurah6)
lahrah3.append(jarak5)

for x in range(0,len(kelurahan)):
    if kelurahan[x] == "JOHAR BARU":
        hanbaru.append(kelurahan[x])
        minbaru.append(kelamin[x])
        lahbaru.append(jumlah[x])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang6 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok6 = (lahbaru[c])
                jarak6= lanang6 + wedok6
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria6 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita6 = (minbaru[k])
                if pria6 != wanita6:
                    lurah7 = "Johar Baru"
lahrah4.append(jarak6)

for x in range(0,len(kelurahan)):
    if kelurahan[x] == "KAMPUNG RAWA":
        hanbaru.append(kelurahan[x])
        minbaru.append(kelamin[x])
        lahbaru.append(jumlah[x])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang7 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok7 = (lahbaru[c])
                jarak7= lanang7 + wedok7
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria7 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita7 = (minbaru[k])
                if pria7 != wanita7:
                    lurah8 = "Kampung Rawa"
lahrah4.append(jarak7)

for x in range(0,len(kelurahan)):
    if kelurahan[x] == "GALUR":
        hanbaru.append(kelurahan[x])
        minbaru.append(kelamin[x])
        lahbaru.append(jumlah[x])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang8 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok8 = (lahbaru[c])
                jarak8= lanang8 + wedok8
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria8 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita8 = (minbaru[k])
                if pria8 != wanita8:
                    lurah9 = "Galur"
lahrah5.append(jarak8)

for x in range(0,len(kelurahan)):
    if kelurahan[x] == "TANAH TINGGI":
        hanbaru.append(kelurahan[x])
        minbaru.append(kelamin[x])
        lahbaru.append(jumlah[x])
        for c in range(0,len(lahbaru)):
            if minbaru[c]=="Laki-Laki":
                lanang9 = (lahbaru[c])
            elif minbaru[c]=="Perempuan":
                wedok9 = (lahbaru[c])
                jarak9= lanang9 + wedok9
        for k in range(0,len(lahbaru)):
            if minbaru[k]=="Laki-Laki":
                pria9 = (minbaru[k])
            elif minbaru[k]=="Perempuan":
                wanita9 = (minbaru[k])
                if pria9 != wanita9:
                    lurah10 = "Tanah Tinggi"
lahrah5.append(jarak9)

#---------------------------------------------#
list=("Senen dan Kenari"),("Paseban dan Kramat"),("Kwitang dan Bungur"),("Johar Baru dan Kampung Rawa"),("Galur dan Tanah Tinggi")
gtarrah=[]
glahrah =[]
glahrah.append(lahrah1)
glahrah.append(lahrah2)
glahrah.append(lahrah3)
glahrah.append(lahrah4)
glahrah.append(lahrah5)
gtarrah.append(tarrah1)
gtarrah.append(tarrah2)
gtarrah.append(tarrah3)

ulahrah = np.array(glahrah)
utarrah = np.array(gtarrah)
print("Kelurahan yang ada di kecamatan Senen:",utarrah)
fig, ax = plt.subplots()
size = 0.3
cmap = plt.get_cmap("tab20")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])
print("Jumlah per Kelurahan:",glahrah)
ax.pie(ulahrah.sum(axis=1), radius=1, colors=outer_colors,autopct='%.0f%%', wedgeprops=dict(width=0.6, edgecolor='black'),
       labels=list,pctdistance=0.85,shadow=True,startangle=0) #pie luar
ax.pie(ulahrah.flatten(), radius=1.0-size, colors=inner_colors, autopct='%.0f%%', wedgeprops=dict(width=0.5, edgecolor='black'),
       pctdistance=0.6,shadow=True,startangle=0) #pie dalam
ax.set(aspect="equal", title='Kedatangan Penduduk Kelurahan yang Termasuk Kecamatan Senen dan Johar Baru')
plt.show()


