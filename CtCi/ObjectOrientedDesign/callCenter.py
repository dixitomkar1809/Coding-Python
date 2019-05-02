# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Call Center

# This is out call handler service which will have all the handlers, list of calls incoming, call stack, 
# Jobs done by this service will be getting handlers for call 
#  dispatch the calls
class CallHandler:
    def __init__(self):
        self.employeeTypes = {1: "Respondent", 2: "Manager", 3: "Director"}
        self.handlers = {
            "Respondent": [],
            "Manager": [],
            "Director": []
        }
        self.callStack = {
            "Respondent": [],
            "Manager": [],
            "Director": []
        }
    
    # Registers Handlers to the map of all handlers with the type
    def registerHandler(self, handler):
        self.handlers[handler.getType()].append(handler)

    # Returns all handlers
    def getAllHandlers(self):
        return self.handlers
    
    # dispatches the call to the emp it has been assigned
    def dispatchCall(self, call):
        emp = self.getHandler(call)
        if emp and emp.isFree():
            emp.receive(call)
            call.setHandler(emp)
            call.message("{} is being attended by {}".format(call.getCaller(), emp.getEmployeeDetails()))
        else:
            call.message("No employee available to take your call please wait")
            self.callStack[call.getHandlerType()].append(call)
    
    def dispatchCaller(self, caller):
        call = Call(caller)
        self.dispatchCall(call)    
    
    def getHandler(self, call):
        if call.getHandler() is None:
            for handler in self.handlers["Respondent"]:
                if handler.isFree():
                    return handler
                else:
                    return None
        else:
            for handler in self.handlers[call.getHandlerType()]:
                if handler.isFree():
                    return handler
                else:
                    return None

#  Our callers
class Caller:
    def __init__(self, caller):
        self.caller = caller
        print("Created Caller {}".format(self.caller))

# Our calls
class Call(Caller):
    def __init__(self, caller):
        Caller.__init__(self, caller)
        self.attendedBy = "Respondent"
        self.handler = None

    def setHandler(self, emp):
        self.handler = emp
        self.attendedBy = emp.getType()

    def disconnect(self):
        pass

    def getHandler(self):
        return self.handler
    
    def getHandlerType(self):
        return self.attendedBy
    
    def message(self, message):
        print(message)
        return
    
    def getCaller(self):
        return self.caller
    
class Employee:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.currentCall = None

    def getEmployeeDetails(self):
        return "{} - {}".format(self.name, self.type)
    
    def getName(self):
        return self.name

    def getType(self):
        return self.type
    
    def isFree(self):
        return self.currentCall==None
    
    def receive(self, call):
        self.currentCall = call
    
    def escalateAndReassign(self, call):
        pass

class Respondent(Employee):
    def __init__(self, name):
        Employee.__init__(self, "Respondent", name)
        print("Created {}({})".format(self.getName(), self.getType()))

class Manager(Employee):
    def __init__(self, name):
        Employee.__init__(self, "Manager", name)
        print("Created {}({})".format(self.getName(), self.getType()))

class Director(Employee):
    def __init__(self, name):
        Employee.__init__(self, "Director", name)
        print("Created {}({})".format(self.getName(), self.getType()))
    

if __name__=="__main__":
    callService = CallHandler()
    callService.registerHandler(Respondent("Ayushi"))
    callService.registerHandler(Manager("Piyush"))
    callService.registerHandler(Director("Aniket"))
    callService.dispatchCaller("Omkar")
    callService.dispatchCaller("Dixit")