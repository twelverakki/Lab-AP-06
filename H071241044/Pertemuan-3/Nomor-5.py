a = int(input("Masukkan populasi awal serangga A: "))
b = int(input("Masukkan populasi awal serangga B: "))
n = int(input("Masukkan jumlah hari penelitian: "))

def hitung(x, y, z, m = False):
	if m:
		populasia = x - x*0.1
		populasib = y - y*0.1
	else:
		populasia = x + x*0.3 if z == 'naik' else x - x*0.2
		populasib = y + y*0.5 if z == 'naik' else y - y*0.4
	return [int(populasia), int(populasib)]

i = 1

while i <= n:
	if i % 5 == 0:
		c = hitung(a, b, 'turun', True)
		a = c[0]
		b = c[1]
		print(f'hari {i}: Predator memakan 10% dari populasi')

	if i % 2 != 0:
		c = hitung(a, b, 'naik')
		a = c[0]
		b = c[1]
	else:
		c = hitung(a, b, 'turun')
		a = c[0]
		b = c[1]

	i += 1

	pesanA = f"Populasi Serangga A = {a}" if a > 0 else "Populasi Serangga A Habis"
	pesanB = f"Populasi Serangga B = {b}" if b > 0 else "Populasi Serangga B Habis"

	print(f"hari {i}: {pesanA}, {pesanB}")
	if a == 0 and b == 0:
		print("Penelitian dihentikan! Populasi serangga a dan b telah habis!")
		break