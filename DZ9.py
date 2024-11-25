class Programming_language:
    def __init__(self, name):
        self.name = name
    def hello(self, name):
        print("Привітання від ", {name})
class Python(Programming_language):
    def __init__(self, name):
        self.name = name
    def __init__(self):
        super().hello(name)

python = Python()