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
# print(type(l))
# print(type(complex(o)))
# print(type(complex(l)))
# print(complex(l))

# s = "2"
# print(type(s))
# print(type(complex(s)))

# boolean
# t = True 
# s = False
# p = 0
# q = 1

# print(bool(p))
# print(bool(q))

# list
# k = [1,2,3,4,5] # tidak boleh di ubah

# print(k[2])
# print(k[2:])
# print(k[1:4])
# print(k[:3])

# k[1] = 6
# k[4] = "saya"
# print(k)

# k.append(7)
# print(k)

# k.remove(4)
# print(k)

# k.sort(reverse=True)
# print(k)

# v = k # dengan bgini value k da tidak ikut berubah
# v[2] = 9

# print(k) 
# print(v)

# v = k.copy() 
# v[2] = 9
# k[0] = 10

# print(k)
# print(v)


# q = ["a","b","c"]
# k.extend(q)
# print(k)

# print(k.clear())
# kkk = "jfjfnjneonwjnfjwnf"
# print(len(kkk))


# tuple
# name = ("budi", "lala", "eko") # -> immutable/tidak bisa di ubah/ konstanta
# print(name[1])
# listname = list(name)
# listname[1] = "po"
# listname.insert(1,"upin")
# # listname.remove("eko")
# name = tuple(listname)    ini di tambahakan.....
# print(name)

# name1= ("tari", "bagas", "raden")
# print(name1)
# print(name2)
# print(name3)

# newname = ("suci","dika","rahman")
# name1 += newname
# kelompok2 = name1 + newname
# print(name1)


# set
# gh = {"dipsi","lala", "po"}

# print(type(gh))
# gh.add("rahul")

# jh = {"eko","eman","sanz"}
# lh = ["edo","gani"]
# gh.update(jh)
# gh.update(lh)


# gh.remove("zaim")
# gh.discard("zul")

# print(gh)



# mh = {"jokowi","prabowo", "anies"}
# nh = {"gagak","kucing","anjing"}
# ll = gh.union(mh,nh)
# lf = gh | mh | nh
# gh.update(mh, nh)
# print(ll)
# print(lf)
# print(gh)


# dictionary
# rumah = {
#     "kamar_ortu":"barang ortu", 
#     "kamar_mu": "barang mu", 
#     "kamar_adik": "barang adik"
# }

# print(rumah["kamar_adik"])
# rumah["kamar_tamu"] = "barang tamu"
# rumah["kamar_mu"] = "barang sepupu"
# del rumah["kamar_tamu"]
# rumah.pop("kamar_tamu")

# print(rumah)

# gabungan 

# siswa = [
#     {
#         "nama_siswa": "Udin",
#         "nilai": [30, 69, 85],
#         "motor": ("supra", "vega"),
#     },
#     {
#         "nama_siswa": "Tani",
#         "nilai": [30, 69,85],
#         "mobil":{"supra", "ferari"},
#     },
# ]

# 1. matematika
# 2. fisika
# 3. olahraga



# siswa[0]["nilai"][0] = 75
# print(siswa)

# udin = siswa[0]["nilai"]
# mtk = udin[0]
# fisika = udin[1]
# olahraga = udin[2]

# print(f"nilai matematika udin adalah {mtk}")
# print(f"nilai fisika udin adalah {fisika}")
# print(f"nilai olahraga udin adalah {olahraga}")




# operator

# operator aritmatika

# a = 4
# b = 3


# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)
# print(a ** b)

# operator penugasan
# c = 5 
# d = 8

# c %= d # c % d
# print(c)

# a = 0

# for i in range(1,11):
    # print(f'nilai a = {a}')
    # print(f'nilai i = {i}')
    # a += i # a = a + i

# print(a)

# operator perbandingan

# a = 4
# b = 3

# print(a < b) # < kurang dari -> 4 < 3
# print(a > b) # > lebih dari -> 4 > 3
# print(a == b) #  == sama dengan -> 4 = 3
# print(a <= b) #  <= kurang dari sama dengan -> 4 < atau sama dengan 3
# print(a >= b) #  >= lebih dari sama dengan -> 4 > atau sama dengan 3
# print(a != b)

# operator logika

"""
and
or 
not
"""

# print(3 > 4 and 4 < 5)
'''
 true and true = true
 false and true = false
 true and false =  false
 false and false = false 
'''

# print(3 > 4 or 4 < 5)
'''
true or true = true 
true or false = true
false or true = true 
f;ase or false = false
'''

#print(not(4 > 4)) # tidak salah
'''
not(true) = false
not(false) = true
'''

# operator indetitas
# kcyinn = "karin"
# zyprush = "zul"
# zenbu = zyprush


# print(kcyinn is zenbu) 
# print(zyprush is zenbu) 
# print(kcyinn is not zenbu) 

# operator member
# zyprush = ["angga","farel","koko"]

# print("karin" not in zyprush)

# operator bitwisee
'''
&
|
^
~
<<
>>
'''

# print(6 & 3)

''' 16 8 4 2 1
--------------
6 = 0  0 1 1 0
3 = 0  0 0 1 1
--------------- &
2 = 0 0 0 1 0    
'''

# print(4 & 2)
''' 4 2 1
--------------
5 = 1 0 1
2 = 0 1 0
--------------- &
0 = 0 0 0
'''


# print(3 | 4)
''' 4 2 1
--------------
3 = 0 1 1
2 = 1 0 0
--------------- |
7 = 1 1 1
'''


# print(5 | 9)

# print(4 ^ 6) #xor
''' 4 2 1
--------------
4 = 1 0 0
6 = 1 1 0
--------------- ^
2 = 0 1 0
'''


# print(12 ^ 16)

# print(~3)

''' 8 4 2 1
--------------
3 = 0 0 1 1
--------------- ~
-4 =1 1 0 0
'''


# print(~1)

# print(4 << 2)
'''32 16 8 4 2 1
--------------
4 = 0 0 0 1 0 0
--------------- <<
16= 0 1 0 0 0 0
'''


# print(5 << 3)


print(8 >> 2)
''' 8 4 2 1
--------------
4 = 1 0 0 0
--------------- >>
r = 0 0 1 0
'''

print(3 >> 2)

''' 8 4 2 1
--------------
3 = 0 0 1 1
--------------- >>
0 = 0 0 0 0
'''

print(6 >> 2)






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
