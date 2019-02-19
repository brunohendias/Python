# coding: utf-8
import os 
import sys 
import socket
import subprocess

IP = "localhost"
PORT = 4444
ADDR = (IP, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

def main():
	try:
		data = s.recv(1024)
		print(data)
		comando = raw_input()
		comando.encode()
		s.send(comando)
	except:
		True
main()


