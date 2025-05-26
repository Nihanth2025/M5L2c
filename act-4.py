class Rec:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length * self.width

obj=Rec(50,62)
result=obj.calculate_area()
print("Area of Rectangle:", result)