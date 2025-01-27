#Creating a class
class Dog:
    #class attribute
    species = "dog"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the dog class
golden_reteiver = Dog("golden_reteiver", 10)
German_Shepard = Dog("German_Shepard", 15)

#access the class attributes
print("golden_reteiver is a {}".format(golden_reteiver.__class__.species))
print("German_Shepard is also a {}".format(German_Shepard.__class__.species))

#access the instance attributes
print("{} is {} years old".format(golden_reteiver.name, golden_reteiver.age))
print("{} is {} years old".format(German_Shepard.name, German_Shepard.age))