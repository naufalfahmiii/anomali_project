print("program menghitung volume tabung")

# menerima input jari-jari dan tinggi tabung
jari_jari = int(input("masukkan jari-jari tabung :"))
tinggi = int(input("masukkan tinggi tabung :"))
phi = 22/7

# menghitung volume tabung
volume_tabung = phi * jari_jari * 2 * tinggi

 # menampilkan hasil
print("jari - jari tabung adalah", jari_jari, "cm")
print("tinggi tabung adalah", tinggi, "cm")
print("phi tabung adalah 22/7")
print("maka volume tabung adalah", volume_tabung, "cm3")
