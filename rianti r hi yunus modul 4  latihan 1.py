total_belanja = float(input("Masukkan total belanja Anda: Rp. "))

if total_belanja >= 250000:
    diskon = total_belanja * 50 / 100
    print("Anda mendapatkan diskon sebesar Rp.", diskon)
else:
    print("Total belanja Anda tidak mencapai Rp. 250.000")
    print("Anda tidak mendapatkan diskon.")
