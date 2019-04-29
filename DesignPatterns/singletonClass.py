# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Singleton Class

'''
This Pattern restricts the instantiation of a class to one object. 
It is a type of creational pattern and involves only one class to create methods and specified objects.
It provides a global point of access to the instance created.
So whatever modifications we do to any variable inside the class through any instace, it affects the variable of the single instance created and is visible if we access that variable through any variable of that class type defined.
Mostly used in loggers
'''

class Singleton:
    __instance = None
    string = ""
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This Class is Singleton")
            # print("This is a Singleton Class")
        else:
            Singleton.__instance = self
            Singleton.string = "Omkar"
    
    def getInstance():
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

if __name__=="__main__":
    s = Singleton.getInstance()
    print(s)
    g = Singleton.getInstance()
    print(g)
    x = Singleton()
    print(x)
