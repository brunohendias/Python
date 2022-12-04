class Command():
    def __init__(self, command, action):
        self.command = command
        self.action = action
        
    def __repr__(self):
        return f"{self.command}"