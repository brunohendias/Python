from Models.Log import Log
from Models.ErrorLog import ErrorLog

def log(user, msg):
    open('Log/logs.txt', 'a').write(f"{Log(user, msg)}\n")
    
def error(e, user, msg):
    open('Log/errors.txt', 'a').write(f"{ErrorLog(e)}{Log(user, msg)}\n")
