import time
import tkinter
import pandas as pd
from tkinter.ttk import *
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import FALSE
from tkinter import messagebox

run = tkinter.Tk()
run.config(bg="crimson")
run.geometry("770x670")
run.title("Population Data Access")
run.resizable(FALSE, FALSE)
run.eval("tk::PlaceWindow . center")

def xv():
    data = pd.read_excel("datasetProject1\KedatanganPenduduk.xlsx", sheet_name="April 2021")
    data1 = pd.read_excel("datasetProject1\KepergianPenduduk.xlsx", sheet_name="April 2021")
    data2 = pd.read_excel("datasetProject1\Kelahiran.xlsx", sheet_name="April 2021")
    data3 = pd.read_excel("datasetProject1\kematian.xlsx", sheet_name="April 2021")

    tahun3 = (data3["Tahun"]).tolist()
    bulan3 = (data3["Bulan"]).tolist()
    kota3 = (data3["Kota Kabupaten"]).tolist()
    kecamatan3 = (data3["Kecamatan"]).tolist()
    kelurahan3 = (data3["Kelurahan"]).tolist()
    kelamin3 = (data3["Jenis Kelamin"]).tolist()
    jumlah3 = (data3["Jumlah"]).tolist()
    ds3 = pd.DataFrame({
        "Tahun": tahun3,
        "Bulan": bulan3,
        "Kota": kota3,
        "Kecamatan": kecamatan3,
        "Kelurahan": kelurahan3,
        "Jenis Kelamin": kelamin3,
        "Jumlah": jumlah3
    })

    tahun2 = (data2["Tahun"]).tolist()
    bulan2 = (data2["Bulan"]).tolist()
    kota2 = (data2["Kota Kabupaten"]).tolist()
    kecamatan2 = (data2["Kecamatan"]).tolist()
    kelurahan2 = (data2["Kelurahan"]).tolist()
    kelamin2 = (data2["Jenis Kelamin"]).tolist()
    jumlah2 = (data2["Jumlah"]).tolist()
    ds2 = pd.DataFrame({
        "Tahun": tahun2,
        "Bulan": bulan2,
        "Kota": kota2,
        "Kecamatan": kecamatan2,
        "Kelurahan": kelurahan2,
        "Jenis Kelamin": kelamin2,
        "Jumlah": jumlah2
    })

    tahun1 = (data1["Tahun"]).tolist()
    bulan1 = (data1["Bulan"]).tolist()
    kota1 = (data1["Kota Kabupaten"]).tolist()
    kecamatan1 = (data1["Kecamatan"]).tolist()
    kelurahan1 = (data1["Kelurahan"]).tolist()
    kelamin1 = (data1["Jenis Kelamin"]).tolist()
    jumlah1 = (data1["Jumlah"]).tolist()
    ds1 = pd.DataFrame({
        "Tahun": tahun1,
        "Bulan": bulan1,
        "Kota": kota1,
        "Kecamatan": kecamatan1,
        "Kelurahan": kelurahan1,
        "Jenis Kelamin": kelamin1,
        "Jumlah": jumlah1
    })

    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    ds = pd.DataFrame({
        "Tahun": tahun,
        "Bulan": bulan,
        "Kota": kota,
        "Kecamatan": kecamatan,
        "Kelurahan": kelurahan,
        "Jenis Kelamin": kelamin,
        "Jumlah": jumlah
    })

    with pd.ExcelWriter("datasetProject1\HasilSave\ "+nv.get()+".xlsx") as writer:
        ds.to_excel(writer, sheet_name="Kedatangan April 2021")
        ds1.to_excel(writer, sheet_name="Kepergian April 2021")
        ds2.to_excel(writer, sheet_name="Kelahiran April 2021")
        ds3.to_excel(writer, sheet_name="Kematian April 2021")
        print("Menyimpan File Berhasil")

global nv
nv=StringVar()
nv.get()
def sv3():
    forget()
    fr9.pack(fill="both", expand=1)
    gq = Label(fr9, text="Masukkan Nama File :", bg="lavender", font=('Times', 12, 'bold'))
    gq.place(x=185, y=280)
    ec = Entry(fr9, textvariable=nv, width=30, font=('Times', 12))
    ec.place(x=350, y=280)
    gh3 = Button(fr9, text="Simpan", width=10, font=('Times', 12, 'bold'), command=xv)
    gh3.place(y=320, x=325)
def sv2():
    forget()
    fr8.pack(fill="both", expand=1)
    gq = Label(fr8, text="Masukkan Nama File :", bg="crimson", font=('Times', 12, 'bold'))
    gq.place(x=185, y=280)
    ec = Entry(fr8, textvariable=nv, width=30, font=('Times', 12))
    ec.place(x=350, y=280)
    gh2 = Button(fr8, text="Simpan", width=10, font=('Times', 12, 'bold'), command=xv)
    gh2.place(y=320, x=325)
def sv1():
    forget()
    fr7.pack(fill="both", expand=1)
    gq = Label(fr7, text="Masukkan Nama File :", bg="khaki", font=('Times', 12, 'bold'))
    gq.place(x=185, y=280)
    ec = Entry(fr7, textvariable=nv, width=30, font=('Times', 12))
    ec.place(x=350, y=280)
    gh1 = Button(fr7, text="Simpan", width=10, font=('Times', 12, 'bold'),command=xv)
    gh1.place(y=320, x=325)
def sv():
    forget()
    fr6.pack(fill="both", expand=1)
    g=Label(fr6,text="Masukkan Nama File :", bg="green", font=('Times', 12, 'bold'))
    g.place(x=185, y=280)
    ec = Entry(fr6,textvariable=nv, width=30, font=('Times', 12))
    ec.place(x=350, y=280)
    gh=Button(fr6,text="Simpan", width=10, font=('Times', 12, 'bold'), command=xv)
    gh.place(y=320, x=325)

d = IntVar()
d1 = IntVar()
d.get()
d1.get()

def meninggal():
    forget()
    fr5.pack(fill='both', expand=1)
    l53 = Label(fr5, text="Akses Data Kematian Provinsi Jakarta", bg="deep sky blue", font=('Times', 12, 'bold'))
    l63 = Label(fr5, text="Pilih Tingkat Data :", bg="deep sky blue", font=('Times', 12))
    l53.place(x=245, y=30)
    l63.place(x=60, y=80)

    rbc = Checkbutton(fr5, text="Kota/Kabupaten", variable=d, onvalue=1, offvalue=14, bg="deep sky blue", font=('Times', 11))
    rbc.deselect()
    rbc.place(x=60, y=105)
    rb13 = Checkbutton(fr5, text="Kecamatan", variable=d1, onvalue=1, offvalue=16, bg="deep sky blue",font=('Times', 11))
    rb13.deselect()
    rb13.place(x=60, y=130)

    btn23 = Button(fr5, text="Lanjut", width=10, font=('Times', 12, 'bold'), command=bt5)
    btn23.place(x=60, y=165)

    btn43 = Button(fr5, text="Visualasi Data Semua Kabupaten", width=25, font=('Times', 12, 'bold'), command=plot4)
    btn43.place(x=450, y=165)

    bts3 = Button(fr5, text="Visualasi Keseluruhan Data", width=25, font=('Times', 12, 'bold'), command=all)
    bts3.place(x=265, y=420)

    nk4 = Button(fr5, text="Save", width=10, font=('Times', 12, 'bold'), command=sv3)
    nk4.place(y=470, x=325)

c = IntVar()
c1 = IntVar()
c.get()
c1.get()


