from datetime import datetime

class Log():
    def __init__(self, user, msg):
        self.user = user
        self.msg = msg
        self.date = datetime.now()
        
    def __repr__(self):
        return f"LOG:\nUser: {self.user} \nMessage: {self.msg} \ndate: {self.date}\n"