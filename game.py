import random
import time
import keyboard
import colorama
import math
from enum import Enum
import fl
import Mensajes
import Acciones
import Eventos
def PerderJuego():
	return
def EspaciosLibres():
	return data["espacios"]-data["ciudadanos"]
def PasarDificultad(difficulty):
	if (difficulty == 1):
		acciones["casas"] = ComprarCasas(1)
		acciones["campaña"] = Campaña(2)
		evB = PosibilidadDeActuacion(100, {"fama": lambda x: x//1.15}, Mensajes.terrEvB)
		prM = PosibilidadDeActuacion(90,{"dn": lambda x: x-1000000, "espacios": lambda x: (x-data["ciudadanos"])//10}, Mensajes.terrPrM)
		prB = PosibilidadDeActuacion(10,{"fama": lambda x: x*1.4, "dn": lambda x: x-1000000}, Mensajes.terrPrB)
		nadater = PosibilidadDeActuacion(100, {"fama": lambda x: x//1.12, "espacios": lambda x: x - EspaciosLibres()//10}, Mensajes.terrNada)
		invDin = PosibilidadDeActuacion(100, {"dn": lambda x: x+500000}, Mensajes.invDin)
		invFam = PosibilidadDeActuacion(100, {"fama": lambda x: x+20}, Mensajes.invFam)
		invCiu = PosibilidadDeActuacion(100, {"ciudadanos": lambda x: min(x+100, EspaciosLibres())}, Mensajes.invCiu)
		invEnf = PosibilidadDeActuacion(300, None, Mensajes.invEnf)
		invNad = PosibilidadDeActuacion(100, None, Mensajes.invNada)
		eventos["inversor"] = Muerte(Mensajes.inversor, [Actuacion(Mensajes.Inv, [invFam, invCiu, invDin, invEnf]), Actuacion("Nada", [invNad])], 15, 0, -1, None )
		eventos["coyotes"] = Muerte(Mensajes.coyotes, [Actuacion(Mensajes.coyPag, [PosibilidadDeActuacion(100, {"dn": lambda x: x-500000, "fama": lambda x: x+5}, Mensajes.coyPagB)]), Actuacion("Nada", [PosibilidadDeActuacion(100, {"ciudadanos": lambda x: x-x//10, "fama": lambda x: x//1.1}, Mensajes.coyNada)])], 15, 1, 1, "test")
		eventos["terremoto"] = Muerte(Mensajes.terremoto, [Actuacion(Mensajes.Ev, [evB]), Actuacion(Mensajes.CompPr, [prM, prB]), Actuacion("Nada", [nadater])], 10, 1, 1, None)
def CalcularWeights(elements, neutrality=0):
	weightcount=neutrality
	for element in elements:
		if (type(element) == str):
			element = elements[element]
		element.weightorder = weightcount
		weightcount += element.weight
		element.maxweight = weightcount
	return weightcount

def CheckJuego():
	if (data["dn"] < 0 or data["fama"] < 0):
		PerderJuego()
	if (data["ciudadanos"] > 200 and data["tiempo"] > 12):
		PasarDificultad()
	return
class Generator:
	def __init__(self, key, keyeffects: dict[str, float]):
		self.keyeffects = keyeffects
		self.key = key
	def Ciclo(self):
		global data
		if (self.keyeffects != None):
			for keyfect in self.keyeffects:
				data[keyfect] = self.keyeffects[keyfect](data[self.key], data[keyfect])
# Esto es un test

class PosibilidadDeActuacion:
	def __init__(self, weight: int, keyEfect: dict[str, float], mensaje: str):
		self.weight = weight
		self.keyEffect = keyEfect
		self.weightorder = 0
		self.maxweight = 0
		self.mensaje = mensaje
	def Actua(self):
		global data
		if (self.keyEffect != None):
			for keyfect in self.keyEffect:
				data[keyfect] = self.keyEffect[keyfect](data[keyfect])
		print(self.mensaje)
class Actuacion:
	def __init__(self, mensaje: str, posibilidades: list[PosibilidadDeActuacion]):
		self.mensaje = mensaje
		self.posibilidades = posibilidades
	def Presentar(self, number):
		print(f"{number}- {self.mensaje}")
	def Accion(self):
		if len(self.posibilidades) == 1:
			self.posibilidades[0].Actua()
			return
		weights = CalcularWeights(self.posibilidades)
		weight = random.randrange(weights)
		for posibilidad in self.posibilidades:
			if weight >= posibilidad.weightorder and weight < posibilidad.maxweight:
				posibilidad.Actua()
				break
	
class Muerte:
	def __init__(self, mensaje: str, actuaciones: list[Actuacion], weight: int, caos: int, protecciones: int, mensajeProtecciones: str):
		self.mensaje = mensaje
		self.actuaciones = actuaciones
		self.weight = weight
		self.weightorder = 0
		self.maxweight = 0
		self.caos = caos
		self.protecciones = protecciones
		self.msgProtec = mensajeProtecciones
	def Acciones(self):
		print(self.mensaje)
		j = 1
		protec = False
		if data["protecciones"] >= self.protecciones and self.protecciones != -1:
			print(f"1- Gastar protecciones ({data["protecciones"]})")
			j += 1
			protec = True
		for accion in self.actuaciones:
			accion.Presentar(j)
			j+=1
		i = int(input())
		if protec and i == 1:
			data["protecciones"] -= self.protecciones
			print(self.msgProtec)
			return
		try:
			self.actuaciones[i-1 if protec == False else i-2].Accion()
		except:
			self.actuaciones[-1].Accion()

class Accion:
	def __init__(self, identificador):
		self.ident = identificador
		self.mensaje = ""
		self.instrucciones = ""
		self.mensajeFinal = ""
	def Mensaje(self):
		print(f"{self.ident}- {self.mensaje}")
	def Instrucciones(self):
		print(self.instrucciones)
	def MensajeFinal(self):
		print(self.mensajeFinal)
	def Accion(self):
		CheckJuego()

class ComprarCasas(Accion):
	def __init__(self, identificador):
		super().__init__(identificador)
		self.mensaje = "Comprar Casas"
		self.instrucciones = """Comprando casas aumentas la cantidad de espacios en tu ciudad haciendo que vvenga mas gente cuando hagas campaña
y aumentan tu fama
Puedes decidir el nivel de lujo y cantidad de casas que quieres, cuanto mayor nivel de lujo más fama conseguirás pero más caras serán las casas
el precio es igual a 100.000 * nivel de lujo^2"""
	def Accion(self):
		lujo = int(input("Introduce el nivel de lujo: "))
		casas = int(input("Introuce cuantas casas quieres: "))
		data["dn"] -= casas*lujo**2*100000
		data["fama"] += casas*lujo**3
		data["espacios"] += casas*lujo
		super().Accion()
  
class Campaña(Accion):
	def __init__(self, identificador):
		super().__init__(identificador)
		self.mensaje = "Hacer Campaña"
		self.instrucciones = """Cuando haces campaña vienen ciudadanos a tu ciudad y ocupan espacios de casas
Cuantos mas espacios de casa tengas y más fama tengas mas ciudadanos vendran
pero cuanta mas fama más cara es la campaña costo: 500.000 + fama * 625"""
	def Accion(self):
		espacioslibres = EspaciosLibres()
		data["ciudadanos"] += (int)(espacioslibres // (10+(espacioslibres**0.1)) + min(espacioslibres//5, (((data["fama"]**0.004)-1) * espacioslibres)))
		data["dn"]-= (500000 + 625 * data["fama"])
		super().Accion()
EXCLUDED_DATA = {}	
data = {}
acciones = {}
eventos = {}
generadores = {"ciudadanos": (Generator("ciudadanos", {"dn": lambda x,y: y+x*2500}))}
internalData = {}
def ShowInfo(difficulty):
	print(f"Tienes: {data["dn"]} €")
	print("\033[1;36m" + f"Tienes {data["ciudadanos"]} ciudadanos")
	print(f"Tienes {EspaciosLibres()} sitios de casas libres")
	print(f"Tienes {data['fama']} de fama" '\033[0;m')
def EligeJuego():
	return int(input("\033[;34m"+" Quieres crear una ciudad o ser un ciudadano: 1-presidente 2-ciudadano\n"'\033[0;m'))
def CargarDatos():
	return
def IniciarJuego():
	global data,acciones,eventos,internalData
	data = {"dn": 30000000, "ciudadanos": 0, "tiempo": 0, "fama": 100, "espacios":0, "protecciones": 0}
	acciones = {}
	eventos = {}
	internalData = {"factorFama": 625, "neutrality":60}
	PasarDificultad(1)
def Ciclo():
	data["tiempo"] += 1 
	Evento()
	for generator in generadores.values():
		generator.Ciclo()
	ShowInfo(1)
def Evento():
	if (len(eventos)) == 1:
		eventos[0].Acciones()
		return
	weights = CalcularWeights(eventos, internalData["neutrality"])
	weight = random.randrange(weights)
	for posibilidad in eventos:
		posibilidad = eventos[posibilidad]
		if weight >= posibilidad.weightorder and weight < posibilidad.maxweight:
			posibilidad.Acciones()
			break
def Accion():
	print("Que quieres hacer? (Escribe otro numero para no hacer nada)")
	actos =[]
	for accion in acciones:
		accion = acciones[accion]
		accion.Mensaje()
		actos.append(accion)
	i = int(input())
	try:
		actos[i-1].Accion()
	except: return
def Settings():
	return
def Instrucciones():
	return
def Fecha(meses):
	return colorama.Fore.LIGHTBLACK_EX + f"Años: {meses//12} Meses: {meses%12}"

def main():
	interval = 2.5
	while True:
		Accion()
		Ciclo()

IniciarJuego()
main()

