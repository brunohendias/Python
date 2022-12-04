from models.Log import Log
from models.ErrorLog import ErrorLog

def log(user, msg, resp):
    open('logs.txt', 'a').write(f"{Log(user, msg, resp)}\n")
    
def error(e, user, msg, resp):
    open('errors.txt', 'a').write(f"{ErrorLog(e)}{Log(user, msg, resp)}\n")
