# soal nomor 1
tup = ('pensil', 'buku', 'penggaris', 1500, 5000, 2000)

barang = []
harga = []

for item in tup:
    if isinstance(item, int):
        harga += (item,)
    elif isinstance(item, str):
        barang.append(item)

barangx = ["pensil", "buku", "penggaris"]
hargax = [1500, 5000, 2000]

def barangs():
    for x in barangx:
        return (x)

def hargas():
    for x in hargax:
        return (x)

print("1. Data tuple : ", tup)
print("2. Pemisahan barang dan harga (dalam tuple):", barang, harga)
print("3. ", barangs(), hargas())
