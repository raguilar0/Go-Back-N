import time

#millis = int(round(time.time() * 1000))

t0 = time.time()

print 'Tiempo 1 ',t0

t1 = time.time()
dif = t1-t0

while dif*1000 < 1000:

	print 'dif ', dif
	dif = t1-t0
	t1 = time.time()
print 'Diferencia ',dif


