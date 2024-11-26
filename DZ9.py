class Programming_language:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("Привітання від ", {self.name})
    def printing(self):
        print("Я вітаюсь так:")
class Python(Programming_language):
    def __init__(self):
        super().__init__("Python")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")
class Java(Programming_language):
    def __init__(self):
        super().__init__("Java")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")
class SPlusPlus(Programming_language):
    def __init__(self):
        super().__init__("S++")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")
class SSharp(Programming_language):
    def __init__(self):
        super().__init__("S#")
    def hello_world(self):
        super().printing()
        print("print('Hello world!')")

if __name__ == "__main__":
    python = Python()
    java = Java()
    ssharp = SSharp()
    splusplus = SPlusPlus()

    python.hello()
    python.hello_world()
    java.hello()
    java.hello_world()
    ssharp.hello()
    ssharp.hello_world()
    splusplus.hello()
    splusplus.hello_world()