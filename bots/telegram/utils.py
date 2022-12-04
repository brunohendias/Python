from os import popen
from Models.Command import Command

def SOCommand(command: str):
    return popen(command).read()

def randomPassword():
    return SOCommand('openssl rand -base64 30')

commands = [
    Command('password', randomPassword)
]