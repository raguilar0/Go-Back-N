import random
import sys


perdida = int(sys.argv[1])

def proba():
   sePerdio = False
   p = random.uniform(0,100)
   if(p < perdida ):
   	sePerdio = True
   return sePerdio;

contador = 0
contadorPerdidos = 0;

while (contador < 100 ):
	p = proba();
	print 'Probabilidad ', p
	if(p):
		print 'El paquete se perdio'
		contadorPerdidos = contadorPerdidos +1
	contador = contador + 1

print 'Total de perdidos ', contadorPerdidos

