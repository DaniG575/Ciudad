
	next_call = time.time() + interval
	while True:
		if keyboard.is_pressed("space"):
			Accion()
			break
		current_time = time.time()
		if current_time >= next_call: 
			current_time = time.time()
			Ciclo()
			next_call = max(current_time + interval, time.time() + interval/4)
		time.sleep(0.1)	


pato = 0
detect = 1
juego=int(input("\033[;34m"+" Quieres crear una ciudad o ser un ciudadano: 1-presidente 2-ciudadano\n"'\033[0;m'))
if juego == 1:
	print("Escribe info para instrucciones escibe jugar para jugar")
	n = input("\033[1;33m")
	if n == ("info"):
		print('\033[0;m' "Instrucciones")
	else:
		print('\033[0;m' "Introduce el nombre de tu ciudad")
	s = input("\033[1;33m")
	print( '\033[0;m'f"Tu ciudad se llama: {s} y empiezas con 0 ciudadanos, 30 millones de € y empiezas en los escombros")
	dn = 30000000
	C = 0
	t = 0
	a = 0
	fama = 100
	sp = 0
	sa = 0
	df = 1
	dff = 0.1
	l = 0
	V = 1
	VB = 0
	LMP = 0
	pato = 0
	PR = 0
	comida = 0
	vecesperdidas=0
	vecesganadas=0
	trabajo=1
while n != ("easter egg") and pato != 1 and juego == 1:
	t += 1
	if t == 12:
		a += 1
		t = 0
	if dn <= 0:
		print("Has perdido")
		break
		print(f"Dinero: {dn}")
	if df == 1:
		fgh = C * 2500 * V
		dn += fgh
		print("\033[1;33m" + f"Ingresos: {fgh}" '\033[0;m')
		print("\033[1;33m" + f"Dinero: {dn} " '\033[0;m')
		print("Inserte 1 para: comprar casas (comprando casas atraeras a mas ciudadanos cuando hagas campañas) costo: 100.000 multiplicado\n por el nivel de lujo de la casa que desee al cuadrado. -1 "	)
		print("Inserte 2 para hacer campaña: (atraeras a ciudadanos para que se alogen en tus casas.) vienen un fama porciento de los huecos que quedan libres. costo:500.000 + fama multiplicado por 250. -2")
		print("inserte 4 para jugar a la loteria")
		print("Pon otro numero para no hacer nada(si tienes ciudadanos, te pagaran por alojarte en las casas que has construido)")
		print(f"Tienes: {dn} €")
		nt = int(input())
		if nt == 2345:
			ntttt = input()
			if ntttt == ("/moneie"):
				dn5 = int(input())
				dn = dn5
			if ntttt == ("/Cudadanos"):
				C5 = int(input())
				C = C5
			if ntttt == ("/DFA"):
				df = int(input())
		if nt == 1:
			lujo = int(input("Nivel de lujo: "))
			qt = int(input("Cantidad de casas: "))
			dn -= (100000 * lujo * lujo * qt)
			fama += lujo * lujo * (lujo) * qt
			sp += lujo * qt
		if nt == 2:
			dn -= 500000 + (fama * 250)
			C += sp // 10
			sp -= sp // 10
		if nt == 4:
			loteria=int(input("\033[;34m"+" En este nivel solo hay dos tipos diferentes de loteria. Esta la loteria normal, que son boletos de 2 cifras que cada uno cuesta 5€ y ganas 10.000€. La última que es la loteria pequeña que son boletos de 1 cifra que cuestan 10€ y ganas 1.000€. Si quieres jugar la normal, inserte 1 y si quieres jugar la pequeña, inserte 2.:\n"'\033[0;m'))
			if loteria==1:
				veces=int(input("cuantas veces quieres jugar"))
				while veces>0:
					a=int(input("Numero de loteria (hasta dos cifras)?: "))
					computer=random.randrange(100)
					if a==computer:
						print("\033[1;32m]" +"HAS ganado la loteria!!!"'\033[0;m')
						print(f"has ganado 10.000, ahora tu dinero sube de {dn}€ a {dn+10000}€")
						dn=dn+10000
						vecesganadas+=1
					else:
						print("\033[1;31m""no has ganado"'\033[0;m')
						print(f"el numero ganador ha sido {computer}")
						print(f"acabas de perder 5€, ahora tu dinero baja de {dn}€ a {dn-5}€")
						dn=dn-5
						vecesperdidas+=1
					veces-=1
					if veces==0 and vecesganadas==0:
						print("\033[1;31m"+f"Acabas de perder {vecesperdidas*10}€")
					if veces==0 and vecesganadas!=0:
						print("\033[1;32m" +f"Acabas de ganar {vecesganadas*1000-vecesperdidas*10}€")
					vecesganadas=0
					vecesperdidas=0
			if loteria==2:
				veces=int(input("cuantas veces quieres jugar: "))
				while veces>0:
					a=int(input("Numero de loteria (solo una cifra)?: "))
					computer=random.randrange(10)
					if a==computer:
						print("\033[1;32m" +"HAS ganado la loteria!!!"'\033[0;m')
						dn=dn+1000
						vecesganadas+=1
					else:
						print("\033[1;31m""no has ganado"'\033[0;m')
						print(f"el numero ganador ha sido {computer}")
						dn=dn-10
						vecesperdidas+=1
					veces-=1
					if veces==0 and vecesganadas==0:
						print("\033[1;31m"+f"Acabas de perder {vecesperdidas*10}€")
						vecesganadas=0
						vecesperdidas=0
					if veces==0 and vecesganadas!=0:
						print("\033[1;32m" +f"Acabas de ganar {vecesganadas*1000-vecesperdidas*10}€")
						vecesganadas=0
						vecesperdidas=0

		if C >= 10000:
			C = 10000
		print("\033[1;36m" + f"Tienes {C} ciudadanos")
		print(f"Tienes {sp} sitios de casas libres")
		print(f"Tienes {fama} de fama" '\033[0;m')
		if C >= 200 and a >= 1:
			df = 2
		k = random.randrange(100) + 1
		print(k)
		if k > 0 and k < 15:
			print("\033[1;31m" + "MUERTE: hay coyotes vamos a morirrrrrr!!!!!"'\033[0;m')
			print("1- Nada 2- Pagar 500000 para comporar a especialistas que los espanten")
			print(f"Tienes: {dn} €")
			kte = int(input())
			if kte == 1:
				print("\033[3;34m" + "Los coyotes mataron a ciudadanos :("'\033[0;m')
				C -= C // 10
				fama //= 1.1
			else:
				dn -= 500000
				print("\033[3;34m" +"Has perdido dinero pero tu fama ha aumentado!!!!!!!!!!!"'\033[0;m')
				fama += 5
		if k > 50 and k < 61:
			print("\033[1;31m" +"MUERTE: hay un mini terremoto vamos a morirrrrrr!!!!!"'\033[0;m')
			print("1- Nada 2- Evacuar 3- Comprar protecciones")
			print(f"Tienes: {dn} €")
			ktp = int(input())
			if ktp == 1:
				print("\033[3;34m" +"El terremoto ha roto casas pierdes espacios :("'\033[0;m')
				sp -= sp // 10
				fama //= 1.12
			elif ktp == 2:
				print("\033[3;34m" + "Pierdes fama pero nada se ha derrumbado"'\033[0;m')
				fama //= 1.15
			else:
				dn -= 1000000
				print("\033[3;34m" +"Has perdido dinero y ademas no llego a tiempo y perdiste espacios y las protecciones"'\033[0;m')
				sp -= sp // 10
		if k > 85 and k < 99:
			inv = int(
					input("\033[1;32m]" +"SUERTE: que suerte has tenido, a un inversor le ha encantado tu ciudad\n, que quieres hacer 1-Invitarle\n a comer o 2-Nada."'\033[0;m'))
			print(f"Tienes: {dn} €")
			if inv == 1:
				kk = random.randrange(6)+1
				if kk == 1 or kk == 0:
					print("\033[3;34m" +f"El inversor te ha dado dinero ahora tu dinero sube 500.000€, ahora tienes {dn+500000}€"'\033[0;m')
					dn += 500000
				if kk == 2:
					print("\033[3;34m" +f"El inversor te ha dado un poco de fama ahora tu fama sube 20, ahora tienes {fama+20} de fama"'\033[0;m')
					fama += 20
				if kk == 3:
					print("\033[3;34m" +f"El inversor te ha dado  100 ciudadanos, ahora tienes {C+100} ciudadanos"'\033[0;m')
					C += 100
				if kk > 3 and kk < 7 or k == 6:
					print("\033[3;34m" +"Has tratado mal al inversor y ya no quiere oir nada mas de ti, no te da nada"'\033[0;m')
			else:
				print("\033[3;34m" +"El inversor se ha enfadado, no te da nada, podría haberte dado muchas cosas"'\033[0;m')
	#dif 2
	if df == 2 and pato != 1:
		print("\033[2;35m" +"HOLA!, subes a nivel 2 ahora recibes 2.000.000€!! y 150000 comida")
		print(f"Tu dinero sube de {dn}€ a {dn+2000000}" '\033[0;m')
		dn += 2000000
		comida = 150000
		print("\033[1;35m" +"Ahora desbloquas: la comida, cada ciudadano gasta 50Kg al mes. Sistema de limpieza, sirve para prevenir enfermedades, protecciones por adelantado que sirve para protegerse de los terremotos y puedes subir/bajar valor de casas"'\033[0;m')
		while df == 2 and pato != 1:
			t += 1
			if t == 12:
				a += 1
				t = 0
			if dn <= 0 or (fama / ((V + 100) * (V**(V * 10)))) <= 1:
				print(f"Has perdido, te has quedado sin dinero.\n numero de ciudadanos: {C}\n espacios que te sobraban: {sp}\n dinero: 0")
				df = 1
				pato = 1
				break
			fgh = C * 2500 * V
			dn += fgh
			print("\033[1;33m" + f"Ingresos: {fgh}" '\033[0;m')
			print("\033[1;33m" + f"Dinero: {dn} " '\033[0;m')
			print("Que quieres hacer? 1- Comprar casas, costo: 100.000 multiplicado\n por el nivel de lujo que desee al cuadrado. "	)
			print("2- Hacer campaña, vienen un porciento de la fama por los hrcos que quedan libres. costo:500.000 + fama multiplicado por 250. -2")
			print("pPon 50 para cambiar el valor de las casas ten en cuenta la fama bajara/subira mucho depende de el valor ")
			print("Pon 10 para comprar comida ")
			print("Pon 23 para mejorar el sistema de limpieza y luego pon cuantos niveles lo mejoras un nivel cuesta 10000000 y tienes que pagar 10000 al mes por nivel")
			print("Pon 45 para comprar protecciones contra desastres")
			print("Pon otro numero para no hacer nada")
			print(f"Tienes: {dn} €")
			nt = int(input())
			if nt == 45:
				PRS = int(input("Cuantas protecciones quieres? valen 500000: "))
				print(f"Tienes: {dn} €")

				PR += PRS
				dn -= PRS * 500000
			if nt == 23:
				limpio = int(input("Cuantos niveles de limpieza mejoras?"))
				print(f"Tienes: {dn} €")
				LMP += limpio
				dn -= limpio * 10000000
			if nt == 10:
				holita = int(
						input("Cuantos kg de comida quieres comprar? cada kg vale 5: "))
				print(f"Tienes: {dn} €")
				comida += holita
				dn -= 5 * holita
			if nt == 50:
				V = float(input("Por cuál es el valor de las casas?:  "))
				print(fama)
			if nt == 1:
				lujo = int(input("Nivel de lujo: "))
				qt = int(input("Cantidad de casas: "))
				dn -= (100000 * lujo * lujo * qt)
				fama += lujo * lujo * (lujo) * qt
				sp += lujo * qt
			if nt == 2:
				dn -= 500000 + (fama * 250)
				C += sp // 10
				sp -= sp // 10
				if C >= 20000:
					C = 20000
			comida -= (60 * C)
			if comida <= 0:
				print("\033[1;31m" +"MUERTE: tus ciudadanos se han quedado sin comida y se han comido tu dinero (has perdido el 70% de tu dinero"'\033[0;m')
				dn *= 0.3
				comida += 100000
			dn -= LMP * 10000
			print("\033[1;36m" + f"tienes {C} ciudadanos")
			print(f"Tienes {sp} sitios de casas libres")
			print(f"Tienes {(fama/((V+100)*(V**(V*10))))} de fama")
			print(f"Tienes {comida} kg de comida")
			print(f"Tienes {PR} protecciones")
			print(f"Tienes {LMP} nivel de limpieza ")
			print(f"Años: {a}" '\033[0;m')
			k = random.randrange(100) + 1
			#print(k)
			if k > 0 and k < 10:
				print("\033[1;31m" +"MUERTE: hay jabalies vamos a morirrrrrr")
				print("1- nada 2- pagar 1500000 para comporar a especialistas que los espanten"'\033[0;m')
				print(f"Tienes: {dn} €")
				kte = int(input())
				if kte == 1:
					print("\033[3;34m" +"Los jabalies mataron a ciudadanos :("'\033[0;m')
					C -= C // 7
					fama //= 1.15
				else:
					dn -= 1500000
					print("\033[3;34m" +"Has perdido dinero pero tu fama ha aumentado!!!!!!!!!!!"'\033[0;m')
					fama += 5
			if k > 50 and k < 65:
				print("\033[1;31m]" +"MUERTE: hay un mini trremoto vamos a morirrrrrr"'\033[0;m')
				print("1- gastar proteccion(1) 2- evacuar ")
				ktp = int(input())
				if ktp == 1 and PR <= 0:
					print("\033[3;34m" +"El terremoto ha roto casas pierdes espacios :("'\033[0;m')
					sp -= sp // 10
					fama //= 1.12
				if ktp == 1 and PR >= 1:
					print("\033[3;34m" + "Te salvaste" '\033[0;m')
					fama *= 1.002
					PR -= 1
				else:
					print("\033[3;34m" +"Pierdes fama pero nada se ha derrumbado")
					fama //= 1.25
			if k > 66 and k < 71:
				print("\033[1;31m]" +"MUERTE: hay un trremoto de magnitud 4 vamos a morirrrrrr"'\033[0;m')
				print("1- gastar proteccion(5) 2- evacuar ")
				ktp = int(input())
				if ktp == 1 and PR <= 4:
					print("\033[3;34m" +"El terremoto ha roto casas pierdes espacios :("'\033[0;m')
					sp -= sp // 2.7
					fama //= 1.20
				if ktp == 1 and PR >= 5:
					print("\033[3;34m" + "Te salvaste" '\033[0;m')
					fama *= 1.005
					PR -= 5
				else:
					print("\033[3;34m" +"Pierdes fama pero nada se ha derrumbado"'\033[0;m')
					fama //= 1.5
			if k > 85 and k < 99:
				inv=int(input("\033[1;32m" +"SUERTE: que suerte has tenido, a un inversor le ha encantado tu ciudad\n, que quieres hacer 1-invitarle a comer o 2-nada.\n (si le invitas a comer gastaras 5.000Kg de comida)"'\033[0;m'))
				if inv == 1:
					comida -= 5000
					kk = random.randrange(8)
					if kk == 1 or kk == 0:
						print( "\033[3;34m" +f"El inversor te ha dado dinero ahora tu dinero sube 1.000.000€, ahora tienes {dn+1000000}€"'\033[0;m')
						dn += 1000000
					if kk == 2:
						print("\033[3;34m" +f"El inversor te ha dado un poco de fama ahora tu fama sube 200, ahora tienes {fama+200} de fama"'\033[0;m')
						fama += 200
					if kk == 3:
						print("\033[3;34m" +f"El inversor te ha dado  200 ciudadanos, ahora tienes {C+200} ciudadanos"'\033[0;m')
						C += 200
					if kk > 3 and kk < 6 or kk == 6:
						print("\033[3;34m" +"El inversor ahora esta obeso y ya no quiere oir nada mas de ti, no te da nada"'\033[0;m')
					if kk == 7:
						print("\033[3;34m" +f"Al inversor le ha encantado la comida y quiere que siguas cocinando, te da 100.000Kg ahora tienes {comida+100000}Kg de comida"'\033[0;m')
						comida += 100000
					if kk == 8:
						print("\033[3;34m" +f"Al inversor le decepciono la limpieza de {s} y quiere darte un  dos niveles mas, aparte de eso quiere darte 240.000€ para poderlo mantenerlo un año. Tu sistema de limpieza sube de nivel {LMP} a nivel {LMP+2}"'\033[0;m')
						LMP += 2
						dn += 240000
					if kk == 9:
						print("\033[3;34m" +f" El inversor era un impostor, te quito 10.000Kg de comida y tambien se llevo 100.000€. Tu comida baja de {comida}Kg de comida {comida-10000}Kg de comida y tu dinero baja de {dn}€ a {dn-1000000}€"'\033[0;m')
						comida -= 10000
						dn -= 100000
				else:
					print("\033[3;34m" +"El inversor se ha enfadado, no te da nada podría haberte dado muchas cosas"'\033[0;m')
			if k > 30 and k < 40:
				print("\033[1;31m]" +"MUERTE: hay un tsunami vamos a morirrrrrr"'\033[0;m')
				print("1- gastar proteccion(3) 2- evacuar 3-subbirse a lo alto de los edificios")
				ktp = int(input())
				if ktp == 1 and PR <= 2:
					print("El terremoto ha roto casas pierdes espacios :(")
					sp -= sp // 4
					fama //= 1.15
				if ktp == 1 and PR >= 3:
					print("Te salvaste")
					fama *= 1.002
					PR -= 3
				elif ktp == 2:
					print("Pierdes fama pero nada se ha derrumbado")
					fama //= 1.35
				else: 
					tttr = random.randrange(2)
					if tttr == 1:
						print("La jugada te ha salido bien, no pierdes nada")
					else:
						print(f"La jugada te ha salido mal y pierdes cultivos y espacios, ahora tines 3.000kg menos, tienes {comida-3000}Kg de comida. Pierdes el 10% de tus espacios, ahora tienes {sp//10} espacios libres")
						comida -= 3000
						sp //= 10
				
