import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('bmh')

dt = pd.read_excel("datasetProject1\Kelahiran.xlsx",sheet_name="Januari 2021")
dt1 = pd.read_excel("datasetProject1\Kelahiran.xlsx",sheet_name="Februari 2021")
dt2 = pd.read_excel("datasetProject1\Kelahiran.xlsx",sheet_name="Maret 2021")
dt3 = pd.read_excel("datasetProject1\Kelahiran.xlsx",sheet_name="April 2021")
dt4 = pd.read_excel("datasetProject1\Kelahiran.xlsx",sheet_name="Mei 2021")

total = []
total1 = []
total2 = []
total3 = []
total4 = []

#BULAN JANUARI
kt = (dt["Kota Kabupaten"]).tolist()
jm = (dt["Jumlah"]).tolist()
km = (dt["Jenis Kelamin"]).tolist()

ktn = []
jmn = []
kmn = []
ktn1 = []
jmn1 = []
kmn1 = []
ktn2 = []
jmn2 = []
kmn2 = []
ktn3 = []
jmn3 = []
kmn3 = []
ktn4 = []
jmn4 = []
kmn4 = []
ktn5 = []
jmn5 = []
kmn5 = []

for i in range (0,len(kt)):
    if kt[i]=="ADM. KEPULAUAN SERIBU":
        ktn.append(kt[i])
        jmn.append(jm[i])
        kmn.append(km[i])
        q = 0
        for w in range(0,len(jmn)):
            q = q+int(jmn[w])

for o in range  (0,len(kt)):
    if kt[o]=="JAKARTA PUSAT":
        ktn1.append(kt[o])
        jmn1.append(jm[o])
        kmn1.append(km[o])
        q1 = 0
        for w in range(0,len(jmn1)):
            q1 = q1+int(jmn1[w])

for c in range(0,len(kt)):
    if kt[c]=="JAKARTA UTARA":
        ktn2.append(kt[c])
        jmn2.append(jm[c])
        kmn2.append(km[c])
        q2 = 0
        for w in range(0,len(jmn2)):
            q2 = q2+int(jmn2[w])

for m in range (0,len(kt)):
    if kt[m]=="JAKARTA BARAT":
        ktn3.append(kt[m])
        jmn3.append(jm[m])
        kmn3.append(km[m])
        q3 = 0
        for e in range (0,len(jmn3)):
            q3 = q3+int(jmn3[e])

for l in range(0,len(kt)):
    if kt[l]=="JAKARTA SELATAN":
        ktn4.append(kt[l])
        jmn4.append(jm[l])
        kmn4.append(km[l])
        q4 = 0
        for y in range (0,len(jmn4)):
            q4=q4+int(jmn4[y])

for b in range(0,len(kt)):
    if kt[b]=="JAKARTA TIMUR":
        ktn5.append(kt[b])
        jmn5.append(jm[b])
        kmn5.append(km[b])
        q5 = 0
        for s in range(0,len(jmn5)):
            q5= q5+ int(jmn5[s])

#BULAN FEBRUARI
kt1 = (dt1["Kota Kabupaten"]).tolist()
jm1 = (dt1["Jumlah"]).tolist()
km1 = (dt1["Jenis Kelamin"]).tolist()

kfn = []
jfn = []
kmfn = []
kfn1 = []
jfn1 = []
kmfn1 = []
kfn2 = []
jfn2 = []
kmfn2 = []
kfn3 = []
jfn3 = []
kmfn3 = []
kfn4 = []
jfn4 = []
kmfn4 = []
kfn5 = []
jfn5= []
kmfn5 = []

for i in range (0,len(kt1)):
    if kt1[i]=="ADM. KEPULAUAN SERIBU":
        kfn.append(kt1[i])
        jfn.append(jm1[i])
        kmfn.append(km1[i])
        d = 0
        for w in range(0,len(jfn)):
            d = d+int(jfn[w])

for o in range  (0,len(kt1)):
    if kt1[o]=="JAKARTA PUSAT":
        kfn1.append(kt1[o])
        jfn1.append(jm1[o])
        kmfn1.append(km1[o])
        d1 = 0
        for w in range(0,len(jfn1)):
            d1 = d1+int(jfn1[w])
for c in range(0,len(kt1)):
    if kt1[c]=="JAKARTA UTARA":
        kfn2.append(kt1[c])
        jfn2.append(jm1[c])
        kmfn2.append(km1[c])
        d2 = 0
        for w in range(0,len(jfn2)):
            d2 = d2+int(jfn2[w])

for m in range (0,len(kt1)):
    if kt1[m]=="JAKARTA BARAT":
        kfn3.append(kt1[m])
        jfn3.append(jm1[m])
        kmfn3.append(km1[m])
        d3 = 0
        for e in range (0,len(jfn3)):
            d3 = d3+int(jfn3[e])

