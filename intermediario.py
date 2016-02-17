#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor Prueba
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

#Modificado por Alejandro Córdoba Soto y Ricardo Aguilar Vargas
#Proyecto del curso CI-1320

import socket
import sys
import random
import threading
 
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

contador = 0

# Escuchando conexiones entrantes
sock.listen(1)

#Probabilidad de que se pierdan los paquetes
def proba():
   sePerdio = False
   p = random.uniform(0,100)
   if(p < perdida ):
    sePerdio = True 
   return sePerdio;

def worker(data):
    print >>sys.stderr, 'recibido %s' % data
    #Se saca la probalilidad de que se pierda
    prob = random.uniform(0,100)
   # print 'NUMERO X',prob
    p = True
    if prob > perdida:
        p = True
        print 'No se pierde el mensaje ',data
    else:
        p = False
        print 'SE PIERDE EL MENSAJE ',data


    
    if p:
        print 'Enviando mensaje al servidor ',data
        sock2.sendall(data)     
        data = sock2.recv(7)
        if data:
            connection.sendall(data)
            print 'Enviando mensaje al cliente ',data
    else:
        print 'SE PERDIO EL PAQUETE %s' % data

                    

    return



threads = list() 
print 'Probabilidad de que se pierda ',perdida
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
 
    try:
        print >>sys.stderr, 'concexion desde', client_address
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(7)
            if data:
                t = threading.Thread(target=worker, args=(data,))
                threads.append(t)
                t.start()
            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break
             
    finally:
        # Cerrando conexion
        connection.close()
        print >>sys.stderr,'terminando'