def lahir():
    forget()
    fr4.pack(fill="both", expand=1)

    l52 = Label(fr4, text="Akses Data Kelahiran Provinsi Jakarta", bg="dark orange", font=('Times', 12, 'bold'))
    l62 = Label(fr4, text="Pilih Tingkat Data :", bg="dark orange", font=('Times', 12))
    l52.place(x=245, y=30)
    l62.place(x=60, y=80)

    rbb = Checkbutton(fr4, text="Kota/Kabupaten", variable=c, onvalue=1, offvalue=10, bg="dark orange", font=('Times', 11))
    rbb.deselect()
    rbb.place(x=60, y=105)
    rb12 = Checkbutton(fr4, text="Kecamatan", variable=c1, onvalue=1, offvalue=12, bg="dark orange", font=('Times', 11))
    rb12.deselect()
    rb12.place(x=60, y=130)

    btn22 = Button(fr4, text="Lanjut", width=10, font=('Times', 12, 'bold'), command=bt4)
    btn22.place(x=60, y=165)

    btn42 = Button(fr4, text="Visualasi Data Semua Kabupaten", width=25, font=('Times', 12, 'bold'), command=plot3)
    btn42.place(x=450, y=165)

    bts2 = Button(fr4, text="Visualasi Keseluruhan Data", width=25, font=('Times', 12, 'bold'), command=all)
    bts2.place(x=265, y=420)

    nk2 = Button(fr4, text="Save", width=10, font=('Times', 12, 'bold'), command=sv2)
    nk2.place(y=470, x=325)


b = IntVar()
b1 = IntVar()
b.get()
b1.get()

def pergi():
    forget()
    fr3.pack(fill="both", expand=1)

    l51 = Label(fr3, text="Akses Data Kepergian Provinsi Jakarta", bg="orange red", font=('Times', 12, 'bold'))
    l61 = Label(fr3, text="Pilih Tingkat Data :", bg="orange red", font=('Times', 12))
    l51.place(x=245, y=30)
    l61.place(x=60, y=80)

    rba = Checkbutton(fr3, text="Kota/Kabupaten", variable=b, onvalue=2, offvalue=0, bg="orange red",font=('Times', 11))
    rba.deselect()
    rba.place(x=60, y=105)
    rb11 = Checkbutton(fr3, text="Kecamatan", variable=b1, onvalue=2, offvalue=0, bg="orange red", font=('Times', 11))
    rb11.deselect()
    rb11.place(x=60, y=130)

    btn21 = Button(fr3, text="Lanjut", width=10, font=('Times', 12, 'bold'), command=bt3)
    btn21.place(x=60, y=165)

    btn41 = Button(fr3, text="Visualasi Data Semua Kabupaten", width=25, font=('Times', 12, 'bold'), command=plot2)
    btn41.place(x=450, y=165)

    bts1 = Button(fr3, text="Visualasi Keseluruhan Data", width=25, font=('Times', 12, 'bold'), command=all)
    bts1.place(x=265, y=420)

    nk1 = Button(fr3, text="Save", width=10, font=('Times', 12, 'bold'), command=sv1)
    nk1.place(y=470, x=325)

a = IntVar()
a1 = IntVar()
a.get()
a1.get()

def datang():
    forget()

    fr2.pack(fill="both", expand=1)

    l5 = Label(fr2, text="Akses Data Kedatangan Provinsi Jakarta", bg="Coral", font=('Times', 12, 'bold'))
    l6 = Label(fr2, text="Pilih Tingkat Data :", bg="Coral", font=('Times', 12))
    l5.place(x=245, y=30)
    l6.place(x=60, y=80)

    rb = Checkbutton(fr2, text="Kota/Kabupaten", variable=a, onvalue=1, offvalue=0, bg="Coral", font=('Times', 11))
    rb.deselect()
    rb.place(x=60, y=105)
    rb1 = Checkbutton(fr2, text="Kecamatan", variable=a1, onvalue=1, offvalue=0, bg="Coral", font=('Times', 11))
    rb1.deselect()
    rb1.place(x=60, y=130)

    btn2 = Button(fr2, text="Lanjut", width=10, font=('Times', 12, 'bold'), command=bt2)
    btn2.place(x=60, y=165)
    btn4 = Button(fr2, text="Visualasi Data Semua Kabupaten", width=25, font=('Times', 12, 'bold'), command=plot)
    btn4.place(x=450, y=165)

    bts = Button(fr2, text="Visualasi Keseluruhan Data", width=25, font=('Times', 12, 'bold'), command=all)
    bts.place(x=265, y=420)

    nk = Button(fr2, text="Save", width=10, font=('Times', 12, 'bold'), command=sv)
    nk.place(y=470, x=325)

m = IntVar()
m.get()

def open1():
    if m.get() == 0:
        forget()

        name1 = nama.get()
        npm1 = npm.get()

        awalan = Menu(run)

        fr1.pack(fill='both', expand=1)

        l3 = Label(fr1, text=name1 + " / " + npm1, bg="Khaki", font=('Times', 12, 'bold'))
        l4 = Label(fr1, text="Anda Sedang Mengakses Data, Gunakan Menu Yang Ada", bg="Khaki",font=('Times', 12, 'bold'))
        l4.place(x=200, y=320)
        l3.place(x=260, y=295)

        akses_kedatangan = Menu(awalan, tearoff=0)
        akses_kepergian = Menu(awalan, tearoff=0)
        akses_kelahiran = Menu(awalan, tearoff=0)
        akses_kematian = Menu(awalan, tearoff=0)
        exitmenu = Menu(awalan, tearoff=0)

        akses_kedatangan.add_command(label="Mengenai Kedatangan", font=('Times', 10), command=datang)
        akses_kepergian.add_command(label="Mengenai Kepergian", font=('Times', 10), command=pergi)
        akses_kelahiran.add_command(label="Mengenai Kelahiran", font=('Times', 10), command=lahir)
        akses_kematian.add_command(label="Mengenai Kematian", font=('Times', 10), command=meninggal)
        exitmenu.add_command(label="Exit From This Section", command=run.quit, font=('Times', 10))

        awalan.add_cascade(label="Arrival", menu=akses_kedatangan)
        awalan.add_cascade(label="Departure", menu=akses_kepergian)
        awalan.add_cascade(label="Nascency", menu=akses_kelahiran)
        awalan.add_cascade(label="Mortality", menu=akses_kematian)
        awalan.add_cascade(label="Exit", menu=exitmenu)

        run.config(menu=awalan)
    elif nama.get()==NONE and npm.get()==NONE:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Isi Data!!!")
    elif m.get() != 0:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Isi Data dan Beri Centang Pada Correct Data!!!")

def forget():
    fr1.pack_forget()
    fr2.pack_forget()
    fr3.pack_forget()
    fr4.pack_forget()
    fr5.pack_forget()
    fr6.pack_forget()
    fr7.pack_forget()
    fr8.pack_forget()
    fr9.pack_forget()
    rx.pack_forget()
    l1.place_forget()
    ll1.place_forget()
    e1.place_forget()
    l2.place_forget()
    e2.place_forget()
    btn1.place_forget()
    ct.place_forget()

nama = StringVar()
npm = StringVar()
nama.get()
npm.get()
nama.set("Edoward Cornelius Tarigan")
npm.set(200610973)

ll1 = Label(run, text="Selamat Datang, Masukkan Data Anda", bg="crimson", font=('Times', 14, 'bold'))
ll1.place(x=230, y=215)
l1 = Label(run, text="Nama :", bg="crimson", font=('Times', 12))
l1.place(x=185, y=262)
e1 = Entry(run, textvariable=nama, width=40, font=('Times', 12))
e1.place(x=240, y=265)

l2 = Label(run, text="NPM :", bg="crimson", font=('Times', 12))
l2.place(x=185, y=303)
e2 = Entry(run, textvariable=npm, width=40, font=('Times', 12))
e2.place(x=240, y=305)

ct = Checkbutton(run, text="Correct Data", bg="crimson", variable=m, onvalue=0, offvalue=9, font=('Times', 12))
ct.place(x=240, y=330)
ct.deselect()

btn1 = Button(run, text="Akses Data", bg='orange', width=12, height=0, font=('Times', 12, 'bold'), command=open1)
btn1.place(y=365, x=325)

fr1 = Frame(run, width=770, height=670, background='Khaki')
fr2 = Frame(run, width=770, height=670, background='Coral')
fr3 = Frame(run, width=770, height=670, background='orange red')
fr4 = Frame(run, width=770, height=670, background='dark orange')
fr5 = Frame(run, width=770, height=670, background='deep sky blue')
fr6 = Frame(run, width=770,height=670, background='green')
fr7 = Frame(run, width=770,height=670, background='khaki')
fr8 = Frame(run, width=770,height=670, background='crimson')
fr9 = Frame(run, width=770,height=670, background='lavender')
rx=Frame(run,width=770,height=670,background='powder blue')

