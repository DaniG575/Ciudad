
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