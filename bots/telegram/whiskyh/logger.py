from Models.Log import Log
from Models.ErrorLog import ErrorLog

def log(user, msg, resp):
    open('Log/logs.txt', 'a').write(f"{Log(user, msg, resp)}\n")
    
def error(e, user, msg, resp):
    open('Log/errors.txt', 'a').write(f"{ErrorLog(e)}{Log(user, msg, resp)}\n")
