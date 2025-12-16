'''
🟦 A. List (data["list"])

Tambahkan "mangga" ke dalam list.

Hapus "pisang".

Ubah "jeruk" menjadi "anggur".

🟨 B. Set (data["set"])

Tambahkan "burung".

Hapus "anjing".

Tambahkan "ikan".

🟩 C. Tuple (data["tuple"])

⚠️ Tuple tidak bisa diubah langsung

Tambahkan angka 40.

Hapus angka 20.

Ubah angka 30 menjadi 35.

🟥 D. Dictionary (data["dict"])

Tambahkan "alamat": "Jakarta".

Ubah "umur" menjadi 18.

Hapus key "kelas".

'''

# jangan di uba
data = {
    "list": ["apel", "pisang", "jeruk"],
    "set": {"kucing", "anjing", "kelinci"},
    "tuple": (10, 20, 30),
    "dict": {
        "nama": "Budi",
        "umur": 17,
        "kelas": "XI"
    }
}


# list
data["list"].append("mangga")
data["list"].remove("pisang")
data["list"][1] = "anggur"
data["set"].add("burung")
data["set"].discard("anjing")
data["set"].add("ikan")
listname = list (data["tuple"])
listname.insert(1, 40)
listname.pop(2)
listname[2] = 35
data["tuple"] = tuple(listname)
data["dict"]["alamat"] = "jakarta"
(data["dict"])["umur"] = 18
del data["dict"]["kelas"]


print(data)