#dificultad 3
			if C >= 10000 and LMP >= 1:
				df = 3
	if df == 3 and pato != 1:
		infectados = 0
		camillas = 0
		HP = 0
		RRR = 1
		pandemia = 1
		print("\033[1;35m" +"HAS SUBIDO DE NIVEL!!!!! recibes una cantidad misteriosa de dinero y muchisima comida "'\033[0;m')
		dn += 1500000 * LMP
		comida = 0
		comida += 15000000
		print("\033[1;31m" +"MUERTE: Una terrible pandemia llamada PARRENE-VIRUS ataca tu ciudad ahora no hay cataclismos pero solo puedes comprar comida, limpieza, hospitales que te dan camillas. contra mas camillas y mas niveles de limpieza, menos gente se ira muriendo. La fama baja mucho cunado la gente se muere"'\033[0;m')
		while df == 3 and pato != 1:
			t += 1
			if t == 12:
				a += 1
				t = 0
			if pandemia == 1:
				print("Pon 10 para comprar comida: ")
				print("Pon 23 para mejorar el sistema de limpieza y luego pon cuantos niveles lo mejoras, un nivel cuesta 10.000.000 y tienes que pagar 10.000 al mes por nivel")
				print("Pon 48 para comprar un hospital: ")
				if dn <= 0 or  (fama / ((V + 100) * (V**(V * 10)))) <= 1 or C <= 100 or comida <=0:
					print(f"HAS PERDIDOOO, te has quedado sin un recurso vitales para la ciudad.\n numero de ciudadanos: {C}\n espacios que te sobraban: {sp}\n dinero: {dn}")
					pato = 1
					break
				fgh = C * 2000 * V
				dn += fgh
				print("\033[1;33m" + f"Dinero: {dn} " '\033[0;m')
				print("\033[1;33m" + f"Ingresos: {fgh}" '\033[0;m')
				nt = int(input())
				if nt == 23:
					limpio = int(input("Cuantos niveles de limpieza mejoras?: "))
					LMP += limpio
					dn -= limpio * 10000000
				if nt == 10:
					holita = int(
							input("Cuantos kg de comida quieres comprar? cada kg vale 5: "))
					comida += holita
					dn -= 5 * holita
				if nt == 48:
					HP = int(input("Cuantos hospitales? 50.000.000€ por cada uno: "))
					camillas += 250 * HP
					dn -= 50000000 * HP
				infectados1 = (C - camillas) // (1 + (LMP / 10))
				if infectados1 <= 1.1:
					infectados1 = 0
				print(infectados1)
				if infectados1 > 0.5:
					C -= infectados1
					infectados += infectados1
					infectedde = infectados // ((1.25 / (LMP / 10)) + 1)
					RRR -= (infectados - infectedde) / 20000
					fama -= infectados - infectedde
					infectados -= (infectados - infectedde)
				xyz = (infectados // 5)
				C += xyz
				infectados -= xyz
				#nivel 4
				if infectados <= 10:
					pandemia = 0
					print("\033[2;35m" +"HAS SUPERADO LA PANDEMIA y HAS SUBIDO DE NIVEL. El valor de las casas ha vuelto ha su precio original. Ademas los otro paises te envian 200.000.000 dinero y bastante fama por haber ganado contra la pandemia"'\033[0;m')
					dn += 200000000
					RRR = 1
					infectados = 0
					infectedde = 0
					infectados1 = 0
					xyz = 0
					fama += 5000
					df = 4
					break
				comida -= 50 * C
				if dn < -1:
					pato = 1
					break
				print("\033[1;36m" + f"Tienes {C} ciudadanos")
				print(f"Tienes {sp} sitios de casas libres")
				print(f"Tienes { (fama / ((V + 100) * (V**(V * 10))))} de fama")
				print(f"Tienes {comida} kg de comida")
				print(f"Tienes {PR} protecciones")
				print(f"Tienes {LMP} nivel de limpieza ")
				print(f"Tienes {infectados} infectados ")
				print(f"Tienes {camillas} camillas " '\033[0;m')
	if df == 4 and pato != 1:
		print(
				"\033[1;35m" +"VAYA VAYA, superaste la pandemia pero ahora todo es mas extenso. Ahora puedes minar y recolectar recursos para hacer distintas cosas, también tienes acceso a los laboratorios y ten cuidado que puede entrar una pandemia ahora puedes tambien realizar dos acciones por mes"'\033[0;m')
		#variables
		progression = a
		VCL = 0
		MMO=0
		MMP=0
		#materiales
		oro = 0
		plata = 0
		bronce = 0
		hierro = 0
		aluminio = 0
		#hierro+carbon
		acero = 0
		carbon = 0
		cobre = 0
		madera = 0
		piedra = 0
		arcilla = 0
		electrico = 0
		cultivado = 0
		#laboratorios
		LB = 0
		#conocimientos
		IQ = 0
		#trabajadores
		#mineros
		MT = 0
		#recolectores
		RT = 0
		#cientificos
		CT = 0
		MRTC = 0
		CTC = 0
		vacuna = 0
		ados = 0
		tdos = 0
		enp = 0
		#umentar valor de casas
		AVC = 0
		#Protecciones avanzadas
		PRA = 0
		#acero hacer
		ACH = 0
		#metal electrico (oro+plata)
		ME = 0
		#electricidad
		ELC = 0
		#Cultivos
		CUL = 0
		#tranquilizadores/drogas
		DROG = 0
		#jabon
		JB = 0
		OV = 1
		# cantidad de PRA
		PRACTT = 0
		drogas = 0
		while df == 4 and pato != 1:
			t += 1
			fama += VCL * 50000
			dn += 50000
			oro += MMO*0.06
			plata+=MMP*2.005
			if a>=35:
				print("Veo que te cuesta subir de nivel, te voy a dar una pista: (electricidad) si yo fuera tu, la descubriria y la activaria")
			
			if t == 12:
				a += 1
				t = 0
			dn -= (MT * 4000 + RT * 4000 + CT * 9000)
			oro += 0.0045 * MT
			plata += 1.15 * MT
			bronce += 2.25 * MT
			hierro += 16 * MT
			aluminio += 7 * MT
			carbon += 21 * MT
			cobre += 1.45 * MT
			piedra += 120 * MT
			arcilla += 10 * RT
			madera += 200 * RT
			IQ += 1 * CT
			comida -= 50 * C

			if dn <= 0 or  (fama / ((V + 100) * (V**(V * 10)))) <= 1 or comida <= 0:
				print(f"Has perdido, te has quedado sin dinero.\n numero de ciudadanos: {C}\n espacios que te sobraban: {sp}\n dinero: 0"	)
				df = 1
				pato = 1
				break
			fgh = C * 2500 * V * OV
			dn += fgh
			if progression < a - 15:
				print("\033[1;31m" +"CAOS: tus ciudadanos no ven progresion la fama disminuye"'\033[0;m')
				fama //= 1.1
			print("\033[1;33m]" + f"ingresos: {fgh}" '\033[0;m')
			print("\033[1;33m]" + f"dinero: {dn} " '\033[0;m')
			comida += cultivado
			print("Que quieres: comprar casas, costo: 100.000 multiplicado\n por el nivel de lujo que desee al cuadrado. -1 ")
			print("Hacer campaña: vienen un porciento de la fama por los hrcos que quedan libres. costo:500.000+fama*250 -2")
			print("Pon 50 para cambiar el valor de las casas ten en cuenta la fama bajara/subira mucho depende de el valor ")
			print("Pon 10 para comprar comida ")
			print("Pon 23 para mejorar el sistema de limpieza y luego pon cuantos niveles lo mejoras un nivel cuesta 10.000.000 y tienes que pagar 10000 al mes por nivel")
			print("Pon 45 para comprar protecciones contra desastres")
			print("Pon otro numero para no hacer nada")
			print("Pon 48 para comprar un hospital: ")
			print("Pon 432 para comprar minas/laboratorios")
			print("Pon 1234 para comprar mineros/recolectores/cientificos ")
			print("Pon 88 para expedicion. Costo: 300.000.000")
			print("Pon 121 para usar las investigaciones")
			print(f"Pon 120 para entrar en un laboratorio y ver las investigaciones ten en cuenta tu IQ : {IQ} IQ")
			#holahola
			print(f"Pon 17 para generar antibioticos/vacuna (necesitas 2000 IQ)(si una vacuna esta en progreso no puedes hacer esto si este numero es 1 ya esta activada {enp}")
			nt = int(input("Accion 1: "))
			snt = int(input("Accion 2: "))
			print(f"Tienes: {dn} €")
			if nt == 48:
				HP = int(input("Cuantos hospitales quiere comprar? Cada hospital vale 50.000.000€ : "))
				camillas += 250 * HP
				dn -= 50000000 * HP
			if nt == 17 and enp == 0:
				if IQ >= 2000:
					tdos = t
					ados = a
					enp = 1
				else:
					print("Te falta IQ ")
			if a == (ados + 2) and t == tdos and ados >= 1 and enp == 1:
				print("La vacuna se ha elaborado, tu vacuna se llama crispasican. Si un virus te ataca esta vacuna esta vacuna ara que los viruses sean mas flojos. ")
				vacuna += 1
				enp = 0
			if nt == 121:
				print("\033[1;36m" +"Que quieres #1 Usar oro para subir la fama/ #2 Crear protecciones avnzadas #3 Hacer acero #4 Hacer metal electrico #5 Activar la electricidad(5000 metal electrico al hacer esto subes a nivel 5 es recomendable tener 1.000.000 ciudadanos) #6 Cultivar #7 hacer tranquilizantes 8# hacer jabon (si no tines el conocimiento no ocurrira nada)"'\033[0;m')
				fghjk = int(input())
				if fghjk == 1 and AVC == 1:
					orou = float(input("\033[1;36m" +"Cuanto oro quieres usas? (cada oro da un 0.001% mas de ingresos): "'\033[0;m'))
					if oro >= orou:
						OV += (orou / 100000)
						oro -= orou
					else:
						print("\033[1;31m" + "No tienes suficiente oro!"'\033[0;m')
				if fghjk == 2 and PRA == 1:
					PRACC = int(input("\033[1;36m" +"Cunatas protecciones avanzadas quieres hacer? (100 aluminio 15 cobre 1000 madera 100 arcilla"'\033[0;m'))
					if aluminio >= 100 * PRACC and cobre >= 15 * PRACC and madera >= 1000 * PRACC and arcilla >= 100 * PRACC:
						PRACTT += PRACC
						aluminio -= 100 * PRACC
						cobre -= 15 * PRACC
						madera -= 1000 * PRACC
						arcilla -= 100 * PRACC
					else:
						print("\033[1;31m" + "No tienes materiales"'\033[0;m')
				if fghjk == 3 and ACH == 1:
					acd = int(
							input("\033[1;36m" +"Cuanto acero quieres hacer, cada uno te costara: 20 de carbon y 1 de hierro"'\033[0;m'))
					if hierro >= 1 * acd and carbon >= 20 * acd:
						acero += acd
						hierro -= acd
						carbon -= 20 * acd
					else:
						print("\033[1;31m" + "minerales insuficientes"'\033[0;m')
				if fghjk == 4 and ME == 1:
					elcd = int(input("\033[1;36m" +"Cuanto metal electrico quieres hacer? (3 acero, 3 plata, 0.25 oro por cada 1)"'\033[0;m'))
					if acero >= 3 * elcd and plata >= 3 * elcd and oro >= 0.25 * elcd:
						electrico += elcd
						plata -= 3 * elcd
						acero -= 3 * elcd
						oro -= 0.25 * elcd
					else:
						print("\033[1;31m" + "Minerales insuficientes"'\033[0;m')
				if fghjk == 5 and ELC == 1:
					if electrico >= 5000:
						df = 5
					else:
						print("\033[1;31m" +"Necesitas 5000 metal electrico"'\033[0;m')
				if fghjk == 6 and CUL == 1:
					cvb = int(input("\033[1;36m" +" Cuanta comida quieres cultivar? por cada 24 que cultives te dara 1 al mes (cada comida que cultives te costara 12 de dinero"'\033[0;m'))
					if comida >= cvb:
						cultivado += cvb / 24
						dn -= 12 * cvb
						comida -= cvb
					else:
						print("\033[1;31m" + "No tienes tanta comida"'\033[0;m')
				if fghjk == 7 and DROG == 1:
					fghjk2 = int(input("\033[1;36m" "Cuantas drogas quieres hacer? cada una vale 250.000.000€ "'\033[0;m'))
					if dn >= fghjk2 * 250000000:
						drogas += fghjk2
						dn -= fghjk2 * 250000000
					else:
						print("\033[1;31m" + "No tienes suficiente dinero!" '\033[0;m')
				elif JB == 1:
					print("\033[1;33m" +"Para hacer jabon necesitas materiales desbloqueados en el siguiente nivel"'\033[0;m')

			if nt == 120:
				print("\033[1;36m" +"Estos son tus experimentos: (0 es no descubierto 1 si descubierto) "'\033[0;m')
				print(f"1- Aumento de valor de casas: {AVC} (1250 IQ)")
				print(f"2- Protecciones avanzadas: {PRA} (2500 IQ)")
				print(f"3- Hacer acero: {ACH} (1500 IQ)")
				print(f"4- Metal electronico: {ME}4000")
				print(f"5- Electricidad: {ELC}(25000 IQ)")
				print(f"6- Cultivos: {CUL} (3000 IQ) ")
				print(f"7- Tranquilizantes/drogas: {DROG} (7000 IQ)")
				print(f"8- Jabon: {JB} (1700 IQ)")
				print("Que experimento quieres hacer? Introduce el numero. Si no tienes suiciente IQ no puedes."'\033[0;m')
				tryu = int(input())
				if tryu == 1 and AVC != 1:
					if IQ >= 1250:
						print("Has descubierto como hacer CASAS AVANZADAS!!!")
						IQ -= 1250
						AVC -= 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 2 and PRA == 0:
					if IQ < 2500:
						print("te falta IQ")
					else:
						print("has descubierto protecciones avanzadas!!!")
						IQ -= 2500
						PRA = 1
				if tryu == 3 and ACH != 1:
					if IQ >= 1500:
						print("has descubierto a hacer acero")
						IQ -= 1500
						ACH = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 4 and ME == 0:
					if IQ >= 4000:
						print("Has creado metal electronico. Metal electronico es oro mezclado con plata.")
						IQ -= 4000
						ME = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 5 and ELC != 1:
					if IQ >= 25000:
						print("has descubierto la electricidad")
						IQ -= 25000
						ELC = 1
					else:
						print("No tienes suficirnte IQ")
				if tryu == 6 and CUL == 0:
					if IQ >= 3000:
						print("has descubierto los cultivos")
						IQ -= 3000
						CUL = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 7 and DROG == 0:
					if IQ >= 7000:
						print("Has descubierto un tranquilizante/droga por si te atacan animales")
						IQ -= 7000
						DROG = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 8 and JB == 0:
					if IQ >= 1700:
						print("Has creado jabon!!!")
						IQ -= 1700
						JB = 1
					else:
						print("No tienes suficiente IQ")

			if nt == 432:
				KKKK = int(input("pon 1 para comprar minas pon 2 para laboratorios "))
				if KKKK == 1:
					lmnk = int(input("cuantas minas cada una puede tener 100 mineros y valen 200.000.000"))
					dn -= lmnk * 200000000
					MRTC += 100 * lmnk
				else:
					lmnkj = int(input("cuantos laboratorios quieres?\n cada uno soporta 100 cientificos costo: 500.000.000"))
					dn -= lmnkj * 500000000
					CTC += 100 * lmnkj
			if nt == 1234:
				KJKJ = int(input("pon 1- para comprar mineros pon 2- para recoletores y pon 3- para cientificos"))
				if KJKJ == 1:
					print(f"puedes comprar {MRTC} como maximo")
					NNB = int(input("cuantos mineros quieres? valen 4.000 por mes:"))
					if NNB > MRTC:
						print("no tienes suficientes minas")
					else:
						MT += NNB
						MRTC -= NNB
				if KJKJ == 2:
					print(f"puedes comprar {MRTC} como maximo")
					NNBB = int(
							input("cuantos recolectores quieres? valen 4.000 por mes: "))
					if NNBB > MRTC:
						print("no tienes suficientes minas")
					else:
						RT += NNBB
						MRTC -= NNBB
				if KJKJ == 3:
					print(f"puedes comprar {CTC} como maximo ")
					NNBBB = int(input("cuantos cientificos? valen 9.000 por mes: "))
					if NNBBB > CTC:
						print("no tienes suficientes laboratorios")
					else:
						CT += NNBBB
						CTC -= NNBBB
			if nt == 45:
				PRS = int(input("cuantas protecciones quieres? valen 500.000: "))
				print(f"Tienes: {dn} €")
				PR += PRS
				dn -= PRS * 500000
			if nt == 88:
				dn -= 300000000
				EX = random.randrange(4)
				if EX == 1:
					print("hemos encontrado un volcan!!!!, quieres comprarlo? Costo:10.000.000")
					print(f"ahora tu numero de volcanes sube de {VCL} a {VCL+1} volcanes. y has conseguido mucha fama 500.000 en concreto, a mas a mas cada mes ganas 50.000 de fama y 50.000€")
					VCL += 1
					fama += 500000
					dn -= 10000000
				elif EX != 1 or EX != 4:
					print("no encontraron nada y perdiste dinero por explorar")
				elif EX == 4:
					print("hemos encontrado unas minas misteriosas muy antiguas!!!!, quieres explorarlas? Costo: 10.000.000 1-Si 2-No")
					MEX = int(input())
					if MEX == 1:
						MEXR = random.randrange(2)
						if MEXR == 1:
							print(" encontraron una fuente de oro, te proporcionara 0.05 al mes")
							MMO+=1
						if MEXR==2:
							print("encontraron una fuente de plata, te proporcionara 2,002 al mes")
							MMP+=1
			if nt == 23:
				limpio = int(input("cuantos niveles de limpieza mejoras?"))
				print(f"Tienes: {dn} €")
				LMP += limpio
				dn -= limpio * 10000000
			if nt == 10:
				holita = int(
						input("cuantos kg de comida quieres comprar? cada kg vale 5: "))
				print(f"Tienes: {dn} €")
				comida += holita
				dn -= 5 * holita
			if nt == 50:
				V = float(input("Por cuál es el valor de las casas?: "))
				print(fama)
			if nt == 1:
				lujo = int(input("nivel de lujo: "))
				qt = int(input("cantidad de casas: "))
				dn -= (100000 * lujo * lujo * qt)
				fama += lujo * lujo * (lujo) * qt
				sp += lujo * qt
			if nt == 2:
				dn -= 500000 + (fama * 250)
				C += sp // 10
				sp -= sp // 10
				if C >= 1500000:
					C = 1500000
			#empieza SNT
			if snt == 17 and enp == 0:
				if IQ >= 2000:
					tdos = t
					ados = a
					enp = 1
				else:
					print("te falta IQ ")
			if a == (ados + 2) and t == tdos and ados >= 1 and enp == 1:
				print("la vacuna se ha elaborado, tu vacuna se llama CRIPASICAN. Si un virus te ataca esta vacuna esta vacuna ara que los viruses sean mas flojos. ")
				vacuna += 1
				enp = 0
			if snt == 121:
				print("\033[1;36m" +"que quieres #1 usar oro para subir la fama/ #2 crear protecciones avnzadas #3 hacer acero #4 hacer metal electrico #5 activar la electricidad(5000 metal electrico al hacer esto subes a nivel 5 es recomendable tener 1.000.000 ciudadanos) #6 cultivar #7 hacer tranquilizantes 8# hacer jabon (si no tines el conocimiento no ocurrira nada)"'\033[0;m')
				fghjk = int(input())
				if fghjk == 1 and AVC == 1:
					orou = float(input("\033[1;36m" +"cuanto oro usas? (cada oro da un 0.001% mas de ingresos): "'\033[0;m'))
					if oro >= orou:
						OV += (orou / 100000)
						oro -= orou
					else:
						print("\033[1;31m" + "no tienes suficiente oro"'\033[0;m')
				if fghjk == 2 and PRA == 1:
					PRACC = int(
							input("\033[1;36m" +"cunatas protecciones avanzadas haces? (100 aluminio 15 cobre 1000 madera 100 arcilla"
									'\033[0;m'))
					if aluminio >= 100 * PRACC and cobre >= 15 * PRACC and madera >= 1000 * PRACC and arcilla >= 100 * PRACC:
						PRACTT += PRACC
						aluminio -= 100 * PRACC
						cobre -= 15 * PRACC
						madera -= 1000 * PRACC
						arcilla -= 100 * PRACC
					else:
						print("\033[1;31m" + "no tienes materiales"'\033[0;m')
				if fghjk == 3 and ACH == 1:
					acd = int(
							input("\033[1;36m" +"cuanto acero quieres hacer cada uno es 20 carbon y 1 de hierro"'\033[0;m'))
					if hierro >= 1 * acd and carbon >= 20 * acd:
						acero += acd
						hierro -= acd
						carbon -= 20 * acd
					else:
						print("\033[1;31m" + "minerales insuficientes")
				if fghjk == 4 and ME == 1:
					elcd = int(
							input("\033[1;36m" +"cuanato metal electrico haces (3 acero 3 plata 0.25 oro por cada 1)"'\033[0;m'))
					if acero >= 3 * elcd and plata >= 3 * elcd and oro >= 0.25 * elcd:
						electrico += elcd
						plata -= 3 * elcd
						acero -= 3 * elcd
						oro -= 0.25 * elcd
					else:
						print("\033[1;31m" + "minerales insuficientes" '\033[0;m')
				if fghjk == 5 and ELC == 1:
					if electrico >= 5000:
						df = 5
					else:
						print("\033[1;31m" +"necesitas 5000 metal electrico"'\033[0;m')
				if fghjk == 6 and CUL == 1:
					cvb = int(input("\033[1;36m" +" Cuanta comida quieres cultivar? por cada 24 que cultives te dara 1 al mes (cada comida que cultives te costara 12 de dinero"'\033[0;m'))
					if comida >= cvb:
						cultivado += cvb / 24
						dn -= 12 * cvb
						comida -= cvb
					else:
						print("\033[1;31m" + "no tienes tanta comida"'\033[0;m')
				if fghjk == 7 and DROG == 1:
					fghjk2 = int(
							input("\033[1;36m" +"cuantas drogas haces valen 250.000.000 cada una"'\033[0;m'))
					if dn >= fghjk2 * 250000000:
						drogas += fghjk2
						dn -= fghjk2 * 250000000
					else:
						print("\033[1;31m" + "no tienes suficiente dinero"'\033[0;m')
				elif JB == 1:
					print("\033[1;33m" +"para hacer jabon necesitas materiales desbloqueados en el siguiente nivel"'\033[0m')

			if snt == 120:
				print("\033[1;36m" +"estos son tus experimentos: (0 es no descubierto 1 si descubierto) "'\033[0;m')
				print(f"1- Aumento de valor de casas: {AVC} (1250 IQ)");
				print(f"2- Protecciones avanzadas: {PRA} (2500 IQ)")
				print(f"3- Hacer acero: {ACH} (1500 IQ)")
				print(f"4- metal electronico: {ME}4000")
				print(f"5- electricidad: {ELC}(25000 IQ)")
				print(f"6- cultivos: {CUL} (3000 IQ) ")
				print(f"7- tranquilizantes/drogas: {DROG} (7000 IQ)")
				print(f"8- jabon: {JB} (1700 IQ)")
				print("que experimento quieres hacer, introduce el numero. Si no tienes suficiente IQ no puedes."'\033[0;m')
				tryu = int(input())
				if tryu == 1 and AVC != 1:
					if IQ >= 1250:
						print("has descubierto a hacer casas avanzadas")
						IQ -= 1250
						AVC = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 2 and PRA == 0:
					if IQ < 2500:
						print("te falta IQ")
					else:
						print("has descubierto protecciones avanzadas!!!")
						IQ -= 2500
						PRA = 1
				if tryu == 3 and ACH != 1:
					if IQ >= 1500:
						print("has descubierto a hacer acero")
						IQ -= 1500
						ACH = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 4 and ME == 0:
					if IQ >= 4000:
						print("Has creado metal electronico. Metal electronico es oro mezclado con plata.")
						IQ -= 4000
						ME = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 5 and ELC != 1:
					if IQ >= 25000:
						print("has descubierto la electricidad")
						IQ -= 25000
						ELC = 1
					else:
						print("No tienes suficirnte IQ")
				if tryu == 6 and CUL == 0:
					if IQ >= 3000:
						print("has descubierto los cultivos")
						IQ -= 3000
						CUL = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 7 and DROG == 0:
					if IQ >= 7000:
						print("Has descubierto un tranquilizante/droga por si te atacan animales")
						IQ -= 7000
						DROG = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 8 and JB == 0:
					if IQ >= 1700:
						print("Has creado jabon!!!")
						IQ -= 1700
						JB = 1
					else:
						print("No tienes suficiente IQ")
			if snt == 48:
				HP = int(input("cuantos hospitales? 50.000.000€ por cada uno: "))
				print(f"Tienes: {dn} €")
				camillas += 250 * HP
				dn -= 50000000 * HP
			if snt == 1234:
				KJKJ = int(input("pon 1- para comprar mineros pon 2- para recoletores y pon 3- para cientificos "))
				if KJKJ == 1:
					print(f"puedes comprar {MRTC} como maximo")
					NNB = int(input("cuantos mineros? valen 4.000 por mes: "))
					if NNB > MRTC:
						print("no tienes suficientes minas")
					else:																
						MT += NNB
						MRTC -= NNB
					if KJKJ == 2:
						print(f"puedes comprar {MRTC} como maximo")
					NNBB = int(input("cuantos recolectores? valen 4.000 por mes: "))
					if NNBB > MRTC:
						print("no tienes suficientes minas")
					else:
						RT += NNBB
						MRTC -= NNBB
				if KJKJ == 3:
					print(f"los  puedes comprar {CTC} como maximo")
					NNBBB = int(input("cuantos cientificos? valen 9.000 por mes: "))
					if NNBBB > CTC:
						print("no tienes suficientes laboratorios")
					else:
						CT += NNBBB
						CTC -= NNBBB
			if snt == 45:
				PRS = int(input("cuantas protecciones quieres? valen 500.000: "))
				print(f"Tienes: {dn} €")
				PR += PRS
				dn -= PRS * 500000
			if snt == 88:
				dn -= 300000000
				EX = random.randrange(4)
				if EX == 1:
					print("hemos encontrado un volcan!!!!, quieres comprarlo? Costo:10.000.000")
					print(f"ahora tu numero de volcanes sube de {VCL} a {VCL+1} volcanes. y has conseguido mucha fama 500.000 en concreto, a mas a mas cada mes ganas 50.000 de fama y 50.000€")
					VCL += 1
					fama += 500000
					dn -= 10000000
				elif EX != 1 or EX != 4:
					print("no encontraron nada y perdiste dinero por explorar")
				elif EX == 4:
					print("hemos encontrado unas minas misteriosas muy antiguas!!!!, quieres explorarlas? Costo: 10.000.000 1-Si 2-No")
					MEX = int(input())
					if MEX == 1:
						MEXR = random.randrange(2)
						if MEXR == 1:
							print(" encontraron una fuente de oro, te proporcionara 0.05 al mes")
							MMO+=1
						if MEXR==2:
							print("encontraron una fuente de plata, te proporcionara 2,002 al mes")
							MMP+=1
			if snt == 23:
				limpio = int(input("cuantos niveles de limpieza mejoras?"))
				print(f"Tienes: {dn} €")
				LMP += limpio
				dn -= limpio * 10000000
			if snt == 10:
				holita = int(input("cuantos kg de comida quieres comprar? cada kg vale 5: "))
				print(f"Tienes: {dn} €")
				comida += holita
				dn -= 5 * holita
			if snt == 50:
				V = float(input("Por cuál es el valor de las casas?: "))
				print(fama)
			if snt == 1:
				lujo = int(input("nivel de lujo: "))
				qt = int(input("cantidad de casas: "))
				dn -= (100000 * lujo * lujo * qt)
				fama += lujo * lujo * (lujo) * qt
				sp += lujo * qt
			if snt == 2:
				dn -= 500000 + (fama * 250)
				C += sp // 10
				sp -= sp // 10
				if C >= 1500000:
					C = 1500000
			if snt == 432:
				KKKK = int(input("1- comprar minas 2- comprar laboratorios"))
				if KKKK == 1:
					lmnk = int(input("cuantas minas compras soportan 100 mineros y valen 200.000.000"))
					if dn>= 200000000*lmnk:
						dn-= 200000000*lmnk
						MRTC += 100*lmnk
				else:
					lmnkj = int(input("cuantos laboratorios\n valen 500.000.000 soportan 100 cientificos"))
					if dn>= 500000000*lmnkj:
						dn-= 500000000*lmnkj
						CTC += 100*lmnkj
			print("\033[1;36m" + f"tienes {C} ciudadanos")
			print(f"tienes {sp} sitios de casas libres")
			print(f"tienes { (fama / ((V + 100) * (V**(V * 10))))} de fama")
			print(f"tienes {comida} kg de comida")
			print(f"tienes {PR} protecciones")
			print(f"tienes {LMP} nivel de limpieza ")
			print(f"tienes {infectados} infectados ")
			print(f"tienes {camillas} camillas ")
			print(f"tienes {vacuna} nivel de vacuna")
			print(f"tienes {IQ} IQ")
			print(f"podrias comprar {MRTC} mineros/recolectores")
			print(f"podrias comprar {CTC} cientificos")
			holiss = int(
					input("quieres ver minerales 1-si 2-no"'\033[0;m'))
			if holiss == 1:
				print("\033[1;36m" +f"tienes: oro: {oro}\n plata: {plata}\n bronce: {bronce}\n hierro: {hierro}\n aluminio: {aluminio}\ acero: {acero}\n carbon: {carbon}\n cobre: {cobre}\n madera: {madera}\n piedra: {piedra} arcilla: {arcilla}\n metal elcetrico : {electrico}\n"'\033[0;m')

			#desastres
			k = random.randrange(100) + 1
			#print(k)
			if C <= 200000:
				if k > 0 and k < 10:
					print("\033[1;31m" +"MUERTE: hay una titanoboa vamos a morirrrrrr")
					print("1- nada 2- pagar 57.000.000 para comporar a especialistas que la espanten"'\033[0;m')
					print(f"Tienes: {dn}€")
					kte = int(input())
					if kte == 1:
						print("\033[3;34m" +"la titanoboa se comio y engullo a ciudadanos :("'\033[0;m')
						C -= C // 6
						fama //= 1.6
					else:
						dn -= 57000000
						print("\033[3;34m" +"has perdido dinero pero tu fama ha aumentado!!!!!!!!!!!"
						'\033[0;m')
						fama += 2800
				if k > 50 and k < 65:
					if VCL >= 1:
						print("\033[1;31m" +"MUERTE: uno de tus volcanes esta en  erupcion, vamos a morirrrrrr"'\033[0;m')
						print("1- gastar protecciones(35*Volcanes) 2- nada 3-destruir volcan")
						ktp = int(input())
						if ktp == 1 and PR <= 34:
							print("\033[3;34m" +"no tenias suficientes protecciones, el volcan ha fundido casas pierdes espacios :("'\033[0;m')
							sp -= sp // 10
							fama //= 2
						if ktp == 1 and PR >= (35 * VCL):
							print("\033[3;34m" + "te salvaste" '\033[0;m')
							fama *= 2
							PR -= 35 * VCL
						elif ktp == 2:
							print("\033[3;34m" +"pierdes mucha fama y se han fundido muchas casas"'\033[0;m')
							fama //= 2
							sp //= 2
						else:
							print("\033[3;34m" +"pierdes mucha fama y un volcan pero nada mas ha pasado"'\033[0;m')
							print(f"tu numero de volcanes es {VCL}")
							fama //= 2
							VCL -= 1
					if k > 66 and k < 71:
						print("\033[1;31m" +"MUERTE: hay un terremoto de magnitud 5 vamos a morirrrrrr"'\033[0;m')
						print("1- gastar proteccion(25) 2- evacuar ")
						ktp = int(input())
						if ktp == 1 and PR <= 24:
							print("\033[3;34m" +"el terremoto ha roto casas pierdes espacios :("'\033[0;m')
							sp -= sp // 2.4
							fama //= 1.4
						if ktp == 1 and PR >= 25:
							print("\033[3;34m" + "te salvaste" '\033[0;m')
							fama *= 1.005
							PR -= 25
						else:
							print("\033[3;34m" +"pierdes fama pero nada se ha derrumbado"'\033[0;m')
							fama //= 1.7
			if k > 85 and k < 99:
				inv = int(input("\033[1;32m"+"SUERTE: que suerte has tenido, a un inversor le ha encantado tu ciudad\n'\033[0;m', que quieres hacer 1-invitarle a comer o 2-nada.\n (si le invitas a comer gastaras 100.000Kg de comida y 100.000.000€)"))
				if inv == 1:
					comida -= 100000
					dn -= 100000000
					kk = random.randrange(10)
					if kk == 1 or kk == 0:
						print("\033[3;34m" +f"el inversor te ha dado dinero ahora tu dinero sube 500.000.000€, ahora tienes {dn+500000000}€"'\033[0;m')
						dn += 500000000
					if kk == 2:
						print("\033[3;34m" +f"el inversor te ha dado un poco de oro ahora tu oro sube 5, ahora tienes {oro+5} de fama"'\033[0;m')
						oro += 5
					if kk == 3:
						print("\033[3;34m"+f"el inversor te ha dado  2 hospitales=500 camillas, ahora tienes {camillas+500} ciudadanos"'\033[0;m')
						camillas += 500
					if kk > 3 and kk < 6 or kk == 6:
						print("\033[3;34m" +"el inversor ahora esta obeso y ya no quiere oir nada mas de ti, no te da nada"'\033[0;m')
					if kk == 7:
						print("\033[3;34m" +f"al inversor le ha encantado la comida y quiere que siguas cocinando, te da 100.000Kg ahora tienes {comida+100000}Kg de comida"'\033[0;m')
						comida += 100000
					if kk == 8:
						print("\033[3;34m" +f"al inversor le decepciono la limpieza de {s} y quiere darte dos niveles mas, aparte de eso quiere darte 240.000€ para poderlo mantenerlo un año. Tu sistema de limpieza sube de nivel {LMP} a nivel {LMP+2}"'\033[0;m')
						LMP += 2
						dn += 240000
					if kk == 9:
						print("\033[3;34m" f" el inversor era un impostor, te quito 10.000Kg de comida y tambien se llevo 100.000€. Tu comida baja de {comida}Kg de comida {comida-10000}Kg de comida y tu dinero baja de {dn}€ a {dn-1000000}€"'\033[0;m')
						comida -= 10000
						dn -= 100000
					if kk == 10:
						print("\033[3;34m"+f"el inversor vio algo a lo lejos, te regala una expedicion para que puedas explorar"'\033[0;m')
						EX = random.randrange(3)
						if EX == 1:
							print("\033[3;34m"+"Hemos encontrado un VOLCAN!!!!, quieres comprarlo? Costo:10.000.000, PERO... al ivestor le a encantado tu descubrimiento. TE LO VA A PAGAR!!!"'\033[0;m')
							print("\033[1;34m" +f"ahora tu numero de volcanes sube de {VCL} a {VCL+1} volcanes. y has conseguido mucha fama 500.000 en concreto, a mas a mas cada mes ganas 50.000 de fama y 50.000€"'\033[0;m')
							VCL += 1
							fama += 500000
						else:
							print("\033[3;34m" +f"No encontraron nada pero al inversor le has dado pena y te da libros de ciencia, subes 500 de IQ. Ahora tienes {IQ+500} de IQ "'\033[0;m')
							IQ += 500
				else:
					print("\033[3;34m" +"El inversor se ha enfadado porque no le a gustado tu comida. No te da nada... podría haberte dado muchas cosas"'\033[0;m')
			if k > 30 and k < 40:
				print("\033[1;31m" + "MUERTE: hay un tornado vamos a morirrrrrr")
				print("1- gastar protecciones(20) 2-nada" '\033[0;m')
				ktp = int(input())
				if ktp == 1 and PR <= 19:
					print("\033[3;34m" + "el tornado ha roto casas, pierdes espacios y ademas pierdes fama por no tener suficientes protecciones :("'\033[0;m')
					sp -= sp // 10
					fama //= 1.5
				if ktp == 1 and PR >= 20:
					print("\033[3;34m" + "TE SALVASTE!!!. Buena elección comprando protecciones!"'\033[0;m')
					fama *= 1.0035
					PR -= 20
				else:
					tttr = random.randrange(2)
					if tttr == 1:
						print("\033[3;34m" + "La jugada te ha salido bien, el tornado pasó de largo, no pierdes nada"'\033[0;m')
					else:
						print("\033[3;34m" + "El tornado no ha sido muy fuerte, no ha destruido edificios pero si que ha matado a ciudadanos. Pierdes ciudadanos y fama por no comprar protecciones"'\033[0;m')
						C //= 8
						fama //= 1.75
		else:
			if k > 0 and k < 10:
				print("\033[1;31m" +"MUERTE: Hay una MEGAtitanoboa vamos a morirrrrrr"'\033[0;m')
				print("1- nada 2- usar un tranquilizante")
				print(f"Tienes: {dn}€")
				kte = int(input())
				if kte == 1:
					print("\033[3;34m" +"La MEGAitanoboa se comio y engullo a ciudadanos :("'\033[0;m')
					C -= C // 6
					fama //= 1.6
				else:
					if drogas >= 1:
						print("\033[3;34m" +"Has perdido un tranquilizante pero tu fama ha aumentado!!!!!!!!!!!"'\033[0;m')
						fama += 50000
					else:
						print("\033[3;34m" +"la MEGAitanoboa se comio y engullo a ciudadanos :('\033[0;m'")
						C -= C // 6
						fama //= 1.6
			if k > 50 and k < 65:
				if VCL >= 1:
					print("\033[1;31m" +"MUERTE: uno de tus volcanes esta en  erupcion, vamos a morirrrrrr"'\033[0;m')
					print("1- gastar protecciones(35*Volcanes) 2- nada 3-destruir volcan")
					ktp = int(input())
					if ktp == 1 and PR <= 34:
						print("\033[3;34m" +"No tenias suficientes protecciones, el volcan ha fundido casas pierdes espacios :("'\033[0;m')
						sp -= sp // 10
						fama //= 2
					if ktp == 1 and PR >= (35 * VCL):
						print("\033[3;34m" + "Te salvaste" '\033[0;m')
						fama *= 2
						PR -= 35 * VCL
					elif ktp == 2:
						print("\033[3;34m" +"Pierdes mucha fama y se han fundido muchas casas"'\033[0;m')
						fama //= 2
						sp //= 2
					else:
						print("\033[3;34m" +"Pierdes mucha fama y un volcan pero nada mas ha pasado"'\033[0;m')
						print(f"tu numero de volcanes es {VCL}")
						fama //= 2
						VCL -= 1
			if k > 66 and k < 78:
				print("\033[1;31m" +"MUERTE: hay un terremoto de magnitud 5.6 vamos a morirrrrrr"'\033[0;m')
				print("1- gastar protecciones avanzadas(7) 2- evacuar ")
				ktp = int(input())
				if ktp == 1 and PRA <= 6:
					print("\033[3;34m" +"El terremoto ha roto casas pierdes espacios :("'\033[0;m')
					sp -= sp // 2.4
					fama //= 2.5
				if ktp == 1 and PR >= 7:
					print("\033[3;34m" + "Te salvaste" '\033[0;m')
					fama *= 1.005
					PRA -= 7
				else:
					print("\033[3;34m" +"pierdes fama pero nada se ha derrumbado"'\033[0;m')
					fama //= 1.7
			# emieza dificultad 555555555555555555555555555555555555555555555555
	if df==5 and pato!= 1:
		print("HOLA, has subido de NIVEL. Estas en la dicifultad 5!!!!!")
		print("Ahora has descubierto la electricidad,investiga electricidad para obtener mas electricidad")
		print("Ahora cuando acabes todas las investigaciones podras hacer nuevos estudios")
		print("Haber desbloqueado la elcetricidad conlleva a grandes cosas puedes cobra impuestos por ella y ademas puedes mejorar laboratorios + minas")
		print("siento decirte esto pero hay una pandemia llamada PAMANELE-VIRUS esta vez las acciones siguen como en el nivel 4 pero no te confies que este virus es extremadamente agresivo y puede matar con mucha facilidad al igul que contagiar")
		pandemia = 99
		resina = 0
		#estudio de la electricidad
		EST1 = 0
		# estudio elementos quimicos
		EST2 = 0
		 #variable
		xxxxx = 0.5
		#materiales
		petroleo = 0
		resina = 0
		goma = 0
		#electricidad
		enginel = 1
		engine = 0

		cables = 0
		energiaIMD = 0
		#climate change
		CCE = 0
		#gasto de energia 
		IMDC = 0

		while df == 5 and pato != 1:
			if EST1 == 2:
				x = 0.6
			if EST1 == 3:
				x = 0.75
			if EST1 == 4:
				x = 0.9
			if EST1 == 5:
				x = 1
			if carbon >= 50000*engine:
				energiaIMD += 20000000000*engine*xxxxx
				CCE += 1*engine
			else:
				print("No tienes suficiente carbon para producir energia:(")
			if energiaIMD >= IMDC*1000000:
				energiaIMD-=1000000*IMDC
				dn += 500*IMDC*V
			else:
				print("tus ciudadanos no tienen electricidad y se enfadan baja la fama levemente")
				fama//= 1.1
			carbon += 5000000*enginel
			if pandemia == 99:
				infectados1 = C / (1 + (LMP / 300))
				if infectados1 <= 1.1:
					infectados1 = 0
				print(infectados1)
				if infectados1 > 0.5:
					C -= infectados1
					infectados += infectados1
					if camillas >= C:
						infectedde = (infectados // ((1.25 / (LMP / 650)/(vacuna + 1)) + 1))
					else:
						infectedde = (infectados // ((3 / (LMP / 2000)/(vacuna + 1)) + 1))
					fama -= infectados - infectedde
					infectados -= (infectados - infectedde)
				xyz = (infectados // 5)
				C += xyz
				infectados -= xyz
				if infectados <= 1000:
					pandemia = 0
					infectados1 = 0
					infectados = 0
					infectedde = 0
					xyz = 0
			t += 1
			fama += VCL * 50000
			dn += 50000 * VCL
			oro += MMO*0.06
			plata+=MMP*2.005
			if t == 12:
				a += 1
				t = 0
			dn -= (MT * 4000 + RT * 4000 + CT * 9000)
			oro += 0.0045 * MT
			plata += 1.15 * MT
			bronce += 2.25 * MT
			hierro += 16 * MT
			aluminio += 7 * MT
			carbon += 21 * MT
			cobre += 1.45 * MT
			piedra += 120 * MT
			arcilla += 10 * RT
			madera += 200 * RT
			resina += 10*RT
			IQ += 1 * CT
			if dn <= 0 or  (fama / ((V + 100) * (V**(V * 10)))) <= 1 or comida <= 0 or C <=100:
				print(f"Has perdido, te has quedado sin dinero.\n numero de ciudadanos: {C}\n espacios que te sobraban: {sp}\n dinero: 0"	)
				df = 1
				pato = 1
				break
			fgh = C * 2500 * V * OV
			dn += fgh
			print("\033[1;33m]" + f"ingresos: {fgh}" '\033[0;m')
			print("\033[1;33m]" + f"dinero: {dn} " '\033[0;m')
			comida += cultivado
			print("Que quieres: comprar casas, costo: 100.000 multiplicado\n por el nivel de lujo que desee al cuadrado. -1 ")
			print("Hacer campaña: vienen un porciento de la fama por los hrcos que quedan libres. costo:500.000+fama*250 -2")
			print("Pon 50 para cambiar el valor de las casas ten en cuenta la fama bajara/subira mucho depende de el valor ")
			print("Pon 10 para comprar comida ")
			print("Pon 23 para mejorar el sistema de limpieza y luego pon cuantos niveles lo mejoras un nivel cuesta 10.000.000 y tienes que pagar 10000 al mes por nivel")
			print("Pon 45 para comprar protecciones contra desastres")
			print("Pon otro numero para no hacer nada")
			print("Pon 48 para comprar un hospital: ")
			print("Pon 432 para comprar minas/laboratorios")
			print("Pon 1234 para comprar mineros/recolectores/cientificos ")
			print("Pon 88 para expedicion. Costo: 300.000.000")
			print("Pon 121 para usar las investigaciones")	
			print(f"Pon 120 para entrar en un laboratorio y ver las investigaciones ten en cuenta tu IQ : {IQ} IQ")
			print("Pon 667 para construir cables/motores y extractores de carbon petrolifero/poner electricidad en las casas/conseguir goma")
			print("Pon 300 para hacer estudios esto funciona distinto a las investigaciones, para un estudio tienes que usar cientificos durante un tiempo sin embargo durante ese tiempo NO generan IQ")
			print(f"Pon 17 para generar antibioticos/vacuna (necesitas 2000 IQ)(si una vacuna esta en progreso no puedes hacer esto si este numero es 1 ya esta activada {enp}")
			nt = int(input("Accion 1: "))
			snt = int(input("Accion 2: "))
			print(f"Tienes: {dn} €")
			#empieza nt
			if nt ==300:
				print("que estudio mejoras el (1-la electricidad)(2-elementos quimicos)")
				print(f"tu nivel de estudio 1 es: 1.{EST1} y el de 2 ------")
				vch = int(input())
				if vch == 1:
					if EST1 == 0:
						print("para mejorar el estudio 1 a 1.1 necesitas 900.000 de IQ, 6.000.000 de hierro, 2.000.000 de aluminio y 500.000 de cobre (el estudio es instantaneo)")
						hg = int(input("quieres mejorarlo? pon 1. Si no quieres pon 2"))
						if hg==1:
							if IQ>=900000 and hierro>=6000000 and aluminio>=2000000 and cobre>=500000:
								print("hola")
				if nt == 667:
					frty = int(input("1- quieres comprar cables 2- (0.1 metal electrico +10 goma)/comprar motores o extractores de carbon (estudio1.1 necesitado)(extractor- 10.000.000.000€ por cada uno da 5.000.000 kg de carbon/mes/// motores- 17.000 bronce + 150.000 hierro + 42000 aluminio + 13775 cobre)(gasta 50.000 de carbon al mes) 3- /pon electricidad en las casas  (gasta 1.000.000 de energiaIMD/mes y te cuesta 10 cables por ciudadano  pero te da 500€ por mes/ 4- haz goma por 1 de resina."))
				if frty == 1:
					jkl = int(input("Cuantos cables quieres? Cada uno son 0.1 metal electrico y 10 de goma"))
					if goma >= 10*jkl and electrico>= 0.1*jkl:
						cables += jkl
						goma-= 10*jkl
						electrico -= 0.1*jkl
				if frty == 2:
					frty2 = int(input("compras motores - 1 o extractores -2(necesitas estudio 1.1)"))
					if frty2 ==1:
						frty21 = int(input("cuantos motores quieres"))
						if bronce>= 17000*frty21 and hierro>= 150000*frty21 and aluminio>= 42000*frty21 and cobre>= 13775*frty21:
							engine+= frty21
							bronce-= 17000*frty21
							hierro -= 150000*frty21
							aluminio-= 42000*frty21
							cobre-=13775*frty21	
					else:
						if EST1 >= 1:
							holk = int(input("Cuantos extractores?"))
							if dn >= 10000000000*holk:
								enginel += holk
								dn-= 10000000000*holk
						else:
							print("necesitas el estudio electrico 1.1")
				if frty == 3:
					ffrry = int(input("Cuantos ciudadanos quieres que tengan electicidad en sus casas??"))
					if cables >= 10*ffrry:
						IMDC += ffrry
				if frty == 4:
					gomitas = int(input("cuanta goma haces?"))
					if resina >= gomitas:
						goma += resina
					else:
						print("no tienes suficientes gomitas")

		  
				if nt == 48:
					HP = int(input("Cuantos hospitales quieres comprar? Cada hospital vale 50.000.000€: "))
				camillas += 250 * HP
				dn -= 50000000 * HP
			if nt == 17 and enp == 0:
				if IQ >= 2000:
					tdos = t
					ados = a
					enp = 1
				else:
					print("Te falta IQ ")
			if a == (ados + 2) and t == tdos and ados >= 1 and enp == 1:
				print("Otra vacuna se ha elaborado, tu vacuna se llama pancato. Si un virus te ataca esta vacuna esta vacuna ara que los viruses sean mas flojos. ")
				vacuna += 1
				enp = 0
			if nt == 121:
				print("\033[1;36m" +"Que quieres #1 Usar oro para subir la fama/ #2 Crear protecciones avnzadas #3 Hacer acero #4 Hacer metal electrico #5 Activar la electricidad(5000 metal electrico) #6 Cultivar #7 hacer tranquilizantes 8# hacer jabon (si no tines el conocimiento no ocurrira nada)"'\033[0;m')
				fghjk = int(input())
				if fghjk == 1 and AVC == 1:
					orou = float(input("\033[1;36m" +"Cuanto oro quieres usas? (cada oro da un 0.001% mas de ingresos): "'\033[0;m'))
					if oro >= orou:
						OV += (orou / 100000)
						oro -= orou
					else:
						print("\033[1;31m" + "No tienes suficiente oro!"'\033[0;m')
				if fghjk == 2 and PRA == 1:
					PRACC = int(input("\033[1;36m" +"Cunatas protecciones avanzadas quieres hacer? (100 aluminio 15 cobre 1000 madera 100 arcilla"'\033[0;m'))
					if aluminio >= 100 * PRACC and cobre >= 15 * PRACC and madera >= 1000 * PRACC and arcilla >= 100 * PRACC:
						PRACTT += PRACC
						aluminio -= 100 * PRACC
						cobre -= 15 * PRACC
						madera -= 1000 * PRACC
						arcilla -= 100 * PRACC
					else:
						print("\033[1;31m" + "No tienes materiales"'\033[0;m')
				if fghjk == 3 and ACH == 1:
					acd = int(
							input("\033[1;36m" +"Cuanto acero quieres hacer, cada uno te costara: 20 de carbon y 1 de hierro"'\033[0;m'))
					if hierro >= 1 * acd and carbon >= 20 * acd:
						acero += acd
						hierro -= acd
						carbon -= 20 * acd
					else:
						print("\033[1;31m" + "minerales insuficientes"'\033[0;m')
				if fghjk == 4 and ME == 1:
					elcd = int(input("\033[1;36m" +"Cuanto metal electrico quieres hacer? (3 acero, 3 plata, 0.25 oro por cada 1)"'\033[0;m'))
					if acero >= 3 * elcd and plata >= 3 * elcd and oro >= 0.25 * elcd:
						electrico += elcd
						plata -= 3 * elcd
						acero -= 3 * elcd
						oro -= 0.25 * elcd
					else:
						print("\033[1;31m" + "Minerales insuficientes"'\033[0;m')
				if fghjk == 5 and ELC == 1:
					if electrico >= 5000:
						df = 5
					else:
						print("\033[1;31m" +"Necesitas 5000 metal electrico"'\033[0;m')
				if fghjk == 6 and CUL == 1:
					cvb = int(
							input("\033[1;36m" +" Cuanta comida quieres cultivar? por cada 24 que cultives te dara 1 al mes"'\033[0;m'))
					if comida >= cvb:
						cultivado += cvb / 24
					else:
						print("\033[1;31m" + "No tienes tanta comida"'\033[0;m')
				if fghjk == 7 and DROG == 1:
					fghjk2 = int(input("\033[1;36m" "Cuantas drogas quieres hacer? cada una vale 250.000.000€ "'\033[0;m'))
					if dn >= fghjk2 * 250000000:
						drogas += fghjk2
						dn -= fghjk2 * 250000000
					else:
						print("\033[1;31m" + "No tienes suficiente dinero!" '\033[0;m')
				elif JB == 1:
					print("\033[1;33m" +"Para hacer jabon necesitas materiales desbloqueados en el siguiente nivel"'\033[0;m')

			if nt == 120:
				print("\033[1;36m" +"Estos son tus experimentos: (0 es no descubierto 1 si descubierto) "'\033[0;m')
				print(f"1- Aumento de valor de casas: {AVC} (1250 IQ)")
				print(f"2- Protecciones avanzadas: {PRA} (2500 IQ)")
				print(f"3- Hacer acero: {ACH} (1500 IQ)")
				print(f"4- Metal electronico: {ME}4000")
				print(f"5- Electricidad: {ELC}(25000 IQ)")
				print(f"6- Cultivos: {CUL} (3000 IQ) ")
				print(f"7- Tranquilizantes/drogas: {DROG} (7000 IQ)")
				print(f"8- Jabon: {JB} (1700 IQ)")
				print("Que experimento quieres hacer? Introduce el numero. Si no tienes suiciente IQ no puedes."'\033[0;m')
				tryu = int(input())
				if tryu == 1 and AVC != 1:
					if IQ >= 1250:
						print("Has descubierto como hacer CASAS AVANZADAS!!!")
						IQ -= 1250
						AVC -= 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 2 and PRA == 0:
					if IQ < 2500:
						print("te falta IQ")
					else:
						print("has descubierto protecciones avanzadas!!!")
						IQ -= 2500
						PRA = 1
				if tryu == 3 and ACH != 1:
					if IQ >= 1500:
						print("has descubierto a hacer acero")
						IQ -= 1500
						ACH = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 4 and ME == 0:
					if IQ >= 4000:
						print("Has creado metal electronico. Metal electronico es oro mezclado con plata.")
						IQ -= 4000
						ME = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 5 and ELC != 1:
					if IQ >= 25000:
						print("has descubierto la electricidad")
						IQ -= 25000
						ELC = 1
					else:
						print("No tienes suficirnte IQ")
				if tryu == 6 and CUL == 0:
					if IQ >= 3000:
						print("has descubierto los cultivos")
						IQ -= 3000
						CUL = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 7 and DROG == 0:
					if IQ >= 7000:
						print("Has descubierto un tranquilizante/droga por si te atacan animales")
						IQ -= 7000
						DROG = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 8 and JB == 0:
					if IQ >= 1700:
						print("Has creado jabon!!!")
						IQ -= 1700
						JB = 1
					else:
						print("No tienes suficiente IQ")

			if nt == 432:
				KKKK = int(input("pon 1 para comprar minas pon 2 para laboratorios "))
				if KKKK == 1:
					lmnk = int(input("cuantas minas cada una puede tener 100 mineros y valen 200.000.000"))
					dn -= lmnk * 200000000
					MRTC += 100 * lmnk
				else:
					lmnkj = int(input("cuantos laboratorios quieres?\n cada uno soporta 100 cientificos costo: 500.000.000"))
					dn -= lmnkj * 500000000
					CTC += 100 * lmnkj
			if nt == 1234:
				KJKJ = int(input("pon 1- para comprar mineros pon 2- para recoletores y pon 3- para cientificos"))
				if KJKJ == 1:
					print(f"puedes comprar {MRTC} como maximo")
					NNB = int(input("cuantos mineros quieres? valen 4.000 por mes:"))
					if NNB > MRTC:
						print("no tienes suficientes minas")
					else:
						MT += NNB
						MRTC -= NNB
				if KJKJ == 2:
					print(f"puedes comprar {MRTC} como maximo")
					NNBB = int(
							input("cuantos recolectores quieres? valen 4.000 por mes: "))
					if NNBB > MRTC:
						print("no tienes suficientes minas")
					else:
						RT += NNBB
						MRTC -= NNBB
				if KJKJ == 3:
					print(f"puedes comprar {CTC} como maximo ")
					NNBBB = int(input("cuantos cientificos? valen 9.000 por mes: "))
					if NNBBB > CTC:
						print("no tienes suficientes laboratorios")
					else:
						CT += NNBBB
						CTC -= NNBBB
			if nt == 45:
				PRS = int(input("cuantas protecciones quieres? valen 500.000: "))
				print(f"Tienes: {dn} €")
				PR += PRS
				dn -= PRS * 500000
			if nt == 88:
				dn -= 300000000
				EX = random.randrange(4)
				if EX == 1:
					print("hemos encontrado un volcan!!!!, quieres comprarlo? Costo:10.000.000")
					print(f"ahora tu numero de volcanes sube de {VCL} a {VCL+1} volcanes. y has conseguido mucha fama 500.000 en concreto, a mas a mas cada mes ganas 50.000 de fama y 50.000€")
					VCL += 1
					fama += 500000
					dn -= 10000000
				elif EX != 1 or EX != 4:
					print("no encontraron nada y perdiste dinero por explorar")
				elif EX == 4:
					print("hemos encontrado unas minas misteriosas muy antiguas!!!!, quieres explorarlas? Costo: 10.000.000 1-Si 2-No")
					MEX = int(input())
					if MEX == 1:
						MEXR = random.randrange(2)
						if MEXR == 1:
							print(" encontraron una fuente de oro, te proporcionara 0.05 al mes")
							MMO+=1
						if MEXR==2:
							print("encontraron una fuente de plata, te proporcionara 2,002 al mes")
							MMP+=1
			if nt == 23:
				limpio = int(input("cuantos niveles de limpieza mejoras?"))
				print(f"Tienes: {dn} €")
				LMP += limpio
				dn -= limpio * 10000000
			if nt == 10:
				holita = int(
						input("cuantos kg de comida quieres comprar? cada kg vale 5: "))
				print(f"Tienes: {dn} €")
				comida += holita
				dn -= 5 * holita
			if nt == 50:
				V = float(input("Por cuál es el valor de las casas?: "))
				print(fama)
			if nt == 1:
				lujo = int(input("nivel de lujo: "))
				qt = int(input("cantidad de casas: "))
				dn -= (100000 * lujo * lujo * qt)
				fama += lujo * lujo * (lujo) * qt
				sp += lujo * qt
			if nt == 2:
				dn -= 15000000000
				C += sp // 10
				sp -= sp // 10
				if C >= 12500000:
					C = 12500000
			#empieza SNT
			if snt == 17 and enp == 0:
				if IQ >= 2000:
					tdos = t
					ados = a
					enp = 1
				else:
					print("te falta IQ ")
			if a == (ados + 2) and t == tdos and ados >= 1 and enp == 1:
				print("la vacuna se ha elaborado, tu vacuna se llama CRIPASICAN. Si un virus te ataca esta vacuna esta vacuna ara que los viruses sean mas flojos. ")
				vacuna += 1
				enp = 0
			if snt == 121:
				print("\033[1;36m" +"que quieres #1 usar oro para subir la fama/ #2 crear protecciones avnzadas #3 hacer acero #4 hacer metal electrico #5 activar la electricidad(5000 metal electrico) #6 cultivar #7 hacer tranquilizantes 8# hacer jabon (si no tines el conocimiento no ocurrira nada)"'\033[0;m')
				fghjk = int(input())
				if fghjk == 1 and AVC == 1:
					orou = float(input("\033[1;36m" +"cuanto oro usas? (cada oro da un 0.001% mas de ingresos): "'\033[0;m'))
					if oro >= orou:
						OV += (orou / 100000)
						oro -= orou
					else:
						print("\033[1;31m" + "no tienes suficiente oro"'\033[0;m')
				if fghjk == 2 and PRA == 1:
					PRACC = int(
							input("\033[1;36m" +"cunatas protecciones avanzadas haces? (100 aluminio 15 cobre 1000 madera 100 arcilla"
									'\033[0;m'))
					if aluminio >= 100 * PRACC and cobre >= 15 * PRACC and madera >= 1000 * PRACC and arcilla >= 100 * PRACC:
						PRACTT += PRACC
						aluminio -= 100 * PRACC
						cobre -= 15 * PRACC
						madera -= 1000 * PRACC
						arcilla -= 100 * PRACC
					else:
						print("\033[1;31m" + "no tienes materiales"'\033[0;m')
				if fghjk == 3 and ACH == 1:
					acd = int(
							input("\033[1;36m" +"cuanto acero quieres hacer cada uno es 20 carbon y 1 de hierro"'\033[0;m'))
					if hierro >= 1 * acd and carbon >= 20 * acd:
						acero += acd
						hierro -= acd
						carbon -= 20 * acd
					else:
						print("\033[1;31m" + "minerales insuficientes")
				if fghjk == 4 and ME == 1:
					elcd = int(
							input("\033[1;36m" +"cuanato metal electrico haces (3 acero 3 plata 0.25 oro por cada 1)"'\033[0;m'))
					if acero >= 3 * elcd and plata >= 3 * elcd and oro >= 0.25 * elcd:
						electrico += elcd
						plata -= 3 * elcd
						acero -= 3 * elcd
						oro -= 0.25 * elcd
					else:
						print("\033[1;31m" + "minerales insuficientes" '\033[0;m')
				if fghjk == 5 and ELC == 1:
					if electrico >= 5000:
						df = 5
					else:
						print("\033[1;31m" +"necesitas 5000 metal electrico"'\033[0;m')
				if fghjk == 6 and CUL == 1:
					cvb = int(
							input("\033[1;36m" +" cunata comida quieres cultivar? por cada 24 que cultives te dara 1 al mes"'\033[0;m'))
					if comida >= cvb:
						cultivado += cvb / 24
					else:
						print("\033[1;31m" + "no tienes tanta comida"'\033[0;m')
				if fghjk == 7 and DROG == 1:
					fghjk2 = int(
							input("\033[1;36m" +"cuantas drogas haces valen 250.000.000 cada una"'\033[0;m'))
					if dn >= fghjk2 * 250000000:
						drogas += fghjk2
						dn -= fghjk2 * 250000000
					else:
						print("\033[1;31m" + "no tienes suficiente dinero"'\033[0;m')
				elif JB == 1:
					print("\033[1;33m" +"para hacer jabon necesitas materiales desbloqueados en el siguiente nivel"'\033[0m')

			if snt == 120:
				print("\033[1;36m" +"estos son tus experimentos: (0 es no descubierto 1 si descubierto) "'\033[0;m')
				print(f"1- Aumento de valor de casas: {AVC} (1250 IQ)");
				print(f"2- Protecciones avanzadas: {PRA} (2500 IQ)")
				print(f"3- Hacer acero: {ACH} (1500 IQ)")
				print(f"4- metal electronico: {ME}4000")
				print(f"5- electricidad: {ELC}(25000 IQ)")
				print(f"6- cultivos: {CUL} (3000 IQ) ")
				print(f"7- tranquilizantes/drogas: {DROG} (7000 IQ)")
				print(f"8- jabon: {JB} (1700 IQ)")
				print("que experimento quieres hacer, introduce el numero. Si no tienes suficiente IQ no puedes."'\033[0;m')
				tryu = int(input())
				if tryu == 1 and AVC != 1:
					if IQ >= 1250:
						print("has descubierto a hacer casas avanzadas")
						IQ -= 1250
						AVC -= 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 2 and PRA == 0:
					if IQ < 2500:
						print("te falta IQ")
					else:
						print("has descubierto protecciones avanzadas!!!")
						IQ -= 2500
						PRA = 1
				if tryu == 3 and ACH != 1:
					if IQ >= 1500:
						print("has descubierto a hacer acero")
						IQ -= 1500
						ACH = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 4 and ME == 0:
					if IQ >= 4000:
						print("Has creado metal electronico. Metal electronico es oro mezclado con plata.")
						IQ -= 4000
						ME = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 5 and ELC != 1:
					if IQ >= 25000:
						print("has descubierto la electricidad")
						IQ -= 25000
						ELC = 1
					else:
						print("No tienes suficirnte IQ")
				if tryu == 6 and CUL == 0:
					if IQ >= 3000:
						print("has descubierto los cultivos")
						IQ -= 3000
						CUL = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 7 and DROG == 0:
					if IQ >= 7000:
						print("Has descubierto un tranquilizante/droga por si te atacan animales")
						IQ -= 7000
						DROG = 1
					else:
						print("No tienes suficiente IQ")
				if tryu == 8 and JB == 0:
					if IQ >= 1700:
						print("Has creado jabon!!!")
						IQ -= 1700
						JB = 1
					else:
						print("No tienes suficiente IQ")
			if snt == 48:
				HP = int(input("cuantos hospitales? 50.000.000€ por cada uno: "))
				print(f"Tienes: {dn} €")
				camillas += 250 * HP
				dn -= 50000000 * HP
			if snt == 1234:
				KJKJ = int(input("pon 1- para comprar mineros pon 2- para recoletores y pon 3- para cientificos "))
				if KJKJ == 1:
					print(f"puedes comprar {MRTC} como maximo")
					NNB = int(input("cuantos mineros? valen 4.000 por mes: "))
					if NNB > MRTC:
						print("no tienes suficientes minas")
					else:																
						MT += NNB
						MRTC -= NNB
					if KJKJ == 2:
						print(f"puedes comprar {MRTC} como maximo")
					NNBB = int(input("cuantos recolectores? valen 4.000 por mes: "))
					if NNBB > MRTC:
						print("no tienes suficientes minas")
					else:
						RT += NNBB
						MRTC -= NNBB
				if KJKJ == 3:
					print(f"los  puedes comprar {CTC} como maximo")
					NNBBB = int(input("cuantos cientificos? valen 9.000 por mes: "))
					if NNBBB > CTC:
						print("no tienes suficientes laboratorios")
					else:
						CT += NNBBB
						CTC -= NNBBB
			if snt == 45:
				PRS = int(input("cuantas protecciones quieres? valen 500.000: "))
				print(f"Tienes: {dn} €")
				PR += PRS
				dn -= PRS * 500000
			if snt == 88:
				dn -= 300000000
				EX = random.randrange(4)
				if EX == 1:
					print("hemos encontrado un volcan!!!!, quieres comprarlo? Costo:10.000.000")
					print(f"ahora tu numero de volcanes sube de {VCL} a {VCL+1} volcanes. y has conseguido mucha fama 500.000 en concreto, a mas a mas cada mes ganas 50.000 de fama y 50.000€")
					VCL += 1
					fama += 500000
					dn -= 10000000
				elif EX != 1 or EX != 4:
					print("no encontraron nada y perdiste dinero por explorar")
				elif EX == 4:
					print("hemos encontrado unas minas misteriosas muy antiguas!!!!, quieres explorarlas? Costo: 10.000.000 1-Si 2-No")
					MEX = int(input())
					if MEX == 1:
						MEXR = random.randrange(2)
						if MEXR == 1:
							print(" encontraron una fuente de oro, te proporcionara 0.05 al mes")
							MMO+=1
						if MEXR==2:
							print("encontraron una fuente de plata, te proporcionara 2,002 al mes")
							MMP+=1
			if snt == 23:
				limpio = int(input("cuantos niveles de limpieza mejoras?"))
				print(f"Tienes: {dn} €")
				LMP += limpio
				dn -= limpio * 10000000
			if snt == 10:
				holita = int(input("cuantos kg de comida quieres comprar? cada kg vale 5: "))
				print(f"Tienes: {dn} €")
				comida += holita
				dn -= 5 * holita
			if snt == 50:
				V = float(input("Por cuál es el valor de las casas?: "))
				print(fama)
			if snt == 1:
				lujo = int(input("nivel de lujo: "))
				qt = int(input("cantidad de casas: "))
				dn -= (100000 * lujo * lujo * qt)
				fama += lujo * lujo * (lujo) * qt
				sp += lujo * qt
			if snt == 2:
				dn -= 15000000000
				C += sp // 10
				sp -= sp // 10
				if C >= 12500000:
					C = 12500000
			if snt == 432:
				KKKK = int(input("1- comprar minas 2- comprar laboratorios"))
				if KKKK == 1:
					lmnk = int(input("cuantas minas compras soportan 100 mineros y valen 200.000.000"))
					if dn>= 200000000*lmnk:
						dn-= 200000000*lmnk
						MRTC += 100*lmnk
				else:
					lmnkj = int(input("cuantos laboratorios\n valen 500.000.000 soportan 100 cientificos"))
					if dn>= 500000000*lmnkj:
						dn-= 500000000*lmnkj
						CTC += 100*lmnkj
			print("\033[1;36m" + f"tienes {C} ciudadanos")
			print(f"tienes {sp} sitios de casas libres")
			print(f"tienes { (fama / ((V + 100) * (V**(V * 10))))} de fama")
			print(f"tienes {comida} kg de comida")
			print(f"tienes {PR} protecciones")
			print(f"tienes {LMP} nivel de limpieza ")
			print(f"tienes {infectados} infectados ")
			print(f"tienes {camillas} camillas ")
			print(f"tienes {vacuna} nivel de vacuna")
			print(f"tienes {IQ} IQ")
			print(f"podrias comprar {MRTC} mineros/recolectores")
			print(f"podrias comprar {CTC} cientificos")
			print(f"tienes {energiaIMD} energiaIMD")
			print(f"gastas {engine*50.000} de carbon/mes")
			print(f"gastas {IMDC*1000000} de energiaIMD/mes")

			holiss = int(
					input("quieres ver minerales 1-si 2-no"'\033[0;m'))
			if holiss == 1:
				print("\033[1;36m" +f"tienes: oro: {oro}\n plata: {plata}\n bronce: {bronce}\n hierro: {hierro}\n aluminio: {aluminio}\ acero: {acero}\n carbon: {carbon}\n cobre: {cobre}\n madera: {madera}\n piedra: {piedra} arcilla: {arcilla}\n metal elcetrico : {electrico}\n resina:{resina} "'\033[0;m')

			#desastres
			k = random.randrange(100) + 1
			#print(k)
			if df ==5:
				if k > 0 and k < 10:
					print("\033[1;31m" +"MUERTE: Hay una ULTRAMEGAtitanoboa vamos a morirrrrrr"'\033[0;m')
					print("1- nada 2- usar un tranquilizantes (8)")
					print(f"Tienes: {dn}€")
					kte = int(input())
					if kte == 1:
						print("\033[3;34m" +"La ULTRAMEGAitanoboa se comio y engullo a ciudadanos :("'\033[0;m')
						C -= C // 4
						fama //= 1.85
					else:
						if drogas >= 8:
							print("\033[3;34m" +"Has perdido 8 tranquilizantes pero tu fama ha aumentado!!!!!!!!!!!"'\033[0;m')
							fama += 250000
						else:
							print("\033[3;34m" +"la ULTRAMEGAitanoboa se comio y engullo a ciudadanos :('\033[0;m'")
							C -= C // 4
							fama //= 1.85
				if k > 50 and k < 65:
					if VCL >= 1:
						print("\033[1;31m" +"MUERTE: uno de tus volcanes esta en  erupcion, vamos a morirrrrrr"'\033[0;m')
						print("1- gastar protecciones(35*Volcanes) 2- nada 3-destruir volcan")
						ktp = int(input())
						if ktp == 1 and PR <= 34:
							print("\033[3;34m" +"No tenias suficientes protecciones, el volcan ha fundido casas pierdes espacios :("'\033[0;m')
							sp -= sp // 10
							fama //= 2
						if ktp == 1 and PR >= (35 * VCL):
							print("\033[3;34m" + "Te salvaste" '\033[0;m')
							fama *= 2
							PR -= 35 * VCL
						elif ktp == 2:
							print("\033[3;34m" +"Pierdes mucha fama y se han fundido muchas casas"'\033[0;m')
							fama //= 2
							sp //= 2
						else:
							print("\033[3;34m" +"Pierdes mucha fama y un volcan pero nada mas ha pasado"'\033[0;m')
							print(f"tu numero de volcanes es {VCL}")
							fama //= 2
							VCL -= 1
					if k > 66 and k < 78:
						print("\033[1;31m" +"MUERTE: hay un terremoto de magnitud 6 vamos a morirrrrrr"'\033[0;m')
						print("1- gastar protecciones avanzadas(30) 2- evacuar ")
						ktp = int(input())
						if ktp == 1 and PRA <= 29:
							print("\033[3;34m" +"El terremoto ha roto casas pierdes espacios!!! :("'\033[0;m')
							sp -= sp // 1.5
							fama //= 2.5
						if ktp == 1 and PR >= 30:
							print("\033[3;34m" + "Te salvaste" '\033[0;m')
							fama *= 1.0062
							PRA -= 30
						else:
							print("\033[3;34m" +"Pierdes fama Y algunos de tus ciudadanos han muerto. Pero nada se ha derrumbado"'\033[0;m')
							fama //= 1.7
							C //= 1.05
					if k > 79 and k < 90:
						print("\033[1;31m" +"MUERTE: hay un terrorrista!!! Quiere destruir tu ciudad!!"'\033[0;m')
						print("1- gastar protecciones avanzadas(30) 2- evacuar 3-mandar a alguien para que intente parar al terrorrista ")
						ktp = int(input())
						if ktp == 1 and PRA <= 29:
							print("\033[3;34m" +"No tienes suficientes protecciones y una bomba ha ESTALLADO!! Pierdes casas y fama!!!:("'\033[0;m')
							fama //= 1.4
							sp//= 2.4
						if ktp == 1 and PR >= 30:
							print("\033[3;34m" + "Gracias a tus protecciones la bomba del terrorrista no ha hecho daño. Ganas fama!!!" '\033[0;m')
							fama *= 1.0062
							PRA -= 30
						if ktp == 2:
							print("\033[3;34m" +"Una bomba ha ESTALLADO mientras evacuabas a tus ciudadanos. Desgraciadamente muchos ciudadanos no han sobrevivido. Tu fama tambien ha bajado.!!!"'\033[0;m')
							fama //= 1.4
							C //=1.6
						else:
							uu=random.randrange(2)
							if uu==1:
								print("Tus refuerzos consiguieron detener al terrorrista. Ganas fama y ademas otros paises te dan 2,000,000,000€")
								dn += 2000000000
								fama*=1.0060
							else:
								print("Tus refuerzos han caido. Te baja fama y ha estallado una bomba que ha destruido casas!!")
								fama//=1.4
								sp//=2.4

#dfff 6666666666666666666666666666666666 MUERTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
	  

if pato == 1:
	print("has perdido de manera drastica, puede ser que te hayas quedado sin fama, comida o dinero.")