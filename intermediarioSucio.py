#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

import socket
import sys
import random
import threading


# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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

paquetes = []
if modo == 1:
    n = int(input("Digite los numeros de los paquetes que desea que se pierdan \n"))
    while n != -1: 
        n = input('')
        paquetes += [n]
    nT = len(paquetes)

# Escuchando conexiones entrantes
sock.listen(1)

def pertenece(num):
    Pertenece = False
    for i in range (0, (len(paquetes)-1)):
        if num == paquetes[i]:
            Pertenece = True
            paquetes[i] = -1
    return Pertenece

def cs(algo):

    print 'Soy el hilo ',algo
    if modo == 0:
        while  True:
            data = connection.recv(7)
            print >>sys.stderr, 'recibido "%s"' % data
            if data:
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
                    print 'enviando mensaje al servidor ', data 
                    sock2.sendall(data)
                else:
                    print 'SE PERDIO EL PAQUETE %s' % data
                    t = perdida/1000
                    tp = 0
                    while t != tp:
                        tp += 1
                    sock2.sendall(data)    

            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break   
    else:
        print 'modo debug'
        while  True:
            data = connection.recv(7)
            print >>sys.stderr, 'recibido "%s"' % data
            
            num = int(data[0:5])
            p = pertenece(num)
            if p == False:
                print 'Enviando mensaje al servidor ',data
                sock2.sendall(data)     
            else:
                print 'SE PERDIO EL PAQUETE %s' % data
                t = perdida/1000
                tp = 0
                while t != tp:
                    tp += 1
                sock2.sendall(data) 
    return

def sc(algo):
    print 'Soy el hilo ',algo
    if modo == 0:
        while  True:
            data = sock2.recv(7)
            if data:
                print 'enviando mensaje de vuelta al cliente ', data 
                connection.sendall(data)

            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break
    else:
        while True:
            data = sock2.recv(7)
            if data:
                connection.sendall(data)
                print 'Enviando mensaje al cliente ',data
            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break
    return
 
inicio = True
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
 
    try:
        if inicio == True:
            t = threading.Thread(target=cs, args=(1,))
            t.start()
            t2 = threading.Thread(target=sc, args=(2,))
            t2.start()
            inicio = False

        
                     
    finally:
        # Cerrando conexion
        #connection.close()
        print >>sys.stderr,'terminando'

