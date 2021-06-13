#dictionary
#d = {
    #"nama" : "Ghiffari",
    #"umur" : 21,
    #"tinggi" : 170.5
    #Key        #Value
#}
#print(d)
#print(type(d["umur"])) #Pemanggilan

#d["umur"] = 20
#print(d)

#d = []

#or i in range(1):
    #nama = input("Masukkan Nama anda : ")
    #umur = int(input("Masukkan Umur anda : "))
    #tinggi = float(input("Masukkan Tinggi anda : "))
    #data = {
        #"nama" : nama,
        #"umur" : umur,
        #"tinggi" : tinggi
    #}
    #d.append(data)

#for i in d:
    #print("Nama Pelanggan : ",i["nama"])
    #print("Umur Pelanggan : ",i["umur"])
    #print("Tinggi Pelanggan : ",i["tinggi"])

def function():
    print("Halo")
function()    

def function1(name="None"):
    print("Halo saya",name)
function1()    

def function2(nama, umur, tinggi):
    print("Umur : ",umur)
    print("Tinggi : ",tinggi)
    print("Nama : ",nama)
function2(nama="Ghiffari", tinggi=160.4, umur= 21)    

def keliling_kotak(p,l):
    keliling = p+p+l+l
    text = "kelilingnya adalah {}".format(keliling)
    return keliling
print(keliling_kotak(20,31))    
x=keliling_kotak(21,30)
print(x)