def check():
    while True:
        number=int(input("masukin nilai mu:"))
        if number>100 or number<0:
            print("masukin yang bener")
        else:
            break
    return number
a = check()


def pengelompokan_nilai(nilai):
    if nilai>= 91 and nilai<=100:
        A = ["skor" , nilai, "A"]
        return A
    elif nilai>= 81 and nilai<=90:
        B = ["skor", nilai, "B"]
        return B
    elif nilai>= 70 and nilai<= 80:
        C = ["skor", nilai, "C"]
        return C
    else:
        D = ["skor", nilai, "D"]
        return D
nilai = pengelompokan_nilai(a)
print(nilai)


def kalimat(nilai_dan_grade):
    nilai_dan_grade[0]= "Score"
    return nilai_dan_grade
print(kalimat(nilai))