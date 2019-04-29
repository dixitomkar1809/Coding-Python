# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Singleton Class

class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This Class is Singleton")
        else:
            Singleton.__instance = self
    
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        else:
            return Singleton.__instance

if __name__=="__main__":
    s = Singleton()
    print(s)
    s = Singleton.getInstance()
    print(s)
    s = Singleton.getInstance()
    print(s)
    g = Singleton()
    print(g)