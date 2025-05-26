class dog:
    sp="Labrodar"

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def display(self):
        print("Name: ",self.name)
        print("Breed: ",self.breed)
        print("Species: ",dog.sp)
        


dog1=dog("Tom", "Labrodar")
dog2=dog("Jhon", "Poodle")


print("Details of dog1")
dog1.display()

print("\nDetails of dog2")
dog2.display()