bar =Progressbar(rx,length=300,orient=HORIZONTAL)
bar.place(x=245, y=300)

percent=StringVar()
text=StringVar()
lb=Label(rx, textvariable=percent,font=('Times', 12, 'bold'),background='powder blue')
lb.place(y=325,x=385)
tb=Label(rx,textvariable=text,font=('Times', 12, 'bold'),background='powder blue')
tb.place(y=355,x=250)

def all():
    forget()
    rx.pack(fill='both', expand=1)
    task=20
    x=0
    while (x<task):
        time.sleep(0.5)
        bar['value']+=5
        x+=1
        rx.update_idletasks()
        percent.set(str(int((x/task)*100))+"%")
        text.set("Generating to Matplotlib on Progress "+str(x)+"/"+str(task))
    run.destroy()
    data = pd.read_excel("datasetProject1\KedatanganPenduduk.xlsx", sheet_name="April 2021")
    data1 = pd.read_excel("datasetProject1\KepergianPenduduk.xlsx", sheet_name="April 2021")
    data2 = pd.read_excel("datasetProject1\Kelahiran.xlsx", sheet_name="April 2021")
    data3 = pd.read_excel("datasetProject1\Kematian.xlsx", sheet_name="April 2021")
    x = data["Kota Kabupaten"]
    y = data["Jumlah"]
    plt.scatter(x, y, marker='o', color='red')
    x1 = data["Kota Kabupaten"]
    y1 = data1["Jumlah"]
    plt.scatter(x1, y1, marker='v', color='green')
    x2 = data["Kota Kabupaten"]
    y2 = data2["Jumlah"]
    plt.scatter(x2, y2, marker='*', color='blue')
    x3 = data["Kota Kabupaten"]
    y3 = data3["Jumlah"]
    plt.scatter(x3, y3, marker='x', color='orange', )
    plt.title("Persebaran Keseluruhan Data Bulan April 2021")
    plt.xlabel("Kota/Kabupaten")
    plt.ylabel("Jumlah Keseluruhan")
    plt.grid(color='black', linestyle='-', linewidth=0.5)
    plt.legend(['Kedatangan', 'Kepergian', 'Kelahiran', 'Kematian'], loc='upper left')
    plt.show()


def plot():
    data = pd.read_excel("datasetProject1\KedatanganPenduduk.xlsx", sheet_name="April 2021")
    x=data["Kota Kabupaten"]
    z=data["Jumlah"]
    plt.scatter(x,z,marker='o',color='red',)
    plt.title("Persebaran Jumlah Kedatangan Penduduk Bulan April 2021")
    plt.xlabel("Kota/Kabupaten")
    plt.ylabel("Jumlah Kedatangan")
    plt.grid(color = 'blue', linestyle = '-', linewidth = 1)
    plt.show()

def plot2():
    data = pd.read_excel("datasetProject1\KepergianPenduduk.xlsx", sheet_name="April 2021")
    x = data["Kota Kabupaten"]
    z = data["Jumlah"]
    plt.scatter(x, z, marker='*', color='green', )
    plt.title("Persebaran Jumlah Kepergian Penduduk Bulan April 2021")
    plt.xlabel("Kota/Kabupaten")
    plt.ylabel("Jumlah Kepergian")
    plt.grid(color='blue', linestyle='-', linewidth=1)
    plt.show()

def plot3():
    data = pd.read_excel("datasetProject1\Kelahiran.xlsx", sheet_name="April 2021")
    x = data["Kota Kabupaten"]
    z = data["Jumlah"]
    plt.scatter(x, z, marker='^', color='blue', )
    plt.title("Persebaran Jumlah Kelahiran Penduduk Bulan April 2021")
    plt.xlabel("Kota/Kabupaten")
    plt.ylabel("Jumlah Kelahiran")
    plt.grid(color='blue', linestyle='-', linewidth=1)
    plt.show()

def plot4():
    data = pd.read_excel("datasetProject1\Kematian.xlsx", sheet_name="April 2021")
    x = data["Kota Kabupaten"]
    z = data["Jumlah"]
    plt.scatter(x, z, marker='v', color='orange', )
    plt.title("Persebaran Jumlah Kematian Penduduk Bulan April 2021")
    plt.xlabel("Kota Kabupaten")
    plt.ylabel("Jumlah kematian")
    plt.grid(color='blue', linestyle='-', linewidth=1)
    plt.show()

