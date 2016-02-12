#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor Prueba
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

#Modificado por Alejandro Córdoba Soto 
#Proyecto del curso CI-1320

import socket
import sys
import random
 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
puertoCliente = int(sys.argv[1])
server_address = ('localhost', puertoCliente)
print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
sock.bind(server_address)

puertoServidor = int(sys.argv[2])
server_address2 = ('localhost', puertoServidor)
print >>sys.stderr, 'conectando a %s puerto %s' % server_address2
sock2.connect(server_address2)

perdida = int(sys.argv[3])
modo= int(sys.argv[4])

# Escuchando conexiones entrantes
sock.listen(1)

#Probabilidad de que se pierdan los paquetes
def proba():
   sePerdio = False
   p = random.uniform(0,100)
   if(p < perdida ):
    sePerdio = True
   return sePerdio;


 
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
 
    try:
        print >>sys.stderr, 'concexion desde', client_address
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(1000)
            p = proba();
            if data:
                print >>sys.stderr, 'recibido "%s"' % data
                if !p:
                    sock2.sendall(data)   
                    print 'Enviando mensaje al servidor'             
                    data = sock2.recv(1000)
                    if data:
                        connection.sendall(data)
                        print 'Enviando mensaje al cliente'

            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break

    def perdido( ):
       # retorna si un paquete se perdio.
       sePerdio = True
       p = random.uniform(0,100)
   return sePerdio;
             
    finally:
        # Cerrando conexion
        connection.close()
        print >>sys.stderr,'terminando'
