from os import system
from datetime import datetime

def view_menu():
	system("cls")
	menu = """
	Pencatatan Stok Makanan
	[A] - TAMBAH STOK
	[B] - TAMPILKAN STOK
	[C] - CARI STOK
	[D] - PERBARUI STOK
	[E] - HAPUS STOK
	[Q] - KELUAR 
	"""
	print(menu)

def verify_ans(job):
	job = job.upper()
	if job =="Y":
		return True
	else:
		return False

def print_system(msg):
	system("cls")
	print(msg)

def create_id_stok():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_stok)+1
	id_stok = str("%4d%02d%02d-C%03d" % (year, month, hari, counter))
	return id_stok

def add_to_stok():
	print_system("-MEMASUKAN DAFTAR STOK BARU-")
	nama = input("NAMA MAKANAN\t:")
	harga = input("HARGA MAKANAN\t:")
	kadarluasa = input("KADARLUASA MAKANAN\t:")
	tanggal = input("TANGGAL MASUK\t:")
	jumlah = input("JUMLAH STOK\t:")

	user_ans = input("Yakin Ingin Menyimpan data(Y/N) : ")

	if verify_ans(user_ans):
		id_stok = create_id_stok()
		print("Menyimpan Data ...")
		data_stok[id_stok] = {
			"nama" : nama,
			"harga" : harga,
			"kadarluasa" : kadarluasa,
			"tanggal" : tanggal,
			"jumlah" : jumlah
		}
		print("Data Telah Disimpan")
	else:
		print("Data batal disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def print_data_stok(id_stok = None, all_fields = False, hobi = True):
	if id_stok != None and all_fields == False:
		print(f"""
		-DATA DITEMUKAN-
	ID \t: {id_stok}
	Nama \t:{data_stok[id_stok]["nama"]}
	harga \t:{data_stok[id_stok]["harga"]}
	kadarluasa \t:{data_stok[id_stok]["kadarluasa"]}
	tanggal \t:{data_stok[id_stok]["tanggal"]}
	jumlah \t:{data_stok[id_stok]["jumlah"]}
			""")
	elif id_stok != None and harga == False:
		print(f"""
		-DATA DITEMUKAN-
	ID \t: {id_stok}
	Nama \t:{data_stok[id_stok]["nama"]}
	harga \t:{data_stok[id_stok]["harga"]}
	kadarluasa \t:{data_stok[id_stok]["kadarluasa"]}
	tanggal \t:{data_stok[id_stok]["tanggal"]}
	jumlah \t:{data_stok[id_stok]["jumlah"]}
			""")
	elif all_fields ==True:
		for id_stok in data_stok:
			nama = data_stok[id_stok]["nama"]
			harga = data_stok[id_stok]["harga"]
			kadarluasa = data_stok[id_stok]["kadarluasa"]
			tanggal = data_stok[id_stok]["tanggal"]
			jumlah = data_stok[id_stok]["jumlah"]
			print(f"ID:{id_stok}\tNama:{nama}\tharga:{harga}\tkadarluasa:{kadarluasa}\ttanggal:{tanggal}\tjumlah:{jumlah}")

def print_stok():
	print_system("SEMUA DATA STOK-")
	if len(data_stok) == 0:
		print("<BELUM ADA DATA YANG DISIMPAN>")
	else:
		print_data_stok(all_fields=True)
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_nama(stok):
	for id_stok in data_stok:
		if data_stok[id_stok]["nama"] == stok:
			print_data_stok(id_stok=id_stok)
			return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def get_id_stok_from_nama(stok):
	for id_stok in data_stok:
		if data_stok[id_stok]["nama"] == stok:
			return id_stok

def seraching_by_id(id_stok):
	if id_stok in data_stok:
		print_data_stok(id_stok=id_stok)
		return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def find_stok():
	print_system("-CARI DATA STOK-\n")
	nama = input("Nama Makanan Yang Dicari : ")
	result = searching_by_nama(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def delete_stok():
	print_system("-MENGHAPUS DATA STOK-")
	nama = input("Masukkan Nama Makanan yang akan Dihapus : ")
	result = searching_by_nama(nama)
	if result:
		respon = input(f"Yakin ingin menghapus {nama} (Y/N): ")
		if verify_ans(respon):
			print("DATA telah dihapus.")
		else:
			print("DATA batal dihapus")
	input("Tekan ENTER untuk kembali ke menu utama")

def update_nama(stok):
	print(f"Nama Lama \t:{stok}")
	new_nama = input("Nama Baru\t: ")
	respon = input("Yakin ingin mengganti datanya? (Y/N) : ")
	if verify_ans(respon):
		id_stok = get_id_stok_from_nama(stok)
		data_stok[id_stok]["nama"] = new_nama
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_harga(stok):
	id_stok = get_id_stok_from_nama(stok)
	print(f"Nama \t:{data_stok[id_stok]['nama']}")
	print(f"Harga Lama\t:{data_stok[id_stok]['harga']}")
	new_harga = input("Harga Baru\t: ")
	respon = input("Yakin ingin mengganti datanya? (Y/N) : ")
	if verify_ans(respon):
		data_stok[id_stok]['harga'] = new_harga
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_kadarluasa(stok):
	id_stok = get_id_stok_from_nama(stok)
	print(f"Nama \t:{data_stok[id_stok]['nama']}")
	print(f"Kadarluasa Lama\t:{data_stok[id_stok]['kadarluasa']}")
	new_kadarluasa = input("Kadarluasa Baru\t: ")
	respon = input("Yakin ingin mengganti datanya? (Y/N) : ")
	if verify_ans(respon):
		data_stok[id_stok]['kadarluasa'] = new_kadarluasa
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_tanggal(stok):
	id_stok = get_id_stok_from_nama(stok)
	print(f"Nama \t:{data_stok[id_stok]['nama']}")
	print(f"Tanggal Lama\t:{data_stok[id_stok]['tanggal']}")
	new_tanggal = input("Tanggal Baru\t: ")
	respon = input("Yakin ingin mengganti datanya? (Y/N) : ")
	if verify_ans(respon):
		data_stok[id_stok]['tanggal'] = new_tanggal
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_jumlah(stok):
	id_stok = get_id_stok_from_nama(stok)
	print(f"Nama \t:{data_stok[id_stok]['nama']}")
	print(f"Jumlah Lama\t:{data_stok[id_stok]['jumlah']}")
	new_jumlah = input("jumlah Baru\t: ")
	respon = input("Yakin ingin mengganti datanya? (Y/N) : ")
	if verify_ans(respon):
		data_stok[id_stok]['jumlah'] = new_jumlah
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")


def update_stok():
	print_system("PERBARUI DATA STOK\n")
	nama = input("Nama Stok yang ingin diperbarui : ")
	result = searching_by_nama(nama)
	if result:
		print("Data yang ingin diperbarui : ")
		print("[1]. Nama , [2]. Harga , [3]. Kadarluasa , [4]. Tanggal , [5]. Jumlah")
		respon = input("Pilihan : ")
		if respon == "1":
			update_nama(nama)
		elif respon == "2":
			update_harga(nama)
		elif respon == "3":
			update_kadarluasa(nama)
		elif respon == "4":
			update_tanggal(nama)
		elif respon =="5":
			update_jumlah(nama)
	input("Tekan ENTER untuk kembali ke menu utama")

def check_input(job):
	job = job.upper()
	if job == "Q":
		return True
	elif job == "A":
		add_to_stok()
	elif job == "B":
		print_stok()
	elif job == "C":
		find_stok()
	elif job == "D":
		update_stok()
	elif job == "E":
		delete_stok()


data_stok = {
	"20201007-C001" : {
		"nama" : "chitato",
		"harga" : "RP 3.000",
		"kadarluasa" : "15/01/2021",
		"tanggal" : "29/09/2020",
		"jumlah" : "50 dus"
	},
	"20201007-C002" : {
		"nama" : "permen",
		"harga" : "RP 500",
		"kadarluasa" : "23/01/2021",
		"tanggal" : "17/09/2020",
		"jumlah" : "30 kotak"
	}
}
stop = False 

while not stop:
	view_menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)



