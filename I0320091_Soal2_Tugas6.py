#Soal 2 Tugas 6

print("************Menghitung Nilai Rata-Rata************")
banyakdata = int(input("Banyak datanya :"))
datanya = []
jumlahnya = 0
for nilai in range(0, banyakdata):
    temp = int(input("Masukkan data ke-%d: " % (nilai + 1)))
    datanya.append(temp)
    jumlahnya += datanya[nilai]
    ratarata = jumlahnya / banyakdata
print("Rata-ratanya adalah: ", ratarata)