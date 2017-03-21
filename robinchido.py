#-*-coding:utf-8-*-

tiempo = 0
fin = []
class proceso:
	def __init__(self, ide, nombre, memoria, rafaga):
		self.ide = ide
		self.nombre = nombre
		self.memoria = memoria
		self.rafaga = rafaga
		self.espera = rafaga
		self.eje = 0
		self.veces = 0

class cola:
	lista = []
	def __init__(self,ram):
		if ram != None:
			self.ram = ram
	def insertar(self, proceso):
		self.lista.append(proceso)
class cola2:
	lista = []
	def __init__(self):
		lista = []
	def insertar(self, proceso):
		self.lista.append(proceso)

def subir_listos_ejec(cola_ejecucion, cola_procesos, q, n):
	while cola_ejecucion.ram >= cola_procesos.lista[0].memoria:
		cola_ejecucion.ram -= cola_procesos.lista[0].memoria
		cola_ejecucion.insertar(cola_procesos.lista[0])
		print("======================================================================================")
		print("Subio el proceso ",cola_procesos.lista[0].nombre," y restan ",cola_ejecucion.ram," unidades de memoria")
		print("======================================================================================")
		print("\n\n")
		#round_robin(cola_ejecucion, cola_procesos)
		del cola_procesos.lista[0]
		print("======================================================================================")
		print("Cola de ejecucion")
		for x in reversed(cola_ejecucion.lista):
			print(x.nombre, end=" ")
		print("")
		print("======================================================================================")
		print("\n\n")
		if len(cola_procesos.lista)==0:
			break
	round_robin(cola_ejecucion, cola_procesos, q, n)
	
def round_robin(cola_ejecucion, cola_procesos, q, n):
	global tiempo
	if  len(cola_ejecucion.lista)!=0:

		#if cola_ejecucion.lista[0].rafaga<=4:
			#cola_ejecucion.lista[0].espera = tiempo - (4*cola_ejecucion.lista[0].veces)
		print("Cola de ejecucion")
		print("======================================================================================")
		for x in reversed(cola_ejecucion.lista):
			print(x.nombre, end=" ")
		print("")
		print("======================================================================================")
		print("\n\n")
		for j in range(1, q+1):
			cola_ejecucion.lista[0].rafaga -= 1
			print(cola_ejecucion.lista[0].nombre+" en ejecucion. Restan "+str(cola_ejecucion.lista[0].rafaga)+" mseg")
			#print(cola_ejecucion.lista[0].rafaga
			tiempo+=1
			if cola_ejecucion.lista[0].rafaga == 0:
				cola_ejecucion.ram += cola_ejecucion.lista[0].memoria
				print("======================================================================================")
				print("Termino de ejecutarse el proceso  ",cola_ejecucion.lista[0].nombre," y ahora hay ",cola_ejecucion.ram," unidades de memoria")
				print("\n\n")
				print("======================================================================================")
				fin.append(cola_ejecucion.lista[0])
				cola_ejecucion.lista[0].eje = tiempo
				del cola_ejecucion.lista[0]
				print("Cola de ejecucion")
				print("======================================================================================")
				for x in reversed(cola_ejecucion.lista):
					print(x.nombre, end=" ")
				print("")
				print("======================================================================================")
				print("\n\n")
				break
				#j=1000000000
			if(j==q):
				cola_ejecucion.lista.append(cola_ejecucion.lista[0])
				del cola_ejecucion.lista[0]
				cola_ejecucion.lista[0].veces+=1
			input()

	else:
		pass

try:
	promedio_ejecucion = 0
	promedio_espera = 0
	print("Bienvenido al planificador de procesos")

	try:
		n = int(input("Ingrese el número de procesos que desea ejecutar: "))
	except:
		print("No ingresó un entero válido")
		exit()
	try:
		q = int(input("Ingrese el quantum que desea que tenga el planificador: "))
	except:
		print("No ingresó un entero válido")
		exit()
	try:
		m = int(input("Ingrese las unidades de memoria que desea tener: "))
	except:
		print("No ingresó un entero válido")
		exit()

	try:	
		ejecucion = cola(m)
	except:
		print("No ingresó un entero válido")
		exit()
	procesos = cola2()

	for k in range(0, n):
		try:
			nombre = input("Ingrese el nombre del proceso "+str(k+1)+": ")
		except:
			print("No ingresó un entero válido")
			exit()
		try:
			memoria = int(input("Ingrese las unidades de memoria del proceso "+str(k+1)+": "))
			while memoria>m:
				memoria = int(input("No hay suficiente espacio para este proceso, ingresa otras unidades de memoria:  "))
			
		except:
			print("No ingresó un entero válido")
			exit()
		try:
			rafaga = int(input("Ingrese la ráfaga del proceso "+str(k+1)+": "))
		except:
			print("No ingresó un entero válido")
			exit()
		try:
			p = proceso(k,nombre,memoria,rafaga)
		except:
			print("No ingresó un entero válido")
			exit()
		procesos.insertar(p)
		print(" ")
	print("Cola de procesos")
	for x in reversed(procesos.lista):
		print(x.nombre, end=" ")
	print("\n\n")
	ch = len(procesos.lista)
	while  len(procesos.lista)!=0 or len(ejecucion.lista)!=0:
		if len(procesos.lista)!=0:
			subir_listos_ejec(ejecucion,procesos, q, n)
			ch-=1
		else:
			if len(ejecucion.lista)!=0:
				round_robin(ejecucion,procesos, q, n)
			else:
				break
	for x in fin:
		promedio_ejecucion += x.eje
		print("Tiempo ejecucion:  ",x.eje, " Nombre",x.nombre)
	for x in fin:
		x.espera = x.eje - x.espera
		promedio_espera += x.espera
		print("Tiempo espera: ",x.espera, " Nombre ",x.nombre)

	print("Tiempo promedio de ejecucion:  ",promedio_ejecucion/len(fin), "mseg")
	print("Tiempo promedio de espera:  ",promedio_espera/len(fin), "mseg")

except KeyboardInterrupt:
	print("Salió de la ejecución con una interrupción del teclado")