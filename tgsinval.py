from tkinter import Tk, Label, Button, Frame, Entry, ttk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Aplikasi Data Peserta Didik")
root.geometry("800x400")
root.resizable(False, False)

data_siswa = []

frame_input = Frame(root, background="#EACE67")
frame_lihat = Frame(root, background="#EACE67")
frame_cari  = Frame(root, background="#EACE67")
for frame in (frame_input, frame_lihat, frame_cari):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

def simpan():
    nama = entry_nama.get()
    kelas = entry_kelas.get()
    alamat = entry_alamat.get()
    if nama=='' or kelas=='' or alamat=='':
        label_coba.config(text='Semua kolom harus di isi', fg='red')
    else:
        label_coba.config(text='Data berhasil disimpan!', fg='green')
        data_siswa.append([nama, kelas, alamat])
        entry_nama.delete(0, END)
        entry_kelas.delete(0, END)
        entry_alamat.delete(0, END)
        tampilkan_tree()

def tampilkan_tree():
    for i in tree.get_children():
        tree.delete(i)
    for s in data_siswa:
        tree.insert("", "end", values=s)

def ke_lihat():
    tampilkan_tree()
    frame_lihat.tkraise()

def cari_data():
    keyword = entry_cari.get().lower()
    for i in hasil_tree.get_children():
        hasil_tree.delete(i)
    for s in data_siswa:
        if keyword in s[0].lower():
            hasil_tree.insert("", "end", values=s)

label_nm=Label(frame_input, text="Nama:", background="#EACE67")
label_nm.pack()
entry_nama = Entry(frame_input)
entry_nama.pack()

label_kls=Label(frame_input, text="Kelas:", background="#EACE67")
label_kls.pack()
entry_kelas = Entry(frame_input)
entry_kelas.pack()

label_almt=Label(frame_input, text="Alamat:", background="#EACE67")
label_almt.pack()
entry_alamat = Entry(frame_input)
entry_alamat.pack()

Button(frame_input, text="Simpan", command=simpan).pack(pady=5)
label_coba=Label(frame_input, text='', background="#EACE67")
label_coba.pack()

frame_button = Frame(frame_input, background="#EACE67")
frame_button.pack()
Button(frame_button, text="Lihat Data", command=ke_lihat).grid(row=0, column=0, padx=5)
Button(frame_button, text="Cari Data", command=lambda: frame_cari.tkraise()).grid(row=0, column=1, padx=5)

Label(frame_lihat, text="Daftar Data Peserta Didik A1", background="#EACE67").pack(pady=5)
tree = ttk.Treeview(frame_lihat, columns=("Nama", "Kelas", "Alamat"), show="headings")
for col in ("Nama", "Kelas", "Alamat"):
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill=BOTH, expand=True, pady=10)
Button(frame_lihat, text="Kembali", command=lambda: frame_input.tkraise()).pack(pady=5)

Label(frame_cari, text="Cari Nama:", background="#EACE67").pack()
entry_cari = Entry(frame_cari)
entry_cari.pack()
Button(frame_cari, text="Cari", command=cari_data).pack(pady=5)
hasil_tree = ttk.Treeview(frame_cari, columns=("Nama", "Kelas", "Alamat"), show="headings")
for col in ("Nama", "Kelas", "Alamat"):
    hasil_tree.heading(col, text=col)
    hasil_tree.column(col, width=150)
hasil_tree.pack(fill=BOTH, expand=True, pady=10)
Button(frame_cari, text="Kembali", command=lambda: frame_input.tkraise()).pack(pady=5)

frame_input.tkraise()
root.mainloop()