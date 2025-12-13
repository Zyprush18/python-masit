# variable

# hallo = "eko"
# umur_saya  = 9
# _saya_address = "jl.banteng"
# isDeath = False
# ALAT = "tameng"
# hello2 = "lala"

# print(type(umur_saya))

# print("hello " + hallo)

# print("Hello nama sya "+ hallo + " umur saya " + str(umur_saya) + " alamat saya " + _saya_address + " dan apakah saya sudah mati: "+ str(isDeath))

# print(f"Hello nama saya {hallo}, umur saya {umur_saya}, alamat saya {_saya_address}, dan apakah saya sudah mati?: {isDeath}")

# aa = f{umur_saya}{isDeath}
# print("kata saya 'jjdj' kkkk kkk pp")
# print('kata saya "jjdj" kkkk kkk pp')

# hallo = "budi"


# print("""   saya manusia. ""
# saya butuh makan.
# saya mau sholat

#     paragraf kedua,,kata saya "kakkaka"
# """)


# print('''   haofjbjkiedbfjjkf
# kjekfkjekjflkejlkfjerlkfe
# fnekwnfknelkenflkeg
# fejefohwefhiwejfpow
# ffnkwelsjgp;slfs
# efwfwefwefd

#     paragraf kedua,,kata saya "kakkaka"
# ''')

# print("hello nama saya koko \njjj\tlalal\b \"kkk\" \'lalala\' \\")


# komentar
"""
    klaal

"""

'''
    ejjoidejijieojroiej
    jeojoeorpoerpojepojr
'''
# isi dengan umur adekmu dan tipe datanya integer
# age = 0




# tipe data

# string
# nama = 'budi'
# nama_besar = 'EKO'
# judul = 'makan ayam geprek'
# whitespace = "   \"awokawok\"   "
# print(type(nama))
# print(nama)
# print(nama.upper()) # uppercase
# print(nama_besar.lower()) # lowercase
# print(nama.capitalize())
# print(judul.title())
# print(nama[1:])
# print(judul[6:10])
# pecah = judul.split()
# print(f"{pecah[1]} {pecah[2]}")
# print(judul.replace("geprek", "goreng"))
# print(whitespace)
# print(whitespace.strip())
# print(whitespace.lstrip())
# print(whitespace.rstrip())


# number
# int
# a = 7
# print(type(a))

# float
# b = 5.7
# print(type(b))

# complex
# c = 50j
# print(type(c))

# konversi int 
# d = 5.6
# print(type(d))
# print(type(int(d)))

# f = 4
# print(type(f))
# print(type(float(f)))


# o = 9
# l = 9.4
# print(type(o))
# print(type(complex(o)))
# print(type(complex(l)))
# print(complex(l))

# boolean
# t = True 
# s = False
# p = 0
# q = 1

# print(type(bool(p)))
# print(type(bool(q)))

# list
# k = [1,2,3,4,5] # ndak boleh diubah
# print(k[2])
# print(k[1:])
# print(k[1:4])
# print(k[:3])

# k[1] = 6
# k[4] = "saya"
# print(k)

# k.append(7)
# print(k)

# k.remove("saya")
# print(k)

# k.sort(reverse=True)
# print(k)

# v = k.copy() 
# v[0] = 9
# k[0] = 10

# print(k)

# q = ["a","b","c"]
# v.extend(q)
# print(v)

# print(v.clear())
# kkk = "jfjfnjneonwjnfjwnf"
# print(len(kkk))


# tuple
# name = ("budi", "lala", "eko") # -> immutable/tidak bisa di ubah/ konstanta
# print(name[1])
# listname = list(name)
# listname[1] = 1
# listname.insert(1, "lalalal")
# listname.remove("eko")
# name = tuple(listname)
# print(name)

# name1,*name2 = name
# print(name1)
# print(name2)

# newname = ("suci","dika","rahman")
# name += newname
# print(name)



# set
# gh = {"dipsi","lala", "po"}

# print(type(gh))
# gh.add("ibnu")

# jh = {"eko","eman","sanz"}
# lh = ["edo","gani"]
# gh.update(jh)
# gh.update(lh)

# gh.remove("po")
# gh.discard("zul")

# mh = {"jokowi","prabowo", "anies"}
# nh = {"gagak","kucing","anjing"}
# ll = gh.union(mh,nh)
# ll = gh | mh | nh
# gh.update(mh, nh)
# print(gh)


# dictionary
kamar = {
    "meja1":{
        "name" : ["Agus", "mamang", "ibnu"], "age": 5, "address": "jl.compang camping"
    },

    "meja2":{
        "name" : ["Agus", "mamang", "ibnu"], "age": 5, "address": "jl.compang camping"
    },

    "meja3": [
        {
            "name": "lala"
        },

        (
            "dipsi",
            "po", 
            [
                "lala", 
                {
                    "name": "ibnu"
                },
                {
                    "maman"
                }
            ]
        ),
        
        [
            {
                "name": 'Maxim'
            }
        ]
    ]

    
}

print(kamar['meja3'][1][2][1]["name"])
kamar['meja3'][1][2][1].update({"name": "zul"})
print(kamar['meja3'][1][2][1]["name"])
print(type(kamar))
# kamar['meja2']["age"] = [5, 10, 45]
kamar["meja2"].update({"age": [5, 10, 45]})
kamar['meja1']["makanan_favorit"] = "nasi goreng"
kamar["meja2"].pop("address")
# del kamar["address"]
print(kamar["meja1"])
print(kamar["meja2"])



# operator

# if

# for sama while




# function
# range
# array
# iterator












# karin
# nama = "karin"
# umur = 18
# tinggi = 150.1
# mahasiswa = True
# hobi = "main"

# print("="*50 + " Punya Karin "+ "="*50)
# print (f"nama saya {nama}, umur saya {umur} ✅")

# zaim

# Nama = "Zaim"
# Umur = "18"
# Alamat = "pongo"
# Status = "Mahasiswa"
# Sudah_Menikah = False
# print("="*50 + " Punya Zaim "+ "="*50)
# print(f" nama saya {Nama}, umur saya {Umur}, alamat saya {Alamat}, saya seorang {Status}, dan apakah sudah menikah {Sudah_Menikah}.")
