from datetime import datetime

class Log():
    def __init__(self, cliente, user, msg, resp):
        self.cliente = {}
        self.user = user
        self.msg = msg
        self.date = datetime.now()
        self.resp = resp
        
    def __repr__(self):
        return f"LOG:\nUser: {self.user} \nMessage: {self.msg} \ndate: {self.date}\nresponse: {self.resp}\n"