def s1():
    data = pd.read_excel("datasetProject1\KedatanganPenduduk.xlsx",sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    global tahunbaru
    global bulanbaru
    global kotabaru
    global kecamatanbaru
    global kelurahanbaru
    global kelaminbaru
    global jumlahbaru
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if a11.get()==1 and a21.get()==1 and a31.get()==1 and a41.get()==1 and a51.get()==1 and a61.get()==1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a11.get()==0 and a21.get()==0 and a31.get()==0 and a41.get()==0 and a51.get()==0 and a61.get()==0:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a11.get()==1:
        for q in range (0,len(kota)):
            if kota[q]=="ADM. KEPULAUAN SERIBU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                ym=Label(fr2,text="Rata-rata = "+ str(average),bg="Coral", font=('Times', 12))
                ym.place(x=450,y=110)
    elif a21.get()==1:
        for q in range (0,len(kota)):
            if kota[q]=="JAKARTA PUSAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                ym1=Label(fr2,text="Rata-rata = "+ str(average),bg="Coral", font=('Times', 12))
                ym1.place(x=450,y=110)
    elif a31.get()==1:
        for q in range (0,len(kota)):
            if kota[q]=="JAKARTA UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                ym2=Label(fr2,text="Rata-rata = "+ str(average),bg="Coral", font=('Times', 12))
                ym2.place(x=450,y=110)
    elif a41.get()==1:
        for q in range (0,len(kota)):
            if kota[q]=="JAKARTA BARAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                ym3=Label(fr2,text="Rata-rata = "+ str(average),bg="Coral", font=('Times', 12))
                ym3.place(x=450,y=110)
    elif a51.get()==1:
        for q in range (0,len(kota)):
            if kota[q]=="JAKARTA SELATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                ym4=Label(fr2,text="Rata-rata = "+ str(average),bg="Coral", font=('Times', 12))
                ym4.place(x=450,y=110)
    elif a61.get()==1:
        for q in range (0,len(kota)):
            if kota[q]=="JAKARTA TIMUR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                ym5=Label(fr2,text="Rata-rata = "+ str(average),bg="Coral", font=('Times', 12))
                ym5.place(x=450,y=110)

def s2():
    data = pd.read_excel("datasetProject1\KepergianPenduduk.xlsx",sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru= []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if a12.get()==1 and a22.get()==1 and a32.get()==1 and a42.get()==1 and a52.get()==1 and a62.get()==1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a12.get()==0 and a22.get()==0 and a32.get()==0 and a42.get()==0 and a52.get()==0 and a62.get()==0:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a12.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "ADM. KEPULAUAN SERIBU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mylabel=Label(fr3,text="Rata-rata = "+ str(average),bg="Orange Red", font=('Times', 12))
                mylabel.place(x=450,y=110)
    elif a22.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "JAKARTA PUSAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mylabel1=Label(fr3,text="Rata-rata = "+ str(average),bg="Orange Red", font=('Times', 12))
                mylabel1.place(x=450,y=110)
    elif a32.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "JAKARTA UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mylabel2=Label(fr3,text="Rata-rata = "+ str(average),bg="Orange Red", font=('Times', 12))
                mylabel2.place(x=450,y=110)
    elif a42.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "JAKARTA BARAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mylabel3=Label(fr3,text="Rata-rata = "+ str(average),bg="Orange Red", font=('Times', 12))
                mylabel3.place(x=450,y=110)
    elif a52.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "JAKARTA SELATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mylabel4=Label(fr3,text="Rata-rata = "+ str(average),bg="Orange Red", font=('Times', 12))
                mylabel4.place(x=450,y=110)
    elif a62.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "JAKARTA TIMUR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mylabel5=Label(fr3,text="Rata-rata = "+ str(average),bg="Orange Red", font=('Times', 12))
                mylabel5.place(x=450,y=110)

def s3():
    data = pd.read_excel("datasetProject1\Kelahiran.xlsx", sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if a13.get()==1 and a23.get()==1 and a33.get()==1 and a43.get()==1 and a53.get()==1 and a63.get()==1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a13.get()==0 and a23.get()==0 and a33.get()==0 and a43.get()==0 and a53.get()==0 and a63.get()==0:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a13.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "ADM. KEPULAUAN SERIBU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                my=Label(fr4,text="Rata-rata = "+ str(average),bg="dark orange", font=('Times', 12))
                my.place(x=450,y=110)
    elif a23.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA PUSAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                my1 = Label(fr4, text="Rata-rata = " + str(average), bg="dark orange", font=('Times', 12))
                my1.place(x=450, y=110)
    elif a33.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                my2 = Label(fr4, text="Rata-rata = " + str(average), bg="dark orange", font=('Times', 12))
                my2.place(x=450, y=110)
    elif a43.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA BARAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                my3 = Label(fr4, text="Rata-rata = " + str(average), bg="dark orange", font=('Times', 12))
                my3.place(x=450, y=110)
    elif a53.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA SELATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                my4 = Label(fr4, text="Rata-rata = " + str(average), bg="dark orange", font=('Times', 12))
                my4.place(x=450, y=110)
    elif a63.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA TIMUR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                my5 = Label(fr4, text="Rata-rata = " + str(average), bg="dark orange", font=('Times', 12))
                my5.place(x=450, y=110)

def s4():
    data = pd.read_excel("datasetProject1\Kematian.xlsx", sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if a14.get()==1 and a24.get()==1 and a34.get()==1 and a44.get()==1 and a54.get()==1 and a64.get()==1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a14.get()==0 and a24.get()==0 and a34.get()==0 and a44.get()==0 and a54.get()==0 and a64.get()==0:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota!!!")
    elif a14.get()==1:
        for q in range (0,len(kota)):
            if kota[q] == "ADM. KEPULAUAN SERIBU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp= 0
                male = 0
                female = 0
                for w in range (0,len(jumlahbaru)):
                    tp=tp+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Laki-Laki":
                        male=male+int(jumlahbaru[w])
                for w in range (0,len(jumlahbaru)):
                    if kelaminbaru[w]=="Perempuan":
                        female=female+int(jumlahbaru[w])
                average= round(tp/len(jumlahbaru),2)
                mm=Label(fr5,text="Rata-rata = "+ str(average),bg="deep sky blue", font=('Times', 12))
                mm.place(x=450,y=110)
    elif a24.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA PUSAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                mm1 = Label(fr5, text="Rata-rata = " + str(average), bg="deep sky blue", font=('Times', 12))
                mm1.place(x=450, y=110)
    elif a34.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                mm2 = Label(fr5, text="Rata-rata = " + str(average), bg="deep sky blue", font=('Times', 12))
                mm2.place(x=450, y=110)
    elif a44.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA BARAT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                mm3 = Label(fr5, text="Rata-rata = " + str(average), bg="deep sky blue", font=('Times', 12))
                mm3.place(x=450, y=110)
    elif a54.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA SELATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                mm4 = Label(fr5, text="Rata-rata = " + str(average), bg="deep sky blue", font=('Times', 12))
                mm4.place(x=450, y=110)
    elif a64.get()==1:
        for q in range(0,len(kota)):
            if kota[q]=="JAKARTA TIMUR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                average = round(tp / len(jumlahbaru), 2)
                mm5 = Label(fr5, text="Rata-rata = " + str(average), bg="deep sky blue", font=('Times', 12))
                mm5.place(x=450, y=110)

def k():
    data = pd.read_excel("datasetProject1\KedatanganPenduduk.xlsx", sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if tekan.get()=="Kepulauan Seribu Utara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEPULAUAN SERIBU UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv.place(x=450, y=110)
    elif tekan.get()=="Gambir":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GAMBIR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv1 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv1.place(x=450, y=110)
    elif tekan.get()=="Sawah Besar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SAWAH BESAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv2 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv2.place(x=450, y=110)
    elif tekan.get()=="Kemayoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMAYORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv3 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv3.place(x=450, y=110)
    elif tekan.get()=="Senen":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SENEN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv4 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv4.place(x=450, y=110)
    elif tekan.get()=="Cempaka Putih":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CEMPAKA PUTIH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv5 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv5.place(x=450, y=110)
    elif tekan.get()=="Menteng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MENTENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv6 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv6.place(x=450, y=110)
    elif tekan.get()=="Tanah Abang":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANAH ABANG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv7 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv7.place(x=450, y=110)
    elif tekan.get()=="Johar Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JOHAR BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv8 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv8.place(x=450, y=110)
    elif tekan.get()=="Penjaringan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PENJARINGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv9 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv9.place(x=450, y=110)
    elif tekan.get()=="Tanjung Priok":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANJUNG PRIOK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv10 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv10.place(x=450, y=110)
    elif tekan.get()=="Koja":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KOJA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv11 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv11.place(x=450, y=110)
    elif tekan.get()=="cilincing":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILINCING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv12 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv12.place(x=450, y=110)
    elif tekan.get()=="Pandemangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PADEMANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv13 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv13.place(x=450, y=110)
    elif tekan.get()=="Kelapa Gading":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KELAPA GADING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv14 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv14.place(x=450, y=110)
    elif tekan.get()=="Cengkareng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CENGKARENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv15 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv15.place(x=450, y=110)
    elif tekan.get()=="Grogol Petamburan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GROGOL PETAMBURAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv16 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv16.place(x=450, y=110)
    elif tekan.get()=="Taman Sari":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMAN SARI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv17 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv17.place(x=450, y=110)
    elif tekan.get()=="Tambora":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMBORA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv18 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv18.place(x=450, y=110)
    elif tekan.get()=="Kebon Jeruk":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBON JERUK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv19 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv19.place(x=450, y=110)
    elif tekan.get()=="Kali Deres":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KALI DERES":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv20 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv20.place(x=450, y=110)
    elif tekan.get()=="Pal Merah":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PAL MERAH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv21 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv21.place(x=450, y=110)
    elif tekan.get()=="Kembangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMBANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv22 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv22.place(x=450, y=110)
    elif tekan.get()=="Tebet":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TEBET":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv23 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv23.place(x=450, y=110)
    elif tekan.get()=="Setia Budi":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SETIA BUDI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv24 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv24.place(x=450, y=110)
    elif tekan.get()=="Mampang Prapatan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAMPANG PRAPATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv25 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv25.place(x=450, y=110)
    elif tekan.get()=="Pasar Minggu":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR MINGGU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv26 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv26.place(x=450, y=110)
    elif tekan.get()=="Kebayoran Lama":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN LAMA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv27 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv27.place(x=450, y=110)
    elif tekan.get()=="Cilandak":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILANDAK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv28 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv28.place(x=450, y=110)
    elif tekan.get()=="Kebayoran Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv29 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv29.place(x=450, y=110)
    elif tekan.get()=="Pancoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PANCORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv30 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv30.place(x=450, y=110)
    elif tekan.get()=="Jagakarsa":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JAGAKARSA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv31 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv31.place(x=450, y=110)
    elif tekan.get()=="Pesanggrahan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PESANGGRAHAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv32 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv32.place(x=450, y=110)
    elif tekan.get()=="Matraman":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MATRAMAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv33 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv33.place(x=450, y=110)
    elif tekan.get()=="Pulo Gadung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PULO GADUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv34 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv34.place(x=450, y=110)
    elif tekan.get()=="Jatinegara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JATINEGARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv35 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv35.place(x=450, y=110)
    elif tekan.get()=="Kramatjati":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KRAMATJATI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv36 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv36.place(x=450, y=110)
    elif tekan.get()=="Pasar Rebo":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR REBO":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv37 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv37.place(x=450, y=110)
    elif tekan.get()=="Cakung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CAKUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv38 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv38.place(x=450, y=110)
    elif tekan.get()=="Duren Sawit":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="DUREN SAWIT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv39 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv39.place(x=450, y=110)
    elif tekan.get()=="Makasar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAKASAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv40 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv40.place(x=450, y=110)
    elif tekan.get()=="Ciracas":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIRACAS":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv41.place(x=450, y=110)
    elif tekan.get()=="Cipayung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIPAYUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr2, text="Rata-rata = " + str(rerata), bg="Coral", font=('Times', 12))
                cv41.place(x=450, y=110)

def k1():
    data = pd.read_excel("datasetProject1\KepergianPenduduk.xlsx", sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if tekan1.get()=="Kepulauan Seribu Utara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEPULAUAN SERIBU UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv.place(x=450, y=110)
    elif tekan1.get()=="Gambir":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GAMBIR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv1 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv1.place(x=450, y=110)
    elif tekan1.get()=="Sawah Besar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SAWAH BESAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv2 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv2.place(x=450, y=110)
    elif tekan1.get()=="Kemayoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMAYORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv3 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv3.place(x=450, y=110)
    elif tekan1.get()=="Senen":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SENEN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv4 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv4.place(x=450, y=110)
    elif tekan1.get()=="Cempaka Putih":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CEMPAKA PUTIH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv5 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv5.place(x=450, y=110)
    elif tekan1.get()=="Menteng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MENTENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv6 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv6.place(x=450, y=110)
    elif tekan1.get()=="Tanah Abang":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANAH ABANG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv7 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv7.place(x=450, y=110)
    elif tekan1.get()=="Johar Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JOHAR BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv8 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv8.place(x=450, y=110)
    elif tekan1.get()=="Penjaringan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PENJARINGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv9 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv9.place(x=450, y=110)
    elif tekan1.get()=="Tanjung Priok":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANJUNG PRIOK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv10 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv10.place(x=450, y=110)
    elif tekan1.get()=="Koja":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KOJA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv11 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv11.place(x=450, y=110)
    elif tekan1.get()=="cilincing":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILINCING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv12 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv12.place(x=450, y=110)
    elif tekan1.get()=="Pandemangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PADEMANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv13 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv13.place(x=450, y=110)
    elif tekan1.get()=="Kelapa Gading":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KELAPA GADING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv14 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv14.place(x=450, y=110)
    elif tekan1.get()=="Cengkareng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CENGKARENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv15 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv15.place(x=450, y=110)
    elif tekan1.get()=="Grogol Petamburan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GROGOL PETAMBURAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv16 = Label(fr2, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv16.place(x=450, y=110)
    elif tekan1.get()=="Taman Sari":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMAN SARI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv17 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv17.place(x=450, y=110)
    elif tekan1.get()=="Tambora":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMBORA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv18 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv18.place(x=450, y=110)
    elif tekan1.get()=="Kebon Jeruk":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBON JERUK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv19 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv19.place(x=450, y=110)
    elif tekan1.get()=="Kali Deres":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KALI DERES":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv20 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv20.place(x=450, y=110)
    elif tekan1.get()=="Pal Merah":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PAL MERAH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv21 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv21.place(x=450, y=110)
    elif tekan1.get()=="Kembangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMBANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv22 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv22.place(x=450, y=110)
    elif tekan1.get()=="Tebet":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TEBET":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv23 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv23.place(x=450, y=110)
    elif tekan1.get()=="Setia Budi":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SETIA BUDI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv24 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv24.place(x=450, y=110)
    elif tekan1.get()=="Mampang Prapatan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAMPANG PRAPATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv25 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv25.place(x=450, y=110)
    elif tekan1.get()=="Pasar Minggu":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR MINGGU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv26 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv26.place(x=450, y=110)
    elif tekan1.get()=="Kebayoran Lama":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN LAMA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv27 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv27.place(x=450, y=110)
    elif tekan1.get()=="Cilandak":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILANDAK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv28 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange redl", font=('Times', 12))
                cv28.place(x=450, y=110)
    elif tekan1.get()=="Kebayoran Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv29 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv29.place(x=450, y=110)
    elif tekan1.get()=="Pancoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PANCORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv30 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv30.place(x=450, y=110)
    elif tekan1.get()=="Jagakarsa":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JAGAKARSA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv31 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv31.place(x=450, y=110)
    elif tekan1.get()=="Pesanggrahan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PESANGGRAHAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv32 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv32.place(x=450, y=110)
    elif tekan1.get()=="Matraman":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MATRAMAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv33 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv33.place(x=450, y=110)
    elif tekan1.get()=="Pulo Gadung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PULO GADUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv34= Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv34.place(x=450, y=110)
    elif tekan1.get()=="Jatinegara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JATINEGARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv35 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv35.place(x=450, y=110)
    elif tekan1.get()=="Kramatjati":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KRAMATJATI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv36 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv36.place(x=450, y=110)
    elif tekan1.get()=="Pasar Rebo":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR REBO":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv37 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv37.place(x=450, y=110)
    elif tekan1.get()=="Cakung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CAKUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv38 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv38.place(x=450, y=110)
    elif tekan1.get()=="Duren Sawit":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="DUREN SAWIT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv39 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv39.place(x=450, y=110)
    elif tekan1.get()=="Makasar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAKASAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv40 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv40.place(x=450, y=110)
    elif tekan1.get()=="Ciracas":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIRACAS":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv41.place(x=450, y=110)
    elif tekan1.get()=="Cipayung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIPAYUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr3, text="Rata-rata = " + str(rerata), bg="orange red", font=('Times', 12))
                cv41.place(x=450, y=110)

def k2():
    data = pd.read_excel("datasetProject1\Kelahiran.xlsx", sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if tekan2.get()=="Kepulauan Seribu Utara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEPULAUAN SERIBU UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv.place(x=450, y=110)
    elif tekan2.get()=="Gambir":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GAMBIR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv1 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv1.place(x=450, y=110)
    elif tekan2.get()=="Sawah Besar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SAWAH BESAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv2 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv2.place(x=450, y=110)
    elif tekan2.get()=="Kemayoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMAYORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv3 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv3.place(x=450, y=110)
    elif tekan2.get()=="Senen":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SENEN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv4 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv4.place(x=450, y=110)
    elif tekan2.get()=="Cempaka Putih":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CEMPAKA PUTIH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv5 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv5.place(x=450, y=110)
    elif tekan2.get()=="Menteng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MENTENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv6 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv6.place(x=450, y=110)
    elif tekan2.get()=="Tanah Abang":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANAH ABANG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv7 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv7.place(x=450, y=110)
    elif tekan2.get()=="Johar Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JOHAR BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv8 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv8.place(x=450, y=110)
    elif tekan2.get()=="Penjaringan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PENJARINGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv9 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv9.place(x=450, y=110)
    elif tekan2.get()=="Tanjung Priok":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANJUNG PRIOK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv10 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv10.place(x=450, y=110)
    elif tekan2.get()=="Koja":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KOJA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv11 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv11.place(x=450, y=110)
    elif tekan2.get()=="cilincing":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILINCING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv12 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv12.place(x=450, y=110)
    elif tekan2.get()=="Pandemangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PADEMANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv13 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv13.place(x=450, y=110)
    elif tekan2.get()=="Kelapa Gading":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KELAPA GADING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv14 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv14.place(x=450, y=110)
    elif tekan2.get()=="Cengkareng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CENGKARENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv15 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv15.place(x=450, y=110)
    elif tekan2.get()=="Grogol Petamburan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GROGOL PETAMBURAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv16 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv16.place(x=450, y=110)
    elif tekan2.get()=="Taman Sari":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMAN SARI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv17 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv17.place(x=450, y=110)
    elif tekan2.get()=="Tambora":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMBORA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv18 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv18.place(x=450, y=110)
    elif tekan2.get()=="Kebon Jeruk":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBON JERUK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv19 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv19.place(x=450, y=110)
    elif tekan2.get()=="Kali Deres":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KALI DERES":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv20 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv20.place(x=450, y=110)
    elif tekan2.get()=="Pal Merah":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PAL MERAH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv21 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv21.place(x=450, y=110)
    elif tekan2.get()=="Kembangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMBANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv22 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv22.place(x=450, y=110)
    elif tekan2.get()=="Tebet":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TEBET":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv23 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv23.place(x=450, y=110)
    elif tekan2.get()=="Mampang Prapatan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAMPANG PRAPATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv25 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv25.place(x=450, y=110)
    elif tekan2.get()=="Pasar Minggu":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR MINGGU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv26 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv26.place(x=450, y=110)
    elif tekan2.get()=="Kebayoran Lama":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN LAMA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv27 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv27.place(x=450, y=110)
    elif tekan2.get()=="Cilandak":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILANDAK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv28 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv28.place(x=450, y=110)
    elif tekan2.get()=="Kebayoran Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv29 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv29.place(x=450, y=110)
    elif tekan2.get()=="Pancoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PANCORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv30 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv30.place(x=450, y=110)
    elif tekan2.get()=="Jagakarsa":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JAGAKARSA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv31 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv31.place(x=450, y=110)
    elif tekan2.get()=="Pesanggrahan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PESANGGRAHAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv32 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv32.place(x=450, y=110)
    elif tekan2.get()=="Matraman":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MATRAMAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv33 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv33.place(x=450, y=110)
    elif tekan2.get()=="Pulo Gadung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PULO GADUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv34= Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv34.place(x=450, y=110)
    elif tekan2.get()=="Jatinegara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JATINEGARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv35 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv35.place(x=450, y=110)
    elif tekan2.get()=="Kramatjati":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KRAMATJATI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv36 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv36.place(x=450, y=110)
    elif tekan2.get()=="Pasar Rebo":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR REBO":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv37 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv37.place(x=450, y=110)
    elif tekan2.get()=="Cakung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CAKUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv38 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv38.place(x=450, y=110)
    elif tekan2.get()=="Duren Sawit":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="DUREN SAWIT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv39 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv39.place(x=450, y=110)
    elif tekan2.get()=="Makasar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAKASAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv40 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv40.place(x=450, y=110)
    elif tekan2.get()=="Ciracas":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIRACAS":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv41.place(x=450, y=110)
    elif tekan2.get()=="Cipayung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIPAYUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr4, text="Rata-rata = " + str(rerata), bg="dark orange", font=('Times', 12))
                cv41.place(x=450, y=110)

def k3():
    data = pd.read_excel("datasetProject1\Kematian.xlsx", sheet_name="April 2021")
    tahun = (data["Tahun"]).tolist()
    bulan = (data["Bulan"]).tolist()
    kota = (data["Kota Kabupaten"]).tolist()
    kecamatan = (data["Kecamatan"]).tolist()
    kelurahan = (data["Kelurahan"]).tolist()
    kelamin = (data["Jenis Kelamin"]).tolist()
    jumlah = (data["Jumlah"]).tolist()
    tahunbaru = []
    bulanbaru = []
    kotabaru = []
    kecamatanbaru = []
    kelurahanbaru = []
    kelaminbaru = []
    jumlahbaru = []
    if tekan3.get()=="Kepulauan Seribu Utara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEPULAUAN SERIBU UTARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv.place(x=450, y=110)
    elif tekan3.get()=="Gambir":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GAMBIR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv1 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv1.place(x=450, y=110)
    elif tekan3.get()=="Sawah Besar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SAWAH BESAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv2 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv2.place(x=450, y=110)
    elif tekan3.get()=="Kemayoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMAYORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv3 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv3.place(x=450, y=110)
    elif tekan3.get()=="Senen":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="SENEN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv4 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv4.place(x=450, y=110)
    elif tekan3.get()=="Cempaka Putih":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CEMPAKA PUTIH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv5 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv5.place(x=450, y=110)
    elif tekan3.get()=="Menteng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MENTENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv6 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv6.place(x=450, y=110)
    elif tekan3.get()=="Tanah Abang":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANAH ABANG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv7 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv7.place(x=450, y=110)
    elif tekan3.get()=="Johar Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JOHAR BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv8 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv8.place(x=450, y=110)
    elif tekan3.get()=="Penjaringan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PENJARINGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv9 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv9.place(x=450, y=110)
    elif tekan3.get()=="Tanjung Priok":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TANJUNG PRIOK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv10 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv10.place(x=450, y=110)
    elif tekan3.get()=="Koja":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KOJA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv11 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv11.place(x=450, y=110)
    elif tekan3.get()=="cilincing":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILINCING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv12 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv12.place(x=450, y=110)
    elif tekan3.get()=="Pandemangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PADEMANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv13 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv13.place(x=450, y=110)
    elif tekan3.get()=="Kelapa Gading":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KELAPA GADING":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv14 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv14.place(x=450, y=110)
    elif tekan3.get()=="Cengkareng":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CENGKARENG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv15 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv15.place(x=450, y=110)
    elif tekan3.get()=="Grogol Petamburan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="GROGOL PETAMBURAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv16 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv16.place(x=450, y=110)
    elif tekan3.get()=="Taman Sari":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMAN SARI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv17 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv17.place(x=450, y=110)
    elif tekan3.get()=="Tambora":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TAMBORA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv18 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv18.place(x=450, y=110)
    elif tekan3.get()=="Kebon Jeruk":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBON JERUK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv19 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv19.place(x=450, y=110)
    elif tekan3.get()=="Kali Deres":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KALI DERES":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv20 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv20.place(x=450, y=110)
    elif tekan3.get()=="Pal Merah":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PAL MERAH":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv21 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv21.place(x=450, y=110)
    elif tekan3.get()=="Kembangan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEMBANGAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv22 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv22.place(x=450, y=110)
    elif tekan3.get()=="Tebet":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="TEBET":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv23 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv23.place(x=450, y=110)
    elif tekan3.get()=="Mampang Prapatan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAMPANG PRAPATAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv25 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv25.place(x=450, y=110)
    elif tekan3.get()=="Pasar Minggu":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR MINGGU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv26 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv26.place(x=450, y=110)
    elif tekan3.get()=="Kebayoran Lama":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN LAMA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv27 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv27.place(x=450, y=110)
    elif tekan3.get()=="Cilandak":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CILANDAK":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv28 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv28.place(x=450, y=110)
    elif tekan3.get()=="Kebayoran Baru":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KEBAYORAN BARU":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv29 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv29.place(x=450, y=110)
    elif tekan3.get()=="Pancoran":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PANCORAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv30 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv30.place(x=450, y=110)
    elif tekan3.get()=="Jagakarsa":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JAGAKARSA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv31 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv31.place(x=450, y=110)
    elif tekan3.get()=="Pesanggrahan":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PESANGGRAHAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv32 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv32.place(x=450, y=110)
    elif tekan3.get()=="Matraman":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MATRAMAN":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv33 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv33.place(x=450, y=110)
    elif tekan3.get()=="Pulo Gadung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PULO GADUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv34= Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv34.place(x=450, y=110)
    elif tekan3.get()=="Jatinegara":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="JATINEGARA":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv35 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv35.place(x=450, y=110)
    elif tekan3.get()=="Kramatjati":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="KRAMATJATI":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv36 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv36.place(x=450, y=110)
    elif tekan3.get()=="Pasar Rebo":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="PASAR REBO":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv37 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv37.place(x=450, y=110)
    elif tekan3.get()=="Cakung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CAKUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv38 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv38.place(x=450, y=110)
    elif tekan3.get()=="Duren Sawit":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="DUREN SAWIT":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv39 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv39.place(x=450, y=110)
    elif tekan3.get()=="Makasar":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="MAKASAR":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv40 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv40.place(x=450, y=110)
    elif tekan3.get()=="Ciracas":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIRACAS":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv41.place(x=450, y=110)
    elif tekan3.get()=="Cipayung":
        for q in range (0,len(kecamatan)):
            if kecamatan[q]=="CIPAYUNG":
                tahunbaru.append(tahun[q])
                bulanbaru.append(bulan[q])
                kotabaru.append(kota[q])
                kecamatanbaru.append(kecamatan[q])
                kelurahanbaru.append(kelurahan[q])
                kelaminbaru.append(kelamin[q])
                jumlahbaru.append(jumlah[q])
                tp = 0
                male = 0
                female = 0
                for w in range(0, len(jumlahbaru)):
                    tp = tp + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Laki-Laki":
                        male = male + int(jumlahbaru[w])
                for w in range(0, len(jumlahbaru)):
                    if kelaminbaru[w] == "Perempuan":
                        female = female + int(jumlahbaru[w])
                rerata = round(tp / len(jumlahbaru), 2)
                cv41 = Label(fr5, text="Rata-rata = " + str(rerata), bg="deep sky blue", font=('Times', 12))
                cv41.place(x=450, y=110)


def bt2():
    global a11
    global a21
    global a31
    global a41
    global a51
    global a61
    a11 = IntVar()
    a21 = IntVar()
    a31 = IntVar()
    a41 = IntVar()
    a51 = IntVar()
    a61 = IntVar()
    a11.get()
    a21.get()
    a31.get()
    a41.get()
    a51.get()
    a61.get()
    if a.get()==1 and a1.get()==1 :
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Salah Satu Kabupaten/Kota atau Kecamatan!!!")
    elif a.get() == 1:
        l7 = Label(fr2, text="Pilih Kota/Kabupaten : ", bg="Coral", font=('Times', 12))
        l7.place(x=60, y=210)
        rb2 = Checkbutton(fr2, text="ADM. Kepulauan Seribu", variable=a11, onvalue=1, offvalue=0, bg="Coral",font=('Times', 12))
        rb2.place(x=60, y=235)
        rb3 = Checkbutton(fr2, text="Jakarta Pusat", variable=a21, onvalue=1, offvalue=0, bg="Coral",font=('Times', 12))
        rb3.place(x=60, y=260)
        rb4 = Checkbutton(fr2, text="Jakarta Utara", variable=a31, onvalue=1, offvalue=0, bg="Coral",font=('Times', 12))
        rb4.place(x=60, y=285)
        rb5 = Checkbutton(fr2, text="Jakarta Barat", variable=a41, onvalue=1, offvalue=0, bg="Coral",font=('Times', 12))
        rb5.place(x=60, y=310)
        rb6 = Checkbutton(fr2, text="Jakarta Selatan", variable=a51, onvalue=1, offvalue=0, bg="Coral",font=('Times', 12))
        rb6.place(x=60, y=335)
        rb7 = Checkbutton(fr2, text="Jakarta Timur", variable=a61, onvalue=1, offvalue=0, bg="Coral",font=('Times', 12))
        rb7.place(x=60, y=360)
        rb2.deselect()
        rb3.deselect()
        rb4.deselect()
        rb4.deselect()
        rb5.deselect()
        rb6.deselect()
        btn3=Button(fr2,text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'),command=s1)
        btn3.place(x=450,y=70)
    elif a1.get() == 1:
        l8 = Label(fr2, text="Pilih Kecamatan :", bg="Coral", font=('Times', 12))
        l8.place(x=450, y=210)
        kecamatan = [
            "Kepulauan Seribu Utara",
            "Gambir",
            "Sawah Besar",
            "Kemayoran",
            "Senen",
            "Cempaka Putih",
            "Menteng",
            "Tanah Abang",
            "Johar Baru",
            "Penjaringan",
            "Tanjung Priok",
            "Koja",
            "Cilincing",
            "Pademangan",
            "Kelapa Gading",
            "Cengkareng",
            "Grogol Petambunan",
            "Taman Sari",
            "Tambora",
            "Kebon Jeruk",
            "Kali Deres",
            "Pal Merah",
            "Kembangan",
            "Tebet",
            "Setia Budi",
            "Mampang Prampatan",
            "Pasar Minggu",
            "Kebayoran Lama",
            "Cilandak",
            "Kebayoran Baru",
            "Pancoran",
            "Jagakarsa",
            "Pesanggrahan",
            "Matraman",
            "Pulo Gadung",
            "Jatinegara",
            "Kramatjati",
            "Pasar Rebo",
            "Cakung",
            "Duren Sawit",
            "Makasar",
            "Ciracas",
            "Cipayung",
        ]
        ttn = Button(fr2, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'), command=k)
        ttn.place(x=450,y=70)
        global tekan
        tekan = StringVar()
        tekan.get()
        drop1 = OptionMenu(fr2, tekan, *kecamatan)
        drop1.place(x=450, y=235)
    elif a.get()!= 1 and a1.get() != 1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Kabupaten/Kota atau Kecamatan")

def bt3():
    global a12
    global a22
    global a32
    global a42
    global a52
    global a62
    a12 = IntVar()
    a22 = IntVar()
    a32 = IntVar()
    a42 = IntVar()
    a52 = IntVar()
    a62 = IntVar()
    a12.get()
    a22.get()
    a32.get()
    a42.get()
    a52.get()
    a62.get()
    if b.get() == 2:
        l71 = Label(fr3, text="Pilih Kota/Kabupaten :", bg="orange red", font=('Times', 12))
        l71.place(x=60, y=210)
        rb21 = Checkbutton(fr3, text="ADM. Kepulauan Seribu", variable=a12, onvalue=1, offvalue=0, bg="orange red",font=('Times', 12))
        rb21.place(x=60, y=235)
        rb31 = Checkbutton(fr3, text="Jakarta Pusat", variable=a22, onvalue=1, offvalue=0, bg="orange red",font=('Times', 12))
        rb31.place(x=60, y=260)
        rb41 = Checkbutton(fr3, text="Jakarta Utara", variable=a32, onvalue=1, offvalue=0, bg="orange red",font=('Times', 12))
        rb41.place(x=60, y=285)
        rb51 = Checkbutton(fr3, text="Jakarta Barat", variable=a42, onvalue=1, offvalue=0, bg="orange red",font=('Times', 12))
        rb51.place(x=60, y=310)
        rb61 = Checkbutton(fr3, text="Jakarta Selatan", variable=a52, onvalue=1, offvalue=0, bg="orange red",font=('Times', 12))
        rb61.place(x=60, y=335)
        rb71 = Checkbutton(fr3, text="Jakarta Timur", variable=a62, onvalue=1, offvalue=0, bg="orange red",font=('Times', 12))
        rb71.place(x=60, y=360)
        btn31 = Button(fr3, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'),command=s2)
        btn31.place(x=450, y=70)
        rb21.deselect()
        rb31.deselect()
        rb41.deselect()
        rb41.deselect()
        rb51.deselect()
        rb61.deselect()
    elif b1.get() == 2:
        l9 = Label(fr3, text="Pilih Kecamatan :", bg="orange red", font=('Times', 12))
        l9.place(x=450, y=210)
        kecamatan = [
            "Kepulauan Seribu Utara",
            "Gambir",
            "Sawah Besar",
            "Kemayoran",
            "Senen",
            "Cempaka Putih",
            "Menteng",
            "Tanah Abang",
            "Johar Baru",
            "Penjaringan",
            "Tanjung Priok",
            "Koja",
            "Cilincing",
            "Pademangan",
            "Kelapa Gading",
            "Cengkareng",
            "Grogol Petambunan",
            "Taman Sari",
            "Tambora",
            "Kebon Jeruk",
            "Kali Deres",
            "Pal Merah",
            "Kembangan",
            "Tebet",
            "Setia Budi",
            "Mampang Prampatan",
            "Pasar Minggu",
            "Kebayoran Lama",
            "Cilandak",
            "Kebayoran Baru",
            "Pancoran",
            "Jagakarsa",
            "Pesanggrahan",
            "Matraman",
            "Pulo Gadung",
            "Jatinegara",
            "Kramajati",
            "Pasar Rebo",
            "Cakung",
            "Duren Sawit",
            "Makasar",
            "Ciracas",
            "Cipayung",
        ]
        ttn1 = Button(fr3, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'), command=k1)
        ttn1.place(x=450, y=70)
        global tekan1
        tekan1 = StringVar()
        tekan1.get()
        drop2 = OptionMenu(fr3, tekan1, *kecamatan)
        drop2.place(x=450, y=235)
    elif b.get() != 2 and b1.get() != 2:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Kabupaten/Kota atau Kecamatan")

def bt4():
    global a13
    global a23
    global a33
    global a43
    global a53
    global a63
    a13 = IntVar()
    a23 = IntVar()
    a33 = IntVar()
    a43 = IntVar()
    a53 = IntVar()
    a63 = IntVar()
    a13.get()
    a23.get()
    a33.get()
    a43.get()
    a53.get()
    a63.get()
    if c.get() == 1:
        l72 = Label(fr4, text="Pilih Kota/Kabupaten :", bg="dark orange", font=('Times', 12))
        l72.place(x=60, y=210)
        rb22 = Checkbutton(fr4, text="ADM. Kepulauan Seribu", variable=a13, onvalue=1, offvalue=0, bg="dark orange",font=('Times', 12))
        rb22.place(x=60, y=235)
        rb32 = Checkbutton(fr4, text="Jakarta Pusat", variable=a23, onvalue=1, offvalue=0, bg="dark orange",font=('Times', 12))
        rb32.place(x=60, y=260)
        rb42 = Checkbutton(fr4, text="Jakarta Utara", variable=a33, onvalue=1, offvalue=0, bg="dark orange",font=('Times', 12))
        rb42.place(x=60, y=285)
        rb52 = Checkbutton(fr4, text="Jakarta Barat", variable=a43, onvalue=1, offvalue=0, bg="dark orange",font=('Times', 12))
        rb52.place(x=60, y=310)
        rb62 = Checkbutton(fr4, text="Jakarta Selatan", variable=a53, onvalue=1, offvalue=0, bg="dark orange",font=('Times', 12))
        rb62.place(x=60, y=335)
        rb72 = Checkbutton(fr4, text="Jakarta Timur", variable=a63, onvalue=1, offvalue=0, bg="dark orange",font=('Times', 12))
        rb72.place(x=60, y=360)
        btn32 = Button(fr4, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'),command=s3)
        btn32.place(x=450, y=70)
        rb22.deselect()
        rb32.deselect()
        rb42.deselect()
        rb42.deselect()
        rb52.deselect()
        rb62.deselect()
    elif c1.get() == 1:
        l10 = Label(fr4, text="Pilih Kecamatan :", bg="dark orange", font=('Times', 12))
        l10.place(x=450, y=210)
        kecamatan = [
            "Kepulauan Seribu Utara",
            "Gambir",
            "Sawah Besar",
            "Kemayoran",
            "Senen",
            "Cempaka Putih",
            "Menteng",
            "Tanah Abang",
            "Johar Baru",
            "Penjaringan",
            "Tanjung Priok",
            "Koja",
            "Cilincing",
            "Pademangan",
            "Kelapa Gading",
            "Cengkareng",
            "Grogol Petambunan",
            "Taman Sari",
            "Tambora",
            "Kebon Jeruk",
            "Kali Deres",
            "Pal Merah",
            "Kembangan",
            "Tebet",
            "Setia Budi",
            "Mampang Prampatan",
            "Pasar Minggu",
            "Kebayoran Lama",
            "Cilandak",
            "Kebayoran Baru",
            "Pancoran",
            "Jagakarsa",
            "Pesanggrahan",
            "Matraman",
            "Pulo Gadung",
            "Jatinegara",
            "Kramajati",
            "Pasar Rebo",
            "Cakung",
            "Duren Sawit",
            "Makasar",
            "Ciracas",
            "Cipayung",
        ]
        global tekan2
        ttn2 = Button(fr4, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'), command=k2)
        ttn2.place(x=450, y=70)
        tekan2 = StringVar()
        tekan2.get()
        drop3 = OptionMenu(fr4, tekan2, *kecamatan)
        drop3.place(x=450, y=235)
    elif c.get() != 1 and c1.get() != 1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Kabupaten/Kota atau Kecamatan")

def bt5():
    global a14
    global a24
    global a34
    global a44
    global a54
    global a64
    a14 = IntVar()
    a24 = IntVar()
    a34 = IntVar()
    a44 = IntVar()
    a54 = IntVar()
    a64 = IntVar()
    a14.get()
    a24.get()
    a34.get()
    a44.get()
    a54.get()
    a64.get()
    if d.get() == 1:
        l73 = Label(fr5, text="Pilih Kota/Kabupaten :", bg="deep sky blue", font=('Times', 12))
        l73.place(x=60, y=210)
        rb23 = Checkbutton(fr5, text="ADM. Kepulauan Seribu", variable=a14, onvalue=1, offvalue=0, bg="deep sky blue",font=('Times', 12))
        rb23.place(x=60, y=235)
        rb33 = Checkbutton(fr5, text="Jakarta Pusat", variable=a24, onvalue=1, offvalue=0, bg="deep sky blue",font=('Times', 12))
        rb33.place(x=60, y=260)
        rb43 = Checkbutton(fr5, text="Jakarta Utara", variable=a34, onvalue=1, offvalue=0, bg="deep sky blue",font=('Times', 12))
        rb43.place(x=60, y=285)
        rb53 = Checkbutton(fr5, text="Jakarta Barat", variable=a44, onvalue=1, offvalue=0, bg="deep sky blue",font=('Times', 12))
        rb53.place(x=60, y=310)
        rb63 = Checkbutton(fr5, text="Jakarta Selatan", variable=a54, onvalue=1, offvalue=0, bg="deep sky blue",font=('Times', 12))
        rb63.place(x=60, y=335)
        rb73 = Checkbutton(fr5, text="Jakarta Timur", variable=a64, onvalue=1, offvalue=0, bg="deep sky blue",font=('Times', 12))
        rb73.place(x=60, y=360)
        btn33 = Button(fr5, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'),command=s4)
        btn33.place(x=450, y=70)
        rb23.deselect()
        rb33.deselect()
        rb43.deselect()
        rb43.deselect()
        rb53.deselect()
        rb63.deselect()
    elif d1.get() == 1:
        l11 = Label(fr5, text="Pilih Kecamatan :", bg="deep sky blue", font=('Times', 12))
        l11.place(x=450, y=210)
        kecamatan = [
            "Kepulauan Seribu Utara",
            "Gambir",
            "Sawah Besar",
            "Kemayoran",
            "Senen",
            "Cempaka Putih",
            "Menteng",
            "Tanah Abang",
            "Johar Baru",
            "Penjaringan",
            "Tanjung Priok",
            "Koja",
            "Cilincing",
            "Pademangan",
            "Kelapa Gading",
            "Cengkareng",
            "Grogol Petambunan",
            "Taman Sari",
            "Tambora",
            "Kebon Jeruk",
            "Kali Deres",
            "Pal Merah",
            "Kembangan",
            "Tebet",
            "Setia Budi",
            "Mampang Prampatan",
            "Pasar Minggu",
            "Kebayoran Lama",
            "Cilandak",
            "Kebayoran Baru",
            "Pancoran",
            "Jagakarsa",
            "Pesanggrahan",
            "Matraman",
            "Pulo Gadung",
            "Jatinegara",
            "Kramajati",
            "Pasar Rebo",
            "Cakung",
            "Duren Sawit",
            "Makasar",
            "Ciracas",
            "Cipayung",
        ]
        global tekan3
        ttx = Button(fr5, text="Hitung rata-rata", width=15, font=('Times', 12, 'bold'), command=k3)
        ttx.place(x=450, y=70)
        tekan3 = StringVar()
        tekan3.get()
        drop4 = OptionMenu(fr5, tekan3, *kecamatan,)
        drop4.place(x=450, y=235)
    elif d.get() != 1 and d1.get() != 1:
        messagebox.showerror("Tidak Dapat Melanjutkan!", "Pilih Kabupaten/Kota atau Kecamatan")

run.mainloop()
