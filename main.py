import random,os
def pilihan():
	string = 'abcdefghijklmnopqrstuvwxyz'
	besak = input('Masukkan Huruf besar ? (y/N): ').lower()
	if besak == 'y':
		string += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	nomor = input('Masukkan Angka ? (y/N): ').lower()
	if nomor == 'y':
		string += '123456789' 
	char = input('Masukkan Special Character ? (y/N): ').lower()
	if char == 'y':
		string += '<>.,!@#$%^&*()-_+='

	return string

jumlah = int(input('Masukkan Jumlah Digit Password : '))
stringY = pilihan() 
print(stringY)
os.system('clear')
print('Saran : ')
data = ''.join([random.choice(stringY) for i in range(jumlah)])
print(data)

