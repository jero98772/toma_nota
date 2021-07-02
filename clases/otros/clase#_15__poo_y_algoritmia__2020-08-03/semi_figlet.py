from pyfiglet import Figlet
h = [["|"," "," ","|"],["|"," "," ","|"],["|","_","_","|"],["|"," "," ","|"],["|"," "," ","|"]]
for i in h :
	print(*i,"\n")
f = Figlet()
print (f.renderText('H'))
def complicarseVida():
	tamaño = 6
	for i in range(tamaño):
		if i == (tamaño/2):
			print("| |__| |\n|  __  |")
		elif i == 0:
			print(" _    _") 
		elif i == tamaño-1:
			print("|_|  |_|")
		else:
			print("| |  | |")
complicarseVida()