for l in range(0,len(kt1)):
    if kt1[l]=="JAKARTA SELATAN":
        kfn4.append(kt1[l])
        jfn4.append(jm1[l])
        kmfn4.append(km1[l])
        d4 = 0
        for y in range (0,len(jfn4)):
            d4=d4+int(jfn4[y])

for b in range(0,len(kt1)):
    if kt1[b]=="JAKARTA TIMUR":
        kfn5.append(kt1[b])
        jfn5.append(jm1[b])
        kmfn5.append(km1[b])
        d5 = 0
        for s in range(0,len(jfn5)):
            d5= d5+ int(jfn5[s])

#BULAN MARET
kt2 = (dt2["Kota Kabupaten"]).tolist()
jm2 = (dt2["Jumlah"]).tolist()
km2 = (dt2["Jenis Kelamin"]).tolist()

kun = []
jun = []
kmun = []
kun1 = []
jun1 = []
kmun1 = []
kun2 = []
jun2= []
kmun2 = []
kun3 = []
jun3 = []
kmun3 = []
kun4 = []
jun4 = []
kmun4 = []
kun5 = []
jun5 = []
kmun5 = []
for i in range (0,len(kt2)):
    if kt2[i]=="ADM. KEPULAUAN SERIBU":
        kun.append(kt2[i])
        jun.append(jm2[i])
        kmun.append(km2[i])
        h = 0
        for w in range(0,len(jun)):
            h = h+int(jun[w])

for o in range  (0,len(kt2)):
    if kt2[o]=="JAKARTA PUSAT":
        kun1.append(kt2[o])
        jun1.append(jm2[o])
        kmun1.append(km2[o])
        h1 = 0
        for w in range(0,len(jun1)):
            h1 = h1+int(jun1[w])

for c in range(0,len(kt2)):
    if kt2[c]=="JAKARTA UTARA":
        kun2.append(kt2[c])
        jun2.append(jm2[c])
        kmun2.append(km2[c])
        h2 = 0
        for w in range(0,len(jun2)):
            h2 = h2+int(jun2[w])

for m in range (0,len(kt2)):
    if kt2[m]=="JAKARTA BARAT":
        kun3.append(kt2[m])
        jun3.append(jm2[m])
        kmun3.append(km2[m])
        h3 = 0
        for e in range (0,len(jun3)):
            h3 = h3+int(jun3[e])

for l in range(0,len(kt2)):
    if kt2[l]=="JAKARTA SELATAN":
        kun4.append(kt2[l])
        jun4.append(jm2[l])
        kmun4.append(km2[l])
        h4 = 0
        for y in range (0,len(jun4)):
            h4=h4+int(jun4[y])

for b in range(0,len(kt2)):
    if kt2[b]=="JAKARTA TIMUR":
        kun5.append(kt2[b])
        jun5.append(jm2[b])
        kmun5.append(km2[b])
        h5 = 0
        for s in range(0,len(jun5)):
            h5= h5+ int(jun5[s])

#BULAN APRIL
kt3 = (dt3["Kota Kabupaten"]).tolist()
jm3 = (dt3["Jumlah"]).tolist()
km3 = (dt3["Jenis Kelamin"]).tolist()

krn = []
jrn = []
krun = []
krn1 = []
jrn1 = []
krun1 = []
krn2 = []
jrn2 = []
krun2 = []
krn3 = []
jrn3 = []
krun3 = []
krn4 = []
jrn4 = []
krun4 = []
krn5 = []
jrn5 = []
krun5 = []
for i in range (0,len(kt3)):
    if kt3[i]=="ADM. KEPULAUAN SERIBU":
        krn.append(kt3[i])
        jrn.append(jm3[i])
        krun.append(km3[i])
        qw = 0
        for w in range(0,len(jrn)):
            qw = qw+int(jrn[w])

for o in range(0,len(kt3)):
    if kt3[o]=="JAKARTA PUSAT":
        krn1.append(kt3[o])
        jrn1.append(jm3[o])
        krun1.append(km3[o])
        qw1 = 0
        for w in range(0,len(jun1)):
            qw1 = qw1+int(jun1[w])

for c in range(0,len(kt3)):
    if kt3[c]=="JAKARTA UTARA":
        krn2.append(kt3[c])
        jrn2.append(jm3[c])
        krun2.append(km3[c])
        qw2 = 0
        for w in range(0,len(jrn2)):
            qw2 = qw2+int(jrn2[w])

for m in range (0,len(kt3)):
    if kt3[m]=="JAKARTA BARAT":
        krn3.append(kt3[m])
        jrn3.append(jm3[m])
        krun3.append(km3[m])
        qw3 = 0
        for e in range (0,len(jrn3)):
            qw3 = qw3+int(jrn3[e])

