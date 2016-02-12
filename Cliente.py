#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

#Modificado por Alejandro Córdoba Soto y Ricardo Aguilar Vargas
#Proyecto del curso CI-1320

import socket
import sys
 
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

try:
     
    # Enviando datos
    archivo = open(nombreArchivo)
    linea = archivo.readline()
    while linea != '':
        tamLinea = len(linea)
        for i in range (0, tamLinea-1):
            caracter = linea[i]
            message = '#"%d":"%s"' % (i, caracter)
            print >>sys.stderr, 'enviando "%s"' % message
            sock.sendall(message)
        linea=archivo.readline()
 
    # Buscando respuesta
    amount_received = 0
    amount_expected = len(message)
     
    while amount_received < amount_expected:
        data = sock.recv(19)
        amount_received += len(data)
        print >>sys.stderr, 'recibiendo "%s"' % data
 
finally:
    print >>sys.stderr, 'cerrando socket'
    sock.close()

