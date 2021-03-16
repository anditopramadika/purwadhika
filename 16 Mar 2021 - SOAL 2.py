def nomorHP():
    nomorHP = input('Masukkan Nomor HP :')

    if len(nomorHP) > 13:
        print('Nomor HP hanya maksimal 13 Angka')
    elif nomorHP.startswith('08') :
        print(nomorHP)
    else :
        print('Nomor HP harus dimulai dengan 08')

nomorHP()