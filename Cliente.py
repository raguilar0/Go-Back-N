#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

#Modificado por Alejandro Córdoba Soto y Ricardo Aguilar Vargas
#Proyecto del curso CI-1320

import socket
import sys
from subprocess import check_output

 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
ventana = int(sys.argv[1])
nombreArchivo = sys.argv[2]
puertoCliente = int(sys.argv[3])
modo = int(sys.argv[4])
timeout = int(5)
server_address = ('localhost', puertoCliente)
print >>sys.stderr, 'conectando a %s puerto %s' % server_address
sock.connect(server_address)

def wc(filename):   
    return int(check_output(["wc", "-m", filename]).split()[0])

try:
     
    # Enviando datos
    archivo = open(nombreArchivo)
    linea = archivo.read(1)
    contador = 0
    letras = wc(nombreArchivo)
    print letras
    while ((linea != '')):
        tamLinea = len(linea)
        for i in range (0, ventana):
            pos = str(contador)
            lenpos = len(pos)
            while lenpos < 5:
                pos = '0'+pos
                lenpos = len(pos)
            pba = int(pos)
            message = '#%s:%s' % (pos, linea)
            print >>sys.stderr, 'enviando %s' % message
            sock.sendall(message)
            contador = contador + 1            
            archivo.seek(contador)
            linea=archivo.read(1)
 
    # Buscando respuesta
    amount_received = 0
    amount_expected = letras*8
     
    while amount_received < amount_expected:
        data = sock.recv(8)
        amount_received += len(data)
        print >>sys.stderr, 'recibiendo "%s"' % data
 
finally:
    print >>sys.stderr, 'cerrando socket'
    sock.close()