for l in range(0,len(kt3)):
    if kt3[l]=="JAKARTA SELATAN":
        krn4.append(kt3[l])
        jrn4.append(jm3[l])
        krun4.append(km3[l])
        qw4 = 0
        for y in range (0,len(jrn4)):
            qw4=qw4+int(jrn4[y])

for b in range(0,len(kt3)):
    if kt3[b]=="JAKARTA TIMUR":
        krn5.append(kt3[b])
        jrn5.append(jm3[b])
        krun5.append(km3[b])
        qw5 = 0
        for s in range(0,len(jrn5)):
            qw5= qw5+ int(jrn5[s])

#BULAN MEI
kt4 = (dt4["Kota Kabupaten"]).tolist()
jm4 = (dt4["Jumlah"]).tolist()
km4 = (dt4["Jenis Kelamin"]).tolist()

kin = []
jin = []
kiun = []
kin1 = []
jin1 = []
kiun1 = []
kin2 = []
jin2 = []
kiun2 = []
kin3 = []
jin3 = []
kiun3 = []
kin4 = []
jin4 = []
kiun4 = []
kin5 = []
jin5 = []
kiun5 = []
for i in range (0,len(kt4)):
    if kt4[i]=="ADM. KEPULAUAN SERIBU":
        kin.append(kt4[i])
        jin.append(jm4[i])
        kiun.append(km4[i])
        df = 0
        for w in range(0,len(jin)):
            df = df+int(jin[w])

for o in range(0,len(kt4)):
    if kt4[o]=="JAKARTA PUSAT":
        kin1.append(kt4[o])
        jin1.append(jm4[o])
        kiun1.append(km4[o])
        df1 = 0
        for w in range(0,len(jin1)):
            df1 = df1+int(jin1[w])

for c in range(0,len(kt4)):
    if kt4[c]=="JAKARTA UTARA":
        kin2.append(kt4[c])
        jin2.append(jm4[c])
        kiun2.append(km4[c])
        df2 = 0
        for w in range(0,len(jin2)):
            df2 = df2+int(jin2[w])

for m in range (0,len(kt4)):
    if kt4[m]=="JAKARTA BARAT":
        kin3.append(kt4[m])
        jin3.append(jm4[m])
        kiun3.append(km4[m])
        df3 = 0
        for e in range (0,len(jin3)):
            df3 = df3+int(jin3[e])

for l in range(0,len(kt4)):
    if kt4[l]=="JAKARTA SELATAN":
        kin4.append(kt4[l])
        jin4.append(jm4[l])
        kiun4.append(km4[l])
        df4 = 0
        for y in range (0,len(jin4)):
            df4=df4+int(jin4[y])

for b in range(0,len(kt4)):
    if kt4[b]=="JAKARTA TIMUR":
        kin5.append(kt4[b])
        jin5.append(jm4[b])
        kiun5.append(km4[b])
        df5 = 0
        for s in range(0,len(jin5)):
            df5= df5+ int(jin5[s])


kota = ["Januari","Februari","Maret","April","May"]
ks = np.array([q,d,h,qw,df])
jp = np.array([q1,d1,h1,qw1,df1])
ju = np.array([q2,d2,h2,qw2,df2])
jb = np.array([q3,d3,h3,qw3,df3])
js = np.array([q4,d4,h4,qw4,df4])
jt = np.array([q5,d5,h5,qw5,df5])

width = 0.1
fig, ax = plt.subplots()
plt.ylim([0,5000])

pos_x = np.arange(len(kota))
bar1 = ax.bar(pos_x+0.5*width, ks ,width,label="Kepulauan Seribu",color='#FFD07B')
bar2 = ax.bar(pos_x+1.5*width, jp ,width,label="Jakarta Pusat",color='#F5BB00')
bar3 = ax.bar(pos_x+2.5*width,ju, width,label="Jakarta Utara",color='#EC9F05')
bar4 = ax.bar(pos_x+3.5*width,jb, width,label="Jakarta Barat",color='#D76A03')
bar5 = ax.bar(pos_x+4.5*width,js, width,label="Jakarta selatan",color='#BF3100')
bar6 = ax.bar(pos_x+5.5*width,jt, width,label="Jakarta Timur",color='#7F557D')

ax.set_ylabel("Persebaran Jumlah Kelahiran")
ax.bar_label(bar1, padding=10)
ax.bar_label(bar2, padding=10)
ax.bar_label(bar3, padding=10)
ax.bar_label(bar4, padding=10)
ax.bar_label(bar5, padding=10)
ax.bar_label(bar6, padding=10)
ax.set_xticks(pos_x+0.35)
ax.set_xticklabels(kota)
ax.set_title("Persentase Kelahiran Januari - Mei")
ax.legend(loc='upper left')

plt.show()

