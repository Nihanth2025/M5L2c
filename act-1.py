class f1:
    def __init__(self):
        self.str1=""
    def enter(self):
        self.str1=input("Enter the string:\n")
    def printfunction(self):
        print("Reasult is:", self.str1.upper())

str1=f1()
str1.enter()
str1.printfunction()