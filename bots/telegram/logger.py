from models.Log import Log
from models.ErrorLog import ErrorLog

def log(cliente, user, msg, resp):
    open('logs.txt', 'a').write(f"{Log(cliente, user, msg, resp)}\n")
    
def error(e, cliente, user, msg, resp):
    open('errors.txt', 'a').write(f"{ErrorLog(e)}{Log(cliente, user, msg, resp)}\n")
