#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor prueb
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

#Modificado por Alejandro Córdoba Soto y Ricardo Aguilar Vargas
#Proyecto del curso CI-1320

import socket
import sys
 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
puertoServidor = int(sys.argv[1])
modo = int(sys.argv[2])
server_address = ('localhost', puertoServidor)
print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
sock.bind(server_address)
archivo = open('salida.txt', 'w')

# Escuchando conexiones entrantes
sock.listen(1)
 
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
 
    try:
        print >>sys.stderr, 'conexion desde', client_address 
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(7)
            print >>sys.stderr, 'recibido %s' % data
            pos = len(data)
            caracter = data[pos-1]
            seq = data[0:pos-2]
            ack = seq+':ACK'
            archivo.write(caracter)
            if data:
                print >>sys.stderr, 'enviando ACK al cliente'+ack
                connection.sendall(ack)
            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break
             
    finally:
        # Cerrando conexion
        connection.close()
        archivo.close()
