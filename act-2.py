class Emp:
    def __init__(self):
        print("Employee class")
    def __del__(self):
        print("Destructor")
    def objfu():
        print("Object created")
        o=Emp()
        print("Object function end")
        return o
print("Calling function")
obj=Emp.objfu()
print("Program End")