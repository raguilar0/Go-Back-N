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
ventanaInicio = 0
ventanaFinal = 0
archivo = open(nombreArchivo)
contador = 0
server_address = ('localhost', puertoCliente)
print >>sys.stderr, 'conectando a %s puerto %s' % server_address
sock.connect(server_address)

def wc(filename):   
    return int(check_output(["wc", "-m", filename]).split()[0])




def enviarMensajesIniciales(mContador, vf):
    archivo.seek(mContador)
    mLinea = archivo.read(1)
    while ((mLinea != '') & (mContador < vf)):
        
        for i in range (ventanaInicio, ventanaFinal):
            pos = str(mContador)
            lenpos = len(pos)
            while lenpos < 5:
                pos = '0'+pos
                lenpos = len(pos)
            pba = int(pos)
            message = '%s:%s' % (pos, mLinea)
            print >>sys.stderr, 'enviando %s' % message
            sock.sendall(message)
            mContador = mContador + 1            
            archivo.seek(mContador)
            contador = mContador
            mLinea=archivo.read(1)
    return mContador

def enviarSiguienteMensaje(mContador, vf):

    archivo.seek(mContador)
    mLinea = archivo.read(1)
    if ((mLinea != '') & (mContador < vf)):
        pos = str(mContador)
        lenpos = len(pos)
        while lenpos < 5:
            pos = '0'+pos
            lenpos = len(pos)
        pba = int(pos)
        message = '%s:%s' % (pos, mLinea)
        print >>sys.stderr, 'enviando %s' % message
        sock.sendall(message)
        mContador = mContador + 1            
        archivo.seek(mContador)
        contador = mContador
        mLinea=archivo.read(1)
    return mContador


try:
    letras = wc(nombreArchivo)
    # Enviando datos
    #Inicializamos la ventana
    ventanaFinal = ventana;
    print 'Ventana final ', ventanaFinal
    contador = enviarMensajesIniciales(contador,ventanaFinal)  
    
 
    # Buscando respuesta
    amount_received = 0
    amount_expected = letras*7
     
    while amount_received < amount_expected:
        data = sock.recv(7)
        amount_received += len(data)
        print >>sys.stderr, 'recibiendo "%s"' % data
        ventanaInicio = ventanaInicio+1
        ventanaFinal = ventanaFinal+1
        if(ventanaFinal < letras):
            contador = enviarSiguienteMensaje(contador, ventanaFinal)
 
finally:
    print >>sys.stderr, 'cerrando socket'
    sock.close()

