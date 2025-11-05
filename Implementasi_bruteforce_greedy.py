# brute force (tanpa angka berulang di tiap kombinasi)
def cari_kombinasi(toples, batas, start=0, kombinasi_sekarang=None, hasil=None):
    if kombinasi_sekarang is None:
        kombinasi_sekarang = []
    if hasil is None:
        hasil = []

    # Jika jumlah kombinasi sekarang tepat sama dengan batas → simpan
    if sum(kombinasi_sekarang) == batas:
        hasil.append(list(kombinasi_sekarang))
        return hasil

    # Jika jumlah sudah melebihi batas → hentikan
    if sum(kombinasi_sekarang) > batas:
        return hasil

    # Coba tambahkan isi toples dari posisi 'start' ke depan (agar tidak berulang)
    for i in range(start, len(toples)):
        kombinasi_sekarang.append(toples[i])
        cari_kombinasi(toples, batas, i + 1, kombinasi_sekarang, hasil)
        kombinasi_sekarang.pop()  # backtrack

    return hasil


# Data contoh (lebih banyak angka supaya hasil lebih banyak)
toples = [int(input(f"Masukkan isi toples ke-{i+1}: ")) for i in range(5)]
batas = int(input("Masukkan batas jumlah permen yang diinginkan: "))

hasil = cari_kombinasi(toples, batas)

print(f"\nSemua kombinasi unik untuk mencapai {batas} permen:")
for i, combo in enumerate(hasil[:50], 1):  # tampilkan maksimal 50 kombinasi pertama
    print(f"{i}. {combo}")

print(f"\nTotal kombinasi ditemukan: {len(hasil)}")

# greedy

def permen_greedy(toples, batas):
    toples.sort(reverse=True)   # urutkan dari terbesar
    total = 0
    hasil = []

    for t in toples:
        if total + t <= batas:  # hanya ambil jika tidak melebihi batas
            hasil.append(t)
            total += t
    return hasil, total

toples = [int(input(f"Masukkan isi toples ke-{i+1}: ")) for i in range(5)]
batas = int(input("Masukkan batas jumlah permen yang diinginkan: "))
hasil, total = permen_greedy(toples, batas)

print("Greedy:")
print("Toples dipilih:", hasil)
print("Jumlah permen maksimal:", total)

