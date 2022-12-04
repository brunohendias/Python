class ErrorLog():
    def __init__(self, e):
        self.e = e
    
    def __repr__(self):
        return f"ERROR:\n{self.e}\n"