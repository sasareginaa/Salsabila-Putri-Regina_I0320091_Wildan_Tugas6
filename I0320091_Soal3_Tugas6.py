#Soal 3 Tugas 6

for angkanya_adalah in range(10,25):
    for i in range(2, angkanya_adalah):
        if (angkanya_adalah % i) == 0:
            print(angkanya_adalah, "bukan bilangan prima")
            break
    else:
        print(angkanya_adalah, "merupakan bilangan prima")