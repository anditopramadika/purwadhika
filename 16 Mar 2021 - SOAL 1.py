import string

def kalimat():
    a = input('Masukkan Sebuah Kalimat : ')

    b = a.upper()
    c = b.replace(' ','')

    if len(a) == 0  :
        print('Masukkan Sebuah Inputan')
    elif len(a) < 200 :
        print('*'+c+'*')
    elif len(a) > 200 :
        print('Batas Karakter Maksimal Hanya 200')

kalimat()